def nombre_usuario():
    name=input("hola usuario, me darias tu nombre?:")
    print(f"¡Hola {str(name.title())}, que gusto saber tu nombre!, te gustaria saber algo mas de python?")
    print(name.title())
    print(name.lower())
    print(name.upper())
print(nombre_usuario())
