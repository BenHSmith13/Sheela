import os
import format


def say(param):
    # os.system("say " + format.for_say(param))
    # os.system("say -v Agnes " + format.for_say(param))
    # os.system("say -v Kathy " + format.for_say(param))
    # os.system("say -v Princess " + format.for_say(param))
    # os.system("say -v Vicki " + format.for_say(param))
    os.system("say -v Victoria " + format.for_say(param))
    # os.system("say -v Bruce " + format.for_say(param))
    # os.system("say -v Fred " + format.for_say(param))
    # os.system("say -v Junior " + format.for_say(param))
    # os.system("say -v Ralph " + format.for_say(param))
    # os.system("say -v Albert " + format.for_say(param))
    # os.system("say -v 'Bad News' " + format.for_say(param))



def open_program(param):
    say("Opening " + param)
    os.system("open -a " + param)
