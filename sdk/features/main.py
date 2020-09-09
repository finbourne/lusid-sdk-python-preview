import argparse
import os
import sys

from features.feature_extractor import extract_all_features_from_package
from features.feature_file_writer import write_features_to_file
from features.get_project_root import get_project_root


def main(argv):
    ap = argparse.ArgumentParser(description="Get arguments from command line")
    ap.add_argument('-p', '--package', help='package name from the root folder, not including the root folder. Eg if '
                                            'root folder is "sdk", then package name should be "tests.tutorials", '
                                            'not "sdk.tests.tutorials"')
    ap.add_argument('-f', '--filename', help='Name of the features file to be created. By default "features.txt" and '
                                             'will be created in the root sdk folder. Path from the sdk root folder '
                                             'can be specified in this format '
                                             '<some-folder>/<another-folder>/filename.txt')

    args = vars(ap.parse_args())
    package_name = args["package"]
    filename = args["filename"]

    if package_name is None:
        package = "tests.tutorials"

    if filename is None:
        filename = "features.txt"

    filepath_from_root = os.path.join(get_project_root(), filename)

    feature_list = extract_all_features_from_package(package)
    write_features_to_file(feature_list, filepath_from_root)


if __name__ == "__main__":
    main(sys.argv)
