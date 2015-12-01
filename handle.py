import web_procedures
import terminal_procedures
import custom


def request(req):
    params = req.partition(" ")

    if params[0] == 'Print' or params[0] == 'print':
        print params[2]
    elif params[0] == 'Google' or params[0] == 'google':
        web_procedures.google(params[2])
    elif params[0] == 'Say' or params[0] == 'say':
        terminal_procedures.say(params[2])
    elif params[0] == 'Open' or params[0] == 'open':
        terminal_procedures.open_program(params[2])
    elif params[0] in custom.commands:
        custom.request(params[0], params[2])
    else:
        terminal_procedures.say("Sorry, I don't know that command")
