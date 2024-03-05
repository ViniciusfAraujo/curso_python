"""
CONSTANTE = "Variaveis" que não vão mudar
muitas condições no mesmo IF (ruim)
<- Contagem de complexidade (ruim)
"""

velocidade = 62 # velocidade atual do carro 
rota = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGER = 1 # A distancia onde o radar pega

velocidade_passa_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = rota >= (LOCAL_1 - RADAR_RANGER) and rota <= (LOCAL_1 + RADAR_RANGER)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_passa_radar_1

if velocidade_passa_radar_1:
    print('velocidade ultrapassada do radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')

