import input
import json
import terminal_procedures
import format
import handle
import pdb

terminal_procedures.say('Welcome to Sheela, your personal digital assistant')

while True:
    result = json.loads(input.process())
    result = format.byteify(result)
    print(result)

    if result['result']['action'] == 'initiateRequest':
        terminal_procedures.say(result['result']['fulfillment']['speech'])
        result = json.loads(input.process())
        result = format.byteify(result)
        if len(result['result']['fulfillment']['speech']) > 0:
            terminal_procedures.say(result['result']['fulfillment']['speech'])
        else:
            handle.request(result)
