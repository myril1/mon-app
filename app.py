def calculer_moyenne(nombre1, nombre2, nombre3):
    # Calcul de la moyenne
    moyenne = (nombre1 + nombre2 + nombre3) / 3
    return moyenne

def main():
    # Saisie des nombres
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    nombre3 = float(input("Entrez le troisième nombre : "))

    # Calcul de la moyenne
    moyenne = calculer_moyenne(nombre1, nombre2, nombre3)

    # Affichage du résultat
    print("La moyenne des nombres est :", moyenne)

if __name__ == "__main__":
    main()
