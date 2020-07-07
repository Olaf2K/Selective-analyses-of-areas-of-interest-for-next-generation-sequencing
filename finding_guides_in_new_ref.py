import pandas as pd

guides_new = open("guides","w")
guides_new.close()


with open("real_ref", "r") as reference:
    for line in reference:
        #print(line)
        if (">" in line) == True:
            reference_name = line
        else:
            origional_length = len(line)
            
#print(origional_length)


with open("finding_guides_in_new_ref", "r") as reference:
    for line in reference:
        #print(line)
        if (">" in line) == True:
            if("ref" in line) == False:
                reference_name = line


#this is to find the location of the inserts in a string


with open("finding_guides_in_new_ref", "r") as reference_aligned:
    for lines in reference_aligned:
        line_holder = next(iter(lines))
        if (lines == reference_name) == True:
            #find location - for the next line
            line_holder = next(iter(reference_aligned))
            locations = ([pos for pos, char in enumerate(str(line_holder)) if char == ("-")])
            #print(len(locations))
            #print(locations)


#to add to the previous locations guides but only to the locations > than the reference table :
guides = pd.read_csv("ref_guides")
#this will define the colums without the column with the guide names
numeric_cols =  numeric_cols = [col for col in guides if guides[col].dtype.kind != 'O']

guide_starts = guides["guide_start"]
guide_ends = guides["guide_end"]

#mod this

i=0
location_roll = -1
for gl in range(len(locations)):
    gl-1
    #print(i)
    #i += 1
    guide_roll= 0
    for number_guides in [(*range(int(len(guides))))]:
        #print(gl)
        if guide_starts[number_guides] > locations[gl]:
            #print("blah" + str(locations[gl]))
            guides["guide_start"][number_guides] += 1
            #print(guide_ends[guide_roll])
        else:
            pass
        if guide_ends[number_guides] > locations[gl-1]:
            #print(guide_ends[guide_roll])
            #add value
            guides["guide_end"][number_guides] += 1
        else:
            #dont add value
            pass

pd.DataFrame.to_csv(guides, "guides", index = False)
#guides[numeric_cols] += to_add-1
##to correct for how python thinks compared to notepad++
guides["guide_end"] -= 1
guides["guide_start"] -= 1
s = 0



#write to file
#guides.to_csv("adjusted_guides", header=True, index=False)
new_leght = len(locations)
to_add = new_leght + origional_length
#print("length ref before correction: " + str(origional_length))
#here we add thhe to add to all the columns
#print("legnth ref after correction: " + str(to_add) + " - total inserts compared to ref: " + str(new_leght))







