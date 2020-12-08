
lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu']


#1. Sortati lista dupa nume
#2. Determinati numarul de aparitii al fiecarui nume
#3. Listati numele care apare de cele mai multe ori in lista initiala.
#4. Listati numele care apare de cele mai putine ori in lista initiala.


def sortare_lista(lista2):
    return sorted(lista2, key=lambda x:x)

print(sortare_lista(lista_nume))

def punctul2(lista_nume):
    pct2=[{x:lista_nume.count(x)} for x in set(lista_nume)]
    return pct2

pct2 = punctul2(lista_nume)
print(pct2)
#valori unice in dictionar ce le voi prelua pt pct3


def functie_punctul3(pct2):
    lista_value = []
    for i in pct2:
        for value in i.values():
            lista_value.append(value)

    max_value = max(lista_value)

    rez_max = [i for i, j in enumerate(lista_value) if j == max_value]

    for value in rez_max:
        return pct2[value]

dict_cel_maimulte= functie_punctul3(pct2)

for i in dict_cel_maimulte.keys():
    print("persoana cu cea mai mare valoare {}".format(i))

def functie_punctul4(pct2):
    lista_value = []
    rez = []
    for i in pct2:
        for value in i.values():
            lista_value.append(value)
    min_value = min(lista_value)
    rez_min = [i for i, j in enumerate(lista_value) if j == min_value]
    for value in rez_min:
        rez.append(pct2[value])
    return rez

print(functie_punctul4(pct2))