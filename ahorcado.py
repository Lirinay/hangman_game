import random
import os

def select_word():
    words = []
    with open('./archivos/data.txt', 'r', encoding = 'utf-8') as file:
      for word in file:
          words.append(word.rstrip('\n'))

    words_index = random.randint(1, len(words))
    word_to_guess = words[words_index]
    a,b = 'áéíóúü','aeiouu'
    trans = str.maketrans(a,b)
    word_to_guess = word_to_guess.translate(trans)
    word_to_guess = word_to_guess.upper()
    return word_to_guess

def guess_word():
    word_to_guess = select_word()
    list_word_to_guess = [i for i in word_to_guess]
    guess_word = ['_' for i in word_to_guess]

    hangman = [
    """
    +-----+
    |
    |
    |
    |
    |
    +++++++"""
    ,
    """
    +-----+
    |     O
    |
    |
    |
    |
    +++++++"""
    ,
    """
    +-----+
    |     O
    |     |
    |
    |
    |
    +++++++"""
    ,
    """
    +-----+
    |     O
    |    >|
    |
    |
    |
    +++++++"""
    ,
    """
    +-----+
    |     O
    |    >|<
    |
    |
    |
    +++++++"""
    ,
    """
    +-----+
    |     O
    |    >|<
    |     |
    |
    |
    +++++++"""
    ,
    """
    +-----+
    |     O
    |    >|<
    |     |
    |    >
    |
    +++++++"""
    ,
    """
    +-----+
    |     O
    |    >|<
    |     |
    |    > <
    |
    +++++"""
       ]
    lives = 0
    input_letters = []
    while guess_word != list_word_to_guess:
        print('\n')
        print('¡Adivina la palabra secreta!')
        print('\n')
        print(*guess_word, '\n')
        print(hangman[lives])
        print('Letras ingresadas: ',*input_letters)
        print('\n')
        print('Te quedan ' + str(8 - lives) + ' vidas')
        letter = input('Ingresa una letra: ').upper()
        assert letter.isalpha(), 'Debes ingresar una letra'
        input_letters.append(letter)
        for position, value in enumerate(list_word_to_guess):
            if value == letter:
                guess_word[position] = letter
        if letter not in list_word_to_guess:
            if lives < 7:
                lives += 1
            else:
                guess_word = list_word_to_guess
        os.system('clear')
    if lives == 7:
        print('Perdiste, la palabra secreta es: ' + word_to_guess)
        print(hangman[lives])
    else:
        print('!Ganaste! la palabra secreta es: ' + word_to_guess)


def main():
    os.system('clear')
    guess_word()


if __name__ == '__main__':
    main()
