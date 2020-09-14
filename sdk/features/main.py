import sys

from lusidfeature.entrypoint import extract_features_to_file


def main(argv):
    extract_features_to_file(sys.argv)

if __name__ == "__main__":
    main(sys.argv)
