from itertools import islice
import pandas as pd
import re

ff = open("final_sorted_fasta", "w")
ff.close()

with open("final_sorted", "r") as f:
    for l in f:
        if ">" in l:
            ll = l.replace(" ","\n")
            ff = open("final_sorted_fasta", "a")
            ff.write(ll)
            ff.close()
