def app_penjumlahan():
    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 + angka2
    print ("hasil penjumlahan", hasil)
    print ("===== program penjumlahan selesai")

def app_pengurangan():

    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 - angka2
    print ("hasil pengurangan", hasil)
    print ("===== program pengurangan selesai")

def app_perkalian():

    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 * angka2
    print ("hasil perkalian", hasil)
    print ("===== program perkalian selesai")


def app_pembagian():

    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 / angka2
    print ("hasil pembagian", hasil)
    print ("===== program pembagian selesai")

def app_menu():
    while True:

        print("=== PROGRAM KALKULATOR SEDERHANA===")
        print("1.penjumlahan")
        print("2.pengurangan")
        print("3.perkalian")
        print("4.pembagian")
        print("5.keluar")
        print("==== PROGRAM SELESAI ====")

        pilihan = int(input("pilihan :"))

        if pilihan == 1:
            app_penjumlahan()
        elif pilihan == 2:
            app_pengurangan()
        elif pilihan == 3:
            app_perkalian()
        elif pilihan == 4:
            app_pembagian()
        elif pilihan == 5:
            print ("===dah lah===")
            break

app_menu()