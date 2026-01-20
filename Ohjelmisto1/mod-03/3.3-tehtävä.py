sukupuoli = input("Anna biologinen sukupuoli: ")
hemoglobiini = int(input("Anna hemoglobiini arvo (g/l): "))

if (sukupuoli == "mies" or sukupuoli == "Mies") and hemoglobiini < 134:
    print("Hemoglobiini arvo on alhainen")

elif (sukupuoli == "mies" or sukupuoli == "Mies") and hemoglobiini > 175:
    print("Hemoglobiini arvo on korkea")

elif (sukupuoli == "nainen" or sukupuoli == "Nainen") and hemoglobiini < 117:
    print("Hemoglobiini arvo on alhainen")

elif (sukupuoli == "nainen" or sukupuoli == "Nainen") and hemoglobiini > 175:
    print("Hemoglobiini arvo on korkea")

else:
    print("Hemoglobiini arvo on normaali")