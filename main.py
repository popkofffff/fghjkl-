import functions 

def main():
    print("🎮 Консольные мини-программы на Python")
    print("Выберите программу для запуска:")
    print("1. 🔢 Угадай число")
    print("2. 🔮 Магический шар")
    print("3. 🛒 Корзина покупок")
    print("4. 💱 Конвертер валют")
    print("5. 🚪 Выход")

    while True:
        choice = input("\nВведите номер программы (1-5): ")
        
        if choice == '1':
            functions.guess_number() 
        elif choice == '2':
            functions.magic_8_ball()  
        elif choice == '3':
            functions.shopping_cart() 
        elif choice == '4':
            functions.currency_converter() 
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите 1-5")

if __name__ == "__main__":
    main()

