grupo = input()
classe = input()
come = input()

if grupo == "vertebrado":
    if classe == "ave":
        if come == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    if classe == "mamifero":
        if come == "onivoro":
            print("homem")
        else:
            print("vaca")
if grupo == "invertebrado":
    if classe == "inseto":
        if come == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    if classe == "anelideo":
        if come == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
