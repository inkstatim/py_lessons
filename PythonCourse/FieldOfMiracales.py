import random

words = ['apple', 'banana', 'cherry', 'orange', 'pear']
word = random.choice(words)
guesses = set()
print(f'Вітаю в грі "Поле чудес"! Слово складається з {len(word)} букв.')
attempts = int(input('Введіть кількість спроб: '))


def is_word_guessed():
    return set(word) == guesses


def get_current_word():
    return ''.join(c if c in guesses else '*' for c in word)


while attempts > 0:
    print(f'У вас залишилось {attempts} спроб.')
    guess = input('Введіть букву або слово: ').strip().lower()

    if guess == word:
        print('Вітаю, ви вгадали слово!')
        break
    if guess in guesses:
        print('Ви вже вводили цю букву або слово. Спробуйте ще раз.')
        continue
    if len(guess) == 1:
        if guess in word:
            guesses.add(guess)
            print(f'Буква "{guess}" є у слові: {get_current_word()}')
        else:
            print(f'Буква "{guess}" відсутня у слові.')
            attempts -= 1
    else:
        print('Це не буква, спробуйте ввести слово або ще раз букву.')

    if is_word_guessed():
        print('Вітаю, ви вгадали слово!')
        break

if attempts == 0:
    print(f'На жаль, ви програли. Слово було "{word}".')
