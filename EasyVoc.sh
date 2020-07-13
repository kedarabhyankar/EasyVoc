#!/bin/bash

echo -e  "\x1B[32mWhat is the name of your Assignment?"
echo -e "\x1B[92mThis should be in the assignment format, for example FA20-HW08-SomethingInJava.\x1B[0m"
read assignmentName
echo 
numDashes=$(echo $assignmentName| grep -o "-" | wc -l)
numDashes=$(echo $numDashes| sed 's/ *$//g')

assignmentSemester=$(echo $assignmentName | cut -d'-' -f 1)
assignmentEnumeration=$(echo $assignmentName | cut -d'-' -f 2)
assignmentName=$(echo $assignmentName | cut -d'-' -f 3)

assignmentType=$(echo $assignmentEnumeration | head -c 2)
assignmentNumber=$(echo $assignmentEnumeration | tail -c 3)

if [ "$assignmentType" != "HW" ] && [ "$assignmentType" != "LB" ] && [ "$assignmentType" != "PJ" ]; then
	echo -e "\x1B[31mThe Assignment Type is invalid. It should be HW, PJ, or LB!"
	exit 1
fi

mkdir -p $assignmentSemester/$assignmentEnumeration/scripts
mkdir -p $assignmentSemester/$assignmentEnumeration/asnlib

echo "\x1B[44mType the names of the files the student should submit, including the extension, as space separated elements."
echo "\x1B[104mFor example, you would type: fileOne.java fileTwo.java fileThree.java\x1B[0m"

if [ "$assignmentType" == "HW" ] || [ "assignmentType" == "PJ" ]; then
	#Create Assignment with puppycrawl
	echo "\x1B[32mNow, enter the points each category should be worth. So, if there are 4 categories, for a total of 95 points, you should enter: 25 25 25 20.\x1B[0m"
	read -a assignmentWeightages
	
	echo "\x1B[32mNow, enter the names for each weightage, in the order you inputted above. So, if you entered 25 25 25 20 above, name them accordingly.\x1B[0m"
	read -a assignmentWeightageNames

	
else
	#Create Assignment without puppycrawl

fi
