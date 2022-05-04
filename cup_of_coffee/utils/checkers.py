"""This module concentrates checkers-like functions, which check the type of variable.

Function list:

    - _check_data_in_range(value, param_name, min, max, language)
    - _check_is_bool(value, param_name, language)
    - _check_is_data_frame(df, param_name, language)
    - _check_is_dict(value, param_name, language)
    - _check_is_integer(value, param_name, language)
    - _check_is_float_or_int(value, param_name, language)
    - _check_is_float(value, param_name, language)
    - _check_is_list(value, param_name, language)
    - _check_is_numpy_1_D(value, param_name, language)
    - _check_is_positive(value, param_name, language)
    - _check_is_str(value, param_name, language)


"""


#########################################
################ Imports ################
#########################################

###### Standard ######

###### Third part ######
import numpy as np
import pandas as pd

###### Home made ######
from cup_of_coffee.database_management import management
from cup_of_coffee.utils import  general


###########################################
################ Functions ################
###########################################

# with tests, with text, with database
def _check_data_in_range(value, param_name, lower, upper, language):
    """This function checks if a 'value' is within the range between min and max.

    Parameters
    ----------
    value : number
        The value to be evaluated
    param_name : string
        The original name of the parameter passed through the parameter 'value'.
    lower : number
        The lower bound
    upper : number
        The upper bound
    language : string
        The language code

    Notes
    -----
    The parameter 'param_name' isn't checked if it is a string.
    The parameter 'language' isn't checked if it is a string.

    If lower is higher than upper, the function corrects these values automatically.

    Returns
    -------
    True if 'value' is in the range: min < value < max
    ValueError if 'value' is not in the range: min < value < max

    """
    _check_is_float_or_int(value, "value", language)
    _check_is_float_or_int(lower, "lower", language)
    _check_is_float_or_int(upper, "upper", language)

    values = [lower, upper]
    lower = min(values)
    upper = max(values)

    if lower < value < upper:
        pass
    else:
        ### quering ###
        func_name = "_check_data_in_range"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            message1 = "The"
            message2 = "parameter must be a number between"
            message3 = "and"
            message4 = "but we got"
            general._display_one_line_attention(
                f"{messages[2][0][0]} '{param_name}' {messages[2][2][0]} '{lower}' {messages[2][4][0]} '{upper}', {messages[2][6][0]} '{value}'",
                                )
            raise
    return True

# with tests, with text, with database
def _check_is_bool(value, param_name, language):
    """This function checks if a 'value' is a boolean.

    This function verifies if the parameter 'value' is the type of bool (True or false). If so, it returns True. If it is not, the function raises a ValueError.

    Parameters
    ----------
    value : any type
        If 'value' is a boolean (True or False) the function returns True.
        If 'value' is not a boolean, raises a ValueError.
    param_name : string
        The original name of the parameter passed through the parameter 'value'.
    language : string
        The language code

    Notes
    -----
    The parameter 'param_name' isn't checked if it is a string.
    The parameter 'language' isn't checked if it is a string.

    Returns
    -------
    True if 'value' is a boolean
    ValueError if 'value' is not a boolean


    """
    ### quering ###
    func_name = "_check_is_bool"
    fk_id_function = management._query_func_id(func_name)
    messages = management._get_messages(fk_id_function, language, func_name)

    if isinstance(value, bool) == False:
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}'  {messages[2][2][0]} '{type(value).__name__}'",
                                )
            raise

    return True

# with tests, with text, with database
def _check_is_data_frame(df, param_name, language):
    """This function checks if 'df' is a valid DataFrame

    This function checks if df a DataFrame and if it is empty.

    Parameters
    ----------
    df : any type
        The value to check if it is a DataFrame.
    param_name : string
        The original name of the parameter passed through the parameter 'df'.
    language : string
        The language code

    Notes
    -----
    The parameter 'param_name' isn't checked if it is a string.
    The parameter 'language' isn't checked if it is a string.

    Returns
    -------
    True if df is a valid DataFrame.
    Raises ValueError is df is not a valid DataFrame.


    """

    if isinstance(df, pd.DataFrame) == False:
        ### quering ###
        func_name = "_check_is_data_frame"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0]) #message
        except ValueError:
            general._display_one_line_attention(
                                text = f"{messages[2][0][0]} '{param_name}' {messages[2][2][0]} '{type(df).__name__}'"
                                )
            raise
    if df.empty:
        ### quering ###
        func_name = "_check_is_data_frame"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[3][0][0]) #message
        except ValueError:
            general._display_one_line_attention(
                                text = f"{messages[4][0][0]} '{param_name}' {messages[4][2][0]}"
                                )
            raise
    return True

# with tests, with text, with database
def _check_is_dict(value, param_name, language):
    """This function checks if a 'value' is a dict

    This function verifies if the parameter 'value' is the type of dict (type(value)==dict). If so, it returns True. If it is not a dict, the function raises a ValueError.

    Parameters
    ----------
    value : any type
        The value to check if it is a dict.
    param_name : string
        The original name of the parameter passed through the parameter 'value'.
    language : string
        The language code

    Notes
    -----
    The parameter 'param_name' isn't checked if it is a string.
    The parameter 'language' isn't checked if it is a string.

    Returns
    -------
    True if 'value' is a dict
    ValueError if 'value' is not a dict

    """
    if isinstance(value, dict) == False:
        ### quering ###
        func_name = "_check_is_dict"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0]) #message
        except ValueError:
            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}'  {messages[2][2][0]} '{type(value).__name__}'",
                                )
            raise
    return True

# with tests, with text, with database
def _check_is_integer(value, param_name, language):
    """This function checks if a 'value' is an integer

    This function verifies if the parameter 'value' is the type of integer (e.g, int, np.uint, np.integer). If so, it returns True. If it is not one of these types, the function raises a ValueError.

    Parameters
    ----------
    value : any type
        The value to check if it is an integer.
    param_name : string
        The original name of the parameter passed through the parameter 'value'.
    language : string
        The language code

    Notes
    -----
    The parameter 'param_name' isn't checked if it is a string.
    The parameter 'language' isn't checked if it is a string.

    Returns
    -------
    True if 'value' is integer
    ValueError if 'value' is not an integer

    """
    if isinstance(value, (int, np.uint, np.integer)) == False:
        ### quering ###
        func_name = "_check_is_integer"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}'  {messages[2][2][0]} '{type(value).__name__}'",
                                )
            raise
    return True

# with tests, with text, with database
def _check_is_float(value, param_name, language):
    """This function checks if a 'value' is an float

    This function verifies if the parameter 'value' is the type of float (e.g, float, np.floating). If so, it returns True. If it is not one of these types, the function raises a ValueError.

    Parameters
    ----------
    value : any type
        If 'value' is an float (e.g, float, np.floating) the function returns True.
        If 'value' is not an float, raises a ValueError.
    param_name : string
        The original name of the parameter passed through the parameter 'value'.
    language : string
        The language code

    Notes
    -----
    The parameter 'param_name' isn't checked if it is a string.
    The parameter 'language' isn't checked if it is a string.

    Returns
    -------
    True if 'value' is float
    ValueError if 'value' is not a float


    """

    if isinstance(value, (float, np.floating)) == False:
        ### quering ###
        func_name = "_check_is_float"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}'  {messages[2][2][0]} '{type(value).__name__}'",
                                )
            raise
    else:
        return True

# with tests, with text, with database
def _check_is_float_or_int(value, param_name, language):
    """This function checks if a 'value' is an float or integer.

    This function verifies if the parameter 'value' is the type of integer (e.g, int, np.uint, np.integer) or float (e.g, float, np.floating). If so, it returns True. If it is not one of these types, the function raises a ValueError.

    Parameters
    ----------
    value : any type
        The value to check if it is a float or integer.
    param_name : string
        The original name of the parameter passed through the parameter 'value'.
    language : string
        The language code

    Notes
    -----
    The parameter 'param_name' isn't checked if it is a string.
    The parameter 'language' isn't checked if it is a string.

    Returns
    -------
    True if 'value' is float or int.
    ValueError if 'value' is not a float or int.

    """

    if isinstance(value, (int, np.uint, np.integer, float, np.floating)) == False:
        ### quering ###
        func_name = "_check_is_float_or_int"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:

            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}' {messages[2][2][0]} '{type(value).__name__}'",
                                )
            raise
    else:
        return True

# with tests, with text, with database
def _check_is_list(value, param_name, language):
    """This function checks if a 'value' is a list

    This function verifies if the parameter 'value' is the type of list (type(value)==list). If so, it returns True. If it is not a list, the function raises a ValueError.

    Parameters
    ----------
    value : any type
        The value to check if it is a list.
    param_name : string
        The original name of the parameter passed through the parameter 'value'.
    language : string
        The language code

    Notes
    -----
    The parameter 'param_name' isn't checked if it is a string.
    The parameter 'language' isn't checked if it is a string.

    Returns
    -------
    True if 'value' is a list
    ValueError if 'value' is not a list

    """
    if isinstance(value, list) == False:
        ### quering ###
        func_name = "_check_is_list"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}'  {messages[2][2][0]} '{type(value).__name__}'",
                                )
            raise
    return True

# with tests, with text, with database
def _check_is_numpy_1_D(value, param_name, language):
    """This function checks if a 'value' is an numpy array of 1 dimension

    This function checks if the value is a 1-dimensional numpy array type. If not np.ndarray, raises ValueError. If value.ndim == 1, raises ValueError and if value.size == 0, raises ValueError. If no error is raised, it returns True indicating that value is a 1-dimensional numpy array.

    Parameters
    ----------
    value : any
        If 'value' is a non-empty 1-dimensional numpy array, returns True
        Else, raises a ValueError.
    param_name : string
        The original name of the parameter passed through the parameter 'value'.
    language : string
        The language code

    Notes
    -----
    The parameter 'param_name' isn't checked if it is a string.
    The parameter 'language' isn't checked if it is a string.

    Returns
    -------
    True if 'value' is a non-empty 1-dimensional numpy array
    ValueError if 'value' is not a non-empty 1-dimensional numpy array

    """
    ### quering ###
    func_name = "_check_is_numpy_1_D"
    fk_id_function = management._query_func_id(func_name)
    messages = management._get_messages(fk_id_function, language, func_name)

    if isinstance(value, np.ndarray) == False:
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}' {messages[2][2][0]} '{type(value).__name__}'",
                                )
            raise
    elif value.ndim != 1:
            try:
                raise ValueError(messages[3][0][0]) #message
            except ValueError:
                general._display_one_line_attention(
                                    f"{messages[4][0][0]} '{param_name}' {messages[4][2][0]} ndim = '{value.ndim}'",
                                    )
                raise
    elif value.size == 0:
            try:
                raise ValueError(messages[5][0][0]) #message
            except ValueError:
                general._display_one_line_attention(
                                    f"{messages[6][0][0]} '{param_name}' {messages[6][2][0]} = '{value.size}'",
                                    )
                raise
    else:
        return True

# with tests, with text, with database
def _check_is_positive(value, param_name, language):
    """This function checks if "value" is a positive number.

    This function verifies if the parameter 'value' has a number higher than 0. If so, it returns True. If the value is negative, Raises ValueError.

    Parameters
    ----------
    value : float or int (not tested)
        The value to be tesed
    param_name : string
        The original name of the parameter passed through the parameter 'value'.
    language : string
        The language code

    Notes
    -----
    The parameter 'param_name' isn't checked if it is a string.
    The parameter 'value' isn't checked if it is a number.
    The parameter 'language' isn't checked if it is a string.

    Returns
    -------
    True if 'value' is positive
    ValueError if 'value' is negative


    """
    if value <= 0:
        ### quering ###
        func_name = "_chek_is_positive"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}' {messages[2][2][0]} '{value}'",
                                )
            raise
    return True

# with tests, with text, with database
def _check_is_str(value, param_name, language):
    """This function checks if a value is a string by checking if it is of type string and if its size is higher than zero.

    Parameters
    ----------
    value : any type
        The value to check if it is a string.
    param_name : string
        The original name of the parameter passed through the parameter 'value'.
    language : string
        The language code

    Notes
    -----
    The parameter 'param_name' isn't checked if it is a string.
    The parameter 'language' isn't checked if it is a string.

    Returns
    -------
    True if value is a valid string.
    Raises ValueError is value is not a valid string.

    """
    ### quering ###
    func_name = "_check_is_str"
    fk_id_function = management._query_func_id(func_name)
    messages = management._get_messages(fk_id_function, language, func_name)
    if isinstance(value, str) == False:
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                                    text = f"{messages[2][0][0]} {param_name} {messages[2][2][0]} '{type(value).__name__}'"
                                )
            raise
    elif len(value) == 0:
        try:
            raise ValueError(messages[3][0][0])
        except ValueError:
            general._display_one_line_attention(
                                    text = f"{messages[4][0][0]} {param_name} {messages[4][2][0]}"
                                )
            raise
    else:
        return True



























# Kingslayer, destroying castles in thе sky https://youtu.be/ogtN8odrJTc?t=215
