def app_tebak_angka():
    import random
    angka_acak = random.randint(1, 10)
    maksimal_tebakan = 3
    tebakan  = 0
    while tebakan < maksimal_tebakan:
        angka_user = int(input("masukkan angka :"))
        if angka_user > angka_acak:
            print("angka terlalu besar")
        elif angka_user < angka_acak:
            print("angka terlau kecil")
        else:
            print("'selamat anda benar")
            break

    else:
        print("yeeey nggak ketebak yah")
        print("jawabannya adalah:", angka_acak)

    input("enter untuk lanjut")

def app_menu():
    while True:

        print("====== main menu ======")
        print("1.mulai")
        print("2.keluar")
        print("===== hellllllooooooowwww ====")

        pilihan = int(input("pilihann :"))

        if  pilihan == 1:
            app_tebak_angka()
        elif pilihan == 2:
            print("====berhasil keluar=====")
            break
        else:
            print("error : pilihan yang aneh")

app_menu()