import random

while True:
    answer = []


    def print_statistics(answer):
        """Считает верные ответы и отправляет результат пользователю"""
        ans_t = 0
        ans_f = 0
        for count in answer:
            if count == True:
                ans_t += 1
            else:
                ans_f += 1

        print(f"Всего задачек: {len(answer)}\nОтвечено верно: {ans_t}\nОтвечено неверно: {ans_f}")


    def hello_for_users():
        """Объясняет правила и просит нажать Enter"""
        print("Сегодня мы потренируемся расшифровывать азбуку Морзе\nНажмите Enter и начнем")
        enter = input()


    hello_for_users()

    for count_up in range(0, 5):
        def get_word():
            """ Получает случайное слово из списка слов и возвращает его"""
            words_list = ["main", "code", "bit", "list", "soul"]
            random.shuffle(words_list)
            return words_list[0]


        word_luky = get_word()


        def get_morse_encode(word):
            """Переписывает случайное слово на морзянку"""
            words = {
                "0": "-----",
                "1": ".----",
                "2": "..---",
                "3": "...--",
                "4": "....-",
                "5": ".....",
                "6": "-....",
                "7": "--...",
                "8": "---..",
                "9": "----.",
                "a": ".-",
                "b": "-...",
                "c": "-.-.",
                "d": "-..",
                "e": ".",
                "f": "..-.",
                "g": "--.",
                "h": "....",
                "i": "..",
                "j": ".---",
                "k": "-.-",
                "l": ".-..",
                "m": "--",
                "n": "-.",
                "o": "---",
                "p": ".--.",
                "q": "--.-",
                "r": ".-.",
                "s": "...",
                "t": "-",
                "u": "..-",
                "v": "...-",
                "w": ".--",
                "x": "-..-",
                "y": "-.--",
                "z": "--..",
                ".": ".-.-.-",
                ",": "--..--",
                "?": "..--..",
                "!": "-.-.--",
                "-": "-....-",
                "/": "-..-.",
                "@": ".--.-.",
                "(": "-.--.",
                ")": "-.--.-"
            }
            morse = []
            for char_morsw in word:
                if char_morsw in words.keys():
                    morse.append(words[char_morsw])
            result = " ".join(morse)
            return result


        morse = get_morse_encode(word_luky)


        def input_answer_users(morse):
            """Проверяет ответ пользователя и возвращает bool"""
            print(f"Слово {count_up + 1}: {morse}")
            user_input = input().lower()
            if user_input == word_luky:
                print(f"Верно, {user_input}!")
                return True
            else:
                print(f"Неверно, {word_luky}!")
                return False


        answer.append(input_answer_users(morse))
    print_statistics(answer)
