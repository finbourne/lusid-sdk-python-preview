import lusid
from utilities import InstrumentLoader
from utilities import TestDataUtilities


class PortfolioLoader(TestDataUtilities):

    def __init__(self, transaction_portfolios_api: lusid.TransactionPortfoliosApi, instruments_api: lusid.InstrumentsApi):
        self.transaction_portfolios_api = transaction_portfolios_api
        self.instruments_api = instruments_api

    portfolio_figis = [
        "BBG00Y271826",
        "BBG005D5KGM0",
        "BBG000DPM932",
    ]

    def setup_gbp_portfolio(self, portfolio_scope, portfolio_code, effective_date) -> None:
        """
        Sets up a GBP portfolio for testing purposes
        :param str portfolio_scope: The scope of the the test portfolio
        :param str portfolio_code: The code of the the test portfolio
        :param datetime effective_date: The portfolio creation date
        :return: None
        """
        instrument_ids = InstrumentLoader(self.instruments_api).load_instruments(return_luids=False)
        for figi in self.portfolio_figis:
            assert figi in instrument_ids

        transactions = [
            self.build_transaction_request(
                instrument_id="BBG00Y271826",
                id_type="Figi",
                units=100,
                price=100,
                currency="GBP",
                trade_date=effective_date,
                transaction_type="StockIn",
            ),
            self.build_transaction_request(
                instrument_id="BBG005D5KGM0",
                id_type="Figi",
                units=100,
                price=100,
                currency="GBP",
                trade_date=effective_date,
                transaction_type="StockIn",
            ),
            self.build_transaction_request(
                instrument_id="BBG000DPM932",
                id_type="Figi",
                units=100,
                price=100,
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
        instrument_ids = InstrumentLoader(self.instruments_api).load_instruments(return_luids=False)
        for figi in self.portfolio_figis:
            assert figi in instrument_ids

        transactions = [
            self.build_transaction_request(
                instrument_id="BBG00Y271826",
                id_type="Figi",
                units=100,
                price=101,
                currency="EUR",
                trade_date=effective_date,
                transaction_type="StockIn",
            ),
            self.build_transaction_request(
                instrument_id="BBG005D5KGM0",
                id_type="Figi",
                units=100,
                price=102,
                currency="USD",
                trade_date=effective_date,
                transaction_type="StockIn",
            ),
            self.build_transaction_request(
                instrument_id="BBG000DPM932",
                id_type="Figi",
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