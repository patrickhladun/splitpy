#!/usr/bin/env python

import sys
import subprocess

def get_first_line(input_string, max_length):
    words = input_string.split()

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
    first_piece, second_piece = get_first_line(input_string, max_length)
    lines = get_lines_from_string(second_piece, max_length)

    formatted_text = '"' + first_piece + ' "\n'
    for line in lines:
        formatted_text += '"' + line + ' "\n'

    return formatted_text


def main():
    if len(sys.argv) != 3:
        print("Usage: pysplit <input_string> <max_length>")
        sys.exit(1)

    input_string = sys.argv[1]
    max_length = int(sys.argv[2])

    formatted_text = format_text(input_string, max_length)
    print(formatted_text)

    # Copy formatted text to clipboard if available
    try:
        subprocess.run(['pbcopy'], input=formatted_text.strip(), encoding='utf-8', check=True)
    except Exception as e:
        pass

if __name__ == "__main__":
    main()
