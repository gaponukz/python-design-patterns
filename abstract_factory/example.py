from shops import IClothingStore
from shops import AdidasStore
from shops import NikeStore

def shopping(shop: IClothingStore):
    shirt = shop.create_shirt()

    print(f"We can buy shirt in {shop.__class__.__name__} for {shirt.get_price()}$")

if __name__ == '__main__':
    shopping(AdidasStore())
    shopping(NikeStore())
