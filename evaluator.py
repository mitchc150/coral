import line_parser
import environment

global_env = environment.standard_env()


def evaluate(x: line_parser.Expression, env) -> line_parser.Expression:
    if isinstance(x, line_parser.Symbol):        # variable reference
        return env[x]
    elif isinstance(x, line_parser.Number):      # constant number
        return x
    elif x[0] == 'if':               # conditional
        (_, test, conseq, alt) = x
        exp = (conseq if evaluate(test, env) else alt)
        return evaluate(exp, env)
    elif x[0] == 'define':           # definition
        (_, symbol, exp) = x
        env[symbol] = evaluate(exp, env)
    elif x[0] == 'lambda':
        (symbol, exp) = args

    else:                            # procedure call
        proc = evaluate(x[0], env)
        args = [evaluate(arg, env) for arg in x[1:]]
        return proc(*args)