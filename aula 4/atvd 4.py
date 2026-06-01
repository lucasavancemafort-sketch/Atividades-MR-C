class Sensor:
    def __init__(self, temperatura):
        self.__temperatura = None
        self.set_temperatura(temperatura)

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, valor):
        if -50 <= valor <= 150:
            self.__temperatura = valor
        else:
            print(f"Erro: {valor}°C fora do limite do sensor")

    def status(self):
        t = self.__temperatura
        if t is None:
            return "Sem leitura"
        elif t <= 80:
            return "Normal"
        elif t <= 120:
            return "Alerta"
        else:
            return "Crítico"

testes = [25, 95, 135, 200]
for t in testes:
    s = Sensor(t)
    print(f"{t:4}°C → {s.status()}")