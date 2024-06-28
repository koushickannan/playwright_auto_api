import configparser
import os

cur_path = os.path.abspath(os.path.dirname(__file__))
config_file = os.path.join(cur_path, r"../../config.ini")


# def get_config(section, key) -> str:
#     """
#     This method is used to fetch the config values for config file.
#     :param section: here we pass the config section value
#     :param key: here we pass the key value
#     :return: it returns the value based on the section & variable
#     """
#     config = configparser.ConfigParser()
#     config.read(config_file)
#     return config.get(section=section, option=key)

def get_config(env, section, key):
    """
    This method is used to fetch the config values for the given environment.
    :param env: the environment section
    :param section: the config section value
    :param key: the key value
    :return: the value based on the environment, section, and key
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    if section == "EndPoints" or section == "TestData":
        return config.get(section, key)
    else:
        return config.get(env, key)


def get_endpoint(key) -> str:
    """
    This method is used to fetch the different endpoints from config file
    :param key: here we pass the key parameter value
    :return: it returns the endpoint string
    """
    return get_config(None, "EndPoints", key)


# def set_config(section, key, value):
#     """
#     This method is used to set the config values in config file.
#     :param section: here we pass the config section value
#     :param key: here we pass the key
#     :param value: here we pass the actual value to be set for the key
#     :return: None
#     """
#     config = configparser.ConfigParser()
#     config.read(config_file)
#     config.set(section=section, option=key, value=value)
#     with open(config_file, "w") as configfile:
#         config.write(configfile)

def set_config(env, key, value):
    """
    This method is used to set the config values in the config file.
    :param env: the environment section
    :param key: the key
    :param value: the actual value to be set for the key
    :return: None
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    config.set(env, key, value)
    with open(config_file, "w") as configfile:
        config.write(configfile)
