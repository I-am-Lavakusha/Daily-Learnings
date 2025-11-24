mat=[]
row, col=4,5
no=0
for i in range(row):
  colu=[]
  for j in range(col):
    colu.append(no)
    no+=1
  mat.append(colu)
print(mat)
for i in range(len(mat)):
  print(i)
  for j in range(len(mat[i])):
    print(mat[i][j], end=" ")
  print()

print(f"this is before the modification: {mat}")
mat[0].extend([6,7,8,9])
print(f"this is after the modification: {mat}")

print(f"let's reverse this matrix: {mat[0].reverse()}")
mat[1]=[54,53,52]
print(mat)

find=int(input("enter the element you want to remove: "))
for row in range(len(mat)):
  for col in range(len(mat[row])-1,-1,-1):
    if find==mat[row][col]:
        mat[row].remove(find)

print(mat)