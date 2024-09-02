Symbol = str
Number = (int, float)
Atom = (Symbol, Number)
List = list
Expression = (Atom, List)
Environment = dict


def parse_line(line):
    tokens = []
    current_token = ''

    for char in line:
        if char in '()':
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(char)
        elif char.isspace() or char == ',':
            if current_token:
                tokens.append(current_token)
            current_token = ''
        else:
            current_token += char

    if current_token:
        tokens.append(current_token)

    return tokens


def interpret_tokens(tokens: list):
    if len(tokens) == 0:
        raise SyntaxError('tokens length is 0')

    token = tokens.pop(0)

    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(interpret_tokens(tokens))
        tokens.pop(0)
        return L
    elif token == ')':
        raise SyntaxError('did not expect end of expression')
    else:
        return translate(token)


def translate(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return str(token)
