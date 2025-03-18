def transporte_fav():
    transportes = ["bicicleta", "carro", "micro"]
    for transporte in transportes:
        if transporte=="bicicleta":
            print(f"me encanta usar {transporte}, ya que se me hace algo economico, pero me gusta estar en este acompañado")
        elif transporte=="carro":
            print(f"cuando estoy en {transporte} me siento relajado, con mucha comodidad, solo manejando y reflexionando sobre el futuro.")
        elif transporte=="micro":
            print(f"estar en este medio me agrada, ya que siempre hay alguien ahi, con el que pueda hablar, nunca se sabe.")
print(transporte_fav())