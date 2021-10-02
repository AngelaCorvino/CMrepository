

Download a book (not covered by copyright) in plain-text format, e.g., from
https://www.gutenberg.org/

(If you have a hard time picking one, we suggest this English translation
of "The Republic" by Plato: http://www.gutenberg.org/cache/epub/1497/pg1497.txt)
#!/usr/bin/env python3
"""First assignment"""
import time
import string
import argparse
import logging
logging.basicConfig(level=logging.DEBUG)




directory='pictures/2021-09-01/'
--- Goal
Write a Python program that prints the relative frequence of each letter
of the alphabet (without distinguishing between lower and upper case) in the
book.

--- Specifications
- the program should have a --help option summarizing the usage
- the program should accept the path to the input file from the command line
- the program should print out the total elapsed time
- the program should have an option to display a histogram of the frequences
- [optional] the program should have an option to skip the parts of the text
  that do not pertain to the book (e.g., preamble and license)
- [optional] the program should have an option to print out the basic book
  stats (e.g., number of characters, number of words, number of lines, etc.)
