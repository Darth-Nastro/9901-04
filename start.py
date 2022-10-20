num = input()
while num  != 1:
    if (num % 2) == 0 and num != 1:
      num = num // 2
      print(num)
    else:
         num =((num*3) + 1)
         print(num)
