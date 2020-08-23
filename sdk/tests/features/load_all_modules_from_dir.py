import importlib
import inspect
import os
import pkgutil


def validate_feature_list(feature_list):
    unique_values = set(feature_list)
    if len(unique_values) != len(feature_list):
        raise ValueError("lusid_feature error: Some decorated methods have the same feature codes. "
                         "Please make sure each feature code is unique.")

    for feature in feature_list:
        if feature == "":
            raise ValueError("lusid_feature error: Some decorated methods have no value passed. "
                             "Please make sure each lusid_feature decorator has a value code passed.")


def load_all_modules_from_dir(package_name):
    root = os.path.dirname(os.path.realpath("..\\"))
    feature_list = []
    for importer, name, is_pkg in pkgutil.walk_packages([root]):
        if is_pkg or not name.startswith(package_name):
            continue

        module = importlib.import_module(name)

        classes = inspect.getmembers(module, predicate=inspect.isclass)

        for cls_name, cls in classes:
            methods = inspect.getmembers(cls)
            for method_name, method in methods:  # Using method option as sourcecode parsing parses comments
                if hasattr(method, "decorator_value"):
                    feature_list.append(method.decorator_value)

    validate_feature_list(feature_list)
    return feature_list


# TODO: Pass package as a parameter as well as path
features = load_all_modules_from_dir("tests.tutorials")
print(features)
