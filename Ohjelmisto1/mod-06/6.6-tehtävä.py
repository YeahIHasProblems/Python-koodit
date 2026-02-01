import math

def pitsanmuunnos(halkaisija, hinta):
    cm_metreiksi = (halkaisija / 2) / 100
    halkaisijametreina = math.pi * cm_metreiksi**2  
    return hinta / halkaisijametreina           

halkaisija1 = float(input("Pitsa 1 halkaisija (cm): "))
hinta1 = float(input("Pitsa 1 hinta (€): "))

halkaisija2 = float(input("Pitsa 2 halkaisija (cm): "))
hinta2 = float(input("Pitsa 2 hinta (€): "))

pitsa1 = pitsanmuunnos(halkaisija1, hinta1)
pitsa2 = pitsanmuunnos(halkaisija2, hinta2)

print(f"Pitsa 1: {pitsa1:.2f} €/m2")
print(f"Pitsa 2: {pitsa2:.2f} €/m2")

if pitsa1 < pitsa2:
    print("Pitsa 1 on parempi")
elif pitsa2 < pitsa1:
    print("Pitsa 2 on parempi")
else:
    print("Pitsoilla on sama yksikköhinta")


