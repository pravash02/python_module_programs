import streamlit as st
import random

st.cache()
def main():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
               'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '*', '#', '$']

    st.header('Random Passwaord Generator')

    nr_letters, nr_numbers, nr_symbols = st.columns([2, 2, 2])
    nr_letters = nr_letters.number_input('How Many Alphabets', min_value=0)
    nr_numbers = nr_numbers.number_input('How Many Numbers', min_value=0)
    nr_symbols = nr_symbols.number_input('How Many Symbols', min_value=0)

    password = ''

    for i in range(nr_letters):
        random_ = random.choice(letters)
        password += random_

    for i in range(nr_numbers):
        random_ = random.choice(numbers)
        password += random_

    for i in range(nr_symbols):
        random_ = random.choice(symbols)
        password += random_

    list_val = list(password)
    random.shuffle(list_val)

    paz = ''.join(list_val)

    st.header('Your Generated Password - ')
    st.warning(paz)


if __name__ == '__main__':
    main()
