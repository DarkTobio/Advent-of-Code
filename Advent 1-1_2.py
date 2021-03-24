#ADVENT OF CODE [1 - 1]

pw = [2,3,20,80,19,1]


for i in pw:
  for j in pw:
    if (i + j) == 100: #si 2 números suman 100, guardo los valores
      num1 = i
      num2 = j
      mult = i * j
      break

print(num1)
print(num2)
print(mult)


#ADVENT OF CODE [1 - 2]

for i in pw:
  for j in pw:
    for k in pw:
      if (i + j + k) == 100: #idem, pero 3 números
        numm1 = i
        numm2 = j
        numm3 = k
        multm = i * j * k
        break

print(numm1)
print(numm2)
print(numm3)
print(multm)