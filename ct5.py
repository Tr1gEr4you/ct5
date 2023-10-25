def process(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("Файл пуст.")
                return []

            num_lines = int(lines[0])
            if num_lines != len(lines) - 1:
                print("Количество строк не соответствует числу, указанному в первой строке.")
                return []

            numbers = []
            for line in lines[1:]:
                try:
                    number = int(line.strip())
                    numbers.append(number)
                except ValueError:
                    print("Ошибка: невозможно преобразовать строку в число:", line.strip())
                    return []

            return numbers
    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
        return []
    except IOError:
        print("Ошибка ввода/вывода при чтении файла.")
        return []

def main():
    file_name = input('Введите имя файла: ')
    data = process(file_name)
    if data:
        total = sum(data)
        print("Сумма чисел в файле:", total)

if __name__ == "__main__":
    main()