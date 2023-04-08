from entities import (
    INikeProduct,
    NikeShirt,
    AdidasShirt,
    SizeSymbol,
    Size
)

def shopping(product: INikeProduct):
    if  39 < product.get_size() < 42:
        print("That's my size!")
    
    else:
        print("That's not my size(")

def problem():
    shopping(NikeShirt(price=20, size=40))
    # what happend if we will try to use adidas shirt?
    print("Old method:")

    try:
        shopping(AdidasShirt(price=20, size='m'))

    except Exception as error:
        print(f"Can not use adidas because of {error}")

'''
Adapter is our solution!
'''
class AdidasShirtAdapter(INikeProduct, AdidasShirt):
    size_table: dict[SizeSymbol, Size] = {
        'xs': 33, 's': 37, 'm': 41, 'l': 45, 'xl': 50
    }

    def get_size(self):
        size = super().get_size_symbol()
        return self.size_table[size]

def solution():
    print("New method:")
    # what happend now? - it will work)
    shopping(AdidasShirtAdapter(price=20, size='m'))

if __name__ == '__main__':
    problem()
    solution()
