from appdata import AppDataPaths

def get_pynecraft_config_path():
    app_path = AppDataPaths(".pynecraft")
    return app_path.app_data_path.replace("..",".")