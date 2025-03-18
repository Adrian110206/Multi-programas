def name():
    nombre = " Juan Hernandez "
    print(f"El nombre con espacios es: '{nombre}'")
    nombre_limpio = nombre.strip()
    print(f"El nombre sin los espacios es: '{nombre_limpio}'")
print(name())