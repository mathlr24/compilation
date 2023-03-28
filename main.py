from optparse import OptionParser

from lexer import Lexer


def main():
    parser = OptionParser()

    parser.add_option("-i",
                      "--input",
                      action="store",
                      type="string",
                      dest="input_file",
                      metavar="INPUT_PATH")

    options, args = parser.parse_args()

    if (not options.input_file):
        parser.print_help()
        exit()

    lexer = Lexer()
    fd = open(options.input_file)
    lines = fd.readlines()
    lexemes = lexer.lex(lines)

    print(lexemes)


if __name__ == '__main__':
    main()