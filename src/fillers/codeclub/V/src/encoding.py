
def encode(string):
    length = len(string)
    i = 0
    while i < length:

        x = 0
        if string[i] == string[i+1]:
            x += 1
        print(i, x)
        i += 1

    print(string[66])
    #x = [x for x in string]
    #print(x)

def decoe():
    pass


string = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

encode(string)
