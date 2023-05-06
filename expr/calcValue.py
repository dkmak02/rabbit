import re
import sys


def calcValue(split_string, dict):

    if isinstance(split_string, list):
        split_string = split_string[0]
    else:
        split_string = split_string
    split_string = re.split(r'([*/+-])', split_string)
    for i in range(len(split_string)):
        if split_string[i] == '':
            split_string[i] = '0'
    for v in split_string:
        if v in dict or v.isdigit() or v in ['*', '/', '+', '-']:
            continue
        else:
            print("Error: Variable not defined")
            sys.exit()
    if split_string[0] == '':
        split_string[0] = '0'
    while '*' in split_string or '/' in split_string:
        for v in split_string:
            if v in ['*', '/']:
                operator = split_string.index(v)
                type = dict[split_string[operator - 1]]['type'] if split_string[operator - 1] in dict else 'int'
                type2 = dict[split_string[operator + 1]]['type'] if split_string[operator + 1] in dict else 'int'
                if type != 'int' or type2 != 'int':
                    print("Error: Can't multiply or divide different types")
                    sys.exit()
                dsa = dict[split_string[operator - 1]]['value'] if split_string[operator - 1] in dict else split_string[
                    operator - 1]
                dsa2 = dict[split_string[operator + 1]]['value'] if split_string[operator + 1] in dict else split_string[
                    operator + 1]
                v1 = operator - 1
                v2 = operator + 1
                if v == '*':
                    split_string[v1] = str(int(dsa) * int(dsa2))
                    split_string.pop(v2)
                    split_string.pop(operator)
                elif v == '/':
                    split_string[v1] = str(int(int(dsa) / int(dsa2)))
                    split_string.pop(v2)
                    split_string.pop(operator)
                break
    while len(split_string) > 1:
        for v in split_string:
            if v in ['+', '-']:
                operator = split_string.index(v)
                type = dict[split_string[operator - 1]]['type'] if split_string[operator - 1] in dict else 'int'
                type2 = dict[split_string[operator + 1]]['type'] if split_string[operator + 1] in dict else 'int'
                if type != 'int' or type2 != 'int':
                    print("Error: Can't add or subtract different types")
                    sys.exit()
                dsa = dict[split_string[operator - 1]]['value'] if split_string[operator - 1] in dict else split_string[
                    operator - 1]
                dsa2 = dict[split_string[operator + 1]]['value'] if split_string[operator + 1] in dict else split_string[
                    operator + 1]
                v1 = operator - 1
                v2 = operator + 1

                if v == '+':
                    split_string[v1] = str(int(dsa) + int(dsa2))
                    split_string.pop(v2)
                    split_string.pop(operator)
                elif v == '-':
                    split_string[v1] = str(int(dsa) - int(dsa2))
                    split_string.pop(v2)
                    split_string.pop(operator)
    if split_string[0] in dict:
        if dict[split_string[0]]['type'] != 'int':
            print("Error: Can't return non int value")
            sys.exit()
        elif dict[split_string[0]]['type'] == 'int':
            return dict[split_string[0]]['value']
    return split_string[0]