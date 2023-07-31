import pandas as pd
import numpy as np

#open_csvData
# df_data = pd.read_csv('assets/supermarket_sales.csv')
# df_data

labels = ['a','b','c']

myList = [10,20,30]

arr = np.array([10,20,30])

dictionary = {'a':10, 'b':20, 'c':30}

#indices automaticos iniciando de 0
pd.Series(labels)

#indices atribuidos
pd.Series(data=labels, index=myList)

#dicionarios ja possuem chaves e valores portanto a chave sera o index e o valor sera definido pelo valor da chave
pd.Series(dictionary)

paises = ['Brasil', 'EUA', 'Argentina', 'Japao', 'Franca']
random = [200000000, 4000000000, 150000000, 200000000, 90000000]

serie1 = pd.Series(data=random, index=paises)

#acessar pelo index
serie1['Brasil']