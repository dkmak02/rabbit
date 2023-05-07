import re
import expr.calcValue as cv

def compare(string, dict):

    split_string = re.split(r'(\s*(?:)!=|>=|<=|==|[<>])', string)
    if (len(split_string) > 3):
        join = ''.join(split_string[2:])
        split_string[2] = compare(join, dict)
    if (len(split_string) == 1):
        if split_string[0] in dict:
            if dict[split_string[0]]['type'] == 'int':
                val = cv.calcValue(split_string, dict)
                return True if int(val) != 0 else False
            return dict[split_string[0]]['value']
        if split_string[0] == 'true' or split_string[0] == 'True':
            return True
        if split_string[0] == 'false' or split_string[0] == 'False':
            return False
        val = cv.calcValue(split_string, dict)
        return True if int(val) != 0 else False
    v1 = 0
    v2 = 0
    tre_check = [True, 'True', 'true']
    false_check = [False, 'False', 'false']
    if split_string[0] in tre_check or split_string[0] in false_check:
        v1 = 1 if split_string[0] in tre_check else 0
    else:
        v1 = int(cv.calcValue(split_string[0], dict))
    if split_string[2] in tre_check or split_string[2] in false_check:
        v2 = 1 if split_string[0] in tre_check else 0
    else:
        v2 = int(cv.calcValue(split_string[2], dict))
    com = split_string[1]
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