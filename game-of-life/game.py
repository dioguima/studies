# import sys
# import time

# matrix_size = 10

# def print_matrix(matrix):
#     string_to_print = ''
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if j < matrix_size - 1:
#                 string_to_print += str(matrix[i][j]) + ' '
#             else:
#                 string_to_print += str(matrix[i][j]) + '\n'
#     print(string_to_print)
#     sys.stdout.flush()

# if __name__ == '__main__':
#     matrix = [[0 for j in range(matrix_size)] for i in range(matrix_size)]

#     print_matrix(matrix)
    
#     # while True:
#     for j in range(1,5):
#         matrix[0][0] += 1
#         # print('waiting : '+ str(j), end='\r')
#         print_matrix(matrix)
#         # sys.stdout.flush()
#         time.sleep(1)

# # print(matrix)

import numpy as np
import matplotlib.pyplot as plt

plt.imshow(np.random.random((50,50)))
plt.colorbar()
plt.show()