import os
import format


def say(param):
    os.system("say " + format.for_say(param))


def open_program(param):
    say("Opening " + param)
    os.system("open -a " + param)
