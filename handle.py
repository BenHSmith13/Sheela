import web_procedures
import terminal_procedures
import custom
# import save_memo


def request(req):
    action = req['result']['action']
    print(action)

    if action.find('search') > -1:
        print(req)
        web_procedures.google(req['result']['parameters']['q'])
    elif action.find('open') > -1:
        print(req)
        terminal_procedures.open_program(req['result']['parameters']['app_name'])
    elif action.find('fun') > -1:
        print(req)
        custom.joke()
    # elif action == 'notes.save':
    #     print(req)
    #     save_memo

