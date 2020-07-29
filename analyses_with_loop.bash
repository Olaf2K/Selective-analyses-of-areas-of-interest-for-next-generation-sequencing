#ngs analyses


#1: generates a time stamp when the script is started
date> time_stamp

#2: generates empty files, or resets files to empty if run a second time. This allows to rerun the script without doubling the output.
wait
echo "" > G1_temp
wait
echo "" > G2_temp
wait
echo "" > G3_temp
wait
echo "" > G4_temp
echo "" > G5_temp
wait
echo "" > G1_less_than_temp
wait
echo "" > G2_less_than_temp
wait
echo "" > G3_less_than_temp
wait
echo "" > G4_less_than_temp
echo "" > G5_less_than_temp
wait
echo "" > G1_more_than_temp
wait
echo "" > G2_more_than_temp
wait
echo "" > G3_more_than_temp
wait
echo "" > G4_more_than_temp
echo "" > G5_more_than_temp
wait
echo "" > to_check_allignment
wait
echo "" > temp_allign
wait
echo "" > G1_freq
wait
echo "" > G2_freq
wait
echo "" > G3_freq
wait
echo "" > G4_freq
echo "" > G5_freq
wait
echo "" > G1
wait
echo "" > G2
wait
echo "" > G3
wait
echo "" > G4
echo "" > G5
wait
echo "" > final
echo "" > to_check_allignment
echo "" > read_for_allignment
echo "" > alligned
wait
echo "" > final_different_in_sequence 
echo "" > different_in_sequence

#3: counts the number of reads, can be used to normalise between experiments
wc -l prereads > Total_Number_of_Reads

#4: uses the file real_ref to check for the expected length, then removes any reads that are 10bp shorter or longer. (see note in script to change the number of bp treshold)
python3 find_length_real_ref.py
wait
#5: sort the reads based on sequence.
sort reads > reads.sorted
wait
#10:count for each unique read how often it exists:
uniq -c reads.sorted > reads.counted
wait
#23 replace big space gap with _, this is to make it mafft allignment friendly
sed 's/\s\+/y/g' reads.counted > reads.counted2
wait
sed 's/\s//g' reads.counted2 > early.fasta
wait
sed 's/^/ /' early.fasta > early.fasta2
wait
sed 's/ /_/g' early.fasta2 > early.fasta3
awk '{print ">" NR $s}' early.fasta3 > pre.fasta
wait
sed 's/_y/_/g'  pre.fasta > pre.fasta2
sed 's/y/\n/g' pre.fasta2 > for_allignment.fasta

wait
#25; The most common read is used to allign individual reads to. The following script find that most common read and makes the file: ref. The allingment later will use this new reference. If you dont want this you can comment this out and make an file containing your reference with the name of the file: "ref"
python3 find_most_common_read.py
wait
#26 alligns the most common read (new ref) to the ref given by the user (eg. from a genome assembly).
cat ref real_ref > for_allignment_of_refs
wait
mafft for_allignment_of_refs > alligned
#27 turns the allignment into an python friendly format.
python fasta_to_pyfriendly.py
wait
sed -z 's/\n_//g'  alligned_for_pyton> pre_alligned_single_line_fasta
wait
sed -z 's/-_//g'  pre_alligned_single_line_fasta> finding_guides_in_new_ref
#28 find the guide locations in the new reference based on the file ref_guides; which contains locations of the start and the end for each guide. This script will adjust these locations based on the allignments, eg. if there is an insertion compared to the genome reference before the guide location, the location will be +1. If an insertion is located after a guide location no change is made.
python3 finding_guides_in_new_ref.py


#29 This first alligns a single read to the new reference, and then calls script needed to see if that read was any different in the guide location. After it will move to the next read in the reads file until it reaches the end. 
while IFS= read -r lines; do
	this_line_is="$lines" 
	echo ""$this_line_is"" > liners
	wait
	if grep -q ">" liners; then
		#echo "$lines"
		echo ""$this_line_is"" > feed
	else
		wait
		echo ""$this_line_is"" > feed_two
		wait
		cat feed feed_two > read_for_allignment
		wait
		cat ref read_for_allignment >read_ready_for_alin
		wait
		mafft read_ready_for_alin > alligned
		wait
		#30 This keeps a log of how each read is alligned to the reference.
		cat temp_allign alligned >> to_check_allignment
		wait
		#40 turn python friendly format
		python fasta_to_pyfriendly.py
		wait
		sed -z 's/\n_//g'  alligned_for_pyton> pre_alligned_single_line_fasta
		wait
		sed -z 's/-_//g'  pre_alligned_single_line_fasta> ready_for_filter
		wait
		#45 similar to before, if there are insertions in the read, then the location of the guides withing the reference will change. The following script adjusts for this.
		python3 location_guides_corrected.py
		wait
		#50 This will only export reads that are different from the reference within the guide locations. If a missmatch !only! occurs outside the guide areas, then this read is ignored. 
		python3 if_in_guide_area.py
		wait
		#python3 iff_in_guide_area_just_different.py
		wait
		#The following lines differentiate whichh type of difference compared to the reference is found (eg. an insertion, deletion or base pair change).
		python3 compare_no_dashes_to_ref.py
		wait
		python3 convert_fasta_to_one_line.py
		wait
		sed 's/_/\t/g' final_one_line > final_temp
		wait
		sort -k2 -n -r final_temp > final_sorted
		wait
		python3 convert_oneline_fasta_to_normal.py
		wait
		cat final_different_in_sequence >> different_in_sequence
		grep "G1,>" final_sorted_fasta >> G1_freq
		wait
		grep "G2,>" final_sorted_fasta >> G2_freq
		wait
		grep "G3,>" final_sorted_fasta >> G3_freq
		wait
		grep "G4,>" final_sorted_fasta >> G4_freq
		wait
		grep "G5,>" final_sorted_fasta >> G5_freq
		wait
		grep "G1," final_sorted_fasta >> G1_temp
		wait
		grep "G2," final_sorted_fasta >> G2_temp
		wait
		grep "G3," final_sorted_fasta >> G3_temp
		wait
		grep "G4," final_sorted_fasta >> G4_temp
		wait
		grep "G5," final_sorted_fasta >> G5_temp
		wait
		python3 convert_fasta_to_one_line_b.py
		wait
		sed 's/_/\t/g' more_than_temp > more_than_temp_a
		wait
		sort -k2 -n -r more_than_temp_a > more_than_temp_b
		wait
		sed 's/_/\t/g' less_than_temp > less_than_temp_a
		wait
		sort -k2 -n -r less_than_temp_a > less_than_temp_b
		wait
		python3 convert_oneline_fasta_to_normal_b.py
		wait
		grep "G1," less_than_temp_c >> G1_less_than_temp
		wait
		grep "G2," less_than_temp_c >> G2_less_than_temp
		wait
		grep "G3," less_than_temp_c >> G3_less_than_temp
		wait
		grep "G4," less_than_temp_c >> G4_less_than_temp
		wait
		grep "G5," less_than_temp_c >> G5_less_than_temp
		wait
		grep "G1," more_than_temp_c >> G1_more_than_temp
		wait
		grep "G2," more_than_temp_c >> G2_more_than_temp
		wait
		grep "G3," more_than_temp_c >> G3_more_than_temp
		wait
		grep "G4," more_than_temp_c >> G4_more_than_temp
		wait
		grep "G5," more_than_temp_c >> G5_more_than_temp
		wait
	fi
done < for_allignment.fasta
#This will write the found differences to the right files.
grep -A1 "ref" ready_for_filter > temp_ref_alligned
wait
sed ':a;N;$!ba;s/>ref\n/   >RE\n    /g' temp_ref_alligned > ref_alligned
wait
wait
cat ref_alligned G1_temp>>G1
wait
cat ref_alligned G2_temp>>G2
wait
cat ref_alligned G3_temp>>G3
wait
cat ref_alligned G4_temp>>G4
wait
cat ref_alligned G5_temp>>G5
wait
cat ref_alligned G1_less_than_temp>less_than_G1
wait
cat ref_alligned G2_less_than_temp>less_than_G2
wait
cat ref_alligned G3_less_than_temp>less_than_G3
wait
cat ref_alligned G4_less_than_temp>less_than_G4
wait
cat ref_alligned G5_less_than_temp>less_than_G5
wait
cat ref_alligned G1_more_than_temp>more_than_G1
wait
cat ref_alligned G2_more_than_temp>more_than_G2
wait
cat ref_alligned G3_more_than_temp>more_than_G3
wait
cat ref_alligned G4_more_than_temp>more_than_G4
wait
cat ref_alligned G5_more_than_temp>more_than_G5
#the following lines will "cleanup" any irrelevent files made during the analyses. If you want to keep these files, comment them out below.
rm G1_temp
rm G2_temp
rm G3_temp
rm G4_temp
rm G5_temp
rm G1_more_than_temp
rm G2_more_than_temp
rm G3_more_than_temp
rm G4_more_than_temp
rm G5_more_than_temp
rm G1_less_than_temp
rm G2_less_than_temp
rm G3_less_than_temp
rm G4_less_than_temp
rm G5_less_than_temp
rm to_check_allignment
rm temp_allign
rm G1_freq
rm G2_freq
rm G3_freq
rm G4_freq
rm G5_freq
rm G1
rm G2
rm G3
rm G4
rm G5
rm reads.sorted
rm reads.counted
rm reads.counted2
rm early.fasta
rm early.fasta2
rm early.fasta3
rm pre.fasta
rm pre.fasta2
rm for_allignment.fasta
rm pre_alligned_single_line_fasta
rm finding_guides_in_new_ref
rm final
rm final_different_in_sequence
rm alligned
rm liners
rm feed
rm feed_two
rm read_for_allignment
rm read_ready_for_alin
rm less_than_temp
rm less_than_temp_a
rm less_than_temp_b
rm less_than_temp_c
rm out
#finally add a timestamp for when the script was finished
date >> time_stamp
