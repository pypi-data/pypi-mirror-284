'''
* Sumary: Script to throw custom errors
* Author: Anthony Carrillo
* Email: anthonyzok521@gmail.com
* Github: https://github.com/Anthonyzok521
* License: MIT
* Datetime: 13/07/2024
'''

from colorama import Fore

class Error(Exception):  # Inherit from `Exception` for proper exception handling
    '''
    Class to represent custom errors.

    Attributes:
        type_error (str): Type of the error (optional).
        message (str): Error message (defaults to an empty string).
    '''
    def __init__(self, message:str, type_error: str = '') -> None:
        super().__init__()
        self.type_e = type_error
        self.msg_e = f"Error: {message}"

    def info(self) -> str:
        '''
        Static Method to show info of the error

        Return:
            error -> str
        '''

        #If type is specificted, return
        _type_e:str = self.type_e

        if self.type_e != '':
            _type_e = f'- Type: {self.type_e}'

        return f"{Fore.RED}{self.msg_e} {_type_e}{Fore.RESET}"
