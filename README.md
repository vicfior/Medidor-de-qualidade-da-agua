<h1 align="center"> Medidor de qualidade da água </h1>

Este projeto de inteligência artificial tem como objetivo criar um medidor simples de qualidade da água baseando-se nos valores de pH e temperatura. 

## :clamp: Tecnologias utilizadas: 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  ![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)

## 	:pushpin: Descrição
O programa constitui em uma combinação entre as linguagens de programação Arduino e Python, para medir o pH e a temperatura da água utilizando sensores de pH e temperatura. O código em python foi utilizado para programar a lógica fuzzy do projeto e a definição das qualidades da água para determinadas faixas de valores de pH e temperaturas. O código em Arduino possibilitou a integração da lógica fuzzy em Python com os sensores e as leds, na protoboard.

## :gear: Ferramentas utilizadas: 
- sensor de pH PH4502C
- sensor de temperatura NTC 10K modelo MF58 tipo sonda
- Arduino UNO
- Protoboard
- Leds

## 	:grey_question: Como funciona o projeto

Para utilizar esse projeto é necessário possuir a IDE do Arduino e a linguagem Python instalada, bem como instalar as bibliotecas ```numpy``` e ```skfuzzy```. Após baixar os arquivos dos códigos, é necessário abrí-los na IDE do Arduino e executá-los. Além disso, será necessário possuir os sensores de pH e temperatura, fazer a montagem na protoboard e inserir as leds.
* Para instalar as bibliotecas execute o seguinte comando ``` pip install -U scikit-fuzzy ``` e ```pip install numpy```
**Interpretando o resultado**
  As leds representam o resultado da qualidade da água, portanto seguem o seguinte padrão quando acesas:
  1. Azul: qualidade da água é excelente
  2. Verde: qualidade da água é boa
  3. Amarelo: qualidade da água é ruim
  4. Vermelho: qualidade da água é muito ruim

> [!IMPORTANT]
> Vale ressaltar que, apesar de esse projeto ter se baseado em artigos e estudos científicos para encontrar valores reais de pH e temperatura para água própria para consumo, somente esses dados não são suficientes para indicar se uma água é de boa qualidade ou não, uma vez que outras substâncias e condições são levadas em consideração para essa definição.

## :white_check_mark: Requisitos
* Arduino IDE
* Linguagem Python instalada
* Protoboard
* Sensores
* Leds
