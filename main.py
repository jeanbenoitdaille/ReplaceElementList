liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
     
nom_a_chercher = "Julie"
nouveau_nom = "Julien"
     
liste = [x.replace(nom_a_chercher, nouveau_nom) for x in liste]
print(liste)  