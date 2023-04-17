def get_input(message, choices=None):
    """
    Prompt the user for input with an optional list of valid choices.
    """
    while True:
        user_input = input(message).strip()
        if not user_input:
            print("Please enter a value.")
        elif choices is not None and user_input not in choices:
            print(f"Please enter one of the following: {', '.join(choices)}.")
        else:
            return user_input
