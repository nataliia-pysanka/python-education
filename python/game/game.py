"""There is a game 'Hangman'.
Player should guesses a word symbol by symbol. There are only 6 wrong symbols.

"""

import random
import os

WORDS_FILE = 'words.txt'
USED_WORDS_FILE = 'used_words.txt'


def cls():
    """
    Clear terminal screen
    :return:
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def read_file(file_name):
    """
    Read file and return list of words in uppercase format
    :param file_name: file[str]
    :return: [str]
    """
    with open(file_name, mode='r', encoding='utf-8') as file:
        words = [line.strip().upper() for line in file]
    return words


def gen_rand_word(words):
    """
    Return random word from input list
    :param words: [str]
    :return: str
    """
    while True:
        word = random.choice(words)
        if word in read_file(USED_WORDS_FILE):
            continue
        else:
            return word


def draw_word(word, letters):
    """
    Draw boxes for input word with standard symbols and return number of
    correct letters
    :param word: str
    :param letters: [str]
    :return: int
    """
    num_letters = 0
    st_upper = ''
    st_middle = '|'
    st_down = ''
    st_word = '|'
    for i in range(len(word)):
        st_upper += ' ___'
        st_middle += '   |'
        if word[i] in letters:
            st_word += f' {word[i]} |'
            num_letters += 1
        else:
            st_word += '   |'
        st_down += ' ---'
    print(st_upper)
    print(st_word)
    print(st_down)
    return num_letters


def draw_hangman(score=0):
    """
    draw picture of hangman with standard symbols
    :param score: int
    :return:
    """
    hang = [
        ' #######',
        ' ##    |',
        ' ##',
        ' ##',
        ' ##',
        ' ##',
        '##########'
        ]
    hangman = {
        0: '',
        1: '    O',
        2: '    |',
        3: r'   \|',
        4: r'   \|/',
        5: '   /',
        6: r'   / \ '
    }
    current_line = 0
    while current_line < len(hang):
        if current_line == 2 and score >= 1:
            print(hang[2] + hangman[1])
        elif current_line == 3 and score >= 2:
            hang_st = hangman[score] if score in (2, 3, 4) else hangman[4]
            print(hang[3] + hang_st)
        elif current_line == 4 and score >= 5:
            hang_st = hangman[score] if score in (5, 6) else hangman[6]
            print(hang[4] + hang_st)
        else:
            print(hang[current_line])
        current_line += 1


def write_word_to_file(word):
    """
    Write used words into file
    """
    with open(USED_WORDS_FILE, mode='a', encoding='utf-8') as file:
        file.write(word + "\n")


def guess_word(word, letters, score):
    """
    Wait for letter and check it. Return inputted letters and score
    :param word: str
    :param letters: [str]
    :param score: int
    :return: dict
    """
    while True:
        cls()
        num_correct_letters = draw_word(word, letters)
        draw_hangman(score)
        print(f"Угадано: {num_correct_letters} букв")
        print(f"Можно ошибиться: {6 - score} раз")
        print(f"Уже использованы буквы: {', '.join(set(letters))}")
        if num_correct_letters == len(word):
            cls()
            draw_word(word, word)
            draw_hangman(score)
            write_word_to_file(word)
            print("Congratulation!!!")
            return {'letters': letters, 'score': score}
        ch = input('Загадай букву (выход - quit) >> ')
        if ch == 'quit':
            quit()
        elif len(ch) > 1:
            continue

        if ch.isalpha():
            letters.append(ch.upper())
            if ch.upper() not in word:
                score += 1
            if score == 6:
                cls()
                print('В этот раз не повезло')
                draw_word(word, word)
                draw_hangman(score)
                return {'letters': letters, 'score': score}


if __name__ == "__main__":
    words_list = read_file(WORDS_FILE)
    while True:
        round = {
            'letters': [],
            'score': 0,
        }
        menu = 'Сыграем? да - Enter, выход - quit, слова - list >> '
        answer = input(menu, )
        if answer == 'quit':
            break
        elif answer == 'list':
            cls()
            used_words = read_file(USED_WORDS_FILE)
            print(f"Прошлые слова: {', '.join(set(used_words))}")
            continue
        elif not answer:
            word = gen_rand_word(words_list)
            # write_word_to_file(word)
            round = guess_word(word, round['letters'], round['score'])
