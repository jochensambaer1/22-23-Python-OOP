import sys
import argparse
import config
import management
import check
import report

def main():
    parser = argparse.ArgumentParser(description='Server monitoring tool')
    parser.add_argument('--config', help='Path to configuration file', default='config.json')
    parser.add_argument('--mode', help='Operating mode: management or check', default='check')
    args = parser.parse_args()

    config.load(args.config)

    if args.mode == 'management':
        management_menu()
    elif args.mode == 'check':
        check.run()
        report.generate()

if __name__ == '__main__':
    main()
