import sys

from lusidfeatures.entrypoint import get_features_file


def main(argv):
    get_features_file(argv)

if __name__ == "__main__":
    main(sys.argv)
