import importlib
import inspect
import os
import pkgutil
import pyclbr


def validate_feature_list(feature_list):
    unique_values = set(feature_list)
    if len(unique_values) != len(feature_list):
        raise ValueError("lusid_feature error: Some decorated methods have the same feature codes. "
                         "Please make sure each feature code is unique.")

    for feature in feature_list:
        if feature == "" or feature is None:
            raise ValueError("lusid_feature error: Some decorated methods have no value passed. "
                             "Please make sure each lusid_feature decorator has a value code passed.")


def load_all_modules_from_dir(root):
    feature_list = []
    for importer, name, is_pkg in pkgutil.walk_packages([root]):
        if is_pkg:
            continue

        classes = pyclbr.readmodule(name)

        for c in classes.values():

            if not c.module.startswith("tutorials"):
                continue

            for _, cls in inspect.getmembers(importlib.import_module(c.module), inspect.isclass):
                source_lines = inspect.getsourcelines(cls)[0]
                for i, line in enumerate(source_lines):
                    line = line.strip()
                    if line.split('(')[0].strip() == "@lusid_feature":  # leaving a bit out
                        feature = line.split('"')
                        if len(feature) < 3:
                            raise ValueError("lusid_feature error: Some decorated methods have no value passed. "
                                             "Please make sure each lusid_feature decorator has a value code passed.")
                        feature = feature[1]
                        feature_list.append(feature.upper())
                        print(feature)

    validate_feature_list(feature_list)
    return feature_list


features = load_all_modules_from_dir(os.path.dirname(os.path.realpath("../tutorials")))
