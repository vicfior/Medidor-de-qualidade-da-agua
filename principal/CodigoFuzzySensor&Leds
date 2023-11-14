import serial
import time
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#Define a porta serial e taxa de transmissão (baud rate) do arduino
porta_serial = 'COM3'
baud_rate = 9600

#Abre a porta serial
ser = serial.Serial(porta_serial, baud_rate, timeout = 0.5)

phValor = 0
temperatura_serial = None
valor_lido = False  # Variável de controle

def ler_dados_arduino():
    linha = ser.readline().strip()  # Lê uma linha de dados da porta serial
    return linha.decode('utf-8')

while not valor_lido:  # Continue lendo até que um valor seja lido
    linha = ler_dados_arduino()
    if linha:
        valores = linha.split('|')
        if len(valores) == 2:  # Verifica se a linha possui os valores necessários
            phValor = float(valores[0].strip().split(":")[1].strip())
            temperatura_str = valores[1].strip().split(":")[1].strip()
            temperatura_str = temperatura_str.replace(u'\xb0C', "")  #Remove "°C"
            temperatura_str = temperatura_str.strip()  #Remove espaços em branco extras
            try:
                temperatura_serial = float(temperatura_str)
                if 0 <= temperatura_serial <= 50:  #Verifica se a temperatura está dentro do intervalo esperado
                    valor_lido = True  # Marque o valor como lido
                else:
                    print("Valor de temperatura fora do intervalo esperado.")
            except ValueError:
                print("Valor inválido para temperatura: " + temperatura_str)

                
print('pH Value: {} | Temperatura: {} C'.format(phValor, temperatura_serial))

if temperatura_serial is not None:
# Variáveis de problema
    potencial = ctrl.Antecedent(np.arange(0, 15, 1), 'potencial')
    temperatura = ctrl.Antecedent(np.arange(0, 51, 1), 'temperatura')
    qualidade = ctrl.Consequent(np.arange(0, 101, 1), 'qualidade')

# funções de pertinência para pH
    potencial['Ácido'] = fuzz.trapmf(potencial.universe, [0,0,5,7])
    potencial['Neutro'] = fuzz.trimf(potencial.universe, [6,7,9])
    potencial['Básico'] = fuzz.trapmf(potencial.universe, [7,9,14,14])

# funções de pertinência para a temperatura
    temperatura['fria'] = fuzz.trapmf(temperatura.universe, [0,0,15,22])
    temperatura['amena'] = fuzz.trapmf(temperatura.universe, [16,22,30,35])
    temperatura['quente'] = fuzz.trapmf(temperatura.universe, [29,35,50,50])

    #funções de pertinência para a qualidade
    qualidade['Muito ruim'] = fuzz.trapmf(qualidade.universe, [0,0,21,33])
    qualidade['ruim'] = fuzz.trapmf(qualidade.universe, [16.6,28,42,51.6])
    qualidade['boa'] = fuzz.trapmf(qualidade.universe, [38.4,55,67,74])
    qualidade['excelente'] = fuzz.trapmf(qualidade.universe, [66.4,86.5,100,100])

    #regras:
    regras = []
    regras.append(ctrl.Rule(potencial['Ácido'] & temperatura['quente'], qualidade['Muito ruim']))
    regras.append(ctrl.Rule(potencial['Ácido'] & temperatura['amena'], qualidade['ruim']))
    regras.append(ctrl.Rule(potencial['Ácido'] & temperatura['fria'], qualidade['Muito ruim']))

    regras.append(ctrl.Rule(potencial['Neutro'] & temperatura['quente'], qualidade['boa']))
    regras.append(ctrl.Rule(potencial['Neutro'] & temperatura['amena'], qualidade['excelente']))
    regras.append(ctrl.Rule(potencial['Neutro'] & temperatura['fria'], qualidade['boa']))

    regras.append(ctrl.Rule(potencial['Básico'] & temperatura['quente'], qualidade['Muito ruim']))
    regras.append(ctrl.Rule(potencial['Básico'] & temperatura['amena'], qualidade['ruim']))
    regras.append(ctrl.Rule(potencial['Básico'] & temperatura['fria'], qualidade['Muito ruim']))

    #Criando um sistema de controle difuso
    sistema = ctrl.ControlSystem(regras)

    #Simular o sistema de controle difuso
    simulacao = ctrl.ControlSystemSimulation(sistema)

    #condições iniciais da simulação
    simulacao.input['potencial'] = phValor
    #condições iniciais da simulação
    simulacao.input['temperatura'] = temperatura_serial
          
    #execução da simulação
    simulacao.compute()

    #saída da simulação
    qualidade_simulada = round(simulacao.output['qualidade'],2)

    if qualidade_simulada <= 33:
      print('A qualidade da água está em ' + str(qualidade_simulada) +  ' e é muito ruim')
    elif 16.6<qualidade_simulada<51.6:
      print('A qualidade da água está em ' + str(qualidade_simulada) +  ' e é ruim')
    elif 38.4<qualidade_simulada<74:
      print('A qualidade da água está em ' + str(qualidade_simulada) +  ' e é boa')
    elif qualidade_simulada>66.4:
      print('A qualidade da água está em ' + str(qualidade_simulada) +  ' e é excelente')

    # Função para acender as leds
    def acender_leds(qualidade):
        comando = ''
        if qualidade <= 33:
            #board.digital[3].write(True)
            comando = 'A'
        elif 16.6<qualidade<51.6:
            #board.digital[4].write(True)
            comando = 'B'
        elif 38.4<qualidade<74:
            #board.digital[5].write(True)
            comando = 'C'
        elif qualidade>66.4:
            #board.digital[6].write(True)
            comando = 'D'

        if comando:
            ser.write(comando.encode())

    # Chamada da função
    acender_leds(qualidade_simulada)
