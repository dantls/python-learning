import pandas as pd
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import mean_absolute_error

observacoes = pd.read_csv('/content/drive/MyDrive/observ.csv', sep=';')

observacoes = np.array(observacoes[:9]["Fechamento"])

dados = []
x_treino = []
x_test = []
y = []
tam_janela = 3

for i in range(0,len(observacoes)-tam_janela): 
   dados.append(observacoes[i:tam_janela+i])
   y.append(observacoes[tam_janela+i])
   
dados = np.array(dados)
y = np.array(y)

dados.shape
y.shape

perceptron = Perceptron()
perceptron.fit(dados,y)
