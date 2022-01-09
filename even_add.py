total1 = 0
total2 = 0
for i in range(2,101,2):
    total1 += i
#or
for i in range(1,101):
    if i % 2 == 0:
        total2 += i
print(total1)
print(total2)