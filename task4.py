import argparse

def main():
    parser = argparse.ArgumentParser(description="Скрипт, который принимает число и строку с необязательными флагами.")
    
    parser.add_argument('number', type=int, help="Числовой ввод")
    parser.add_argument('string', type=str, help="Строковый ввод")
    parser.add_argument('--verbose', action='store_true', help="Показать дополнительную информацию о процессе")
    parser.add_argument('--repeat', type=int, default=1, help="Количество повторений строки")

    args = parser.parse_args()
    
    if args.verbose:
        print(f"Число: {args.number}, Строка: '{args.string}', Количество повторений: {args.repeat}")
    
    result = (args.string + ' ') * args.repeat
    print(result.strip())

if __name__ == '__main__':
    main()
