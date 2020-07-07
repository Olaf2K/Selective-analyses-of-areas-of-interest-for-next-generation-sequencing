import re

ref = open("ref", "w")
ref.close()
highest_read = 0

with open("for_allignment.fasta","r") as a:
    for l in a:
        if ">" in l:
            l_split = l.split("_")
            read_count = int(l_split[1])
            if read_count > highest_read:
                highest_read = read_count
                read_no = l
                highest_read_sequence = next(a)
ref = open("ref", "a")
ref.write(str(read_no))
ref.write(str(highest_read_sequence))
ref.close()
