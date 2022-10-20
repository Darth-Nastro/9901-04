//itteration 1 this version only displays the values after input in the code under num
// This also displays each value after each operation
num = 1
while num  != 1:
    if (num % 2) == 0 and num != 1:
      num = num // 2
      print(num)
    else:
         num =((num*3) + 1)
         print(num)
// this section is the new code possibly looping. attempted test on repl.it but it didn' work due to cpu limit being reached.
// will attempt at home on visual studio system specs-> Rog Strix amd rx 600
num = 3 ** 3
while True:
  while num  != 1:
      if (num % 2) == 0 and num != 1:
        num = num // 2
        print(num)
      else:
           num =((num*3) + 1)
           print(num)
if (num == 1):
  num = num +1
  print(num)
