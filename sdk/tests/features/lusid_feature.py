def lusid_feature(feature_code):
    if type(feature_code) != str:
        raise ValueError("lusid_feature error: Only strings should be passed as the decorator parameter")

    def wrap_method(method_for_testing):
        def method(*unit_test_args):
            return method_for_testing(*unit_test_args)
        method.decorator_value = feature_code  # <-- store the feature
        return method

    return wrap_method



