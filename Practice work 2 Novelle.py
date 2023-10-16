print ("Напишите Начать чтобы начать\nНапишите Выход чтобы закончить")

inpt = input()

#Переменные
lvl = 1
money = 100
wood = 50
iron = 50
rock = 50
food = 50
cow = 0
chicken = 0
ovca = 0
pshenica = 0
fruit = 0
vegetable = 0
warior = 0
luchnik = 0
naesdnik = 0
spy = 0
people = 100
day = 1
food_res = 5
wood_res = 5
rock_res = 5
iron_res = 5
hranilishe_animal = 20

#Массивы
builds = [" Ферма", " Шахта", " Лесопилка", " Казарма", "Жилое здание", "Рыбатское судно"]

#Функции
def text_1():
    return("Что вы хотите построить:\n1.Ферма\n2.Казарма\n3.Шахта\n4.Жилое здание\n5.Рыбатское судно")
def stats():
    return(f" Ур: {lvl} Деньги: {money}\n")
def resources():
    return(f"Древесина: {wood} Камень: {rock} Железо: {iron} Еда: {food}")
def menu():
    return("Введите число для:\n1.Строительство      4.Фермерство\n2.Шахты и Лесопилки  3.Казармы\n5.Продажа")

#Игра
if inpt == "Начать" or inpt == "начать":

    print("День - ", day, stats(), resources())
    while(True):

        print(menu())
        inpt = input()

        try:
            #Строительство
            if (inpt == "1"):

                print(text_1())
                inpt = input()

                #Ферма
                if(inpt == "1"):
                    print("Необходимые ресурсы\n25 Дерева, 15 Камня, 10 Еды\nПостроить?")
                    inpt = input()
                    if (inpt == "Да" or inpt == "да"):
                        if (wood >= 25 and rock >= 15 and food >= 10):
                            builds.append(" Ферма")
                            hranilishe_animal += 20
                            print("Успешно построенно")
                    elif (inpt == "Нет" or inpt == "нет"):
                        print(text_1()) 
                
                #Казарма
                elif(inpt == "2"):
                    print("Необходимые ресурсы\n20 Дерева, 25 Камня, 15 Еды\nПостроить?")
                    inpt = input()
                    if (inpt == "Да" or inpt == "да"):
                        if (wood >= 20 and rock >= 25 and food >= 15):
                            builds.append (" Казарма")
                            print("Успешно построенно")
                    elif (inpt == "Нет" or inpt == "нет"):
                        print(text_1())
                
                #Шахта
                elif(inpt == "3"):
                    print("Необходимые ресурсы\n25 Дерева, 30 Камня, 20 Еды\nПостроить?")
                    inpt = input()
                    if (inpt == "Да" or inpt == "да"):
                        if (wood >= 25 and rock >= 30 and food >= 20):
                            builds.append (" Шахта")
                            rock_res += 5
                            iron_res += 5
                            print("Успешно построенно")
                    elif (inpt == "Нет" or inpt == "нет"):
                        print(text_1())

                #Жилое здание
                elif(inpt == "4"):
                    print("Необходимые ресурсы\n20 Дерева, 10 Камня, 10 Еды\nПостроить?")
                    inpt = input()
                    if (inpt == "Да" or inpt == "да"):
                        if (wood >= 20 and rock >= 10 and food >= 10):
                            builds.append (" Жилое здание")
                            people += 15
                            print("Успешно построенно")
                    elif (inpt == "Нет" or inpt == "нет"):
                        print(text_1())
                    
                #Рыбатское судно
                elif(inpt == "5"):
                    print("Необходимые ресурсы\n30 Дерева, 10 Камня, 15 Еды\nПостроить?")
                    inpt = input()
                    if (inpt == "Да" or inpt == "да"):
                        if (wood >= 30 and rock >= 10 and food >= 15):
                            builds.append [" Рыбатское судно"]
                            food_res += 2
                            print("Успешно построенно")
                    elif (inpt == "Нет" or inpt == "нет"):
                        print(text_1())
            #Шахты и лесопилки
            elif (inpt == "2"):
                print("Что вы хотите добыть:\n1.Камень\n2.Железо\n3.Древесина")
                inpt = input()
                #Камень
                if(inpt == "1"):
                    print("Скольких людей вы хотите выделить?")
                    inpt = input()
                    if (people >= int(inpt)):
                        people -= int(inpt)
                        rock_res += int(inpt) / 2
                        print("Успешно")
                    else:
                        print("Нехватка свободных людей")
                #Железо
                elif(inpt == "2"):
                    print("Скольких людей вы хотите выделить?")
                    inpt = input()
                    if (people >= int(inpt)):
                        people -= int(inpt)
                        iron_res += int(inpt) / 5
                    else:
                        print("Нехватка свободных людей")
                #Дерево
                elif(inpt == "3"):
                    print("Скольких людей вы хотите выделить?")
                    inpt = input()
                    if (people >= int(inpt)):
                        people -= int(inpt)
                        wood_res += int(inpt) / 2
                    else:
                        print("Нехватка свободных людей")
            #Казармы
            elif (inpt == "3"):
                print("Кого вы хотите обучить:\n1.Войн\n2.Лучник\n3.Наездник\n4.Разведчик")
                inpt = input()
                #Войн
                if(inpt == "1"):
                    print("Скольких вы хотите обучить?")
                    inpt = input()
                    if (people >= int(inpt)):
                        people -= int(inpt)
                        warior += int(inpt)
                    else:
                        print("Нехватка свободных людей")
                #Лучник
                elif(inpt == "2"):
                    print("Скольких вы хотите обучить?")
                    inpt = input()
                    if (people >= int(inpt)):
                        people -= int(inpt)
                        luchnik += int(inpt)
                    else:
                        print("Нехватка свободных людей")
                #Наездник
                elif(inpt == "3"):
                    print("Скольких вы хотите обучить?")
                    inpt = input()
                    if (people >= int(inpt)):
                        people -= int(inpt)
                        naesdnik += int(inpt)
                    else:
                        print("Нехватка свободных людей")
                #Разведчик
                elif(inpt == "4"):
                    print("Скольких вы хотите обучить?")
                    inpt = input()
                    if (people >= int(inpt)):
                        people -= int(inpt)
                        spy += int(inpt)
                    else:
                        print("Нехватка свободных людей")
            #Фермерство
            elif (inpt == "4"):
                print("Кого/Что вы хоите содежать/выращивать:\n1.Коровы\n2.Курица\n3.Овцы\n4.Пшеница\n5.Фрукты\n6.Овощи")
                inpt = input()
                #Коровы
                if(inpt == "1"):
                    print("Скольких вы хотите купить?\n10 монета = 1 ед")
                    inpt = input()
                    if (inpt <= hranilishe_animal and money >= int(inpt) * 10):
                        cow += int(inpt)
                        hranilishe_animal -= int(inpt)
                        food_res += cow 
                    elif (money < int(inpt) * 10):
                        print("Нехватает средств")
            
                #Курица
                elif(inpt == "2"):
                    print("Скольких вы хотите купить?5 монета = 1 ед")
                    inpt = input()
                    if (inpt <= hranilishe_animal and money >= int(inpt) * 5):
                        chicken += int(inpt)
                        hranilishe_animal -= int(inpt)
                        food_res += chicken / 2
                    elif (money < int(inpt) * 5):
                        print("Нехватает средств")
                #Овцы
                elif(inpt == "3"):
                    print("Скольких вы хотите купить?8 монета = 1 ед")
                    inpt = input()
                    if (inpt <= hranilishe_animal and money >= int(inpt) * 8):
                        ovca += int(inpt)
                        hranilishe_animal -= int(inpt)
                        food_res += ovca / 1,5
                    elif (money < int(inpt) * 8):
                        print("Нехватает средств")
                #Пшеница
                elif(inpt == "4"):
                    print("Скольких вы хотите вырастить?1 монета = 1 ед")
                    inpt = input()
                    if (inpt <= hranilishe_animal and money >= int(inpt)):
                        food_res += pshenica / 4
                    elif (money < int(inpt)):
                        print("Нехватает средств")
                #Фрукты
                elif(inpt == "5"):
                    print("Скольких вы хотите вырастить?1 монета = 1 ед")
                    inpt = input()
                    if (inpt <= hranilishe_animal and money >= int(inpt)):
                        food_res += fruit / 3
                    elif (money < int(inpt)):
                        print("Нехватает средств")
                #Овощи
                elif(inpt == "6"):
                    print("Скольких вы хотите вырастить?1 монета = 1 ед")
                    inpt = input()
                    if (inpt <= hranilishe_animal and money >= int(inpt)):
                        food_res += vegetable / 3
                    elif (money < int(inpt)):
                        print("Нехватает средств")
            elif (inpt == "5"):
                print ("Что вы хотите продать?")
                print (f"1.Древесина: {wood} 2.Камень: {rock} 3.Железо: {iron} 4.Еда: {food}")
                inpt = input()
                if (inpt == "1"):
                    print("Введите кол-во:")
                    inpt = input()
                    print("Вы получили: ", inpt)
                elif (inpt == "2"):
                    print("Введите кол-во:")
                    inpt = input()
                    print("Вы получили: ", inpt)
                elif (inpt == "3"):
                    print("Введите кол-во:")
                    inpt = input()
                    print("Вы получили: ", int(inpt) * 2)
                elif (inpt == "4"):
                    print("Введите кол-во:")
                    inpt = input()
                    print("Вы получили: ", inpt)

        except:
            print("Вы ввели некорректное значение\n")
        #Выход
        if(inpt == "выход" or inpt == "Выход"):
            print("Спасибо за игру")
            break
        #Пропуск дня
        elif (inpt == "пропустить" or inpt == "Пропустить"):
            day += 1
            food += food_res
            rock += rock_res
            wood += wood_res
            iron += iron_res
            lvl += 0,25

elif inpt == "exit" or inpt == "Exit":
    print("Спасибо за игру")
else:
    print("Вы ввели некорректное значение")