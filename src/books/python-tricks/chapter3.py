def yell(text):
    return text.upper() + '!'

def greet(func):
    greeting = func('Testing out stuff')
    print(greeting)

x = list(map(yell, ['asd', 'ttt', 'pos']))
print(x)

def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)

x = speak('tere maailm')
print(x)


class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return self.n + x



add = lambda x, y: x + y

