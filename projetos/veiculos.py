from datetime import datetime
import math


class Veiculo:

    def __init__(self, placa, modelo, ano, cor):

        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

        self.entrada = datetime.now()
        self.saida = None

        self.vaga = None

        self.valor_pago = 0



    def pagamento(self):

        tempo = self.saida - self.entrada

        horas = tempo.total_seconds() / 3600

        valor = math.ceil(horas) * 10

        self.valor_pago = valor

        return valor



class Carro(Veiculo):
    pass



class Moto(Veiculo):
    pass