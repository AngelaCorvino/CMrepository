
#!/usr/bin/env python3
"""First assignment"""
import time
import string
import argparse
import logging
import matplotlib.pyplot as plt
import numpy as np
logging.basicConfig(level=logging.INFO)

"""
parser = argparse.ArgumentParser()
parser.add_argument(
    "-log",
    "--log",
    default="warning",
    help=(
        "Provide logging level. "
        "Example --log debug', default='warning'"),
    )

options = parser.parse_args()
levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
}
level = levels.get(options.log.lower())
if level is None:
    raise ValueError(
        f"log level given: {options.log}"
        f" -- must be one of: {' | '.join(levels.keys())}")
logging.basicConfig(level=level)
logger = logging.getLogger(__name__)
"""


def process(file_path):
    """Read the txt file and compile the letter statistics"""
    start_time=time.time()
    logging.info("Reading input file %s ..",file_path)



    with open(file_path) as input_file:   #il with è un context manager stiamo dicendo inputfile=open(file_path) solo ora quando usciamo da questo blocco di codice il file viene aiutomaticamente chiuso
        text=input_file.read() #mi restituisce una stringa
    num_chars=len(text)
    logging.info("Done,%d characters found.",num_chars)
    #char_dict={chr(x):0 for x in range(ord('a'),ord('z')+1)}     #dizionario vuoto
    #The ord() method in Python converts a character into its Unicode code value
    char_dict={ch:0 for ch in string.ascii_lowercase}  #creo un dizionario in cui la chiave è la letta del dizionario e inizialemnte ad ogni lettera è associato 0
    """ In Python, string ascii_lowercase will give the lowercase letters ‘abcdefghijklmnopqrstuvwxyz """
    for ch in text:
        #ch=ch.lower()
        if ch in char_dict:
            char_dict[ch]+=1
        #try :
        #    char_dict[ch.lower()]+=1  #trasformiamo le maiuscole in minuscole
        #except KeyError:
        #    pass

    num_letters=sum(char_dict.values())
    for ch, num in char_dict.items():
        print(f"{ch}->{num/num_letters:.3%}")

    elapsed_time=time.time()-start_time
    logging.info("Done in %.3f seconds.",elapsed_time)

    return(char_dict)
    
def plotter(char_dict):
    frequencies=np.zeros(len(char_dict))
    num_letters=sum(char_dict.values())
    i=0
    for ch, num in char_dict.items():
        frequencies[i]=num/num_letters
        i+=1
    print(frequencies)

    plt.style.use('Solarize_Light2')
    params = {'axes.labelsize': '20',
         'axes.titlesize':'30',
         'xtick.labelsize':'15',
         'ytick.labelsize':'15',
         'legend.fontsize': '15',
         'lines.linewidth': '2',
         'font.size': '25',
         'font.family': 'sans-serif'}
    plt.rcParams.update(params)
    x=np.linspace(0, len(char_dict), len(char_dict))
    plt.title('Letter frequency in the book')
    plt.bar(x, frequencies, alpha=0.5)
    plt.xlabel('letters')
    plt.ylabel('frequency percentage')
    plt.legend(loc=2)
    plt.savefig('histo.png', bbox_inches='tight', dpi=100)
    plt.show()
    
if __name__ =="__main__" :  #
    parser = argparse.ArgumentParser()
    parser.add_argument('infile',type=str, help="Path to the input file")
    args=parser.parse_args()

    dictionary=process(args.infile)
    plotter(dictionary)
