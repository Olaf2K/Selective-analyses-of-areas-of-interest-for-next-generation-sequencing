from itertools import islice
import pandas as pd
import re

ff = open("more_than_temp_c", "w")
ff.close()

with open("more_than_temp_b", "r") as f:
    for l in f:
        if ">" in l:
            ll = l.replace(" ","\n")
            ff = open("more_than_temp_c", "a")
            ff.write(ll)
            ff.close()



ff = open("less_than_temp_c", "w")
ff.close()

with open("less_than_temp_b", "r") as f:
    for l in f:
        if ">" in l:
            ll = l.replace(" ","\n")
            ff = open("less_than_temp_c", "a")
            ff.write(ll)
            ff.close()