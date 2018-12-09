"""Эта программа "гадает" по книге
Вам нужно заполнить функции своим кодом в соответствии с вашим вариантом,
дописывайте нужные функции по необходимости.
"""
"""
Вариант 4:
Пусть вопрос состоит из w слов, самое длинное слово в нём — из c букв.
В качестве ответа выдайте первое слово из строки под
    номером w * c (нумерация с нуля).
Если номер слишком большой, то в качестве ответа выдайте слово «джакузи».
"""

def lines_count(filename):
    file = open(filename, "r")
    lines = sum(1 for line in file)
    file.close()
    return lines
    
def longest_word(Text):
    max_letters = 0 
    word = ""
    current_word = ""

    position = "out"
    for letter in Text:
        if letter != " " and position == "out":
            current_word += letter
            position = "in"
        elif letter != " " and letter != "?" and position == "in":
            current_word += letter
        elif letter == " " or letter == "?":
            position = "out"
            if(len(current_word) > max_letters):
                max_letters = len(current_word)
                word = word[:0] + current_word
            current_word = ""
            
    return word

def words_count(Text):
    words = 0

    position = 'out'
    for letter in Text:
        if letter != " " and position == "out":
            words += 1
            position = "in"
        elif letter == " ":
            position = "out"

    return words

def get_first_word(Text):
    position = 'out'
    word = ""
    for letter in Text:
        if letter != " " and position == "out":
            word += letter
            position = "in"
        elif letter != " " and position == "in":
            word += letter
        else:
            return word
            

def read_book(filename):
    """Эта функция должна возвращать текст книги
    
    filename : str
        Строка с путём до книги
    Возвращает строку с текстом книги
    """
    file = open(filename, "r")
    text = file.read()
    file.close()
    
    return text


def listen_question():
    """Эта функция должна попросить пользователя задать вопрос и вернуть ответ
    Если введённое не заканчивается на знак вопроса, нужно переспросить
    Возвращает строку с введённым вопросом
    """
    print("Я отвечу на любой твой вопрос. Только запиши его:")

    correct_input = False
    while not correct_input:
        question = input()
        
        if (not question.endswith("?")):
            print("Wrong input. Try again:")
        else:
            correct_input = True

    return question


def answer(text, question):
    """Отвечает на вопрос, используя книгу
    
    text : str
        Текст книги
    question : str
        Строка с вопросом
    Возвращает строку с найденным ответом
    """
    lines = open("book.txt", "r").readlines()

    w = words_count(question)
    c = len(longest_word(question))

    if(w*c > lines_count("book.txt")):
        answer = "Джакузи"
    else:
        answer = get_first_word(lines[w*c])
        
    return answer


def print_answer(answer):
    """Печатает ответ, обрамляя его красивой фразой
    
    Эта функция ничего не возвращает
    """
    print("Кажется, моя подкова из заячьих лапок упала на книгу на слове:" + answer + '"')

def main():
    """С этой функции начинается выполнение программы"""
    print_answer(answer(read_book("book.txt"), listen_question()))

if __name__ == '__main__':
    main()

