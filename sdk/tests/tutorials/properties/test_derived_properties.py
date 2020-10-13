import unittest

import json

import lusid

import lusid.models as models
from utilities import InstrumentLoader
from utilities import TestDataUtilities

class DerivedPropertyTests(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = TestDataUtilities.api_client()
        cls.scopes_api = lusid.ScopesApi(api_client)
        cls.property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        # load instruments from InstrumentLoader
        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

    def create_ratings_property(self, figi, fitch_value=None, moodys_value=None):

        ratings = ["Fitch", "Moodys"]

        for rating in ratings:
            property_definition = models.CreatePropertyDefinitionRequest(
                domain="Instrument",
                scope="Test-Demo",
                code="{}Rating".format(rating),
                display_name="{}Rating".format(rating),
                data_type_id=lusid.ResourceId(
                    scope="system", code="number"))

            try:
                # create property definition
                self.property_definitions_api.create_property_definition(
                    create_property_definition_request=property_definition)
            except lusid.ApiException as e:
                if json.loads(e.body)["name"] == "PropertyAlreadyExists":
                    pass

        properties = {"Instrument/Test-Demo/FitchRating": fitch_value, "Instrument/Test-Demo/MoodysRating": moodys_value}

        # upsert property definition
        for key in properties:
            if properties[key] is not None:
                property_request = [
                    models.UpsertInstrumentPropertyRequest(
                        identifier_type="Figi",
                        identifier=figi,
                        properties=[
                            models.ModelProperty(key=key,
                                                 value=models.PropertyValue(
                                                     metric_value=models.MetricValue(value=properties[key]))
                                                 )]
                    )]

                response = self.instruments_api.upsert_instruments_properties(
                    upsert_instrument_property_request=property_request)

    def get_instruments_with_deriv_prop(self, Figi):
        response = self.instruments_api.list_instruments(
                instrument_property_keys=["Instrument/Test-Demo/TestDerivedRating"],
                filter="Identifiers[Figi] eq '{}'".format(Figi))

        return response.values[0].properties[0].value.metric_value.value

    # def get_instruments_with_deriv_prop(self, Figi):
    #     response = self.instruments_api.get_instruments(identifier_type="Figi", request_body=[Figi])
    #     return response

    def test_derived_property(self):

        # create instrument property edge cases
        self.create_ratings_property("BBG000FD8G46", fitch_value = 10, moodys_value = 5)
        self.create_ratings_property("BBG000DW76R4")
        self.create_ratings_property("BBG000PQKVN8", moodys_value = 5)
        self.create_ratings_property("BBG000BDWPY0", fitch_value = 10)

        # create derived property using the 'Coalesce' derivation formula
        derivation_formula = "Coalesce(Properties[Instrument/Test-Demo/MoodysRating], Properties[Instrument/Test-Demo/FitchRating],0)"

        #create derived property request
        derived_prop_definition_req = models.CreateDerivedPropertyDefinitionRequest(
            domain="Instrument",
            scope="Test-Demo",
            code="TestDerivedRating",
            display_name="TestDerivedRating",
            data_type_id=lusid.ResourceId(
                scope="system",
                code="number"),
            derivation_formula=derivation_formula
        )

        try:
            # create property definition
            derived_prop_response = self.property_definitions_api.create_derived_property_definition(
                derived_prop_definition_req)
        except lusid.ApiException as e:
            if json.loads(e.body)["name"] == "PropertyAlreadyExists":
                pass

        #self.assertGreater(len(derived_prop_response.values), 0, "Response = 0")
        #todo add more tests for property defintion response

        #test case for derived property with both ratings
        both_ratings = self.get_instruments_with_deriv_prop("BBG000FD8G46")
        self.assertEqual(both_ratings, 5.0)

        #test case for derived property with no ratings
        no_ratings = self.get_instruments_with_deriv_prop("BBG000DW76R4")
        self.assertEqual(no_ratings, 0.0)

        #test case for derived property with fitch only
        fitch_only = self.get_instruments_with_deriv_prop("BBG000BDWPY0")
        self.assertEqual(fitch_only, 10.0)

        #test case for derived property with moodys only
        moodys_only = self.get_instruments_with_deriv_prop("BBG000PQKVN8")
        self.assertEqual(moodys_only, 5.0)

        #check why get_instruments response is empty at properties
        # both_ratings = self.get_instruments_with_deriv_prop("BBG000FD8G46")
        # print(both_ratings)


if __name__ == '__main__':
    unittest.main()
