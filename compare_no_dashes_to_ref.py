from itertools import islice
import pandas as pd
import re

guides = pd.read_csv("adjusted_guides")


numeric_cols =  numeric_cols = [col for col in guides if guides[col].dtype.kind != 'O']

number_of_guides = len(guides)


if number_of_guides < 1:
    guides = 1
    number_of_guides = len(guides)

number_of_guides = [*range(int(number_of_guides))]

count = [*range(len(open("guides", "r").readlines())-1)]




guide_start = guides["guide_start"]
guide_end = guides["guide_end"]
guide_name = guides["guides"]


#count_number_of_dashes_in_a_guide

f = open("Number_dashes_in_guides", "w")
f.close()

with open("guide_location_sequences", "r") as ff:
    for l in ff:
        l_replace = l.replace("\n",",")
        l_count = l.count("-")
        fff= open("Number_dashes_in_guides","a")
        fff.write(str(l_count) + "\n")
        fff.close()
        
        



#find reads that have in the guide area more dashes than in the ref
equal = open("equal","w")
equal.close()
less_than = open("less_than","w")
less_than.close()
more_than = open("more_than","w")
more_than.close()


s=0
with open("ready_for_filter", "r") as ff:
    for linez in ff:
        s = 0
        if (re.search(">", linez) == None) == False:
                #guide_names = linez.split(",")[0]
                store = linez
        else:
            with open("guide_location_sequences", "r") as refseq:
                for lll in refseq:
                    print(1)
                    ##print(lll.split)
                    lll_split = lll.split(",")
                    lll_count = lll.count("-")
                    ##print(lll_count)
                    #linez_split = linez.split(",")
                    ##print(guide_start[s])
                    ##print(guide_end[s])
                    #print(line[(guide_start[s]):(guide_end[s])])
                    ##print(linez_split[1][(guide_start[s]):(guide_end[s])])
                    ready_to_count = str(linez[(guide_start[s]):(guide_end[s])])
                    #ready_to_count
                    counted_linez = ready_to_count.count("-")
                    count_lll = lll.count("-")
                    ##print(count_lll)
                    ##print(counted_linez)
                    #if linez_split[0] == lll_split[0]:
                    if counted_linez == count_lll:
                        equal = open("equal","a")
                        equal.write(lll_split[0] + "," + store)
                        equal.write(lll_split[0] + "," +linez)
                        equal.close()
                    elif counted_linez < count_lll:
                        less_than = open("less_than","a")
                        less_than.write(lll_split[0] + "," +store)
                        less_than.write(lll_split[0] + "," +linez)
                        less_than.close()
                    else:
                        more_than = open("more_than","a")
                        more_than.write(lll_split[0] + "," +store)
                        more_than.write(lll_split[0] + "," +linez)
                        more_than.close()
                    s += 1