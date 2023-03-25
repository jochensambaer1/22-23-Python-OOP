import argparse
import json
import os
import platform
import subprocess
import sys
import time
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import requests

# Define the default configuration file name and path
DEFAULT_CONFIG_FILE = 'config.json'
DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), DEFAULT_CONFIG_FILE)

# Define the default log file name and path
DEFAULT_LOG_FILE = 'log.json'
DEFAULT_LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), DEFAULT_LOG_FILE)

# Define the default report file name and path
DEFAULT_REPORT_FILE = 'report.html'
DEFAULT_REPORT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), DEFAULT_REPORT_FILE)

# Define the default interval for checks in seconds
DEFAULT_CHECK_INTERVAL = 60

# Define the available check types
CHECK_TYPES = ['ping', 'web']

# Define the HTML template file name and path
HTML_TEMPLATE_FILE = 'template.html'
HTML_TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), HTML_TEMPLATE_FILE)


def ping(host):
    """
    Ping a given host using the ping command.
    Returns True if the ping was successful, False otherwise.
    """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0


def check_web(url):
    """
    Check if a given URL is reachable using the requests library.
    Returns True if the check was successful, False otherwise.
    """
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def load_config(config_path):
    """
    Load the configuration from a JSON file.
    Returns a dictionary with the configuration.
    """
    if not os.path.isfile(config_path):
        return {}
    with open(config_path) as config_file:
        return json.load(config_file)


def save_config(config_path, config):
    """
    Save the configuration to a JSON file.
    """
    with open(config_path, 'w') as config_file:
        json.dump(config, config_file)


def load_log(log_path):
    """
    Load the log data from a JSON file.
    Returns a list of log entries.
    """
    if not os.path.isfile(log_path):
        return []
    with open(log_path) as log_file:
        return json.load(log_file)


def save_log(log_path, log):
    """
    Save the log data to a JSON file.
    """
    with open(log_path, 'w') as log_file:
        json.dump(log, log_file)


def load_servers(config):
    """
    Load the server list from the configuration.
    Returns a list of server dictionaries.
    """
    if 'servers' not in config:
        return []
    return config['servers']


def save_servers(config, servers):
    """
    Save the server list to the configuration.
    """
    config['servers'] = servers


def add_server(config, address):
    """
    Add a new server to the server list in the configuration.
    """
    servers = load_servers(config)
    servers.append({'address': address})
    save_servers(config, servers)


def remove_server(config, index):
    """
    Remove a server from the server list in the configuration.
    """
    servers = load_servers(config)
    if index < 0 or index >= len(servers):
        return False
    del servers[index]
    save_servers(config, servers)
    return
