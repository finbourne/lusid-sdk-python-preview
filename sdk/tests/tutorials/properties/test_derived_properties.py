import json
import logging
import unittest

import lusid
import lusid.models as models
from utilities import InstrumentLoader, IdGenerator
from utilities import TestDataUtilities
from utilities.id_generator_utilities import delete_entities


class DerivedPropertyTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        logging.basicConfig(level=logging.INFO)

        # create a configured API client
        api_client = TestDataUtilities.api_client()
        cls.property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)

        # load instruments from InstrumentLoader
        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()
        cls.id_generator = IdGenerator(scope=TestDataUtilities.tutorials_scope)

    @classmethod
    def tearDownClass(cls):
        delete_entities(cls.id_generator)

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
            finally:
                self.id_generator.add_scope_and_code("property_definition", property_definition.scope,
                                                     property_definition.code, ["Instrument"])

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
        self.upsert_ratings_property("BBG00KTDTF73", fitch_value=10, moodys_value=5)
        self.upsert_ratings_property("BBG00Y271826")
        self.upsert_ratings_property("BBG00L7XVNP1", moodys_value=5)
        self.upsert_ratings_property("BBG005D5KGM0", fitch_value=10)

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
        finally:
            self.id_generator.add_scope_and_code("property_definition", derived_prop_definition_req.scope,
                                                 derived_prop_definition_req.code, ["Instrument"])

        # test case for derived property with both ratings
        moodys_then_fitch = self.get_instruments_with_derived_prop("BBG00KTDTF73")
        self.assertEqual(moodys_then_fitch, 5.0)

        # test case for derived property with no ratings
        no_ratings = self.get_instruments_with_derived_prop("BBG00Y271826")
        self.assertEqual(no_ratings, 0.0)

        # # test case for derived property with fitch only
        fitch_only = self.get_instruments_with_derived_prop("BBG005D5KGM0")
        self.assertEqual(fitch_only, 10.0)

        # test case for derived property with moodys only
        moodys_only = self.get_instruments_with_derived_prop("BBG00L7XVNP1")
        self.assertEqual(moodys_only, 5.0)


if __name__ == "__main__":
    unittest.main()
