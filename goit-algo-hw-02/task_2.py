from collections import deque

def is_palindrome(string: str):
    string = ''.join(string.split())
    char_deque = deque(string)
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

def test(sample_string):
    for string in sample_string:
        if is_palindrome(string.lower()):
            print(f"| {string} | -> Цей рядок є паліндром.")
        else:
            print(f"| {string} | -> Не є паліндром.")

if __name__ == "__main__":
    
    sample_strings = [
    "Привіт",
    "На ринок дід Кониран",
    "Сіно ніс",
    "Курка біб а крук",
    "Сир і рис",
    "Кіт утік",
    "Випив",
    "Вижив",
    "її",
    "вижив",
    "випив",
    "Лилипут сома на мосту пилил",
    "Нажал кабан на баклажан",
    "Город дорог",
    "Кому думок",
    "У дива на виду",
    "Мир дум мудрим"]
    
    test(sample_strings)
