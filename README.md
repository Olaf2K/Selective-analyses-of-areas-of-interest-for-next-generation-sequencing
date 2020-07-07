# Selective-analyses-of-areas-of-interest-for-next-generation-sequencing
This script is used to compare NGS reads to a given reference for only in areas of interest. In other words, the script only compares the sequence in a location where you expect a difference to be. It currently does so for up to five different locations. The outputs is generated for each given location of interest (if less than five the last files will be empty) as less_than (fewer mismatches in allignment than the reference (insertion)) more_than (more mismatches than reference (deletion)) and different_in_sequence (general difference in sequence).

Requirements:
Debian GNU/Linux system
Python 2.7
Python 3.7.3+:
Pandas


Files needed :
(note: these files need to have these exact same names for the script to work.)
prereads:
This file contains the sequences from the reads with every read on a new line.
real_ref:
This is the reference you have used to design your experiment, eg. A sequence from a genome assembly.
ref_guides:
This file contains the name of a guide and the locations of binding (start and end) in the real_ref.

Notes: 
1.	real_ref and ref_guides are needed to automatically adjust the guide locations if there is an allele present in the population of your experiment. It does this by comparing the most common read in your data to the “genome assembly reference”, if there are differences in sequence, the script will adjust the guides that are effected by this difference. For further information please refer to “#28” in the script “analyses_with_loop.bash”. 
2.	Examples of the required files are in the folder “examples”.
