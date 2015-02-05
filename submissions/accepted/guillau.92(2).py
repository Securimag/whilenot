
"""
    +:  no import

    -:  for
        long solution
        not original
        active loop

"""

#Une boucle while c'est juste une histoire d'iterateur et d'exception
#La on boucle sur n'importe quelle chaine/tableau etc dans sens puis dans dans l'autre
class InfStr(str):
    def __iter__(self):
        return ItInfStr(self)
class ItInfStr:
    def __init__(self, sentence):
        self.sens = False
        self.sentence = sentence
        self.position = 0
    def __next__(self):
        if self.position == len(self.sentence)-1 or self.position == 0:
            self.sens = not self.sens
        old = self.position
        self.position = self.position+1 if self.sens else self.position-1
        return self.sentence[old]

st = InfStr("success")
for l in st :
    print(l);
