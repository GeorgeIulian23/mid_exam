
string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."

# [start, end, text]

patches = [[5, 14, "Conquista"], [26, 30, "King"], [43, 49, "Palace"]]

def inputuri():
    string = input("Da ne stringul")
    start = int(input("Te rog introdu startul"))
    end = int(input("Te rog introdu sfarsitul"))
    word = input("alege un cuvant care sa aiba dimensiunile egale cu diferenta dintr start end")
    while start > len(list(string)):
            start = int(input("Te rog introdu startul"))

    while end > len(list(string)):
            end = int(input("Te rog introdu sfarsitul"))

    while len(word) > end - start:
            word = input("alege un cuvant care sa aiba dimensiunile egale cu diferenta dintr start end")

    return string, start, end, word

def functie_inlocuire():
    vrei_sa_in = 'D'
    aux = 0
    while vrei_sa_in == 'D':
        try:
            if aux == 0:
                string, start, end, word = inputuri()
            else:
                start = int(input("Te rog introdu startul"))
                end = int(input("Te rog introdu sfarsitul"))
                word = input("alege un cuvant care sa aiba dimensiunile egale cu diferenta dintr start end")
                while start > len(list(stringul_facut)):
                    start = int(input("Te rog introdu startul"))

                while end > len(list(stringul_facut)):
                    end = int(input("Te rog introdu sfarsitul"))

                while len(word) > end - start:
                    word = input("alege un cuvant care sa aiba dimensiunile egale cu diferenta dintr start end")

            list_word = list(word)
            if aux == 0:
                lista_string = list(string)
            else:
                lista_string = list(stringul_facut)
            index_lista_word = 0
            for index, value in enumerate(lista_string):
                if start-1 < index < end:
                    lista_string[index-1] = list_word[index_lista_word]
                    if index_lista_word < 9:
                        index_lista_word += 1
                    else:
                        break
            stringul_facut =''.join(lista_string)
            print(stringul_facut)
            aux += 1
            vrei_sa_in = input("Mai vrei sa inlocuiesti  alte variabile? Apasa D pt aface asta").upper()
        except Exception as e:
            print("pare rau {}".format(e))

functie_inlocuire()