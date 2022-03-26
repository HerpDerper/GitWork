def Stroka():
    simvols = 0
    prob = 0
    zap = 0
    stroka = input("Cтрока: ")
    for i in stroka:
        if i ==" ":
            prob+=1
        if i ==",":
            zap+=1
        simvols+=1
    print("Символов: %s" %simvols)
    print("Пробелов: %s" %prob)
    print("Запятых: %s" %zap)