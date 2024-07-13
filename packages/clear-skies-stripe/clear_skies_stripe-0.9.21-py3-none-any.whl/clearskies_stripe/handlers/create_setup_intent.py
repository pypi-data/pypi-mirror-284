import clearskies
from clearskies.handlers.base import Base

class CreateSetupIntent(Base):
    _configuration_defaults = {
        "automatic_payment_methods": None,
        "confirm": None,
        "description": None,
        "metadata": None,
        "payment_method": None,
        "usage": None,
        "attach_to_self": None,
        "confirmation_token": None,
        "flow_directions": None,
        "mandate_data": None,
        "on_behalf_of": None,
        "payment_method_configuration": None,
        "payment_method_data": None,
        "payment_method_options": None,
        "payment_method_types": None,
        "return_url": None,
        "single_use": None,
        "use_stripe_sdk": None,
        "parameters_callable": None,
        "output_callable": None,
        "environment": None,
    }

    # these are the config options that get passed along to our create_setup_intent call to stripe
    _create_setup_intent_kwargs = [
        "automatic_payment_methods",
        "confirm",
        "description",
        "metadata",
        "payment_method",
        "usage",
        "attach_to_self",
        "confirmation_token",
        "flow_directions",
        "mandate_data",
        "on_behalf_of",
        "payment_method_configuration",
        "payment_method_data",
        "payment_method_options",
        "payment_method_types",
        "return_url",
        "single_use",
        "use_stripe_sdk",
    ]

    def __init__(self, di, stripe):
        super().__init__(di)
        self.stripe = stripe

    def _check_configuration(self, configuration):
        super()._check_configuration(configuration)
        error_prefix = "Configuration error for %s:" % (self.__class__.__name__)
        if configuration.get("parameters_callable") is not None and not callable(configuration["parameters_callable"]):
            raise ValueError(f"{error_prefix} 'parameters_callable' must be a callable")
        if configuration.get("output_callable") is not None and not callable(configuration["output_callable"]):
            raise ValueError(f"{error_prefix} 'output_callable' must be a callable")
        environment = configuration.get("environment")
        if environment and not isinstance(environment, str) and not callable(environment):
            raise ValueError(f"{error_prefix} 'environment must be either a string with an environment name or a callable that retunrs the environment name.  Instead, it was something of type '{environment.__class__.__name__}")

    def handle(self, input_output):
        # grab all the config keys that are for stripe arguments
        stripe_params = {
            key: self._configuration[key] for key in self._create_setup_intent_kwargs if self._configuration.get(key) is not None
        }
        stripe_kwargs = {}

        callable_kwargs = {
            "input_output": input_output,
            "routing_data": input_output.routing_data(),
            "request_data": input_output.request_data(required=False),
            "authorization_data": input_output.get_authorization_data(),
            "context_specifics": input_output.context_specifics(),
        }

        parameters_callable = self._configuration.get("parameters_callable")
        if parameters_callable is not None:
            stripe_params = {
                **stripe_params,
                **self._di.call_function(
                    parameters_callable,
                    **callable_kwargs,
                )
            }
            if not isinstance(stripe_params, dict):
                raise ValueError("parameters_callable for handler " + (self.__class__.__name__) + " must return a dictionary, but returned something else.")

        environment_config = self._configuration.get("environment")
        if environment_config:
            # our environment configuration is either the name of the environment or a function to call that returns the name of the environment
            if isinstance(environment_config, str):
                environment = environment_config
            else:
                environment = self._di.call_function(environment_config, **callable_kwargs)
                if environment is not None and not isinstance(environment, str):
                    raise ValueError(f"Error in handler {self.__class__.__name__} I have an environment callable, '{environment_config.__name__}', but when I called it it retruned an object of type '{environment.__class__.__name__}'.  It needs to return a string to specify the name of the environment that I have to work with")
            stripe_kwargs["environment"] = environment

        response = {
            **self.stripe.setup_intents.create(stripe_params, **stripe_kwargs),
            "publishable_key": self.stripe.get_publishable_key(**stripe_kwargs),
        }
        output_callable = self._configuration.get("output_callable")
        if output_callable is not None:
            response = self._di.call_function(
                output_callable,
                response=response,
                **callable_kwargs,
            )
            if not isinstance(response, dict):
                raise ValueError("output_callable for handler " + (self.__class__.__name__) + " must return a dictionary, but returned something else.")

        return self.success(input_output, response)
