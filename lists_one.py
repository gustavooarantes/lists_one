# 3-4

lista = ["Sorele", "Gustavo", "Camila"]
for i in range(len(lista)):
    print(f"Olá {lista[i]}, você foi convidado(a)!")

print("======================================================")

# 3-5

print(f"Infelizmente, {lista[2]} não poderá comparecer.\n")
lista[2] = "Rogério"
for i in range(len(lista)):
    print(f"Olá {lista[i]}, você foi convidado(a)!")

print("======================================================")

# 3-6

print("Encontramos uma mesa maior!\n")

lista.insert(0, "Laura")
lista.insert(1, "Marcelo")
lista.append("José")
for i in range(len(lista)):
    print(f"Olá {lista[i]}, você foi convidado(a)!")

print("======================================================")

# 3-7

print("Só poderei convidar duas pessoas! Sorry :(\n")

i = 5
while i >= 2:
    removido = lista.pop(i)
    print(f"Desculpe, {removido}, mas você está desconvidado(a)!")
    i -= 1

for i in range(len(lista)):
    print(f"Relaxa, {lista[i]}, você segue convidado(a)!")

print("======================================================")

i = 0
while i < 2:
    del lista[0]
    i += 1

print(lista)