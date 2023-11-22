import json
faila_vards = input("Ievadi JSON datnes nosaukumu: ")

try:
    with open(faila_vards) as fails:
        datu_vardnica=json.load(fails)
        print(f"Vārdnīcas garums: {len(datu_vardnica)}")
        if len(datu_vardnica) > 0:
            print(f"Visas vārdnīcas atslēgas: {list(datu_vardnica.keys())}")
            print(f"Visas vārdnīcas vērtības: {list(datu_vardnica.values())}")
            ievades_atslega = input("Ievadiet atslēgu, lai atrastu to vērtibas: ")
            if ievades_atslega in datu_vardnica:
                print(f"Atslēga '{ievades_atslega}' eksistē un to vērtības ir {datu_vardnica[ievades_atslega]}")
            else:
                print(f"Atslēga '{ievades_atslega}' nav datu vārdnīcā!")
        else:
            print("Vārdnīca ir tukša :/")
except FileNotFoundError:
    print("Datne nēeksistē :/")
except json.JSONDecodeError as e:
    print("JSON datnes formāts nav pareizs!")