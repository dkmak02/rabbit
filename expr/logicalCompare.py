import expr.compareValue as compareValue
def compare(string,dict):
    while len(string)>1:
        for exp in string:
            if exp == 'and':
                char_index = string.index(exp)
                if compareValue.compare(string[char_index-1], dict) is True and compareValue.compare(string[char_index+1], dict) is True:
                    string[char_index-1] = True
                    string.pop(char_index+1)
                    string.pop(char_index)
                else:
                    string[char_index-1] = False
                    string.pop(char_index+1)
                    string.pop(char_index)
            elif exp == 'or':
                char_index = string.index(exp)
                if compareValue.compare(string[char_index-1], dict) is True or compareValue.compare(string[char_index+1], dict) is True:
                    string[char_index - 1] = True
                    string.pop(char_index + 1)
                    string.pop(char_index)
                else:
                    string[char_index - 1] = False
                    string.pop(char_index + 1)
                    string.pop(char_index)
    return True if string[0] is True else False