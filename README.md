# Analisis de soluciones.
*Juan David Cruz Salamanca*
## Diagrama
<img src = "Untitled Diagram.drawio.png">

## Procedimiento
Para solucionar el problema lo primero tenia claro es que la función *main* solo fuera para capturar y entregar información. El siguiente paso que pensé fue en enviar el número a una función que hiciera todas las comprobaciones que se pedian. 

Para la primera parte del problema cree la función *check_num* con el fin de usar condicionales para verificar si el número es positivo, si el número es negativo o si el número es cero.

Para la segunda parte modifique la función *check_num* en el condicional que rectifica si el nuúmero es positivo, esto porque tanto los números primos y los números de la serie de fibonnacci son positivos. Para verificar si el número pertenece a uno de estos conjuntos pense dos funciones más que se llaman dentro del condicional de los números positivos y que retornan valores Booleanos `{True, False}`  

**Función num_primo:** Para saber si el número es primo se debe tener en cuenta que solo es divicible por 1 y por el mismo. Por eso en esta funcion use un contador inicializado en 0. Después use un ciclo `for` para recorrer desde 1 hasta el número dado y asi calcular el modulo de la división. Si el modúlo es 0 el contador suma 1. Al finalizar el ciclo se comprueba que si el contador es 2 se retorne `True` y en cualquier otro caso retorne `False`.

**Función e_fibonacci:** Con esta función queria saber si el número pertenecia a la serie de Fibonacci. En internet encontre un método en el que se explicaba que dada esta función $f(x) = \sqrt{5x^2+4}$, si al remplazar por un número $x$ en función esta da como resultado un número entero este número pertenece a la serie de fibonacci. Así queria hacer la comprobación y de nuevo devolver un valor Booleano. [*(Link donde encontre la ecuación usada.)*](https://www.geeksforgeeks.org/dsa/check-number-fibonacci-number/)

Al momento de entregar las respuestas mi idea era en el condicional para comprobar si el número es positivo, llamar a las funciones `num_primo` y `e_fibonacci`, con sus respectivos valores booleanos hacer mas ciclos anidados para entregar todas las respuestas posibles dependiendo de la clasificación del número.

## Codigo

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
