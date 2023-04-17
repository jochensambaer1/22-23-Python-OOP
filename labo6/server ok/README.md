Network Monitoring Tool
This is a Python command-line tool for monitoring the online status of servers on a network. It uses ping to check whether a server is online, and stores the results of the checks in a JSON file. The tool can be run in two modes: management mode and check mode.

In management mode, the user can add or remove servers, view the list of servers, and modify program settings. In check mode, the tool performs periodic checks on the registered servers and generates an HTML report of the check results.

Usage
To run the program in management mode:

css
Copy code
python main.py manage
To run the program in check mode:

css
Copy code
python main.py check
Dependencies
Python 3.5+
Requests (optional, for HTTP checks)
Directory Structure
graphql
Copy code
.
├── checkers/                 # directory for checker modules
│   ├── base.py               # abstract base class for checkers
│   ├── ping.py               # checker module for ping checks
│   ├── http.py               # checker module for HTTP checks (optional)
│   └── ...                   # other checker modules (optional)
├── data/                     # directory for data files
│   ├── servers.json          # file for storing server information
│   ├── checks.json           # file for storing check results
│   └── ...                   # other data files (optional)
├── templates/                # directory for HTML templates
│   ├── report.html           # template for the report page
│   └── ...                   # other template files (optional)
├── utils/                    # directory for utility modules
│   ├── input.py              # module for handling user input
│   ├── output.py             # module for outputting information
│   └── ...                   # other utility modules (optional)
├── config.py                 # module for managing program settings
├── main.py                   # main module for running the program
└── README.md                 # documentation for the program