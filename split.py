import argparse


def get_first_line(input_string, max_length):
    # Split the input string into words
    words = input_string.split()

    # Initialize variables
    first_piece = ''
    second_piece = ''
    current_length = 0
    total = max_length - 4

    for word in words:
        # Calculate the length of the current word plus one space
        word_length = len(word) + 1

        # Check if adding the current word would exceed the max length
        if current_length + word_length <= total:
            # Add the word to the first piece
            if first_piece:
                first_piece += ' ' + word
            else:
                first_piece = word
            current_length += word_length
        else:
            # Add the word to the second piece
            if second_piece:
                second_piece += ' ' + word
            else:
                second_piece = word

    return first_piece, second_piece


def get_lines_from_string(input_string, max_length):
    # Split the input string into words
    words = input_string.split()

    # Initialize variables
    lines = []
    current_line = ''
    current_length = 0

    for word in words:
        # Calculate the length of the current word plus one space
        word_length = len(word) + 1

        # Check if adding the current word would exceed the max length
        if current_length + word_length <= max_length:
            # Add the word to the current line
            if current_line:
                current_line += ' ' + word
            else:
                current_line = word
            current_length += word_length
        else:
            # Add the current line to the list of lines and start a new line
            lines.append(current_line)
            current_line = word
            current_length = word_length

    # Add the last line to the list of lines
    if current_line:
        lines.append(current_line)

    return lines


def format_text(input_string, max_length):
    combined_string = ' '.join(input_string.strip().split())
    first_piece, second_piece = get_first_line(combined_string, max_length)
    lines = get_lines_from_string(second_piece, max_length)

    print('"' + first_piece + ' "')
    for line in lines:
        print('"' + line + ' "')


def main():
    parser = argparse.ArgumentParser(description='Split and combine strings based on maximum line length.')
    parser.add_argument('input_string', type=str, help='The input string to split or combine')
    parser.add_argument('max_length', type=int, help='The maximum length of each line')
    args = parser.parse_args()

    format_text(args.input_string, args.max_length)


if __name__ == '__main__':
    main()
