import csv
faila_vards = input("Ievadi CSV datnes nosaukumu: ")

try:
    with open(faila_vards, newline='') as fails:
        csv.reader = csv.reader(fails)
        datu_masivs=list(csv.reader)
        print(f"Masīva garums: {len(datu_masivs)}")
        if len(datu_masivs) > 0:

            print(f"Masīva pirmā elementa saturu: {datu_masivs[0]}")
            print("Masīva pirmie 5 elementi:")
            for i in range(min(5, len(datu_masivs))):
                print(datu_masivs[i])
        else:
            print("Masīvā nekā nav...")
except FileNotFoundError:
    print("Datu nav :/")