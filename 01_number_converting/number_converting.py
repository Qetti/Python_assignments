from config import number_spelling


def convert(number):
    result = ""

    if number in number_spelling.keys():
        result = number_spelling[number]
    else:
        if 20 < number < 100:
            result += convert(number - number % 20)[:-1] + "და" + convert(number % 20)
        elif 100 < number < 200:
            result += convert(number - number % 100)[:-1] + " " + convert(number % 100)
        elif 200 <= number < 1000:
            if number % 100 == 0:
                result += (convert(number / 100)[:-1] if convert(number / 100)[-1] == "ი" else convert(
                    number / 100)) + convert(100)
            else:
                result += (convert(number // 100)[:-1] if convert(number // 100)[-1] == "ი" else convert(
                    number // 100)) + convert(100)[:-1] + " " + convert(number % 100)
        elif 1000 <= number < 1000000:
            if number % 1000 == 0:
                result += (convert(number // 1000) if number // 1000 > 1 else "") + " " + convert(10)[:-1] + convert(
                    100)
            else:
                result += (convert(number // 1000) if convert(number // 1000)[-1] == "ი" else convert(
                    number // 1000)) + convert(1000)[:-1] + " " + convert(number % 1000)
        elif 1000000 <= number < 1000000000:
            if number % 1000000 == 0:
                result += (convert(number // 1000000) if number // 1000000 > 1 else "") + " " + convert(
                    1000000)
            else:
                result += (convert(number // 1000000) if convert(number // 1000000)[-1] == "ი" else convert(
                    number // 1000000)) + " " + convert(1000000)[:-1] + " " + convert(number % 1000000)
        elif 1000000000 <= number < 1000000000000:
            if number % 1000000000 == 0:
                result += (convert(number // 1000000000) if number // 1000000000 > 1 else "") + " " + convert(
                    1000000000)
            else:
                result += (convert(number // 1000000000) if convert(number // 1000000000)[-1] == "ი" else convert(
                    number // 1000000000)) + " " + convert(1000000000)[:-1] + " " + convert(number % 1000000000)

    return result


while True:
    try:
        user_input = int(input("შეიყვანეთ სასურველი რიცხვი: "))
        break
    except ValueError:
        print("!!! შეყვანილი მნიშვნელობა არასწორია, გთხოვთ შეიყვანოთ მხოლოდ რიცხვი !!!")

print(str(user_input), " : ", convert(user_input))

print("-----------------------------")
print("სხვა მაგალითები: ")
print()

example_list = [7, 90, 512, 1_963, 15_265, 126_092, 9_943_409, 90_956_790, 701_679_742, 1_204_580_080,
                12_040_092_123, 928_289_300_763]

for num in example_list:
    print(f"{num} : ", convert(num))
