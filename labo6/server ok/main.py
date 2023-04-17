import sys
import argparse

from server import ServerManager
from checker import ServerChecker

# Define argparse to parse command line arguments
parser = argparse.ArgumentParser(description='Network monitoring tool')
subparsers = parser.add_subparsers(dest='mode', help='Management mode or Check mode')

# Management mode parser
management_parser = subparsers.add_parser('manage', help='Management mode')
management_parser.add_argument('--add', help='Add server', metavar=('IP/hostname', 'description'))
management_parser.add_argument('--remove', help='Remove server', metavar='IP/hostname')
management_parser.add_argument('--show', help='Show registered servers', action='store_true')
management_parser.add_argument('--settings', help='Show current settings', action='store_true')

# Check mode parser
check_parser = subparsers.add_parser('check', help='Check mode')
check_parser.add_argument('--once', help='Perform checks once and exit', action='store_true')

args = parser.parse_args()

if args.mode == 'manage':
    # Create ServerManager object
    server_manager = ServerManager()

    if args.add:
        # Parse server description
        server_desc = args.add.split()
        if len(server_desc) > 1:
            server_manager.add_server(server_desc[0], server_desc[1])
        else:
            server_manager.add_server(server_desc[0])
    elif args.remove:
        server_manager.remove_server(args.remove)
    elif args.show:
        server_manager.show_servers()
    elif args.settings:
        server_manager.show_settings()
    else:
        # No command specified, show management mode help
        management_parser.print_help()

elif args.mode == 'check':
    # Create ServerChecker object
    server_checker = ServerChecker()

    if args.once:
        server_checker.check_servers()
    else:
        # Regular check mode, loop indefinitely
        while True:
            server_checker.check_servers()
