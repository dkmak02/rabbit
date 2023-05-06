import re
import expr.calcValue as cv

def compare(string, dict):
    split_string = re.split(r'(\s*(?:)!=|>=|<=|==|[<>])', string)

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
    v1 = int(cv.calcValue(split_string[0], dict))
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