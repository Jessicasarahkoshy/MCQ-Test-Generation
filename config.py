import yaml
def config(file_name):
    file= open(file_name, 'r')
    config_values = yaml.safe_load(file)
    return config_values
