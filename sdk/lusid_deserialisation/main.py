import argparse
import cProfile
import json
import logging
import pstats
import sys
import uuid
from datetime import datetime, timedelta

import pytz

import lusid as lu
import lusid.models as lm
from lusid.utilities import ApiClientFactory


def setup_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.INFO)
    logging_formatter = logging.Formatter('%(levelname)s %(asctime)s - %(message)s')
    stdout_handler.setFormatter(logging_formatter)
    root_logger.addHandler(stdout_handler)


def create_portfolio(txn_api, prop_api, scope, pf_code, effective_date, num, num_props):
    logging.info(f"creating properties {scope}/{pf_code}")

    for i in range(num_props):
        try:
            defn = lm.CreatePropertyDefinitionRequest(
                domain="Transaction",
                scope=scope,
                code=f"prop{i}",
                display_name=f"prop{i}",
                life_time="Perpetual",
                value_required=False,
                data_type_id=lm.resource_id.ResourceId(scope="system", code="string")
            )
            prop_api.create_property_definition(defn)
        except lu.ApiException as e:
            logging.warning(json.loads(e.body)["title"])

    logging.info(f"creating portfolio {scope}/{pf_code}")
    try:
        txn_api.create_portfolio(scope, lm.CreateTransactionPortfolioRequest(
            display_name=pf_code, code=pf_code, base_currency="GBP", created=effective_date))
    except lu.ApiException as e:
        logging.warning(json.loads(e.body)["title"])

    logging.info("creating transactions")

    txns = [
        lm.TransactionRequest(
            transaction_id=str(uuid.uuid4()),
            type="FundsIn",
            instrument_identifiers={"Instrument/default/Currency": "GBP"},
            transaction_date=effective_date + timedelta(days=num),
            settlement_date=effective_date + timedelta(days=num),
            units=i,
            total_consideration=lm.CurrencyAndAmount(currency="GBP"),
            transaction_price=lm.TransactionPrice(price=0.0),
            properties={
                f"Transaction/{scope}/prop{pn}": lm.PerpetualProperty(
                    key=f"Transaction/{scope}/prop{pn}",
                    value=lm.PropertyValue(label_value=f"{pn}")
                )
                for pn in range(num_props)
            }
        )
        for i in range(num)
    ]

    logging.info(f"uploading {num} transactions")
    txn_api.upsert_transactions(scope=scope, code=pf_code, transaction_request=txns)

    logging.info(f"created {num} transactions")


def main(argv):
    setup_logging()

    ap = argparse.ArgumentParser()

    ap.add_argument("-s", "--secrets", type=str, help="full path to json file")
    ap.add_argument("-n", "--num", type=int, action="store", required=True, help="number of transactions")
    ap.add_argument("-c", "--create", action="store_true")
    ap.add_argument("-d", "--delete", action="store_true")
    ap.add_argument("-p", "--num_props", default=10, type=int, help="number of properties")

    args = ap.parse_args()

    api_factory = ApiClientFactory(api_secrets_filename=args.secrets)
    txn_api = api_factory.build(lu.TransactionPortfoliosApi)
    pf_api = api_factory.build(lu.PortfoliosApi)
    prop_api = api_factory.build(lu.PropertyDefinitionsApi)

    scope = "sdk-test"
    pf_code = "deserialization"
    effective_date = datetime(2022, 1, 1, tzinfo=pytz.UTC)

    if args.create:
        create_portfolio(txn_api, prop_api, scope, pf_code, effective_date, args.num, args.num_props)

    profiler = cProfile.Profile()
    profiler.enable()

    logging.info(f"getting transactions for portfolio {scope}/{pf_code}")
    txns = txn_api.get_transactions(scope, pf_code, limit=5000)

    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats(pstats.SortKey.CUMULATIVE)
    stats.print_stats()

    if args.delete:

        logging.info(f"deleting properties")
        for i in range(args.num_props):
            prop_api.delete_property_definition("Transaction", scope, f"prop{i}")

        logging.info(f"deleting portfolio {scope}/{pf_code}")
        pf_api.delete_portfolio(scope, pf_code)


if __name__ == "__main__":
    main(sys.argv)
