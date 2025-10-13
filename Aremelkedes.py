crntPrice: int = int(input("Az alkatrész jelenlegi ára: "))
priceHike: float = float(input("Áremeles (százalékban): "))

print(f"Az alkatrész új ára: {int(crntPrice + (crntPrice * (priceHike / 100)))}")
