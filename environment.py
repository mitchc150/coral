import math
import operator as op
import line_parser


def standard_env() -> line_parser.Environment:
    env = line_parser.Environment()
    env.update(vars(math))  # sin, cos, sqrt, pi, ...
    env.update({
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': op.truediv,
        '>': op.gt,
        '<': op.lt,
        '>=': op.ge,
        '<=': op.le,
        '=': op.eq,
        '<<': op.rshift,
        '>>': op.lshift,
        '&': op.and_,
        '^': op.xor,
        '~': op.invert,
        '|': op.or_,
        'abs': abs,
        'append': op.add,
        'apply': lambda proc, args: proc(*args),
        'begin': lambda *x: x[-1],
        'car': lambda x: x[0],
        'cdr': lambda x: x[1:],
        'cons': lambda x, y: [x] + y,
        'getitem': op.getitem,
        'eq?': op.is_,
        'expt': pow,
        'equal?': op.eq,
        'length': len,
        'list': lambda *x: line_parser.List(x),
        'list?': lambda x: isinstance(x, line_parser.List),
        'map': map,
        'max': max,
        'min': min,
        'not': op.not_,
        'null?': lambda x: x == [],
        'number?': lambda x: isinstance(x, line_parser.Number),
        'print': print,
        'procedure?': callable,
        'round': round,
        'symbol?': lambda x: isinstance(x, line_parser.Symbol),
        'while': lambda x, y: whileLoop(x, y),
    })
    return env


def whileLoop(x, y):
    while x:
        y()
