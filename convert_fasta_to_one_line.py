from itertools import islice
import pandas as pd
import re

ff = open("final_one_line", "w")
ff.close()

with open("final", "r") as f:
    for l in f:
        if ">" in l:
            ll = l.replace("\n"," ")
            ff = open("final_one_line", "a")
            ff.write(ll)
            ff.write(next(f))
            ff.close()
