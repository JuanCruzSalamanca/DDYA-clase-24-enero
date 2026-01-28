# Analisis de soluciones.
***Juan David Cruz Salamanca***

## Ejercicio 1
### Procedimiento
Para solucionar el problema lo primero tenia claro es que la función ``main`` solo fuera para capturar y entregar información. El siguiente paso que pensé fue en enviar el número a una función que hiciera todas las comprobaciones que se pedian. 

Para la primera parte del problema cree la función ``check_num`` con el fin de usar condicionales para verificar si el número es positivo, si el número es negativo o si el número es cero.

Para la segunda parte modifique la función ``check_num`` en el condicional que rectifica si el número es positivo, esto porque tanto los números primos y los números de la serie de fibonnacci son positivos. Para verificar si el número pertenece a uno de estos conjuntos pense en hacer dos funciones más que se llaman dentro del condicional de los números positivos y que retornan valores Booleanos `{True, False}`  

**Función num_primo:** Para saber si el número es primo se debe tener en cuenta que solo es divicible por 1 y por el mismo. Por eso en esta funcion use un contador inicializado en 0. Después use un ciclo `for` para recorrer desde 1 hasta el número dado y asi calcular el modulo de la división. Si el modúlo es 0 el contador suma 1. Al finalizar el ciclo se comprueba que si el contador es 2 se retorne `True` y en cualquier otro caso retorne `False`.

**Función e_fibonacci:** Con esta función queria saber si el número pertenecia a la serie de Fibonacci. En internet encontre un método en el que se explicaba que dada esta función $f(x) = \sqrt{5x^2+4}$, si al remplazar por un número $x$ en función esta da como resultado un número entero este número pertenece a la serie de fibonacci. Así queria hacer la comprobación y de nuevo devolver un valor Booleano. [[1]](#1)

Al momento de entregar las respuestas mi idea era en el condicional para comprobar si el número es positivo, llamar a las funciones `num_primo` y `e_fibonacci`, con sus respectivos valores booleanos hacer mas ciclos anidados para entregar todas las respuestas posibles dependiendo de la clasificación del número.

### Codigo
```python
def num_primo(x):
    cont = 0
    for i in range(0, x + 1):
        if x % i == 0:
            cont += 1

    if cont == 2:
        return True
    else:
        return False
    
def e_fibonacci(x):
    eq = 5(x)**2 + 4
    if (eq)**1/2 
    
def check_num(x):
    if x > 0:
        primo = num_primo(x)
        
    elif x < 0:
        return ("El número es negativo")
    else:
        return ("El número es cero")

def main():
    num = int(input("Ingrese número:"))
    answer = check_num(num)
    print(answer)
main()
```

### Diagrama
<img src = "/Users/juancruz/Desktop/DDYA-clase-24-enero/Anexos/Diagrama1.png" width = "600">

## Ejercicio 2
### Procedimiento
Dado que en este problema la entrada es una sola linea de texto y cada elemento esta separado por un espacio, con el use de ``.split()`` hago que cada elemento pase a ser el elemento de una lista.

**Funcion notas:** En esta funcion esta toda la logica de la solucion, para empezar creo 3 listas vacias *names, notes y aprove*. Despues con un ciclo que empieza en 1, termina en la longitud del primer arreglo que contiene todos los datos y que va en pasos de 2 unidades guardo tanto los nombres como las notas en listas diferentes.

Ahora recorro la lista de notas y comparo todos los valores bajo el criterio de cuanto se necesita para pasar, como la nota y el nombre del estudiante tienen la misma posicion en sus respectivas listas, lo siguiente es guardar en la listra *aprove* todos los nombres que aprobaron y entregarle esta lista a la funcion ``main``.

Para entregar los datos al usuario solo uso el metodo ``.join()`` para entregar en una sola linea de texto los nombres de las personas que aprovaron. 

### Codigo
```python
def notas(x):
    l_data = x.split()
    names = []
    notes = []
    aprove = []
    for i in range (1,len(l_data),2):
        names.append(l_data[i-1])
        notes.append(float(l_data[i]))
    
    for i in range (len(notes)):
        if notes[i] >= 3:
            aprove.append(names[i])
    return aprove

def main():
    est_note = input("Escriba el nombre de los estudiantes y sus notas separadas por espacio: ")
    print("==================")
    aprov_names = notas(est_note)
    answer = " ".join(aprov_names)
    print(answer)
main()
```

### Diagrama
<img src = "">

## Bibliografia
<a id = "1">[1]</a>
GeeksforGeeks. How to check if a given number is Fibonacci number? GeeksforGeeks. https://www.geeksforgeeks.org/dsa/check-number-fibonacci-number/. Published 23 de julio de 2025.