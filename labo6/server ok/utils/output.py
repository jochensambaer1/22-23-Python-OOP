def print_servers(servers):
    """
    Print a list of servers to the console.
    """
    if not servers:
        print("There are no servers registered.")
    else:
        print("Registered servers:")
        for i, server in enumerate(servers, start=1):
            print(f"{i}. {server}")

def print_checks(checks):
    """
    Print a list of check results to the console.
    """
    if not checks:
        print("There are no check results.")
    else:
        print("Check results:")
        for check in checks:
            status = "online" if check["online"] else "offline"
            print(f"{check['timestamp']}: {check['server']} is {status}")
