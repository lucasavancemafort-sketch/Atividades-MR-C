class Instrumento:
    def tocar(self):
        pass

class Violao(Instrumento):
    def tocar(self):
        return "Strum... Som de violão acústico."

class Bateria(Instrumento):
    def tocar(self):
        return "Tum Dum Tá! Som de bateria batendo forte."

class Piano(Instrumento):
    def tocar(self):
        return "Plim plam... Som de piano clássico."

instrumentos = [Violao(), Bateria(), Piano()]

for instrumento in instrumentos:
    print(instrumento.tocar())