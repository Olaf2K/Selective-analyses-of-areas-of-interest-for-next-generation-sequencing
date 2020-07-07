from itertools import islice
import re
i = 0
output = open("alligned_for_pyton", "w")
with open('alligned') as f:
        for line in f:
                if (re.search(">.*",line) == None) == False:
                        output.write(line+"-")
		else:
                        output.write("_"+line)

