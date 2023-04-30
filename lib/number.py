'''
Created By: Mahershi Bhavsar
Email: mahershi1999@gmail.com
Last Modified: April 30, 2023
Modified By: Mahershi Bhavsar
'''


from lib.global_vars import GlobalVars


"""
NumberResolve
Purpose: Number handling functions. 
"""
class NumberResolve:
    deci = ''
    prev = ''

    @staticmethod
    def __reset():
        NumberResolve.deci = ''
        NumberResolve.prev = ''

    @staticmethod
    def __maxmatch(word):
        for i in GlobalVars.units_dict:
            if i in word:
                return i

        for i in GlobalVars.tens_dict:
            if i in word:
                return i

        return None

    @staticmethod
    def __resolve_sub(w):
        if w in GlobalVars.scales_dict:
            if NumberResolve.prev == 'unit':
                return str(00)
            NumberResolve.prev = 'scales'
            return str(GlobalVars.scales_dict[w])

        if w in GlobalVars.tens_dict:
            if NumberResolve.prev == 'scales':
                NumberResolve.deci = NumberResolve.deci[:-2]

            NumberResolve.prev = 'tens'
            return str(GlobalVars.tens_dict[w])

        if w in GlobalVars.units_dict:
            if NumberResolve.prev == 'tens':
                NumberResolve.deci = NumberResolve.deci[:-1]

            NumberResolve.prev = 'unit'
            return str(GlobalVars.units_dict[w])
        match = NumberResolve.__maxmatch(w)
        if match:
            return NumberResolve.__resolve_sub(match)
        else:
            if w in GlobalVars.stemmer:
                return NumberResolve.__resolve_sub(GlobalVars.stemmer[w])

        return ''

    # Call this to convert number in words to number in digits
    @staticmethod
    def resolve_number_words(words):
        NumberResolve.__reset()
        if type(words) != list:
            words = words.split(' ')
        for w in words:
            # cannot write deci+=resolve_sub(w), bcz desi is modified in resolve_sub and resolve has the older version
            c = NumberResolve.__resolve_sub(w)
            NumberResolve.deci += c

        return NumberResolve.deci


