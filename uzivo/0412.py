# lista = list(range(1_000_000))
# print(type(range(100)))
from collections import Counter
import hashlib
hsh = hashlib.sha256("Poruka".encode("utf -8")).hexdigest()

print("Hash:", hsh)

podaci = (range(1_000_000))

suma = ""
suma2 = 0
for x in podaci:
    suma += hashlib.sha256(str(x**4).encode("utf-8")).hexdigest()
    suma = hashlib.sha256(suma.encode("utf-8")).hexdigest()

for x in podaci:
    hsh += hashlib.sha256(str(x**4).encode("utf-8")).hexdigest()
    suma2 += Counter(hsh)["a"]
print("Konačna suma:", suma)
print("Konačna suma:", suma2)