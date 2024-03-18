# Input n
n = int(input("n = "))

# Fungsi untuk mencari faktorial
def factorial(n):
    x = 1
    # Factorial n didapatkan dengan perkalian semua bilangan dari 1 sampai n
    for i in range(n, 0, -1):
        x = x*i
    return x

# Perulangan untuk menuliskan factorial dan baris bilangan
for i in range(n, 0, -1):
    # Factorial diprint lebih dahulu lalu disambung dengan baris bilangan
    print(factorial(i), end=' ')
    # Perulangan untuk menghasilkan baris bilangan
    for j in range(i, 0, -1):
        print(j, end=' ')
    # Jika perulangan berakhir maka akan lanjut perulangan berikutnya
    print(" ")
    
