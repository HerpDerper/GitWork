import math as m

def Calculator():
    while(True):
        try:
            ch1 = int(input("Число 1: "))
            doing = input("Действие\n(log10 - логарифм по основанию 10, log2 - логарифм по основанию 10, ! - факториал, √ - корень\n* - умножение, / - деление, + - сложение, - - вычитание\n** - возведение в степень, // - деление нацело, % - остаток от деления,\nP - периметр параллелепипеда, S - площадь параллелепипеда, 0 - выход): ")
            if doing == "!":
                ch1 = m.factorial(ch1)
            elif doing =="log10":
                ch1=m.log10(ch1)
            elif doing =="log2":
                ch1=m.log2(ch1)
            elif doing =="√":
                ch1=m.sqrt(ch1)
            elif doing =="0":
                return
            else:
                ch2 = int(input("Число 2: "))
                if doing == "+":
                    ch1=ch1+ch2
                elif doing == "-":
                    ch1=ch1-ch2
                elif doing == "*":
                    ch1=ch1*ch2
                elif doing == "/":
                    ch1=ch1/ch2
                elif doing == "**":
                    ch1=ch1**ch2
                elif doing == "//":
                    ch1=ch1//ch2
                elif doing == "%":
                    ch1=ch1%ch2
                elif doing == "P":
                    ch3 = int(input("Число 3: "))
                    P = lambda a, b, c: 4 *(a + b + c)
                    ch1 = P(ch1, ch2, ch3)
                elif doing == "S":
                    ch3 = int(input("Число 3: "))
                    S = lambda a, b, c: 2 *(a * b + b * c + a * c)
                    ch1 = S(ch1, ch2, ch3)
            print("Итог: %s"%ch1)
        except:
            print("Неправильный ввод")
            continue