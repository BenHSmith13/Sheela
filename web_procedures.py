import webbrowser
import terminal_procedures
import format


def google(param):
    terminal_procedures.say("Googleing " + param)
    url = "https://www.google.com/#q=" + format.for_google_search(param)
    webbrowser.open(url, new=2)


