import unittest

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from lusid.exceptions import ApiException
from utilities import TestDataUtilities


class Instruments(unittest.TestCase):
    property_definitions_api = None

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = TestDataUtilities.api_client()

        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.property_definitions_api = lusid.PropertyDefinitionsApi(api_client)

    @classmethod
    def ensure_property_definition(cls, code):

        try:
            cls.property_definitions_api.get_property_definition(
                domain="Instrument",
                scope=TestDataUtilities.tutorials_scope,
                code=code
            )
        except ApiException as e:
            # property definition doesn't exist (returns 404), so create one
            property_definition = models.CreatePropertyDefinitionRequest(
                domain="Instrument",
                scope=TestDataUtilities.tutorials_scope,
                life_time="Perpetual",
                code=code,
                value_required=False,
                data_type_id=models.ResourceId("system", "string")
            )

            # create the property
            cls.property_definitions_api.create_property_definition(definition=property_definition)

    @lusid_feature("F41")
    def test_seed_instrument_master(self):
        response = self.instruments_api.upsert_instruments(request_body={

            "BBG000HC9638": models.InstrumentDefinition(
                name="PEARSON PLC",
                identifiers={
                    "Figi": models.InstrumentIdValue(value="BBG000HC9638"),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_1")
                }
            ),

            "BBG009LHM8H9": models.InstrumentDefinition(
                name="FRESNILLO PLC",
                identifiers={
                    "Figi": models.InstrumentIdValue(value="BBG009LHM8H9"),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_2")
                }
            ),

            "BBG001CY5LY0": models.InstrumentDefinition(
                name="RIO TINTO PLC",
                identifiers={
                    "Figi": models.InstrumentIdValue(value="BBG001CY5LY0"),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_3")
                }
            ),

            "BBG000GJZW38": models.InstrumentDefinition(
                name="BHP GROUP PLC",
                identifiers={
                    "Figi": models.InstrumentIdValue(value="BBG000GJZW38"),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_4")
                }
            ),

            "BBG000GL1MN0": models.InstrumentDefinition(
                name="SCHRODERS PLC",
                identifiers={
                    "Figi": models.InstrumentIdValue(value="BBG000GL1MN0"),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_5")
                }
            )
        })

        self.assertEqual(len(response.values), 5, response.failed)

    @lusid_feature("F22")
    def test_lookup_instrument_by_unique_id(self):

        figi = "BBG000HC9638"

        # set up the instrument
        response = self.instruments_api.upsert_instruments(request_body={
            figi: models.InstrumentDefinition(
                name="PEARSON PLC",
                identifiers={
                    "Figi": models.InstrumentIdValue(value=figi),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_1")
                }
            )
        })
        self.assertEqual(len(response.values), 1, response.failed)

        # look up an instrument that already exists in the instrument master by a
        # unique id, in this case an OpenFigi, and also return a list of aliases
        looked_up_instruments = self.instruments_api.get_instruments(identifier_type="Figi",
                                                                     request_body=[figi],
                                                                     property_keys=[
                                                                         "Instrument/default/ClientInternal"
                                                                     ])

        self.assertTrue(figi in looked_up_instruments.values, msg=f"cannot find {figi}")

        instrument = looked_up_instruments.values[figi]
        self.assertTrue(instrument.name, "PEARSON PLC")

        property = next(filter(lambda i: i.key == "Instrument/default/ClientInternal", instrument.properties), None)
        self.assertTrue(property.value, "internal_id_1")

    @lusid_feature("F23")
    def test_list_available_identifiers(self):

        identifiers = self.instruments_api.get_instrument_identifier_types()
        self.assertGreater(len(identifiers.values), 0)

    @lusid_feature("F24")
    def test_list_all_instruments(self):

        page_size = 5

        # list the instruments, restricting the number that are returned
        instruments = self.instruments_api.list_instruments(limit=page_size)

        self.assertLessEqual(len(instruments.values), page_size)

    @lusid_feature("F25")
    def test_list_instruments_by_identifier_type(self):

        figis = ["BBG000HC9638", "BBG009LHM8H9", "BBG001CY5LY0"]

        # get a set of instruments querying by FIGIs
        instruments = self.instruments_api.get_instruments(identifier_type="Figi", request_body=figis)

        for figi in figis:
            self.assertTrue(figi in instruments.values, msg=f"{figi} not returned")

    @lusid_feature("F26")
    def test_edit_instrument_property(self):

        property_value = models.PropertyValue(label_value="Insurance")
        property_key = f"Instrument/{TestDataUtilities.tutorials_scope}/CustomSector"
        identifier_type = "Figi"
        identifier = "BBG000HC9638"

        # update the instrument
        self.instruments_api.upsert_instruments_properties(upsert_instrument_property_request=[
            models.UpsertInstrumentPropertyRequest(
                identifier_type=identifier_type,
                identifier=identifier,
                properties=[models.ModelProperty(key=property_key, value=property_value)]
            )
        ])

        # get the instrument with value
        instrument = self.instruments_api.get_instrument(
            identifier_type=identifier_type,
            identifier=identifier,
            property_keys=[property_key]
        )

        self.assertGreaterEqual(len(instrument.properties), 1)

        prop = list(
            filter(lambda p: p.key == property_key and p.value.label_value == property_value.label_value, instrument.properties))

        self.assertEqual(len(prop), 1, f"cannot find property key=${property_key} value={property_value}")

