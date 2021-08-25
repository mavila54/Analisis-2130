import numpy as np
import matplotlib.pyplot as plt
import time

f = input("Escriba la funcion: ") #x**3-2*x-5
a = float(input("Escriba el limite inferior del intervalo: ")) #1
b = float(input("Escriba el limite superior del intervalo: ")) #5
e = float(input("Escriba la tolerancia: ")) #10e-16

x = np.linspace(a, b, 100)

t1 = time.time()


def fct(f, x):
    r = eval(f)
    return r  # Definimos la función que queremos encontrar la raíz


if fct(f, a) * fct(f, b) < 0: #En los extremos la funciona adopta signos distintos

    if abs(fct(f, a)) < abs(fct(f, b)):  # a es una mejor aproximación que b
        a, b = b, a

    c = a
    mflag = True
    i = 0

    while fct(f, b) != 0 and abs(b - a) > e:  # condición de convergencia
        i += 1
        if fct(f, a) != fct(f, c) and fct(f, b) != fct(f, c):  # interpolación cuadrática inversa
            s = (a * fct(f, b) * fct(f, c)) / ((fct(f, a) - fct(f, b)) * (fct(f, a) - fct(f, c)))
            s += (b * fct(f, a) * fct(f, c)) / ((fct(f, b) - fct(f, a)) * (fct(f, b) - fct(f, c)))
            s += (c * fct(f, a) * fct(f, b)) / ((fct(f, c) - fct(f, a)) * (fct(f, c) - fct(f, b)))

        else:
            s = b - fct(f, b) * (b - a) / (fct(f, b) - fct(f, a))  # metodo de la secante

        if (s < min((3 * a + b) / 4, b) or s > max((3 * a + b) / 4, b)) or (
                mflag == True and abs(s - b) >= abs(b - c) / 2) or (mflag == False and abs(s - b) >= abs(c - d) / 2):
            # la condición para aceptar el valor de interpolación s
            s = (a + b) / 2  # método de biseccion
            mflag = True  # usamos el método de biseccion

        else:
            mflag = False  # no se utilizó el método de biseccion

        print("Pantalla de iteración", i, ":")
        print(s, fct(f, s))
        plt.plot(s, fct(f, s), color='blue', marker='o')

        d = c
        c = b

        if fct(f, a) * fct(f, s) < 0:
            b = s
        else:
            a = s

        if abs(fct(f, a)) < abs(fct(f, b)):  # a es una mejor aproximación que b
            a, b = b, a

    print("Raiz aproximada :")
    print(b)
    print("El número final de iteraciones es:", i)

    plt.plot(x, fct(f, x), label='Curva de f', linewidth=2, color='green')
    plt.plot(b, fct(f, b), color='red', marker='*', label='Punto final')
    plt.legend()
    print("El tiempo de ejecución es ", time.time() - t1)