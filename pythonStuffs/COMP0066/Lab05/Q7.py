import pandas as pd


def convert_dict_to_pandas(dict):
    return pd.Series(dict)


if __name__ == "__main__":
    sample_dict = {"a": 12, "b": 24, "c": 48}
    s = convert_dict_to_pandas(sample_dict)
    print(s)
