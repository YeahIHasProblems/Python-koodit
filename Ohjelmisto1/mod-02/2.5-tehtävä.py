leiviska = float(input("Anna leviskät.\n"))
naula = float(input("Anna naulat.\n"))
luoti = float(input("Anna luodit.\n"))

leiviskamuutos = ((leiviska)*20*32*13.3)
naulamuutos = ((naula)*32*13.3)
luotimuutos = ((luoti)*13.3)
grammat = ((leiviskamuutos)+(naulamuutos)+(luotimuutos))
kg = (grammat // 1000)
g = (grammat % 1000)

print(f"\nMassanykymittojen mukaan:\n{kg:.0f} kilogrammaa ja {g:.2f} grammaa.")