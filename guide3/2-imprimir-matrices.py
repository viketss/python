#GENERAR MATRICES (VER EJ2, GUIA 3)
'''
Las siguientes matrices responden distintos patrones de relleno. Desarrollar funcio-
nes que generen cada una de ellas sin intervención humana y escribir un programa
que las invoque e imprima por pantalla. El tamaño de las matrices debe estable-
cerse como N x N, donde N se ingresa a través del teclado.
'''
def generar_matriz_a(n):
    """Genera la matriz 'a' de tamaño NxN."""
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matriz[i][i] = i + 1
    return matriz

def generar_matriz_b(n):
    """Genera la matriz 'b' de tamaño NxN."""
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matriz[i][n - 1 - i] = (i + 1) * (3 if i < n - 1 else 9)
    return matriz

def generar_matriz_c(n):
    """Genera la matriz 'c' de tamaño NxN con valores decrecientes por columnas y ceros fuera de la diagonal inferior izquierda."""
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for i in range(j, n):  # Solo llenar desde la diagonal inferior izquierda
            matriz[i][j] = n - i
    return matriz

def generar_matriz_d(n):
    """Genera la matriz 'd' de tamaño NxN con valores constantes por filas decrecientes."""
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matriz[i][j] = n - i
    return matriz

def generar_matriz_e(n):
    """Genera la matriz 'e' de tamaño NxN con un 0 entre cada número, incrementando en toda la matriz."""
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    contador = 1  # Contador para los números
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 1:  # Alternar entre números y ceros
                matriz[i][j] = contador
                contador += 1
    return matriz

def generar_matriz_f(n):
    """Genera la matriz 'f' de tamaño NxN con columnas alternadas y ceros en las posiciones no utilizadas."""
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for i in range(j, n):  # Solo llenar desde la diagonal inferior izquierda
            matriz[i][j] = n - j
    return matriz

def generar_matriz_g(n):
    """Genera la matriz 'g' de tamaño NxN con valores en forma de espiral."""
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    contador = 1
    inicio_fila = 0
    fin_fila = n - 1
    inicio_col = 0
    fin_col = n - 1

    while inicio_fila <= fin_fila and inicio_col <= fin_col:
        # Llenar la fila superior
        for j in range(inicio_col, fin_col + 1):
            matriz[inicio_fila][j] = contador
            contador += 1
        inicio_fila += 1

        # Llenar la columna derecha
        for i in range(inicio_fila, fin_fila + 1):
            matriz[i][fin_col] = contador
            contador += 1
        fin_col -= 1

        # Llenar la fila inferior (si queda)
        if inicio_fila <= fin_fila:
            for j in range(fin_col, inicio_col - 1, -1):
                matriz[fin_fila][j] = contador
                contador += 1
            fin_fila -= 1

        # Llenar la columna izquierda (si queda)
        if inicio_col <= fin_col:
            for i in range(fin_fila, inicio_fila - 1, -1):
                matriz[i][inicio_col] = contador
                contador += 1
            inicio_col += 1

    return matriz

def generar_matriz_h(n):
    """Genera la matriz 'h' de tamaño NxN con llenado diagonal."""
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    for k in range(2 * n - 1):
        for i in range(n):
            for j in range(n):
                if i + j == k:
                    matriz[i][j] = num
                    num += 1
    return matriz

def generar_matriz_i(n):
    """Genera la matriz 'i' de tamaño NxN con el patrón específico."""
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    for k in range(n):
        # Llenar la primera "sub-diagonal"
        for i in range(k + 1):
            matriz[i][k - i] = num
            num += 1
        if k < n - 1:
            # Llenar la "sub-diagonal" superior desplazada
            for i in range(k + 1):
                if k + 1 + i < n and n - 2 - i >= 0:
                    matriz[k + 1 + i][n - 2 - i] = num
                    num += 1
    return matriz

def imprimir_matriz(matriz):
    """Imprime una matriz de forma legible."""
    for fila in matriz:
        print(" ".join(map(str, fila)))

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Ingrese el tamaño N de las matrices (entero positivo): "))
            if n > 0:
                break
            else:
                print("Por favor, ingrese un número entero positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    print(f"\n--- Matrices de tamaño {n}x{n} ---")

    print("\nMatriz a:")
    imprimir_matriz(generar_matriz_a(n))

    print("\nMatriz b:")
    imprimir_matriz(generar_matriz_b(n))

    print("\nMatriz c:")
    imprimir_matriz(generar_matriz_c(n))

    print("\nMatriz d:")
    imprimir_matriz(generar_matriz_d(n))

    print("\nMatriz e:")
    imprimir_matriz(generar_matriz_e(n))

    print("\nMatriz f:")
    imprimir_matriz(generar_matriz_f(n))

    print("\nMatriz g:")
    imprimir_matriz(generar_matriz_g(n))

    print("\nMatriz h:")
    imprimir_matriz(generar_matriz_h(n))

    print("\nMatriz i:")
    imprimir_matriz(generar_matriz_i(n))