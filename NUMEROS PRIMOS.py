num= int(input("Define el numero que necesitas comprobar: "))
flag = False
if num == 0 or num == 1:
    print(num, "no es un numero primo")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if flag:
        print(num, "no es un numero primo")
    else:
        print(num, "es un numero primo")