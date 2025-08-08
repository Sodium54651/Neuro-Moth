# import numpy as np
# # нажевать скалярное умножение и так и так
# def no_numpy_scalar(v1, v2):
#     rhh = 0
#     for rh in range(len(v1)):
#         rhh += v2[rh] * v1[rh]
#     return rh
# def numpy_scalar(v1, v2):
#     return v1 @ v2

# ===============================================================================
# что быстрее умножение без или с numpy ну конечно я да но нет короче numpy

# import numpy as np
# def no_numpy_mult(first, second):
#     losos = [[0 for rh in range(len(first))] for rhh in range(len(second))]
#     print(losos)
#     for rh in range(len(first)):
#         for rhh in range(len(second)):
#             losos[rh][rhh] = first[rh][rhh] * second[rhh][rh]
#     return losos
# def numpy_mult(first, second):
#     return first * second
# print(no_numpy_mult(np.arange(1, 10).reshape(3, 3), np.arange(1, 10).reshape(3, 3)))
# print(numpy_mult(np.arange(1, 10).reshape(3, 3), np.arange(1, 10).reshape(3, 3)))

# ======================================================================
# линейная нормаль

# import numpy as np
# def calculate_loss_function(X, w, y):
#     return np.linalg.norm(X @ w -y) ** 2

# ====================================================================
# линейная регрессия W*

# import numpy as np
# def solve_linear_regression(X, y):
#     return np.linalg.inv(X.T @ X) @ X.T @ y
























