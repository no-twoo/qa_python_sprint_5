import random

login_email = "irina_anokhina9826@yandex.ru"
login_password = "11223344"

registration_name = "Ирина"
correct_password = "11223344"
incorrect_password = "123"


def generate_new_email():
    new_email = f"irina_anokhina9{random.randint(100, 999)}@yandex.ru"
    return new_email
