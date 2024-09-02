import evaluator
import line_parser
import environment

# the global environment which the program runs in. This is required to persistently store
# variables, function definitions, and so forth.
global_env = environment.standard_env()

prompt = ">>"


def repl(prompt='>>'):
    while True:
        user_input = input(prompt)

        expression_value = evaluator.evaluate(line_parser.interpret_tokens(line_parser.parse_line(user_input)), global_env)

        if expression_value is not None:
            print(coralize(expression_value))


def coralize(exp):
    if isinstance(exp, line_parser.List):
        return '(' + ' '.join(map(coralize, exp)) + ')'
    else:
        return str(exp)
