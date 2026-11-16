def calcular_area(base, altura):
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser valores positivos")

    return base * altura


if __name__ == "__main__":
    base = float(input("Ingrese la base del rectangulo: "))
    altura = float(input("Ingrese la altura del rectangulo: "))

    area = calcular_area(base, altura)

    print(f"El area del rectangulo es: {area}")
