import datetime

# NOTE: This is old code - one of my first big projects.
# I've learned much since then.

# selling points:
# 1. no ads
# 2. quicker than manually typing it out
# 3. join the open-source revolution!
# 4. easy to use
# 5. endorsed by <TODO: find someone to endorse the product>
# 6. Very flexible - experienced programmers can add aditional features,
# with lots of useful code already built in. Turing complete!

if __name__ == "__main__":
    import sys

    sys.setrecursionlimit(5000)  # make it bigger if necessary
    print(
        """Current version: 3.6.12
Updated to: MLA 9"""
    )

definitions = {
    # basic math - base 26 math with letters
    "add": [
        "if",
        "access_b",
        "a",
        "access_a",
        ["inc", ["add", "access_a", ["dec", "access_b"]]],
    ],
    "sub": [
        "if",
        "access_b",
        "a",
        "access_a",
        ["dec", ["sub", "access_a", ["dec", "access_b"]]],
    ],
    "mul": [
        "if",
        "access_b",
        "b",
        "access_a",
        ["add", "access_a", ["mul", "access_a", ["dec", "access_b"]]],
    ],
    "comp": ["if", ["sort", "access_a", "access_b"], "access_a", "a", "b"],
    "div_qt": [
        "if",
        ["comp", "access_b", "access_a"],
        "b",
        "a",
        ["inc", ["div_qt", ["sub", "access_a", "access_b"], "access_b"]],
    ],
    "div_rm": [
        "sub",
        "access_a",
        ["mul", ["div_qt", "access_a", "access_b"], "access_b"],
    ],
    "pwr": [
        "if",
        "access_b",
        "b",
        "access_a",
        ["mul", "access_a", ["pwr", "access_a", ["dec", "access_b"]]],
    ],
    # math v2 - base 10 math, integers
    # logic
    "and": [
        "if",
        "access_a",
        "a",
        ["if", "access_b", "a", "a", "a"],
        ["if", "access_b", "a", "a", "b"],
    ],
    "nand": [
        "if",
        "access_a",
        "a",
        ["if", "access_b", "a", "b", "b"],
        ["if", "access_b", "a", "b", "a"],
    ],
    "or": [
        "if",
        "access_a",
        "a",
        ["if", "access_b", "a", "a", "b"],
        ["if", "access_b", "a", "b", "b"],
    ],
    "nor": [
        "if",
        "access_a",
        "a",
        ["if", "access_b", "a", "b", "a"],
        ["if", "access_b", "a", "a", "a"],
    ],
    "xor": [
        "if",
        "access_a",
        "a",
        ["if", "access_b", "a", "a", "b"],
        ["if", "access_b", "a", "b", "a"],
    ],
    "xnor": [
        "if",
        "access_a",
        "a",
        ["if", "access_b", "a", "b", "a"],
        ["if", "access_b", "a", "a", "b"],
    ],
    # lists - '|' is break between items - TODO speedup
    "list_start": "{",
    "list_step": "}",
    "nil": "|",
    "cons": ["append", ["list_start"], "access_a", ["list_step"], "access_b"],
    "list_car": ["list_car_helper", ["cdr", "access_a"], "b"],
    "list_car_helper": [
        "if",
        "access_b",
        "a",
        "",
        [
            "append",
            ["car", "access_a"],
            [
                "list_car_helper",
                ["cdr", "access_a"],
                [
                    "if",
                    ["car", ["cdr", "access_a"]],
                    ["list_start"],
                    ["inc", "access_b"],
                    [
                        "if",
                        ["car", ["cdr", "access_a"]],
                        ["list_step"],
                        ["dec", "access_b"],
                        "access_b",
                    ],
                ],
            ],
        ],
    ],
    "list_cdr": ["list_cdr_helper", ["cdr", "access_a"], "b"],
    "list_cdr_helper": [
        "if",
        "access_b",
        "a",
        ["cdr", "access_a"],
        [
            "list_cdr_helper",
            ["cdr", "access_a"],
            [
                "if",
                ["car", ["cdr", "access_a"]],
                ["list_start"],
                ["inc", "access_b"],
                [
                    "if",
                    ["car", ["cdr", "access_a"]],
                    ["list_step"],
                    ["dec", "access_b"],
                    "access_b",
                ],
            ],
        ],
    ],
    "list_len": [
        "if",
        "access_a",
        ["nil"],
        "a",
        ["inc", ["list_len", ["list_cdr", "access_a"]]],
    ],
    "list_select_single": [
        "if",
        "access_a",
        "a",
        ["list_car", "access_b"],
        ["select_single", ["dec", "access_a"], ["list_cdr", "access_b"]],
    ],
    # BSTs abcde, xyz -> axbyczd_e
    "": [],
    "": [],
    "": [],
    "": [],
    # strings
    "count": [
        "if",
        "access_a",
        "",
        "a",
        [
            "if",
            ["car", "access_a"],
            "access_b",
            ["inc", ["count", ["cdr", "access_a"], "access_b"]],
            ["count", ["cdr", "access_a"], "access_b"],
        ],
    ],
    "find_place_front": [
        "if",
        ["car", "access_b"],
        "access_a",
        "a",
        [
            "if",
            ["len", "access_b"],
            "b",
            "--!error!--",
            ["inc", ["find_place_front", "access_a", ["cdr", "access_b"]]],
        ],
    ],
    "find_place_back": [
        "dec",
        [
            "sub",
            ["len", "access_b"],
            ["find_place_front", "access_a", ["reverse", "access_b"]],
        ],
    ],
    "len": ["if", "access_a", "", "a", ["inc", ["len", ["cdr", "access_a"]]]],
    "reverse": [
        "if",
        "access_a",
        "",
        "",
        ["append", ["reverse", ["cdr", "access_a"]], ["car", "access_a"]],
    ],
    "select_single": [
        "if",
        "access_a",
        "a",
        ["car", "access_b"],
        ["select_single", ["dec", "access_a"], ["cdr", "access_b"]],
    ],
    "select_multi": [
        "if",
        "access_b",
        "a",
        "",
        [
            "if",
            "access_a",
            "a",
            [
                "append",
                ["car", "access_c"],
                ["select_multi", "a", ["dec", "access_b"], ["cdr", "access_c"]],
            ],
            [
                "select_multi",
                ["dec", "access_a"],
                ["dec", "access_b"],
                ["cdr", "access_c"],
            ],
        ],
    ],
    # functions
    "lambda": ["append", ["define", "lambda_call", "access_a"], "lambda_call"],
    # loops
    "for": [
        "if",
        "access_a",
        ["nil"],
        "access_c",
        ["access_b", ["list_car", "access_a"], ["list_cdr", "access_a"]],
    ],
    "accumulate": [
        "if",
        "access_a",
        ["nil"],
        "access_c",
        [
            "access_b",
            ["list_car", "access_a"],
            ["accumulate", ["list_cdr", "access_a"], "access_b", "access_c"],
        ],
    ],
    "map": [
        "if",
        "access_a",
        ["nil"],
        "access_c",
        [
            "list_append",
            ["access_b", ["list_car", "access_a"]],
            ["list_cdr", "access_a"],
        ],
    ],
    "cond": [
        "if",
        ["list_car", "access_a"],
        ["list_car", "access_b"],
        ["list_car", "access_c"],
        [
            "cond",
            ["list_cdr", "access_a"],
            ["list_cdr", "access_b"],
            ["list_cdr", "access_c"],
        ],
    ],
    # special form based general use functions
    "ask_input_available": [
        "if",
        ["input", ["append", "Is ", "access_a", " available? y/n "]],
        "y",
        ["append", "access_b", ["input", ["append", "access_a", ": "]], "access_c"],
        "access_d",
    ],
    "ask_time_available": [
        "ask_input_available",
        "access_a",
        "access_b",
        "access_c",
        [
            "if",
            ["input", "Use current date? y/n "],
            "y",
            ["append", "access_b", ["time"], "access_c"],
            "access_d",
        ],
    ],
    # ciphers
    "rotate_once": [
        "if",
        "access_a",
        "",
        "",
        ["append", ["inc", ["car", "access_a"]], ["rotate_once", ["cdr", "access_a"]]],
    ],
    "ceaser": [
        "if",
        "access_a",
        "",
        "",
        [
            "append",
            ["add", ["car", "access_a"], "access_b"],
            ["ceaser", ["cdr", "access_a"], "access_b"],
        ],
    ],
    "vigenere": [
        "if",
        "access_a",
        "",
        "",
        [
            "append",
            ["add", ["car", "access_a"], ["car", "access_b"]],
            ["vigenere", ["cdr", "access_a"], ["rotate_once", "access_b"]],
        ],
    ],
    "undo_key": [
        "if",
        "access_a",
        "",
        "",
        [
            "append",
            ["sub", "a", ["car", "access_a"]],
            ["undo_key", ["cdr", "access_a"]],
        ],
    ],
    # random
    # sorting
    "list_insert_alphabetical": [
        "if",
        "access_a",
        "",
        "access_b",
        [
            "if",
            ["sort", "access_b", ["list_car", "access_a"]],
            "access_b",
            ["cons", "access_b", "access_a"],
            [
                "cons",
                ["list_car", "access_a"],
                ["list_insert_alphabetical", ["list_cdr", "access_a"], "access_b"],
            ],
        ],
    ],
    "list_alphabetical": [
        "if",  # TODO fix
        "access_a",
        ["nil"],
        "access_a",
        [
            "if",
            ["list_len", "access_a"],
            "b",
            ["append", ["list_car", "access_a"], "access_b"],
            [
                "list_insert_alphabetical",
                ["list_alphabetical", ["list_cdr", "access_a"], "access_b"],
                ["append", ["list_car", "access_a"], "access_b"],
            ],
        ],
    ],
    "shuffle_sort_single": [  # TODO fix
        "if",
        "access_a",
        ["nil"],
        "access_b",
        [
            "if",
            "access_b",
            ["nil"],
            "access_a",
            [
                "if",
                ["sort", ["list_car", "access_a"], ["car", "access_b"]],
                ["car", "access_a"],
                [
                    "append",
                    ["car", "access_a"],
                    ["shuffle_sort", ["cdr", "access_a"], "access_b"],
                ],
                [
                    "append",
                    ["car", "access_b"],
                    ["shuffle_sort", ["cdr", "access_b"], "access_a"],
                ],
            ],
        ],
    ],
    "shuffle_sort": [
        "shuffle_sort_single",
        [
            "shuffle_sort",
            ["select_multi", "a", ["div_qt", ["list_len", "access_a"], "c"]],
            [
                "select_multi",
                ["div_qt", ["list_len", "access_a"], "c"],
                "list_len",
                "access_a",
            ],
        ],
    ],
    # MLA
    "get_authors_MLA": [
        "if",
        ["input", "Is there at least one known author? y/n "],
        "y",
        [
            "append",
            [
                "if",
                ["input", "is only a username available? y/n "],
                "y",
                ["input", "Username: "],
                [
                    "append",
                    ["input", "Author 1 last name: "],
                    ", ",
                    ["input", "Author 1 first name: "],
                ],
            ],
            [
                "if",
                ["input", "Is there a second author? y/n "],
                "y",
                [
                    "if",
                    ["input", "Are there more than two authors? y/n "],
                    "y",
                    [
                        "append",
                        ", ",
                        "if",
                        ["input", "is only a username available? y/n "],
                        "y",
                        ["input" "Username: "],
                        [
                            "append",
                            ["input", "Author 2 last name: "],
                            ", ",
                            ["input", "Author 2 first name: "],
                        ],
                        ", Et Al. ",
                    ],
                    [
                        "append",
                        " and ",
                        "if",
                        ["input", "is only a username available? y/n "],
                        "y",
                        ["input" "Username: "],
                        [
                            "append",
                            ["input", "Author 2 last name: "],
                            ", ",
                            ["input", "Author 2 first name: "],
                        ],
                        ". ",
                    ],
                ],
                ". ",
            ],
        ],
        [
            "if",
            ["input", "Is the orginization that wrote it available? y/n "],
            "y",
            ["append", ["input", "Author orginization: "], ". "],
            "",
        ],
    ],
    "book_MLA": [
        "append",
        ["get_authors_MLA"],
        "<ITAL>",
        ["input", "Title: "],
        ".<ITAL> ",
        ["ask_input_available", "series/container title", "", "", ""],
        ["ask_input_available", "version/edition number", ", ", "", ""],
        ["ask_input_available", "volume number", ", ", "", ""],
        ". ",
        ["input", "Publisher: "],
        ["ask_time_available", "publication date", "", ". ", " "],
    ],
    "online_article_MLA": [
        "append",
        ["get_authors_MLA"],
        '"',
        ["input", "Title: "],
        '." <ITAL>',
        ["input", "Website title: "],
        ".<ITAL> ",
        ["ask_input_available", "version/edition number", ", ", "", ""],
        ["ask_input_available", "volume number", ", ", "", ""],
        ". ",
        ["input", "Publisher: "],
        ["ask_time_available", "publication date", "", ". ", " "],
        ["input", "URL: "],
        ". ",
        ["ask_time_available", "date of access", "Accessed ", ".", ""],
    ],
    "image_MLA": [
        "append",
        ["get_authors_MLA"],
        ' "',
        ["input", "Art title: "],
        ["ask_time_available", "creation date", ", ", '." ', '." '],
        "<ITAL>",
        ["input", "Website title: "],
        "<ITAL> ",
        ["ask_input_available", "version number", ", ", ". ", ". "],
        ["input", "Publisher: "],
        ["ask_time_available", "creation date", "", ". ", " "],
        ["input", "URL: "],
        ". ",
        ["ask_time_available", "date of access", "Accessed ", ".", ""],
    ],
    "whole_website_MLA": [
        "append",
        ["get_authors_MLA"],
        "<ITAL>",
        ["input", "Website title: "],
        ".<ITAL> ",
        ["ask_input_available", "version number", ", ", "", ""],
        ". ",
        ["input", "Publisher: "],
        ["ask_time_available", "creation date", "", ". ", " "],
        ["input", "URL: "],
        ". ",
        ["ask_time_available", "date of access", "Accessed ", ".", ""],
    ],
    "manual_MLA": ["input", "Manual citation: "],
    # general citation machine - finally!
    "create_biblio_MLA": [
        "alphabetical",
        [
            "append",
            ["create_biblio_MLA_helper"],
            ["print", "Creating your citation, please wait..."],
        ],
        "\n",
    ],
    "create_biblio_MLA_helper": [
        "if",
        ["input", "Any more sources? y/n "],
        "y",
        [
            "append",
            [
                "print",
                """Possible source types: online_article, whole_website, book, image, and manual. 
Other types will be supported in later updates.""",
            ],
            ["list_start"],
            [["append", ["input", "Source type: "], "_MLA"]],
            ["list_step"],
            ["create_biblio_MLA_helper"],
        ],
        ["nil"],
    ],
    # turing completeness proof TODO finish
    # current state, left strip, right/current strip, list of 26 states (list of 26 for what to go to), list of states(go/b/a/halt)
    "turing": [
        "turing_helper01",
        ["list_select_single", "access_a", "access_d"],
        ["list_select_single", "access_a", "access_e"],
        "access_b",
        "access_c",
    ],
    "turing_helper01": [
        "if",
        "access_b",
        "h",
        "halt",
        [
            "if",
            "access_b",
            "a",
            "a",
            [
                "if",
                "access_b",
                "b",
                "b",
            ],
        ],
    ],
    "turing_helper02": [],
    "turing_helper03": [],
    "turing_helper04": [],
}


# parsing functions
def tokenize(inputStr):
    output = []
    token = ""
    for char in inputStr:
        if char in "()":
            if token != "":
                output.append(token)
                token = ""
            output.append(char)
        elif (
            not char
            in """
    , """
        ):
            token += char
    return output


def parseTokens(inputLst):
    output = []
    position = 1
    while position < len(inputLst):
        token = inputLst[position]
        if token == ")":
            return output, position
        elif token == "(":
            block = parseTokens(inputLst[position:-1])
            output.append(block[0])
            position += block[1]
        else:
            output.append(token)
        position += 1


def parse(inputStr):
    return parseTokens(tokenize(inputStr))[0]


inputs = """"""
if inputs != "":
    totalInputs = inputs.split("\n")

accessList = []
for char in "abcdefghijklmnopqrstuvwxyz":
    accessList.append("access_" + char)


def searchTree(tree, search):
    if tree in search:
        return True
    elif type(tree) is str:
        return False
    else:
        check = False
        for branch in tree:
            if branch in search:
                check = True
                break
            elif type(branch) is list:
                if searchTree(branch, search):
                    check = True
                    break
        return check


def apply(expression, inputs):
    if searchTree(expression, accessList):
        filledExp = []
        for subExp in expression:
            if subExp in accessList:
                try:
                    filledExp.append(inputs[ord(subExp[-1]) - ord("a")])
                except:
                    raise Exception(
                        "Missing inputs! exp: "
                        + str(expression)
                        + " inputs: "
                        + str(inputs)
                    )
            else:
                if searchTree(subExp, accessList):
                    filledExp.append(apply(subExp, inputs)[0])
                else:
                    filledExp.append(subExp)
        return filledExp, inputs
    else:
        return expression, inputs


def eval(instruction, log=False):
    if log:
        print("Evaluating: " + str(instruction))

    if type(instruction) is str:
        return instruction

    else:
        operationName = instruction[0]
        if type(operationName) is list:
            operationName = eval(operationName, log=log)

        if operationName == "input":
            # return totalInputs.pop(0) # input from the list
            return input(eval(instruction[1], log=log))  # normal input

        elif operationName == "if":
            if eval(instruction[1], log=log) == eval(instruction[2], log=log):
                return eval(instruction[3], log=log)
            else:
                return eval(instruction[4], log=log)

        elif operationName == "define":
            definitions[eval(instruction[1], log=log)] = instruction[2]
            return ""

        elif operationName == "undefine":
            try:
                del definitions[eval(instruction[1], log=log)]
            except:
                pass
            return ""

        elif operationName == "is_defined":
            if eval(instruction[1], log=log) in definitions.keys():
                return "b"
            else:
                return "a"

        elif operationName == "append":
            total = ""
            for string in instruction[1:]:
                total += eval(string, log=log)
            return total

        elif operationName == "sort":
            total = []
            for string in instruction[1:]:
                total.append(eval(string, log=log))
            return sorted(total)[0]

        elif operationName == "alphabetical":
            total = []
            listIn = eval(instruction[1], log=log)
            while True:
                if listIn in ["|", ""]:
                    break
                total.append(eval(["list_car", listIn[:]], log=log))
                listIn = eval(["list_cdr", listIn[:]], log=log)
            totalSorted = sorted(total)
            totalString = ""
            for item in totalSorted:
                totalString += item[:]
                totalString += instruction[2]
            try:
                return totalString[:-1]
            except:
                return ""

        elif operationName == "inc":
            try:
                return chr(((ord(eval(instruction[1], log=log)) - 96) % 26) + 97)
            except:
                return str(int(eval(instruction[1], log=log)) + 1)

        elif operationName == "dec":
            try:
                return chr(((ord(eval(instruction[1], log=log)) - 98) % 26) + 97)
            except:
                return str(int(eval(instruction[1], log=log)) - 1)

        elif operationName == "car":
            output = eval(instruction[1], log=log)
            if len(output) == 0:
                return ""
            else:
                return output[0]

        elif operationName == "cdr":
            output = eval(instruction[1], log=log)
            if len(output) == 0:
                return ""
            elif len(output) == 1:
                return ""
            else:
                return output[1:]

        elif operationName == "time":
            return datetime.datetime.now().strftime("%x")

        elif operationName == "print":
            print(eval(instruction[1], log=log))
            return ""

        elif operationName == "halt":
            raise Exception(eval(instruction[1]))

        elif operationName in definitions.keys():
            definition = definitions[operationName][:]
            evaldInstructions = []
            for item in instruction[1:]:
                evaldInstructions.append(eval(item))
            return eval(apply(definition, evaldInstructions)[0], log=log)
        else:
            raise Exception("Called undefined function: " + operationName)


if __name__ == "__main__":
    print(eval(parse("(create_biblio_MLA)")))
