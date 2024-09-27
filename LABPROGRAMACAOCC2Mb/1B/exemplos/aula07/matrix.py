def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(n) for n in row))

mat = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

print_matrix(mat)
#print(mat[1][1])

#for i in range(len(mat)):
#  for j in range(len(mat[i])):
#    print(mat[i][j])

#print("sem o indice")
#for row in mat:
#  for n in row:
#    print(n)