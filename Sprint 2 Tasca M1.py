#Quantes vegades apareix el número 3.

print(ls.count(3))

#Quantes vegades apareixen els nombres 3 i 4?

print(ls.count(4))

#Quin és el número més gran?

print(max(ls))

#Quins són els 3 números més petits?

ls.sort()

print(ls[0:3])

#Quin és el rang d’aquesta llista?

print(range(len(ls)))

#Crea un diccionari de la següent forma i respon a les preguntes:
compra = { "Pomes" : {"Qty": 5, "€": 0.42}, "Peres" : {"Qty": 3, "€": 0.66} }

#Afegeix alguna fruita més
compra.update({"Platan": {"Qty": 4, "€": 0.99}})

#Quant han costat les peres en total?
peresCost = compra.get("Peres").get("Qty") * compra.get("Peres").get("€")
print(peresCost)

#Quantes fruites hem comprat en total?
totalFrutes = 0

for key in compra.keys():
totalFrutes = compra[key].get("Qty") + totalFrutes
     
print(totalFrutes)

#Quina és la fruita més cara?
preuMes = 0

for k in list(compra.keys()):
if compra[k].get("€") > preuMes:
      preuMes = compra[k].get("€")

print(preuMes)