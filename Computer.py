import random


class IA:
    def __init__(self, numero):
        self.numero = numero

    def joue(self, grille):
        pass


class IA_stp(IA):
    def __init__(self, numero):
        super().__init__(numero)
        
    def joue(self, grille):
        for i in range(3):
            for j in range(3):
                if grille[i, j] == 0:
                    return i, j


class IA_rdm(IA):
    def __init__(self, numero):
        super().__init__(numero)
        
    def joue(self, grille):
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        while grille[i, j] != 0:
            i = random.randint(0, 2)
            j = random.randint(0, 2)
        return i, j