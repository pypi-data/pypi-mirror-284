import clearskies
from clearskies.column_types import boolean, integer, string, timestamp
from .column_types import stripe_object
from collections import OrderedDict


class StripeCharge(clearskies.Model):
    id_column_alt_name = "charge"

    def __init__(self, stripe_sdk_backend, columns):
        super().__init__(stripe_sdk_backend, columns)

    @classmethod
    def table_name(cls):
        return "charges"

    def columns_configuration(self):
        return OrderedDict(
            [
                string("id"),
                string("environment"),
                string("object"),
                integer("amount"),
                integer("amount_captured"),
                integer("amount_refunded"),
                string("application"),
                string("application_fee"),
                integer("application_amount"),
                string("balance_transaction"),
                stripe_object("billing_details"),
                string("calculated_statement_descriptor"),
                boolean("captured"),
                timestamp("created"),
                string("currency"),
                string("customer"),
                string("description"),
                boolean("disputed"),
                string("failure_balance_transaction"),
                string("failure_code"),
                string("failure_message"),
                stripe_object("fraud_details"),
                string("invoice"),
                stripe_object("metadata"),
                string("on_behalf_of"),
                stripe_object("outcome"),
                boolean("paid"),
                string("payment_intent"),
                string("payment_method"),
                stripe_object("payment_method_details"),
                string("receipt_email"),
                string("receipt_number"),
                string("receipt_url"),
                boolean("refunded"),
                string("review"),
                stripe_object("shipping"),
                string("source_transfer"),
                string("statement_descriptor"),
                string("statement_descriptor_suffix"),
                select("status", values=["succeeded", "pending", "failed"]),
                stripe_object("transfer_data"),
                string("transfer_group"),
                string("customer"),
            ]
        )
