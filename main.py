from random import choice

print('Hello! I am a magic 8 ball. I can answer your questions')

ANSWERS = ["Undoubtedly", "I think yes", "It’s not clear yet, try again", "Don’t even think",
           "Foregone conclusion", "Most likely", "Ask later", "My answer is no",
           "No doubt", "Good prospects", "It's better not to tell", "According to my data - no",
           "You can be sure of this", "Yes", "Concentrate and ask again", "Very doubtful"]


def get_answer(question):
    question = clear_text_question(question)
    if question.isspace() or question == '' or question.isdigit():
        return 'No question - no answer.'

    return f'To the question "{question}" I answer: {choice(ANSWERS)}'


def clear_text_question(text):
    clear_text = ''
    for char in text:
        if char.isalnum() or char == ' ':
            clear_text += char
    return clear_text.lower()


def game():
    name = clear_text_question(input('What is your name? ')).capitalize()
    if name == '':
        name = "Stranger"
    print(f'Hey {name}')
    while True:
        question = input(f'{name}! What is your question?')
        print(get_answer(question))
        one_more = input('One more question? Press "Y" to continue or other key to end.')
        if one_more.lower() == 'y':
            continue
        else:
            print('See you again!')
            break


if __name__ == '__main__':
    game()
