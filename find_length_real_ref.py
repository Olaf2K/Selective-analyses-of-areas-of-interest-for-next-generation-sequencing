"""find length in real_ref and use this length to remove reads in prereads that are +/- different depending on treshold
"""
# to change the strictness of the filter, you can adjust the treshhold. Default = 10 bp
set_treshold = 10

with open("real_ref", "r") as ref:
    for l in ref:
        if ">" in l:
            pass
        else:
            length_ref_plus10= len(l)+set_treshold
            length_ref_min10=  len(l)-set_treshold

#print(length_ref_plus10)
#print(length_ref_min10)

# to filter out reads that are outside this range

output = open("reads","w")
output.close()


with open("prereads","r") as reads:
    for ll in reads:
        if len(ll) > length_ref_min10:
            if len(ll) < length_ref_plus10:
                output = open("reads","a")
                output.write(ll)
                output.close()