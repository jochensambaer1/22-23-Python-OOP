import json
import os

LOGS_FILE = 'data/checks.json'

def log_check(server, success):
    # Read the current logs from the file
    logs = []
    if os.path.isfile(LOGS_FILE):
        with open(LOGS_FILE, 'r') as f:
            logs = json.load(f)

    # Append a new log entry
    logs.append({
        'timestamp': datetime.now().isoformat(),
        'server': server.hostname,
        'success': success,
    })

    # Write the logs back to the file
    with open(LOGS_FILE, 'w') as f:
        json.dump(logs, f, indent=2)
