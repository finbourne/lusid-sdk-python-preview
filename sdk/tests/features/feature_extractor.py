import importlib
import inspect
import pkgutil

from features.get_project_root import get_project_root


def validate_feature_list(feature_list):
    for feature in feature_list:
        if feature == "":
            raise ValueError("lusid_feature error: Some decorated methods have no value passed. "
                             "Please make sure each lusid_feature decorator has a value code passed.")

    unique_features = set(feature_list)
    if len(unique_features) != len(feature_list):
        sorted_features = sorted(feature_list)
        for i, code in enumerate(sorted_features):
            if sorted_features[i] == sorted_features[i + 1]:
                raise ValueError(f'lusid_feature error: Feature code "{code}" is a duplicate. '
                                 'Please make sure each feature code is unique.')


def get_decorator_values_from_classes(module, feature_list):
    classes = inspect.getmembers(module, predicate=inspect.isclass)
    for cls_name, cls in classes:
        methods = inspect.getmembers(cls)
        for method_name, method in methods:  # Using method option as sourcecode parsing parses comments
            if hasattr(method, "decorator_value"):
                feature_list.append(method.decorator_value)


def get_decorator_values_from_functions(module, feature_list):
    functions = inspect.getmembers(module, predicate=inspect.isfunction)
    for function_name, function in functions:
        if hasattr(function, "decorator_value"):
            feature_list.append(function.decorator_value)


def extract_all_features_from_package(package_name):
    root = get_project_root()
    feature_list = []
    for importer, name, is_pkg in pkgutil.walk_packages([root]):
        if is_pkg or not name.startswith(package_name):
            continue

        module = importlib.import_module(name)
        get_decorator_values_from_classes(module, feature_list)
        # Functions are optional. To be decided after review.
        get_decorator_values_from_functions(module, feature_list)

    validate_feature_list(feature_list)
    return feature_list
