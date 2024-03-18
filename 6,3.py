# Input tinggi dan lebar
tinggi = int(input("Masukan tinggi : "))
lebar = int(input("Masukan lebar : "))

# x dan y berawal dari 1
x = 1
y = 1

# Perulangan untuk hanya print sampai tinggi saja
while y <= tinggi:
    # Perulangan untuk hanya print sampai lebar saja
    for i in range(lebar):
        # Kalau tidak melebihi lebar maka x akan di print
        print(x, end=' ')
        # x ditambah 1 tiap perulangan
        x += 1
    # Ketika sudah mencapai lebar, maka akan print di bawahnya
    print(" ")
    # y ditambah satu tiap kali perulangan lebar habis
    y += 1



