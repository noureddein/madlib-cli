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
    """
        This function catch all the tempelates fields in the text.
        Input:
            String --> Text

        Output:
            Tuple --> Return all tempelates fields.
    """
    pattern = r'{([^}]+)}'
    match = tuple(re.findall(pattern, text))
    return match


def get_user_inputs(fields):
    """
        The function ask the user for inputs, depending on the tempelates fields.
        Input:
            Tuple --> Tuple containing fields tempelates.
        Output:
            list --> Return list of the user inputs.
    """
    user_inputs = []
    for field in fields:
        user_answer = input(f'Enter a {field}: ')
        while user_answer == None or user_answer == '':
            user_answer = input(f'Enter a {field}: ')
        user_inputs.append(user_answer)
    return user_inputs


def read_template(path):
    """
        Function take a path of a file, and return it's containt.
        Input:
            String --> Path of the file as a string.
        Output:
            String --> Return file content.
    """
    try:
        with open(f'../{path}', 'r') as f:
            content = f.read()
    except:
        raise FileNotFoundError('Check file path!')
    else:
        return content


def parse_template(text):
    """
        The function replace all the tempelates fields with empty curly braces,
        to prepare the text for filling of user inputs.
        Input:
            String --> The text of tempelates fields
        Output:
            String --> Return The new prepared text.
            Tuple --> Return all tempelates fields.

    """
    fields = get_fields(text)
    pattern = r'{([^}]+)}'
    new_text = re.sub(pattern, "{}", text)
    return new_text, fields


def merge(new_text, user_inputs):
    """
        The function fill all user inputs into the text.
        and return a new text.

        Input:
            String --> Text with empty tempelates fields.
            Tuple -->  User inputs.
    """
    return new_text.format(*user_inputs)


print(welcome_msg)
text = read_template('assets/sample.txt')
new_text, user_inputs = parse_template(text)
fields = get_fields(text)
user_inputs = tuple(get_user_inputs(fields))
print('------------------------------ Here are your answers ------------------------')
print(merge(new_text, user_inputs))
