Count = int(input("Введите количество действий: "))
FirstNum = float(input("Введите первое число: "))
i = 0
Result = float
while i != Count:
    deistv = input("Выберите действие +, -, *, /, ** ")
    try: SecondNum = float(input("Введите число: "))
    except: print("Введите число!!!")
    if deistv == "+":
        Result = FirstNum + SecondNum
        print(f"Ответ: {Result}")
        FirstNum = Result
        i += 1
    elif deistv == "-":
        Result = FirstNum - SecondNum
        print(f"Ответ: {Result}")
        FirstNum = Result
        i += 1
    elif deistv == "/":
        if SecondNum != 0:
            Result = FirstNum / SecondNum
            print(f"Ответ: {Result}")
            FirstNum = Result
            i += 1
        else:
            print("Введенное число не может равняться 0 ")
    elif deistv == "*":
        Result = FirstNum * SecondNum
        print(f"Ответ: {Result}")
        FirstNum = Result
        i += 1
    elif deistv == "**":
        Result = FirstNum ** SecondNum
        print(f"Ответ: {Result}")
        FirstNum = Result
        i += 1
    else:
        print("Выберите корректное действие!")
    

