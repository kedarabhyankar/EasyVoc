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
