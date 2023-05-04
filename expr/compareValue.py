import re
import expr.calcValue as cv

def compare(string, dict):
    split_string = re.split(r'(\s*(?:)!=|>=|<=|==|[<>])', string)
    if (len(split_string) == 1):
        if split_string[0] in dict:
            return dict[split_string[0]]['value']
        if split_string[0] == 'true' or split_string[0] == 'True':
            return True
        if split_string[0] == 'false' or split_string[0] == 'False':
            return False
        val = cv.calcValue(split_string, dict)
        return True if int(val) != 0 else False
    v1 = cv.calcValue(split_string[0], dict)
    v2 = cv.calcValue(split_string[2], dict)
    com = split_string[1]
    v1 = dict[v1] if v1 in dict else v1
    v2 = dict[v2] if v2 in dict else v2
    if com == '==':
        if v1 == v2:
            return True
    elif com == '!=':
        if v1 != v2:
            return True
    elif com == '>':
        if v1 > v2:
            return True
    elif com == '<':
        if v1 < v2:
            return True
    elif com == '>=':
        if v1 >= v2:
            return True
    elif com == '<=':
        if v1 <= v2:
            return True
    return False