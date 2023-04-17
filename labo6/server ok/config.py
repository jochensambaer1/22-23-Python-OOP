import json

SETTINGS = {
    "check_interval": 120,  # in seconds
}

def load_servers():
    """
    Load the registered servers from the data file.
    """
    try:
        with open("data/servers.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_servers(servers):
    """
    Save the registered servers to the data file.
    """
    with open("data/servers.json", "w") as f:
        json.dump(servers, f)

def load_checks():
    """
    Load the check results from the data file.
    """
    try:
        with open("data/checks.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_check(check):
    """
    Save a check result to the data file.
    """
    checks = load_checks()
    checks.append(check)
    with open("data/checks.json", "w") as f:
        json.dump(checks, f)

def get_setting(name):
    """
    Get the value of the specified setting.
    """
    return SETTINGS.get(name)

def set_setting(name, value):
    """
    Set the value of the specified setting.
    """
    SETTINGS[name] = value
