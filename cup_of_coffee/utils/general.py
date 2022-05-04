"""This module concentrates all generic helper functions, e.g, functions that does not require language management

Function list:

    - _display_n_line_warn(flat_list)
    - _display_one_line_attention(text)
    - _display_n_line_attention(flat_list)
    - _display_two_line_attention(text1, text2)
    - _display_warn(aviso, texto)
    - _flatten_list_of_list_string(list_of_lists)

"""
#########################################
################ Imports ################
#########################################

###### Standard ######

###### Third part ######
from colorama import Fore, Style, Back, init

###### Home made ######


###########################################
################ Functions ################
###########################################


def _display_n_line_warn(flat_list):
    init()
    size = len(max(flat_list, key=len))
    print("\n")
    print(Fore.RED, "-"*size)
    i = 0
    for text in flat_list:
        if i == 0:
            print(Fore.RED, text)
        else:
            print(Fore.WHITE, text)
        i += 1
    print(Fore.RED, "-"*size)
    print("\n")
    print(Style.RESET_ALL)

def _display_one_line_attention(text):
    print("\n")
    print("^"*len(text))
    print(text)
    print("^"*len(text))
    print("\n")

def _display_n_line_attention(flat_list):
    size = len(max(flat_list, key=len))
    print("\n")
    print("^"*size)
    for text in flat_list:
        print(text)
    print("^"*size)
    print("\n")

def _display_two_line_attention(text1, text2):
    size = max(len(text1), len(text2))
    print("\n")
    print("^"*size)
    print(text1)
    print(text2)
    print("^"*size)
    print("\n")

def _display_warn(aviso, texto):
    init()
    size = max(len(aviso), len(texto))
    print("\n")
    print(Fore.RED, "-"*size)
    print(Fore.RED, aviso)
    print(Fore.WHITE, texto)
    print(Fore.RED, "-"*size)
    print("\n")
    print(Style.RESET_ALL)

def _flatten_list_of_list_string(list_of_lists):
    """
    Example:
    a = ['The language enn is not available yet.', 'The languages available are:', ['  --->  en', '  --->  pt-br']]
    flat_list = _flatten_list_of_list_string(a)
    flat_list = list(flat_list)

    source: https://stackoverflow.com/a/5286571/17872198
    """
    for x in list_of_lists:
        if hasattr(x, '__iter__') and not isinstance(x, str):
            for y in _flatten_list_of_list_string(x):
                yield y
        else:
            yield x











# But I remember... everything   https://youtu.be/76iQNS9VLkc?t=70
