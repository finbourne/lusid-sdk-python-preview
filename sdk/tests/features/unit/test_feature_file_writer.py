import os
import unittest

from features.feature_extractor import extract_all_features_from_package
from features.feature_file_writer import write_features_to_file
from features.get_project_root import get_project_root


def remove_file(filepath):
    is_file = os.path.isfile(filepath)
    if is_file:
        os.remove(filepath)


def read_file(filepath):
    with open(filepath, "r") as f:
        features_from_file = f.read().splitlines()
    return features_from_file


class FeatureFileWriterTests(unittest.TestCase):
    def test_if_writer_writes_correctly(self):
        package = "tests.tutorials"
        features_filepath = os.path.join(get_project_root(), "features.txt")

        feature_list_from_function = extract_all_features_from_package(package)
        remove_file(features_filepath)
        write_features_to_file(feature_list_from_function, features_filepath)
        feature_list_from_file = read_file(features_filepath)

        self.assertEqual(feature_list_from_function, feature_list_from_file)
