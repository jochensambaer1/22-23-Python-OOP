# Oefening 15
# Bij het schrijven van een functie is een goede manier van werken om een docstring
# te voorzien die de werking van de functie beschrijft. Soms vergeet de ontwikkelaar
# evenwel om de docstring toe te voegen. Maak een programma dat één of meerdere
# .py bestanden inleest en functies detecteert die niet voorzien zijn van een docstring.
# Je programma toont alle functies, vergezeld van de bestandsnaam waar de functie
# zich bevindt. De gebruiker zal de naam of namen van één of meerdere bestanden
# die moeten nagekeken worden meegeven als command-line argument(en). Je
# voorziet een gepaste foutmelding wanneer bestanden niet bestaan of kunnen
# worden geopend. Je programma loopt wel verder en analyseert de bestanden die
# wel bestaan.
import sys
import os
import ast


def check_docstrings(filename):
    try:
        with open(filename) as f:
            code = f.read()
    except OSError:
        print(f"Could not open file {filename}")
        return []

    class DocstringChecker(ast.NodeVisitor):
        def __init__(self, filename):
            self.filename = filename
            self.functions = []

        def visit_FunctionDef(self, node):
            if not ast.get_docstring(node):
                self.functions.append((node.name, self.filename))

    tree = ast.parse(code)
    checker = DocstringChecker(filename)
    checker.visit(tree)
    return checker.functions


if __name__ == "__main__":
    filenames = sys.argv[1:]
    if not filenames:
        print("Usage: python check_docstrings.py <filename>...")
        sys.exit(1)

    functions_without_docstrings = []
    for filename in filenames:
        functions_without_docstrings.extend(check_docstrings(filename))

    if functions_without_docstrings:
        for function, filename in functions_without_docstrings:
            print(f"Function {function} in file {filename} is missing a docstring")
    else:
        print("All functions have a docstring")
