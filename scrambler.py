from clavis_modules import *

def generator(list1, list2, list3, list4):    
    password = "".join(shuffle_list((list1+list2+list3+list4),get_number(SHUFFLE_PROMPT)))
    return password

def satisfaction_check():
    while True:
        c = input(SATISFACTION_PROMPT)
        if c.lower()[0]=='y':
            return True
        elif c.lower()[0]=='n':
            return False
        else:
            continue

def main():
    while True:
        ups_selected = select_randomly(ups,get_number(UPPERCASE_PROMPT))
        print(ups_selected)
        lows_selected = select_randomly(lows,get_number(LOWERCASE_PROMPT))
        print(lows_selected)
        nums_selected = select_randomly(nums,get_number(NUMERIC_PROMPT))
        print(nums_selected)
        puncs_before_selection = exclude_from_puncs(get_excluded_puncstring(GET_EXCLUDED_PUNCSTRING))
        print(f"The functional list of punctuation symbols is: {puncs_before_selection}")
        puncs_selected = select_randomly(puncs_before_selection,get_number(PUNCTUATION_PROMPT))
        print(puncs_selected)
        print(f"The generated password is: \n{generator(ups_selected,lows_selected,nums_selected,puncs_selected)}")
        if satisfaction_check()==False: 
            print("Commencing password regeneration...")
            continue
        else:
            break

main()