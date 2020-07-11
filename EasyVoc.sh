#!/bin/bash
echo "What is the name of your Assignment?"
echo "This should be in the assignment format, for example FA20-HW08-SomethingInJava."
read assignmentName
numDashes=$(echo $assignmentName| grep -o "-" | wc -l)
numDashes=$(echo $numDashes| sed 's/ *$//g')
