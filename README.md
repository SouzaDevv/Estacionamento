# 🚗 Sistema de Estacionamento em Python

## 📖 Sobre o projeto

Este projeto consiste em um sistema de gerenciamento de estacionamento desenvolvido em Python utilizando Programação Orientada a Objetos (POO).

O sistema permite cadastrar veículos, controlar vagas, registrar entrada e saída, calcular automaticamente o valor da permanência e gerar relatórios.

Além disso, possui exportação dos dados em CSV, análise utilizando Pandas e envio do relatório por e-mail utilizando SMTP.

---

## 🚀 Funcionalidades

- Cadastro de veículos
- Remoção de veículos
- Busca por placa
- Edição de informações
- Controle das vagas
- Histórico de veículos
- Cálculo automático do pagamento
- Exportação do histórico em CSV
- Geração de relatório com Pandas
- Envio do relatório por e-mail

---

## 🛠 Tecnologias utilizadas

- Python 3
- Programação Orientada a Objetos
- datetime
- csv
- pandas
- smtplib
- EmailMessage

---

## 📂 Estrutura

```
projeto/

│
├── main.py
├── estacionamento.py
├── veiculos.py
├── historico.csv
├── relatorio.csv
└── README.md
```

---

## 💰 Regras do sistema

- Carros pagam R$10,00 por hora.
- Motos pagam R$5,00 por hora.
- O tempo é arredondado para cima.
- Não é permitido cadastrar placas duplicadas.
- O sistema controla automaticamente as vagas disponíveis.

---

## 📊 Relatórios

O sistema consegue gerar:

- Quantidade de veículos atendidos
- Valor total arrecadado
- Maior pagamento
- Valor médio dos pagamentos

---

## 📧 Envio de e-mail

O relatório pode ser enviado por e-mail utilizando SMTP do Gmail.

Para utilizar essa funcionalidade é necessário configurar uma Senha de Aplicativo do Google.

---

## 👨‍💻 Autor

Projeto desenvolvido como atividade prática da disciplina de Programação em Python.
