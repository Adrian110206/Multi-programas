def animales():
    felinos = ["Leopardo", "Tigre", "Leon"]
    for felino in felinos:
        if felino=="Leopardo":
            print("El leopardo es el animal muy veloz de a tierra, un depredador nato, especializado a sus presas veloces, haceindo ataques sigilosos y rapidos.")
        elif felino=="Tigre":
            print("el felino con la mordida siendo una de las mas fuertes y no solo eso, el tigre es muy fuerte dependiendo de su fuerza para cazar")
        elif felino=="Leon":
            print("el leon es el cazador en grupo de 3 o 4 siendo el mas fuerte de su grupo.")
    felinos.append("Jaguar")
    print("Nuevo felino añadida:", felinos[-1])
    print(felinos)
print(animales())