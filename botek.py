from cleverbot import Cleverbot

def bot(pytanie):
    cb = Cleverbot()
    ans = cb.ask(pytanie)
    return ans


