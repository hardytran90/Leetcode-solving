s = "LLRRLR"

balance = 0
count = 0
   
for i in s:
    if i == "R":
        balance += 1
        if balance == 0:
            count += 1
    elif i == "L":
        balance -= 1
        if balance == 0:
            count += 1

print(count)