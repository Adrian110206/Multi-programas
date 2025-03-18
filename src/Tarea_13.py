def pizzas():
    pizzas_fav = ["extra extra", "Pepperoni", "con carne"]
    for pizza in pizzas_fav:
        if pizza=="extra extra":
            print("Me gusta esta pizza ya que pudo disfrutar de la mitad extra pepperoni y exrta queso")
        elif pizza=="Pepperoni":
            print("Me gusta esta pizza por que es la clasica.")
        elif pizza=="con carne":
            print("Me gusta esta pizza ya que aveces se necesita salir de la rutina diaria.")
    pizzas_fav.append("la Mexicana")
    print("Nueva pizza favorita añadida:", pizzas_fav[-1])
    print(pizzas_fav)
print(pizzas())