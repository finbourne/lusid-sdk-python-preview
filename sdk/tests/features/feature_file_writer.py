def write_features_to_file(feature_list, filepath):
    text_to_write = "\n".join(feature_list)
    with open(filepath, "w+") as f:
        f.write(text_to_write)