import unittest
from features.lusid_feature import lusid_feature


class ValidTests(unittest.TestCase):

    @lusid_feature("F1")
    def test_dummy_method_1(self):
        pass

    @lusid_feature("F2")
    def test_dummy_method_2(self):
        pass

    def test_control_method(self):
        pass

