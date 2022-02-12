#matriz_np.py

#matriz com numpy

#para instalar um módulo (ou biblioteca) do python
#Entrar em C:\Users\Professor\AppData\Local\Programs\Python\Python37\Scripts
#pip install numpy

import numpy as np

print('Matriz usando numpy...')
matriz = np.array([
                                 [1,2,5,6],
                                 [3,4,8,9],
                                 [3,4,8,9],
                                 [1,2,5,6]
                            ])

print(matriz)
print('Matriz[3,3] = ', matriz[3][3])
