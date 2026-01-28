def num_primo(x:int) -> bool:
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