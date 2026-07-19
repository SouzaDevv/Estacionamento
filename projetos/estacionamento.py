from datetime import datetime
import csv
import pandas as pd
import smtplib
from email.message import EmailMessage

from veiculos import Carro, Moto


class Estacionamento:

    def __init__(self):

        self.veiculos = []

        self.historico = []

        self.vagas = {
            "A1": None, "A2": None, "A3": None,
            "B1": None, "B2": None, "B3": None,
            "C1": None, "C2": None, "C3": None
        }

    def inserir_veiculo(self):

        if None not in self.vagas.values():
            print("\nEstacionamento lotado.")
            return

        placa = input("Placa: ").upper()

        for veiculo in self.veiculos:

            if veiculo.placa == placa:
                print("Já existe um veículo com essa placa.")
                return

        modelo = input("Modelo: ")
        cor = input("Cor: ")
        ano = int(input("Ano: "))

        tipo = input("1 - Carro | 2 - Moto: ")

        if tipo == "1":

            veiculo = Carro(
                placa,
                modelo,
                ano,
                cor
            )

        elif tipo == "2":

            veiculo = Moto(
                placa,
                modelo,
                ano,
                cor
            )

        else:

            print("Tipo inválido.")
            return

        vaga = input("Digite a vaga: ").upper()

        if vaga not in self.vagas:

            print("Vaga inválida.")
            return

        if self.vagas[vaga] is not None:

            print("Essa vaga já está ocupada.")
            return

        veiculo.vaga = vaga

        self.vagas[vaga] = veiculo

        self.veiculos.append(veiculo)

        print(f"\nVeículo estacionado na vaga {vaga}!")

    def listar_veiculos(self):

        if len(self.veiculos) == 0:

            print("\nNenhum veículo estacionado.")
            return

        print("\n========== VEÍCULOS ==========")

        for veiculo in self.veiculos:

            print("----------------------------")
            print(f"Placa   : {veiculo.placa}")
            print(f"Modelo  : {veiculo.modelo}")
            print(f"Cor     : {veiculo.cor}")
            print(f"Ano     : {veiculo.ano}")
            print(f"Vaga    : {veiculo.vaga}")
            print(f"Entrada : {veiculo.entrada}")

    def procurar_veiculo(self):

        placa = input("Digite a placa: ").upper()

        for veiculo in self.veiculos:

            if veiculo.placa == placa:

                print("\nVeículo encontrado!\n")

                print(f"Placa   : {veiculo.placa}")
                print(f"Modelo  : {veiculo.modelo}")
                print(f"Cor     : {veiculo.cor}")
                print(f"Ano     : {veiculo.ano}")
                print(f"Vaga    : {veiculo.vaga}")
                print(f"Entrada : {veiculo.entrada}")

                return

        print("\nVeículo não encontrado.")


    def remover_veiculo(self):

        placa = input("Digite a placa do veículo: ").upper()

        for veiculo in self.veiculos:

            if veiculo.placa == placa:

                print("\nVeículo removido.")

                veiculo.saida = datetime.now()

                valor = veiculo.pagamento()

                print(f"Valor a pagar: R$ {valor:.2f}")

                self.historico.append(veiculo)

                self.vagas[veiculo.vaga] = None

                veiculo.vaga = None

                self.veiculos.remove(veiculo)

                return

    print("Veículo não encontrado.")

    def editar_veiculo(self):

        placa = input("Digite a placa do veículo: ").upper()

        for veiculo in self.veiculos:

            if veiculo.placa == placa:

                nova_placa = input("Nova placa: ").upper()

                for outro in self.veiculos:

                    if outro.placa == nova_placa and outro != veiculo:

                        print("Já existe um veículo com essa placa.")
                        return

                novo_modelo = input("Novo modelo: ")
                nova_cor = input("Nova cor: ")
                novo_ano = int(input("Novo ano: "))

                veiculo.placa = nova_placa
                veiculo.modelo = novo_modelo
                veiculo.cor = nova_cor
                veiculo.ano = novo_ano

                print("\nVeículo atualizado com sucesso!")

                return

        print("Veículo não encontrado.")

    def mostrar_estacionamento(self):

        print("\n========== MAPA DAS VAGAS ==========\n")

        for vaga, veiculo in self.vagas.items():

            if veiculo is None:

                print(f"{vaga} -> Livre")

            else:

                print(f"{vaga} -> {veiculo.placa}")

        def mostrar_estacionamento(self):

            print("\n========== MAPA DAS VAGAS ==========\n")

            for vaga, veiculo in self.vagas.items():

                if veiculo is None:

                    print(f"{vaga} -> Livre")

                else:

                    print(f"{vaga} -> {veiculo.placa}")

    def exportar_csv(self):

        if len(self.historico) == 0:

            print("Nenhum histórico para exportar.")
            return

        with open("historico.csv", "w", newline="", encoding="utf-8") as arquivo:

            escritor = csv.writer(arquivo)

            escritor.writerow([
                "Placa",
                "Modelo",
                "Cor",
                "Ano",
                "Entrada",
                "Saida",
                "Valor"
            ])

            for veiculo in self.historico:

                escritor.writerow([
                    veiculo.placa,
                    veiculo.modelo,
                    veiculo.cor,
                    veiculo.ano,
                    veiculo.entrada,
                    veiculo.saida,
                    veiculo.valor_pago
                ])

        print("CSV exportado com sucesso.")

    def filtrar_csv(self):

        try:

            df = pd.read_csv("historico.csv")

        except FileNotFoundError:

            print("O arquivo historico.csv não foi encontrado.")
            return

        quantidade = len(df)

        total = df["Valor"].sum()

        maior = df["Valor"].max()

        media = df["Valor"].mean()

        relatorio = pd.DataFrame({

            "Informação": [

                "Quantidade de veículos",

                "Valor arrecadado",

                "Maior pagamento",

                "Pagamento médio"

            ],

            "Valor": [

                quantidade,

                total,

                maior,

                media

            ]

        })

        relatorio.to_csv("relatorio.csv", index=False)

        print("Relatório criado com sucesso.")

    def enviar_email(self):

        destino = input("Digite o e-mail que receberá o relatório: ")

        email = EmailMessage()

        email["Subject"] = "Relatório Diário - Estacionamento"

        email["From"] = "SEU_EMAIL@gmail.com"

        email["To"] = destino

        email.set_content("""

Olá!

Segue em anexo o relatório diário do estacionamento.

Att,

Sistema de Estacionamento

""")

        try:

            with open("relatorio.csv", "rb") as arquivo:

                email.add_attachment(

                    arquivo.read(),

                    maintype="application",

                    subtype="octet-stream",

                    filename="relatorio.csv"

                )

        except FileNotFoundError:

            print("Crie o relatório antes de enviar o e-mail.")

            return

        try:

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

                smtp.login(

                    "SEU_EMAIL@gmail.com",

                    "SUA_SENHA_DE_APLICATIVO"

                )

                smtp.send_message(email)

            print("Relatório enviado com sucesso!")

        except Exception as erro:

            print(f"Erro ao enviar e-mail: {erro}")