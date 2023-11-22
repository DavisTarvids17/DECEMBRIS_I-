faila_vards = input("Ievadiet datnes nosaukumu: ")

try:
    with open(faila_vards, 'r') as file:
        saturs = file.read()

        print(f"Datnē ir {len(saturs)} simboli.")
        print(f"Pirmie 10 simboli: {saturs[:10]}")
        print(f"Pirmais simbols: {saturs[0]}, Pēdējais simbols: {saturs[-1]}")
        garums = int(input("Lūdzu, ievadiet garumu:"))
        print(f"Simboli no datnes sākuma līdz {garums}: {saturs[garums]}")

except FileNotFoundError:
    print("Dati nav atrasti!")
except ValueError:
    print("Ievadītais garums nav skaitlis!")