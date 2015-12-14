import web_procedures
import terminal_procedures
import custom


def request(req):
    action = req['result']['action']
    print(action)

    if action.find('search') > -1:
        print(req)
        web_procedures.google(req['result']['resolvedQuery'])
    elif action.find('open') > -1:
        print(req)
        terminal_procedures.open_program(req['result']['parameters']['app_name'])
    elif action.find('fun') > -1:
        print(req)
        custom.joke()
    # elif params[0] in custom.commands:
    #     custom.request(params[0], params[2])
    # else:
    #     terminal_procedures.say("Sorry, I don't know that command")

