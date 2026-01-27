luku = int(input("Anna kokonaisluku: "))
onkoalkuluku = True
for x in range(2, int(luku)):
        if luku % x == 0:
            onkoalkuluku = False
            break
if onkoalkuluku:
      print("Alkuluku")
else:
      print("Ei ole alkuluku")
            