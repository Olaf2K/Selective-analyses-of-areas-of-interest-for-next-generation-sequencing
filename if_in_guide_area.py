from itertools import islice
import pandas as pd
import re
import os
from os.path import basename
pd.options.mode.chained_assignment = None

i = 0

guides = pd.read_csv("adjusted_guides")

numeric_cols =  numeric_cols = [col for col in guides if guides[col].dtype.kind != 'O']

number_of_guides = len(guides)

if number_of_guides < 1:
    guides = 1
    number_of_guides = len(guides)

number_of_guides = [*range(int(number_of_guides))]

guide_start = guides["guide_start"]
guide_end = guides["guide_end"]
guide_name = guides["guides"]

###this may have been causing the crashes
edits_in_range = open("edits_in_range", "w")
edits_in_range.close()

#this will add guide number in front of every read, so later we can use these to avoid duplication
with open("ready_for_filter", "r") as f:
    for line in f:
        s = 0
        if(re.search(">.*",line) == None) == False:
            store = line
        else:
            for no_guides in number_of_guides:
                    output = open("edits_in_range", "a")
                    output.write(guide_name[s] + ","+store)
                    output.write(guide_name[s] + "," + line)
                    output.close()
                    s += 1

s=0
#to see if it matches the ref: this means that the - is generated by an insertion in another read.
guide_location_sequences = open("guide_location_sequences", "w")
guide_location_sequences.close()

with open("ref","r") as fff:
    for llll in fff:
        if ">" in llll:
            ref_name = llll

with open ("ready_for_filter","r") as looking_for_ref:
    for the_read in looking_for_ref:
        if ref_name in the_read:
            reference_seq = next(iter(looking_for_ref))


s=0

count = [*range(len(open("guides", "r").readlines())-1)]


for ll in ((count)):
    guide_location_sequences = open("guide_location_sequences", "a")
    guide_location_sequences.write(guide_name[s] + ",")
    guide_location_sequences.write(reference_seq[guide_start[s]:guide_end[s]] + "\n")
    guide_location_sequences.close()
    s += 1
s=0


cwd = os.getcwd()
folder_name = basename(cwd)
for folders in cwd.split("/"):
    if ("gene" in folders) == True:
        gene_name = folders

final = open("final", "w")
final.close()

s=0
with open("edits_in_range", "r") as ff:
    for linez in ff:
        s=0
        if (re.search(">", linez) == None) == False:
                guide_names = linez.split(",")[0]
                store = linez
        else:
            with open("guide_location_sequences", "r") as refseq:
                for lll in refseq:
                    lll_split = lll.split(",")
                    refseq_locations = lll_split[1]
                    linez_split = linez.split(",")
                    read_guide_seq = (linez_split[1][guide_start[s]:guide_end[s]])
                    refeq_location_dash_n = refseq_locations.replace("\n","")
                    refseq_locations_a = refeq_location_dash_n.replace("a","n")
                    refseq_locations_t = refseq_locations_a.replace("t","n")
                    refseq_locations_c = refseq_locations_t.replace("c","n")
                    refseq_locations_normalised = refseq_locations_c.replace("g","n")
                    read_guide_seq_a = read_guide_seq.replace("a","n")
                    read_guide_seq_t = read_guide_seq_a.replace("t","n")
                    read_guide_seq_c = read_guide_seq_t.replace("c","n")
                    read_guide_seq_normalised = read_guide_seq_c.replace("g","n")
                    if linez_split[0] == lll_split[0]:
                        if read_guide_seq_normalised == refseq_locations_normalised:
                            pass
                        else:
                            final = open("final", "a")
                            final.write(str(store)+ ",")
                            final.write(linez)
                            final.close()
                    s +=1


with open("Total_Number_of_Reads", "r") as files:
    for liners in files:
        aaa = open(liners,"w")
        aaa.close()


##just different
final = open("final_different_in_sequence", "w")
final.close()



s=0
with open("edits_in_range", "r") as ff:
    for linez in ff:
        s=0
        if (re.search(">", linez) == None) == False:
                guide_names = linez.split(",")[0]
                store = linez
        else:
            with open("guide_location_sequences", "r") as refseq:
                for lll in refseq:
                    lll_split = lll.split(",")
                    refseq_locations = lll_split[1]
                    linez_split = linez.split(",")
                    read_guide_seq = (linez_split[1][guide_start[s]:guide_end[s]])
                    refeq_location_dash_n = refseq_locations.replace("\n","")
                    if linez_split[0] == lll_split[0]:
                        if read_guide_seq == refeq_location_dash_n:
                            pass
                        else:
                            final = open("final_different_in_sequence", "a")
                            final.write(str(store)+ ",")
                            final.write(linez)
                            final.close()
                    s +=1




