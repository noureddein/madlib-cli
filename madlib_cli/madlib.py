from importlib.resources import contents
import re

"""
    ? Create read_template function
    ? Create parse_template function
    ? Create merge function

"""


from calendar import c


welcome_msg = """
    ******************************************************
    **      Welcome to MADLIB game.                     **
    **      MADLIB game is a funny game.                **
    **      We will ask you some question.              **
    **      Answer the questions to see the magic.      **
    ******************************************************
"""


def get_fields(text):
    pattern = r'{([^}]+)}'
    match = tuple(re.findall(pattern, text))
    return match


def get_user_inputs(fields):
    user_inputs = []
    for field in fields:
        user_answer = input(f'Enter a {field}: ')
        while user_answer == None or user_answer == '':
            user_answer = input(f'Enter a {field}: ')
        user_inputs.append(user_answer)
    return user_inputs


def read_template(path):
    try:
        with open(f'../{path}', 'r') as f:
            content = f.read()
    except:
        raise FileNotFoundError('Check the path of the file!')
    else:
        return content


def parse_template(text):
    fields = get_fields(text)
    pattern = r'{([^}]+)}'
    new_text = re.sub(pattern, "{}", text)
    return new_text, fields


def merge(text, user_inputs):
    return text.format(*user_inputs)


# print(welcome_msg)
# text = read_template('assets/sample.txt')
# new_text, user_inputs = parse_template(text)
# user_inputs = tuple(get_user_inputs(fields))
# print('------------------------------ Here are your answers ------------------------')
# print(merge(new_text, user_inputs))
