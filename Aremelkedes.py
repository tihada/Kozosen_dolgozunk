crntPrice: int = int(input("Az alkatresz jelenlegi ara: "))
priceHike: float = float(input("Aremeles (szazalekban): "))

print(f"Az alkatresz uj ara: {int(crntPrice + (crntPrice * (priceHike / 100)))}")
