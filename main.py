import pandas
nato_csv = "nato_phonetic_alphabet.csv"
nato_file = pandas.read_csv(nato_csv)

nato_dict = {row.letter:row.code for (index, row) in nato_file.iterrows()}

try:
    user_input = input("What would you like to have translated to Nato code?: ").upper()
except TypeError:
    if user_input == range(0, 9):
        print(f"Sorry, letters only please")
else:
    nato_code = [nato_dict[letter] for letter in user_input]
    print(nato_code)

    letter_list = [letter for letter in user_input]
    phonetics = [code for code in letter_list if code in nato_dict]
    # print(phonetics)

"""alt code"""
# print(nato_file.to_dict())
phonetic_dict = {row.letter:row.code for (index, row) in nato_file.iterrows()}
# print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
