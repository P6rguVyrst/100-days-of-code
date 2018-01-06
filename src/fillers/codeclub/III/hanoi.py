# -*- coding: utf8 -*

class Hanoi(object):


    def __init__(self):
        self.turn = 0
        self.instructions = []

    def solve(self, N):
        r = self.worker(N, 'starting', 'ending', 'middle')
        return '\n'.join(self.instructions)

    def worker(self, n, source, target, helper):
        if n >= 1:
            self.worker(n-1, source, helper, target)
            self.move_disk(source, target)
            self.worker(n-1, helper, target, source)

    def move_disk(self, source, destination):
        self.turn += 1
        self.instructions.append(f'{self.turn}. Move disk from {source} pole to {destination} pole.')


def hanoi(N):
    push = Hanoi()
    instructions = push.solve(N)
    return instructions
