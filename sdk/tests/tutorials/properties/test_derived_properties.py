from collections import namedtuple

import lusid
import lusid.models as models
from lusid.api import instruments_api


class InstrumentLoader:
    __InstrumentSpec = namedtuple("InstrumentSpec", ["Figi", "Name","MoodysRating", "FitchRating"])

    __instruments = [
        __InstrumentSpec("BBG000FD8G46", "HISCOX LTD","Aaa","AAA"),
        __InstrumentSpec("BBG000DW76R4", "ITV PLC","Aaa","AAA"),
        __InstrumentSpec("BBG000PQKVN8", "MONDI PLC","Aaa","AAA"),
        __InstrumentSpec("BBG000BDWPY0", "NEXT PLC","Aaa","AAA"),
        __InstrumentSpec("BBG000BF46Y8", "TESCO PLC","Aaa","AAA"),
        __InstrumentSpec("BBG000BJPDZ1", "INTUITIVE SURGICAL Inc.","Aaa","AAA")
    ]

    def __init__(self, instruments_api: lusid.InstrumentsApi):
        self.instruments_api = instruments_api

    def load_instruments(self):
        instruments_to_create = {
            i.Figi: models.InstrumentDefinition(
                name=i.Name,
                identifiers={
                    "Figi": models.InstrumentIdValue(value=i.Figi)
                },
                properties=[
                    models.ModelProperty(key="Rating/MoodysRating/Value", value=models.PropertyValue(i.MoodysRating)),
                    models.ModelProperty(key="Rating/FitchRating/Value", value=models.PropertyValue(i.FitchRating))
                ]
            ) for i in self.__instruments
        }

        response = self.instruments_api.upsert_instruments(request_body=instruments_to_create)

        assert (len(response.failed) == 0)

        return sorted([i.lusid_instrument_id for i in response.values.values()])

    def delete_instruments(self):
        for i in self.__instruments:
            self.instruments_api.delete_instrument("Figi", i.Figi)



#instruments_api.get_instruments(identifier_type="Figi", request_body=["BBG000FD8G46"])
# response

# security_id = "BBG000FD8G46"
# response = query_otc_from_lusid(security_id)
# equity_test = response.values[security_id].instrument_definition

    #def create_derived_instrument_property_definition(code, display_name, data_type, derivation_formula):
    #    property_definitions_api = lusid_api_factory.build(lusid.api.PropertyDefinitionsApi)


        #Coalesce(Properties[Rating/MoodysRating/Value], Properties[Transaction/FitchRating/Value], 'Unknown')