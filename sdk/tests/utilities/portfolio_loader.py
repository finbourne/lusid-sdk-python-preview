import lusid
import lusid.models as models
from utilities import InstrumentLoader
import uuid


class PortfolioLoader:

    def __init__(self, transaction_portfolios_api: lusid.TransactionPortfoliosApi, instruments_api: lusid.InstrumentsApi):
        self.transaction_portfolios_api = transaction_portfolios_api
        self.instruments_api = instruments_api

    def load_instruments(self, instruments_api) -> list:

        instrument_loader = InstrumentLoader(instruments_api)
        return instrument_loader.load_instruments()

    def build_transaction_request(self, instrument_id, id_type, units, price, currency, trade_date, transaction_type):
        return models.TransactionRequest(transaction_id=str(uuid.uuid4()),
                                         type=transaction_type,
                                         instrument_identifiers={f"Instrument/default/{id_type}": instrument_id},
                                         transaction_date=trade_date,
                                         settlement_date=trade_date,
                                         units=units,
                                         transaction_price=models.TransactionPrice(price=price),
                                         total_consideration=models.CurrencyAndAmount(amount=price * units,
                                                                                      currency=currency),
                                         source="Broker")

    def setup_gbp_portfolio(self, portfolio_scope, portfolio_code, effective_date) -> None:
        """
        Sets up a GBP portfolio for testing purposes
        :param str portfolio_scope: The scope of the the test portfolio
        :param str portfolio_code: The code of the the test portfolio
        :param datetime effective_date: The portfolio creation date
        :return: None
        """
        instrument_ids = self.load_instruments(self.instruments_api)

        transactions = [
            self.build_transaction_request(
                instrument_id=instrument_ids[0],
                id_type="LusidInstrumentId",
                units=100,
                price=101,
                currency="GBP",
                trade_date=effective_date,
                transaction_type="StockIn",
            ),
            self.build_transaction_request(
                instrument_id=instrument_ids[1],
                id_type="LusidInstrumentId",
                units=100,
                price=102,
                currency="GBP",
                trade_date=effective_date,
                transaction_type="StockIn",
            ),
            self.build_transaction_request(
                instrument_id=instrument_ids[2],
                id_type="LusidInstrumentId",
                units=100,
                price=103,
                currency="GBP",
                trade_date=effective_date,
                transaction_type="StockIn",
            ),
        ]

        self.transaction_portfolios_api.upsert_transactions(
            scope=portfolio_scope,
            code=portfolio_code,
            transaction_request=transactions,
        )

    def setup_xccy_portfolio(self, portfolio_scope, portfolio_code, effective_date) -> None:
        """
        Sets up a cross-currency portfolio for testing purposes
        :param str portfolio_scope: The scope of the the test portfolio
        :param str portfolio_code: The code of the the test portfolio
        :param datetime effective_date: The portfolio creation date
        :return: None
        """
        instrument_ids = self.load_instruments(self.instruments_api)

        transactions = [
            self.build_transaction_request(
                instrument_id=instrument_ids[0],
                id_type="LusidInstrumentId",
                units=100,
                price=101,
                currency="EUR",
                trade_date=effective_date,
                transaction_type="StockIn",
            ),
            self.build_transaction_request(
                instrument_id=instrument_ids[1],
                id_type="LusidInstrumentId",
                units=100,
                price=102,
                currency="USD",
                trade_date=effective_date,
                transaction_type="StockIn",
            ),
            self.build_transaction_request(
                instrument_id=instrument_ids[2],
                id_type="LusidInstrumentId",
                units=100,
                price=103,
                currency="JPY",
                trade_date=effective_date,
                transaction_type="StockIn",
            ),
        ]

        self.transaction_portfolios_api.upsert_transactions(
            scope=portfolio_scope,
            code=portfolio_code,
            transaction_request=transactions,
        )