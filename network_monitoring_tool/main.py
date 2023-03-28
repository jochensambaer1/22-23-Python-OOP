from server import Server
import checks
import logs

import argparse
import json

from server import Server
import checks
import logs


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Network monitoring tool.')
    parser.add_argument('--add', metavar='HOSTNAME', help='Add a new server to monitor.')
    parser.add_argument('--remove', metavar='HOSTNAME', help='Remove a server from monitoring.')
    parser.add_argument('--list', action='store_true', help='List all monitored servers.')
    parser.add_argument('--check', action='store_true', help='Perform a check on all monitored servers.')
    args = parser.parse_args()

    # Initialize the servers list
    servers = []
    with open('data/servers.json', 'r') as f:
        server_data = json.load(f)
        for server_dict in server_data:
            servers.append(Server.from_dict(server_dict))

    # Handle command-line arguments
    if args.add:
        servers.append(Server(args.add))
        with open('data/servers.json', 'w') as f:
            json.dump([s.to_dict() for s in servers], f, indent=2)
        print(f'Server "{args.add}" added.')
    elif args.remove:
        servers = [s for s in servers if s.hostname != args.remove]
        with open('data/servers.json', 'w') as f:
            json.dump([s.to_dict() for s in servers], f, indent=2)
        print(f'Server "{args.remove}" removed.')
    elif args.list:
        for server in servers:
            print(server.hostname)
    elif args.check:
        for server in servers:
            success = checks.ping(server.hostname)
            if success:
                print(f'Ping check for {server.hostname} succeeded.')
            else:
                print(f'Ping check for {server.hostname} failed.')
                logs.log(server.hostname, 'Ping check failed.')
