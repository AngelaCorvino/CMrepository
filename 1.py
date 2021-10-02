
#!/usr/bin/env python3
"""First assignment"""
import time
import string
import argparse
import logging
logging.basicConfig(level=logging.DEBUG)






def process(file_path):
    """Read the txt file and compile the letter statistics"""
    start_time=time.time()
    logging.info("Reading input file %s ..",file_path)


    """
    with open(file_path) as input_file:   #il with è un context manager stiamo dicendo inputfile=open(file_path) solo ora quando usciamo da questo blocco di codice il file viene aiutomaticamente chiuso
        text=input_file.read() #mi restituisce una stringa
    num_chars=len(text)
    logging.info("Done,%d characters found.",num_chars)
    #char_dict={chr(x):0 for x in range(ord('a'),ord('z')+1)}     #dizionario vuoto
    char_dict={ch:0 for ch in string.ascii_lowercase}
    """
    elapsed_time=time.time()-start_time
    logging.info("Done in %.3f seconds.",elapsed_time)

if __name__ =="__main__" :  #
    parser = argparse.ArgumentParser()
    parser.add_argument('infile',type=str, help="Path to the input file")
    args=parser.parse_args()
    process(args.infile)

"""
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
"""
