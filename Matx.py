def Matrix(stolbec, stroka, nachalo, shag):
    chislo = nachalo
    print("Итог:\n")
    for i in range(nachalo, stroka*shag+nachalo, shag):
        for j in range (nachalo, stolbec*shag+nachalo, shag):
            print(chislo, end=" ")
            chislo+=shag
        print()