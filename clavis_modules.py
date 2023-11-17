import string
import secrets

ups = list(string.ascii_uppercase)
lows = list(string.ascii_lowercase)
nums = list(string.digits)
puncs = list(string.punctuation)



def printups():
    print(ups)

def printlows():
    print(lows)

def printnums():
    print(nums)

def printpuncs():
    print(puncs)

def get_number(prompt): #tested
    while True:            
        try:
            number = int(input(prompt))
            if number<=0: raise ValueError
            break
        except ValueError:
            print("ERROR: Entry is not an positive integer.")
            continue
    return number

def swap_in_list(any_list, pos1, pos2): #tested
    temp = any_list[pos1]
    any_list[pos1] = any_list[pos2]
    any_list[pos2] = temp
    return any_list

def shuffle_list(any_list, times = 3): #tested
    for _ in range(times):
        for i in range(len(any_list)):
            pos2 = secrets.randbelow(len(any_list))
            any_list = swap_in_list(any_list, i, pos2)
    return any_list

def select_randomly(any_list, num = 6): #tested
    selected_list = []
    for _ in range(num):
        selected_list.append(any_list[secrets.randbelow(len(any_list))])
    return selected_list

def get_excluded_puncstring(prompt): #tested
    excluded_punclist = list(input(prompt))
    clean_excluded_puncstring = []
    for punc in excluded_punclist:
        if punc in puncs:
            clean_excluded_puncstring.append(punc)
    clean_excluded_puncstring = list(set(clean_excluded_puncstring))
    return clean_excluded_puncstring

def exclude_from_puncs(excluded_punc_string): #tested
    for punc in excluded_punc_string:
        puncs.remove(punc)
    if sorted(puncs) == sorted(string.punctuation):
        print("No symbols were excluded")
    return puncs

UPPERCASE_PROMPT = "\nEnter the number of uppercase alphabetic characters that must be included in the password (default = 6): "
LOWERCASE_PROMPT = "\nEnter the number of lowercase alphabetic characters that must be included in the password (default = 6): "
NUMERIC_PROMPT = "\nEnter the number of numeric characters that must be included in the password (default = 6): "
PUNCTUATION_PROMPT = "\nEnter the number of punctuation symbols that must be included in the password (default = 6): "
GET_EXCLUDED_PUNCSTRING = f"\n{puncs}" + "\nEnter the punctuation symbols to be excluded from your password: "
SHUFFLE_PROMPT = "\nEnter the number of times to shuffle the password (default = 3): "
SATISFACTION_PROMPT = "\nAre you satisfied with the password generation? (y/n) "