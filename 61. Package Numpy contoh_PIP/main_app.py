import numpy as np

list_a = [1,2,3,4,5]
maatrix_a = np.array([1,2,3])

# print(f"list A : {list_a**2}") <- tidak bisa 
print(f"matrix A : {maatrix_a**3}")

maatrix_b = np.array([(1,2), (2,3)])
print(f"matrix B : {maatrix_b**3}")

zeros_a = np.zeros((2,3))
print(f"zero A : {zeros_a}")

zeros_b = np.ones((2,2))
print(f"zero B : {zeros_b}")

jumlah = maatrix_b + maatrix_b**2
print(f"jumlah {jumlah}")