import typing
from entities import User, UserWithHome, Address

def wrong_accommodate_user_to(whom: User, to: UserWithHome) -> UserWithHome:
    # problem
    return UserWithHome(
        first_name=whom.first_name,
        last_name=whom.last_name,
        age=whom.age,
        address=to.address
    )

def corect_accommodate_user_to(whom: User, to: UserWithHome) -> UserWithHome:
    # solution
    return UserWithHome(
        first_name=whom.first_name,
        last_name=whom.last_name,
        age=whom.age,
        address=to.address.copy()
    )

def change_user_street(user: UserWithHome, street: str):
    user.address.street = street

def sad_story(accommodate_user_function: typing.Callable[[User, UserWithHome], UserWithHome]):
    user_with_home = UserWithHome(
        first_name="Adam",
        last_name="Smith",
        age=21,
        address=Address(
            country="Ukraine",
            city="Kiev",
            street="Shevchenko 2"
        )
    )

    user_without_home = User(
        first_name="Anna",
        last_name="Smith",
        age=19
    )
    '''
    Adam and Anna want to live together
    '''
    not_homeless = accommodate_user_function(user_without_home, user_with_home)

    '''
    But something went wrong and Anna want to change address street
    '''
    change_user_street(not_homeless, "Bavovny 200")
    
    '''
    But Adam does not want to change street
    '''
    assert user_with_home.address.street != not_homeless.address.street

if __name__ == '__main__':
    # sad_story(wrong_accommodate_user_to)
    sad_story(corect_accommodate_user_to)
