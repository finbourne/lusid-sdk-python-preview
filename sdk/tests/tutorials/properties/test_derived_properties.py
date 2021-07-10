# import general python packages
import unittest
import logging
import json

# import lusid specific packages
import lusid
import lusid.models as models
from utilities import InstrumentLoader
from utilities import TestDataUtilities

# setup logging configuration
logging.basicConfig(level=logging.INFO)


class DerivedPropertyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a configured API client factory
        api_client_factory = TestDataUtilities.api_client_factory()
        cls.property_definitions_api = api_client_factory.build(lusid.PropertyDefinitionsApi)
        cls.instruments_api = api_client_factory.build(lusid.InstrumentsApi)
        # load instruments from InstrumentLoader
        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

    def create_ratings_property(self, *ratings):

        ratings = [*ratings]
        global scope
        scope = "Derived"

        for rating in ratings:
            property_definition = models.CreatePropertyDefinitionRequest(
                domain="Instrument",
                scope=scope,
                code=f"{rating}Rating",
                display_name=f"{rating}Rating",
                data_type_id=lusid.ResourceId(scope="system", code="number"),
            )

            try:
                # create property definition
                self.property_definitions_api.create_property_definition(
                    create_property_definition_request=property_definition
                )
            except lusid.ApiException as e:
                if json.loads(e.body)["name"] == "PropertyAlreadyExists":
                    logging.info(
                        f"Property {property_definition.domain}/{property_definition.scope}/{property_definition.display_name} already exists"
                    )

    def upsert_ratings_property(self, figi, fitch_value=None, moodys_value=None):

        properties = {
            f"Instrument/{scope}/FitchRating": fitch_value,
            f"Instrument/{scope}/MoodysRating": moodys_value,
        }

        # upsert property definition
        for key in properties:
            if properties[key] is not None:
                property_request = [
                    models.UpsertInstrumentPropertyRequest(
                        identifier_type="Figi",
                        identifier=figi,
                        properties=[
                            models.ModelProperty(
                                key=key,
                                value=models.PropertyValue(
                                    metric_value=models.MetricValue(
                                        value=properties[key]
                                    )
                                ),
                            )
                        ],
                    )
                ]

                self.instruments_api.upsert_instruments_properties(
                    upsert_instrument_property_request=property_request
                )

    def get_instruments_with_derived_prop(self, figi):
        response = self.instruments_api.get_instruments(
            identifier_type="Figi",
            request_body=[figi],
            property_keys=[f"Instrument/{scope}/DerivedRating"],
        )

        return response.values[figi].properties[0].value.metric_value.value

    def test_derived_property(self):

        self.create_ratings_property("Fitch", "Moodys")

        # create instrument property edge cases and upsert (using arbitrary numeric ratings)
        self.upsert_ratings_property("BBG000FD8G46", fitch_value=10, moodys_value=5)
        self.upsert_ratings_property("BBG000DW76R4")
        self.upsert_ratings_property("BBG000PQKVN8", moodys_value=5)
        self.upsert_ratings_property("BBG000BDWPY0", fitch_value=10)

        # create derived property using the 'Coalesce' derivation formula
        code = "DerivedRating"
        derivation_formula = f"Coalesce(Properties[Instrument/{scope}/MoodysRating], Properties[Instrument/{scope}/FitchRating], 0)"

        # create derived property request
        derived_prop_definition_req = models.CreateDerivedPropertyDefinitionRequest(
            domain="Instrument",
            scope=scope,
            code=code,
            display_name=code,
            data_type_id=lusid.ResourceId(scope="system", code="number"),
            derivation_formula=derivation_formula,
        )

        try:
            # create property definition
            self.property_definitions_api.create_derived_property_definition(
                derived_prop_definition_req
            )
        except lusid.ApiException as e:
            if json.loads(e.body)["name"] == "PropertyAlreadyExists":
                logging.info(
                    f"Property {derived_prop_definition_req.domain}{derived_prop_definition_req.scope}/{derived_prop_definition_req.display_name} already exists"
                )

        # test case for derived property with both ratings
        moodys_then_fitch = self.get_instruments_with_derived_prop("BBG000FD8G46")
        self.assertEqual(moodys_then_fitch, 5.0)

        # test case for derived property with no ratings
        no_ratings = self.get_instruments_with_derived_prop("BBG000DW76R4")
        self.assertEqual(no_ratings, 0.0)

        # # test case for derived property with fitch only
        fitch_only = self.get_instruments_with_derived_prop("BBG000BDWPY0")
        self.assertEqual(fitch_only, 10.0)

        # test case for derived property with moodys only
        moodys_only = self.get_instruments_with_derived_prop("BBG000PQKVN8")
        self.assertEqual(moodys_only, 5.0)


if __name__ == "__main__":
    unittest.main()
