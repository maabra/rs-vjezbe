"""#printanje

print("Hello World")

a = 5

print (type(a))

#b = input("Unesi neku vrijednost: ")
b = 4 

print(b)

print("a + b", a + b)

a="Moje"
b="je"
c="ime" 
d="Pero "

print(a,b,c,d, sep=",")

if bool("123"):
    print("da")
else:
    print("ne")
    
print(False and x)

print(5 and "cvrcak")

a = [1,2,3]
b = [1,2,3]

print(a is b)

y = 10
if False:
    x = 5
else:
    y = 6
    
    print (y)
    
"""

a = float(input("Unesi prvi broj: "))
b = float(input("Unesi drugi broj: "))
c = input("Unesi aritmetičku operaciju (+, -, *, /): ")

if c == '+':
    rezultat = a + b
elif c == '-':
    rezultat = a - b
elif c == '*':
    rezultat = a * b
elif c == '/':
    if b != 0:
        rezultat = a / b
    else:
        rezultat = 'Dijeljenje s nulom nije moguće!'
else:
    rezultat = 'Nepoznata operacija!'
def remove(n):
    return n.quantize(rezultat(1)) if n == n.to_integral() else n.normalize()
# Print the rezultat
print(f'Rezultat: {rezultat}')
