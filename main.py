import random

def guess_number():
    """Игра 'Угадай число'"""
    secret_number = random.randint(1, 100)
    attempts_left = 5
    print("\n🔢 Робот загадал число от 1 до 100. У вас 5 попыток!")

    for attempt in range(attempts_left):
        print(f"\nПопытка {attempt + 1} из {attempts_left}")
        try:
            user_guess = int(input("Ваше число: "))
            if user_guess < secret_number:
                print("Загаданное число БОЛЬШЕ")
            elif user_guess > secret_number:
                print("Загаданное число МЕНЬШЕ")
            else:
                print(f"🎉 Поздравляем! Вы угадали число {secret_number}!")
                return
        except ValueError:
            print("Ошибка: введите целое число!")

    print(f"\n❌ Попытки закончились. Загаданное число было {secret_number}")

def magic_8_ball():
    """Магический шар для предсказаний"""
    answers = [
        'Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да',
        'Можешь быть уверен в этом', 'Мне кажется — да', 'Вероятнее всего',
        'Хорошие перспективы', 'Знаки говорят — да', 'Да',
        'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать',
        'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять',
        'Даже не думай', 'Мой ответ — нет', 'По моим данным — нет',
        'Перспективы не очень хорошие', 'Весьма сомнительно'
    ]
    
    print("\n🎱 Привет, я Магический шар!")
    name = input("Как тебя зовут? ")
    print(f"{name}, задай мне любой вопрос и получишь ответ судьбы!")

    while True:
        question = input("\nТвой вопрос (или 'стоп' для выхода): ")
        if question.lower() == 'стоп':
            break
        print(f"🔮 Ответ: {random.choice(answers)}")

def shopping_cart():
    """Калькулятор покупок"""
    total = 0.0
    print("\n🛒 Введите суммы покупок (для выхода введите 'стоп')")

    while True:
        amount = input("Сумма: ")
        if amount.lower() == 'стоп':
            break
        try:
            total += float(amount)
            print(f"Общая сумма: {total:.2f} ₽")
        except ValueError:
            print("Ошибка: введите число или 'стоп'!")

    print(f"\n💳 Итого к оплате: {total:.2f} ₽")

def currency_converter():
    """Конвертер валют"""
    rates = {
        'BTC': 7113814.56,
        'EUR': 91.75,
        'USD': 88.34,
        'CNY': 12.15
    }

    print("\n💱 Конвертер RUB в BTC/EUR/USD/CNY")
    try:
        rub = float(input("Введите сумму в рублях: "))
        for currency, rate in rates.items():
            print(f"{rub} RUB = {rub / rate:.6f} {currency}")
    except ValueError:
        print("Ошибка: введите числовое значение!")

def show_menu():
    """Главное меню"""
    print("\n" + "="*50)
    print("🎮 ГЛАВНОЕ МЕНЮ".center(50))
    print("="*50)
    print("1. 🔢 Угадай число")
    print("2. 🎱 Магический шар")
    print("3. 🛒 Корзина покупок")
    print("4. 💱 Конвертер валют")
    print("0. ❌ Выход")
    print("="*50)

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Выберите программу (0-4): ")

        if choice == "1":
            guess_number()
        elif choice == "2":
            magic_8_ball()
        elif choice == "3":
            shopping_cart()
        elif choice == "4":
            currency_converter()
        elif choice == "0":
            print("\nДо свидания! 👋")
            break
        else:
            print("Ошибка: выберите пункт 0-4!")

        input("\nНажмите Enter чтобы продолжить...")
