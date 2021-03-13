# program to print first 30 prime numbers

count =0
for i in range(2,200):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        count+=1
    if count == 30:
        break
