# Input batas
batas = int(input("Masukan batas: "))

# Fungsi
def ganjil_prima_tertinggi(batas):
    # Memulai Perulangan for dengan range batas dari besar ke kecil
    for i in range(batas-1, 2, -1):
        # j = 2 karena bilangan prima semua bisa dibagi 1
        j = 2
        # Perulangan untuk membagi i dengan j satu persatu untuk mencari bilangan prima
        while i >= j:
            # Jika bilangan bilangan j tidak bisa membagi i maka artinya i bilangan prima
            if i == j:
                return i
            else:
                # Jika bisa dibagi dengan j maka break karena bukan prima 
                if i % j == 0:
                    break
                # Jika tidak bisa dibagi dengan j maka lanjut ke bilangan j + 1
                # Dan seterusnya sampai mendapatkan bilangan prima
                else:
                    j += 1
                    continue
                
print(ganjil_prima_tertinggi(batas))