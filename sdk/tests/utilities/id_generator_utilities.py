import lusid
from lusid import ApiException
from utilities import TestDataUtilities


def delete_entities(id_generator):

    api_client = TestDataUtilities.api_client()

    property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
    portfolios_api = lusid.PortfoliosApi(api_client)
    cut_labels = lusid.CutLabelDefinitionsApi(api_client)
    orders_api = lusid.OrdersApi(api_client)
    recipes_api = lusid.ConfigurationRecipeApi(api_client)
    corporate_action_sources_api = lusid.CorporateActionSourcesApi(api_client)

    for item in id_generator.pop_scope_and_codes():
        entity = item[0]
        scope = item[1]
        code = item[2]
        try:
            if entity == "property_definition":
                domain = item[3]
                property_definitions_api.delete_property_definition(domain, scope, code)
            elif entity == "portfolio":
                portfolios_api.delete_portfolio(scope, code)
            elif entity == "cut_label":
                cut_labels.delete_cut_label_definition(code)
            elif entity == "order":
                orders_api.delete_order(scope, code)
            elif entity == "recipe":
                recipes_api.delete_configuration_recipe(scope, code)
            if entity == "ca_source":
                corporate_action_sources_api.delete_corporate_action_source(scope, code)
        except ApiException as ex:
            print(ex)
