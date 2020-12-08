
string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."

# [start, end, text]

patches = [[5, 14, "Conquist"], [26, 31, "King"], [43, 49, "Palace"]]
def inputuri():
    string = input("Te rog introdu un string")

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

    while vrei_sa_in == 'D':
        try:
            string, start, end, word = inputuri()
            list_word = list(word)
            lista_string = list(string)
            index_lista_word = 0
            for index, value in enumerate(lista_string):
                if start-1 < index < end:
                    lista_string[index-1] = list_word[index_lista_word]
                    if index_lista_word < 9:
                        index_lista_word += 1
                    else:
                        break
            string =''.join(lista_string)
            print(string)
            vrei_sa_in = input("Mai vrei sa inlocuiesti  alte variabile? Apasa D pt aface asta").upper()
        except Exception:
            print("pare rau :(")
functie_inlocuire()