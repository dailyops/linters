# -- Linter to validate SpEL and Jinja2 based Spinnaker templates -- #

import sys
import re
from jinja2 import Environment, FileSystemLoader, TemplateSyntaxError

# Placeholder jsonpath filter to avoid syntax errors during linting
def jsonpath(value, expression):
    return []

def lint_jinja2(template_path):
    try:
        env = Environment(loader=FileSystemLoader('.'), extensions=['jinja2.ext.do'])
        env.filters['jsonpath'] = jsonpath  # Add the placeholder jsonpath filter
        env.get_template(template_path)
        print(f'[Jinja2] {template_path}: Syntax OK')
    except TemplateSyntaxError as e:
        print(f'[Jinja2] Syntax Error in {template_path} (Line {e.lineno}): {e}')

def is_balanced(expression):
    # Check for balanced brackets and quotes
    stack = []
    quote = None
    for char in expression:
        if char in "'\"":
            if quote is None:
                quote = char
            elif quote == char:
                quote = None
        elif quote is None:
            if char in '[({':
                stack.append(char)
            elif char in '])}':
                if not stack or {')': '(', ']': '[', '}': '{'}[char] != stack.pop():
                    return False
    return not stack and quote is None

def lint_spel(template_path):
    spel_pattern = r'\${[^}]+}'  # Detects SpEL expressions like ${expression}
    try:
        with open(template_path, 'r') as file:
            for lineno, line in enumerate(file, start=1):
                # Extract potential SpEL expressions within Jinja2 syntax
                matches = re.findall(spel_pattern, line)
                for match in matches:
                    expression = match[2:-1].strip()
                    if not is_balanced(expression):
                        print(f'[SpEL] Possible Syntax Error in {template_path} (Line {lineno}): {match}')
        print(f'[SpEL] {template_path}: Syntax OK')
    except Exception as e:
        print(f'[SpEL] Error reading {template_path}: {e}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python linter.py <template_path>')
        sys.exit(1)
    template_path = sys.argv[1]
    lint_jinja2(template_path)
    lint_spel(template_path)
