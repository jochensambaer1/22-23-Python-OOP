import json
import os

LOGS_FILE = 'data/checks.json'

def log_check(server, success):
    # If the file exists, load it; otherwise, use an empty list
    if not os.path.isfile(LOGS_FILE):
        logs = []
    else:
        try:
            with open(LOGS_FILE, 'r') as f:
                logs = json.load(f)
        except (OSError, json.JSONDecodeError):
            logs = []

    # Log the check
    logs.append({
        'timestamp': datetime.now().isoformat(),
        'server': server.hostname,
        'success': success,
    })

    # Write the updated logs to the file
    try:
        with open(LOGS_FILE, 'w') as f:
            json.dump(logs, f, indent=2)
    except OSError:
        pass
