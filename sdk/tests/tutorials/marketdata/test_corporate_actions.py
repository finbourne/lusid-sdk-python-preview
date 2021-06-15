import unittest
import uuid
import pytz
from datetime import datetime, timedelta

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from fbnsdkutilities import ApiClientBuilder
from utilities.credentials_source import CredentialsSource
from utilities.test_data_utilities import TestDataUtilities


class CorporateActions(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # create a configured API client
        api_client = ApiClientBuilder().build(lusid, str(CredentialsSource.secrets_path()))

        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)
        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.corporate_actions_sources_api = lusid.CorporateActionSourcesApi(api_client)

    def get_guid(self):
        # creates random alphanumeric code
        return str(uuid.uuid4())[:12]

    @lusid_feature("F12-4")
    def test_name_change_corporate_action(self):
        """The code below shows how to process a corporate action name change in LUSID:
             Create two instruments, the original and the updated instrument.
             Create a portfolio and add a transaction to it for the original instrument.
             Create a corporate action source, and a corporate action comprising a transition.
             Upsert the corporate action, then check that the holding instrument was changed.
         """
        # Define details for the corporate action.
        instrument_name = "instrument-name"
        instrument_original_figi = "FR0123456789"
        instrument_updated_figi = "FR5555555555"
        portfolio_code = "corporate-actions-portfolio"
        effective_at_date = datetime(2021, 1, 1, tzinfo=pytz.utc)
        corporate_action_source_code = "name-change-corporate-actions-source"
        corporate_action_code = "name-change-corporate-action"

        # Create two instruments: an "original" instrument which
        # will be renamed and the instrument it will be renamed to.
        self.instruments_api.upsert_instruments(
            request_body={
                instrument_original_figi: models.InstrumentDefinition(
                    name=instrument_name,
                    identifiers={
                        "Figi": models.InstrumentIdValue(value=instrument_original_figi)
                    },
                ),
                instrument_updated_figi: models.InstrumentDefinition(
                    name=instrument_name,
                    identifiers={
                        "Figi": models.InstrumentIdValue(value=instrument_updated_figi)
                    },
                ),
            }
        )

        # Create a transaction portfolio to hold the original instrument.
        self.transaction_portfolios_api.create_portfolio(
            scope=TestDataUtilities.tutorials_scope,
            create_transaction_portfolio_request=models.CreateTransactionPortfolioRequest(
                code=portfolio_code,
                display_name=portfolio_code,
                base_currency="GBP",
                created=effective_at_date,
            ),
        )

        # Add a transaction for the original instrument.
        self.transaction_portfolios_api.upsert_transactions(
            scope=TestDataUtilities.tutorials_scope,
            code=portfolio_code,
            transaction_request=[
                models.TransactionRequest(
                    transaction_id=str(uuid.uuid4()),
                    type="Buy",
                    instrument_identifiers={
                        TestDataUtilities.lusid_figi_identifier: instrument_original_figi
                    },
                    transaction_date=effective_at_date,
                    settlement_date=effective_at_date,
                    transaction_price=models.TransactionPrice(0.0),
                    units=60000,
                    total_consideration=models.CurrencyAndAmount(0, "GBP"),
                    source="Client",
                )
            ],
        )

        # Create a corporate actions source.
        corporate_action_source = models.CreateCorporateActionSourceRequest(
            scope=TestDataUtilities.tutorials_scope,
            code=corporate_action_source_code,
            display_name=corporate_action_source_code,
            description="Name change corporate actions source",
        )

        self.corporate_actions_sources_api.create_corporate_action_source(
            create_corporate_action_source_request=corporate_action_source
        )

        # Apply the corporate actions source to the transaction portfolio.
        self.transaction_portfolios_api.upsert_portfolio_details(
            scope=TestDataUtilities.tutorials_scope,
            code=portfolio_code,
            effective_at=effective_at_date,
            create_portfolio_details=models.CreatePortfolioDetails(
                corporate_action_source_id=models.ResourceId(
                    scope=TestDataUtilities.tutorials_scope,
                    code=corporate_action_source_code,
                )
            ),
        )

        # Create a transition which applies to the original instrument above
        transition_in = models.CorporateActionTransitionComponentRequest(
            instrument_identifiers={
                TestDataUtilities.lusid_figi_identifier: instrument_original_figi
            },
            cost_factor=1,
            units_factor=1,
        )

        # and has the effect of changing its FIGI to the updated FIGI
        rename_figi_transition = models.CorporateActionTransitionComponentRequest(
            instrument_identifiers={
                TestDataUtilities.lusid_figi_identifier: instrument_updated_figi
            },
            cost_factor=1,
            units_factor=1,
        )

        #   while zeroing the original instrument's position.
        zero_previous_position_transition = (
            models.CorporateActionTransitionComponentRequest(
                instrument_identifiers={
                    TestDataUtilities.lusid_figi_identifier: instrument_original_figi
                },
                cost_factor=0,
                units_factor=0,
            )
        )

        # The effect of the corporate action is the transition which
        # combines the input transition and the output transitions.
        transition = models.CorporateActionTransitionRequest(
            input_transition=transition_in,
            output_transitions=[
                rename_figi_transition,
                zero_previous_position_transition,
            ],
        )

        # Create a request to upsert a corporate action with the transition above.
        corporate_action_request = models.UpsertCorporateActionRequest(
            corporate_action_code=corporate_action_code,
            announcement_date=effective_at_date + timedelta(days=1),
            ex_date=effective_at_date + timedelta(days=1),
            record_date=effective_at_date + timedelta(days=1),
            payment_date=effective_at_date + timedelta(days=1),
            transitions=[transition],
        )

        # Make the request through the CorporateActionSourcesApi.
        upsert_corp_act_response = self.corporate_actions_sources_api.batch_upsert_corporate_actions(
            scope=TestDataUtilities.tutorials_scope,
            code=corporate_action_source_code,
            upsert_corporate_action_request=[corporate_action_request],
        )

        # Fetch holdings in portfolio once corporate action is applied.
        holdings = self.transaction_portfolios_api.get_holdings(
            scope=TestDataUtilities.tutorials_scope,
            code=portfolio_code,
            property_keys=["Instrument/default/Figi"],
        )

        # The holding for the original instrument is now against the new instrument's FIGI.
        self.assertEqual(
            holdings.values[0]
            .properties[TestDataUtilities.lusid_figi_identifier]
            .value.label_value,
            instrument_updated_figi,
        )

        # Remove all data that was created for the test.
        # Delete the two instruments.
        self.instruments_api.delete_instrument("Figi", instrument_original_figi)

        self.instruments_api.delete_instrument("Figi", instrument_updated_figi)

        # Delete the portfolio.
        self.portfolios_api.delete_portfolio(
            TestDataUtilities.tutorials_scope, portfolio_code
        )

        # Delete the corporate action source.
        self.corporate_actions_sources_api.delete_corporate_action_source(
            TestDataUtilities.tutorials_scope, corporate_action_source_code
        )

    @lusid_feature("F33")
    def test_list_corporate_action_sources(self):
        _uuid = self.get_guid()
        request = models.CreateCorporateActionSourceRequest(
            scope=TestDataUtilities.tutorials_scope,
            code=f"test-corp-action-code-{_uuid}",
            display_name=f"test-corp-action-{_uuid}",
        )
        self.corporate_actions_sources_api.create_corporate_action_source(request)
        sources = self.corporate_actions_sources_api.list_corporate_action_sources()
        self.assertGreater(len(sources.values), 0)

    @unittest.skip("Not Implemented")
    def test_list_corporate_actions_for_one_day(self):
        _uuid = self.get_guid()
        request = models.CreateCorporateActionSourceRequest(
            scope=TestDataUtilities.tutorials_scope,
            code=f"test-corp-action-code-{_uuid}",
            display_name=f"test-corp-action-{_uuid}",
        )
        self.corporate_actions_sources_api.create_corporate_action_source(request)
        sources = self.corporate_actions_sources_api.get_corporate_actions(
            scope=f"test-corp-action-code-{_uuid}",
            code=f"test-corp-action-code-{_uuid}",
        )
