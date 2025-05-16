import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts_left = 5
    print("Робот загадал число от 1 до 100.")

    for attempt in range(attempts_left):
        print("Попытка", str(attempt + 1), "из", attempts_left)
        user_guess = int(input("Введите ваше число: "))

        if user_guess < secret_number:
            print("Загаданное число больше.")
        elif user_guess > secret_number:
            print("Загаданное число меньше.")
        else:
            print("Поздравляем! Вы угадали число", str(secret_number), "!")
            break
    else:
        print("Попытки закончились. Загаданное число было", str(secret_number), ".")


def magic_8_ball():
    possible_answers = [
        'Это точно!', 'Разумеется!', 'Да.', 'Так и есть.', 'Попробуйте другой вариант.',
        'Возможно.', 'Скорее всего, да.', 'Скорее всего, нет.', 'В другой раз.', 'Бесспорнно да.',
        'Лучше отложить решение.', 'Точно нет!', 'Никогда.', 'Даже не думайте!', 'Лучше не стоит.',
        'Подумайте сами.', 'Вы уверены, что вам это нужно?', 'Подумайте еще раз.', 'Нет.', 'Взвесьте все "за" и "против"',
    ]
    user_name = input("Привет, я Магический шар! А вас как зовут? ")
    print("Привет,", user_name + "!", "Я помогу вам с ответом на ваш вопрос!")

    while True:
        user_question = input("Задайте ваш вопрос: ")
        random_answer = random.choice(possible_answers)
        print("Магический шар говорит:", random_answer)


def shopping_cart():
    total_amount = 0.0
    while True:
        purchase_amount = input("Введите сумму покупки (или 'выход' для завершения): ")
        if purchase_amount.lower() == 'выход':
            break
        total_amount += float(purchase_amount)
        print("Текущая общая сумма:", total_amount)
    print("Итоговая сумма покупок:", total_amount)
    return total_amount


def currency_converter():
    btc_rate = 7113814.56
    eur_rate = 91.75
    usd_rate = 88.34

    rubles = float(input("Введите количество рублей: "))
    print(rubles, "RUB =", rubles / btc_rate, "BTC")
    print(rubles, "RUB =", rubles / eur_rate, "EUR")
    print(rubles, "RUB =", rubles / usd_rate, "USD")
