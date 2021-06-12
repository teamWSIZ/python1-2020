from random import choice
from time import sleep

from faker import Faker

from algorytmy.utils import ts

fake = Faker()

from algorytmy.cache_.user import User


# todo: write cached version of this method!
def get_user_data(username) -> User:
    # tu normalnie call do bazy danych userów... lub serwisu userów... odpowiedź po 100ms
    sleep(0.1)
    return User(username, fake.address(), fake.text())


if __name__ == '__main__':
    s = []
    st = ts()
    usernames = [fake.name() for _ in range(20)]  # userzy którzy są aktualnie zalogowani
    for i in range(100):
        # ściągamy dane usera by dowiedzieć się czy ma prawo wykonać jakąś operację
        u = get_user_data(choice(usernames))

    en = ts()
    print(f'{en - st}s')
