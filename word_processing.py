"""Приходит текст из 5 строк.
Задача:
 - строка не должна начинаться с пробелов, допустима только табуляция (отступ).
 - сделать так, чтобы все предложения начинались с большой буквы;
 - не было подряд несколько пробелов и знаков пунктуации;
Не забывайте, что точка не всегда значит конец предложения! Например, "и т.д. и т.п."
"""
text_str = """    \thello,,,, world.    how are you???    
    \t I'm fine, thank   you.     
\tI am fine too!!!     
do you know what means "и т.д. и т.п."?
   \t   I'm fine. Thank you   for your question!           """

# =============== РЕЗУЛЬТАТ ==================
# 	Hello, world. How are you?
# 	I'm fine, thank you.
# 	I am fine too!
# Do you know what means "и т.д. и т.п."
# 	I'm fine. Thank you for your question!

# решение задачи
from functools import wraps

PUNCTUATION = " ,.:;!?"
UNIQ_MARK = "!№;%:?"
ABBREVIATION = "и т.д. и т.п."


def is_startswith_tab(func):
    """Проверка наличия табуляции в начале строки"""

    @wraps(func)  # сохраняет документацию оборачиваемой функции
    def wrapper(line: str):
        if line.startswith('\t') or line.strip(' ').startswith('\t'):
            return '\t' + func(line)
        return func(line)

    return wrapper


def corrected_word(word: str) -> str:
    """Обработка слов"""
    i = 0
    while i < len(PUNCTUATION):  # перебираем знаки препинания и пробелы
        duplicate = PUNCTUATION[i] * 2
        while duplicate in word:  # пока встречаются два знака подряд, заменяем одинарным
            word = word.replace(duplicate, PUNCTUATION[i])
        i += 1
    return word


def corrected_sentence(sentence: str) -> str:
    """Обработка предложений"""
    words = sentence.split()  # разбираем на слова
    i = 0
    while i < len(words):
        words[i] = corrected_word(words[i])  # меняем каждое слово в списке на обработанное
        i += 1
    return ' '.join(words)  # соединяем слова через пробел обратно в предложение


@is_startswith_tab
def corrected_line(line: str) -> str:
    """Обработка строк"""
    if ABBREVIATION in line:
        line = line.replace(ABBREVIATION, UNIQ_MARK)  # заменяем "и т.д. и т.п." на "!№;%:?"

    sentences = line.split('. ')  # разбиваем на предложения
    i = 0
    while i < len(sentences):  # перебираем предложения в списке
        sentences[i] = corrected_sentence(sentences[i]).strip('').capitalize()
        # удаляем пробельные символы по краям и делаем первую букву предложения заглавной
        if UNIQ_MARK in sentences[i]:
            sentences[i] = sentences[i].replace(UNIQ_MARK, ABBREVIATION)  # возвращаем на место "и т.д. и т.п."
        i += 1
    return '. '.join(sentences)
    # склеиваем предложения обратно в строку, а декоратор добавляет спереди строки табуляцию, если она там была


def corrected_text(text: str) -> str:
    """Обработка текста построчно"""
    lines = text.split('\n')  # делим текст на строки
    new_text = ''
    i = 0
    while i < len(lines):
        new_text += corrected_line(lines[i]) + '\n'  # записываем обработанные строки в новую переменную через Enter
        i += 1
    return new_text


print(corrected_text(text_str))
