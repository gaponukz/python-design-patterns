from entities import *

class SpotFlyweight:
    _spots: dict[str, Spot] = {}

    @classmethod
    def get_spot(cls, spot: Spot) -> "Spot":
        spot_id = str(spot)

        if spot_id not in cls._spots:
            cls._spots[spot_id] = spot.copy(deep=True)
        
        return cls._spots[spot_id]

if __name__ == "__main__":
    date1 = datetime.datetime.now()
    date2 = datetime.datetime.now()

    place1 = Place(country="USA", city="New York", street="123 Main St")
    place2 = Place(country="Canada", city="Toronto", street="456 Queen St")

    spot1 = Spot(place=place1, date=date1)
    spot2 = Spot(place=place2, date=date2)
    spot3 = Spot(place=place2, date=date2)

    if spot2 is spot3:
        print("spot2 and spot3 are the same object")
    
    else:
        print("spot2 and spot3 are different objects")


    spot1 = SpotFlyweight.get_spot(spot1)
    spot2 = SpotFlyweight.get_spot(spot2)
    spot3 = SpotFlyweight.get_spot(spot3)

    print(f"spot1 id: {id(spot1)}")
    print(f"spot2 id: {id(spot2)}")
    print(f"spot3 id: {id(spot3)}")

    if spot2 is spot3:
        print("spot2 and spot3 are the same object")
    
    else:
        print("spot2 and spot3 are different objects")
