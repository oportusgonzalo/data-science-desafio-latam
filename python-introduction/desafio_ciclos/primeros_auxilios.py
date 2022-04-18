
estimulos = input("¿Responde a estímulos? ").lower()

if estimulos == "si":
    print('Valorar la necesidad de llevarlo al hospital más cercano')
    print("Fin")
elif estimulos == "no":
    print("Abrir la vía aérea")
    respira = input("¿Respira? ").lower()
    if respira == "si":
        print("Permitirle posición de suficiente ventilación")
        print("Fin")
    elif respira == "no":
        print("Administrar 5 ventilaciones y llamar a ambulancia")
        signos_vida = input("¿Signos de vida? ").lower()
        if signos_vida == "si":
            print("Reevaluar a la espera de la ambulancia")
        elif signos_vida == "no":
            print("Administrar compresiones torácicas hasta que llegue ambulancia")

        while input("¿LLegó la ambulancia? ") != "si":
            signos_vida = input("¿Signos de vida? ").lower()
            if signos_vida == "si":
                print("Reevaluar a la espera de la ambulancia")
            elif signos_vida == "no":
                print("Administrar compresiones torácicas hasta que llegue ambulancia")
        print("Fin")
