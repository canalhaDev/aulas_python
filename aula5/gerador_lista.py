lista = [
    {"nome":"Nickolas", "numero": "3195524546"},
    {"nome": "Lucas" , "numero": "31986029421"},
    {"nome": "Bruna", "numero": "3195524546"},
    {"nome": "Geovanna", "numero": "31971150522"},
    {"nome": "Fred", "numero": "31991204512"},
    {"nome": "Maysa", "numero": "31992195153"},
    {"nome": "Breno", "numero": "31996580028"},
    {"nome": "Duda", "numero": "31987540919"}
]

for pessoa in lista:
    print(pessoa["nome"])
    print(f"wa.me/{pessoa['numero']}")
    print("-="*20)