#!/bin/bash

echo "What is the name of your Assignment?"
echo "This should be in the assignment format, for example FA20-HW08-SomethingInJava."
read assignmentName
numDashes=$(echo $assignmentName| grep -o "-" | wc -l)
numDashes=$(echo $numDashes| sed 's/ *$//g')

assignmentSemester=$(echo $assignmentName | cut -d'-' -f 1)
assignmentEnumeration=$(echo $assignmentName | cut -d'-' -f 2)
assignmentName=$(echo $assignmentName | cut -d'-' -f 3)

assignmentType=$(echo $assignmentEnumeration | head -c 2)
assignmentNumber=$(echo $assignmentEnumeration | tail -c 3)

if [ "$assignmentType" != "HW" ] && [ "$assignmentType" != "LB" ] && [ "$assignmentType" != "PJ" ]; then
	echo "The Assignment Type is invalid. It should be HW, PJ, or LB!"
	exit 1
fi

mkdir -p $assignmentSemester/$assignmentEnumeration/

echo "Type the names of the files the student should submit, including the extension, as space separated elements."
echo "For example, you would type: fileOne.java fileTwo.java fileThree.java"
read -a filenames

