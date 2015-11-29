# Import anything you need for custom commands
# import terminal_procedures

# Add any command you want to handle in this file to the commands list
commands = ['Custom', 'custom']


# Handle custom commands
def request(command, param):
    if command == 'Custom' or command == 'custom':
        print('Add Custom Commands')
