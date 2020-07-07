#manipulate_freq_files to a format r likes
import os
dir_name = os.path.basename(os.getcwd())

##G1
##find in current path the folder
create = open("G1_freq_for_plot","w")
create.close()
with open("G1_freq_trimmed","r") as G1:
    for l in G1:
        to_write = dir_name+ "," + l
        G1_write = open("G1_freq_for_plot","a")
        G1_write.write(to_write)
        G1_write.close()

##G2
##find in current path the folder
create = open("G2_freq_for_plot","w")
create.close()
with open("G2_freq_trimmed","r") as G2:
    for l in G2:
        to_write = dir_name+ "," + l
        G2_write = open("G2_freq_for_plot","a")
        G2_write.write(to_write)
        G2_write.close()

##G3
##find in current path the folder
create = open("G3_freq_for_plot","w")
create.close()
with open("G3_freq_trimmed","r") as G3:
    for l in G3:
        to_write = dir_name+ "," + l
        G3_write = open("G3_freq_for_plot","a")
        G3_write.write(to_write)
        G3_write.close()
    
##G4
##find in current path the folder
create = open("G4_freq_for_plot","w")
create.close()
with open("G4_freq_trimmed","r") as G4:
    for l in G4:
        to_write = dir_name+ "," + l
        G4_write = open("G4_freq_for_plot","a")
        G4_write.write(to_write)
        G4_write.close()

##G5
##find in current path the folder
create = open("G5_freq_for_plot","w")
create.close()
with open("G5_freq_trimmed","r") as G5:
    for l in G5:
        to_write = dir_name+ "," + l
        G5_write = open("G5_freq_for_plot","a")
        G5_write.write(to_write)
        G5_write.close()

###lowe than

# manipulate_freq_files to a format r likes
import os

dir_name = os.path.basename(os.getcwd())

##G1
##find in current path the folder
create = open("G1_lower_freq_for_plot", "w")
create.close()
with open("less_than_G1_trimmed", "r") as G1:
    for l in G1:
        to_write = dir_name + "," + l
        G1_write = open("G1_lower_freq_for_plot", "a")
        G1_write.write(to_write)
        G1_write.close()

##G2
##find in current path the folder
create = open("G2_lower_freq_for_plot", "w")
create.close()
with open("less_than_G2_trimmed", "r") as G2:
    for l in G2:
        to_write = dir_name + "," + l
        G2_write = open("G2_lower_freq_for_plot", "a")
        G2_write.write(to_write)
        G2_write.close()

##G3
##find in current path the folder
create = open("G3_lower_freq_for_plot", "w")
create.close()
with open("less_than_G3_trimmed", "r") as G3:
    for l in G3:
        to_write = dir_name + "," + l
        G3_write = open("G3_lower_freq_for_plot", "a")
        G3_write.write(to_write)
        G3_write.close()

##G4
##find in current path the folder
create = open("G4_lower_freq_for_plot", "w")
create.close()
with open("less_than_G4_trimmed", "r") as G4:
    for l in G4:
        to_write = dir_name + "," + l
        G4_write = open("G4_lower_freq_for_plot", "a")
        G4_write.write(to_write)
        G4_write.close()

##G5
##find in current path the folder
create = open("G5_lower_freq_for_plot", "w")
create.close()
with open("less_than_G5_trimmed", "r") as G5:
    for l in G5:
        to_write = dir_name + "," + l
        G5_write = open("G5_lower_freq_for_plot", "a")
        G5_write.write(to_write)
        G5_write.close()


###########higher than

# manipulate_freq_files to a format r likes
import os

dir_name = os.path.basename(os.getcwd())

##G1
##find in current path the folder
create = open("G1_higher_freq_for_plot", "w")
create.close()
with open("more_than_G1_trimmed", "r") as G1:
    for l in G1:
        to_write = dir_name + "," + l
        G1_write = open("G1_higher_freq_for_plot", "a")
        G1_write.write(to_write)
        G1_write.close()

##G2
##find in current path the folder
create = open("G2_higher_freq_for_plot", "w")
create.close()
with open("more_than_G2_trimmed", "r") as G2:
    for l in G2:
        to_write = dir_name + "," + l
        G2_write = open("G2_higher_freq_for_plot", "a")
        G2_write.write(to_write)
        G2_write.close()

##G3
##find in current path the folder
create = open("G3_higher_freq_for_plot", "w")
create.close()
with open("more_than_G3_trimmed", "r") as G3:
    for l in G3:
        to_write = dir_name + "," + l
        G3_write = open("G3_higher_freq_for_plot", "a")
        G3_write.write(to_write)
        G3_write.close()

##G4
##find in current path the folder
create = open("G4_higher_freq_for_plot", "w")
create.close()
with open("more_than_G4_trimmed", "r") as G4:
    for l in G4:
        to_write = dir_name + "," + l
        G4_write = open("G4_higher_freq_for_plot", "a")
        G4_write.write(to_write)
        G4_write.close()

##G5
##find in current path the folder
create = open("G5_higher_freq_for_plot", "w")
create.close()
with open("more_than_G5_trimmed", "r") as G5:
    for l in G5:
        to_write = dir_name + "," + l
        G5_write = open("G5_higher_freq_for_plot", "a")
        G5_write.write(to_write)
        G5_write.close()