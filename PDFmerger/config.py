import json


def get_conf(conf_path):
    conf_data = json.load(conf_path)
    return conf_data
