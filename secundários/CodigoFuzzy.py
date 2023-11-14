import numpy as np #biblioteca de funções de arrays multidimensionais, álgebra linear e estatística
import skfuzzy as fuzz #biblioteca de lógica fuzzy
from skfuzzy import control as ctrl #importa o módulo control, usado junto com a biblioteca para desenvolver sistemas difusos

# Criando as variáveis de problema
potencial = ctrl.Antecedent(np.arange(0, 15, 1), 'potencial')
temperatura = ctrl.Antecedent(np.arange(0, 51, 1), 'temperatura')
qualidade = ctrl.Consequent(np.arange(0, 101, 1), 'qualidade')

# Criando as funções de pertinência para pH
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

#definir as condições iniciais da simulação
simulacao.input['potencial'] = 6.68
simulacao.input['temperatura'] = 19.0

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

# Visualizando o gráfico de cada função de pertinência
potencial.view()
temperatura.view()
qualidade.view()
