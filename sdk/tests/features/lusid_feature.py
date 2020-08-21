

def lusid_feature(*feature_code):
    def wrap(f):
        def wrap_check_features(*args, **kwargs):
            return f(*args, **kwargs)
        wrap_check_features.decorator_value = feature_code    # <-- store the feature
        return wrap_check_features
    return wrap




