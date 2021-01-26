source $LIB/public/vocTerminalInit.sh
#Initial Setup Checks
lines=`grep -R ".*package.*;.*" *.java | wc -l`
if [ $lines -gt 0 ]
then
	echo
	echo "ERROR: package statement detected. Please remove all package statements from your classes"and resubmit.
	exit 0
fi
lines=`grep -R "System.exit" *.java | wc -l`
if [ $lines -gt 0 ]
then
	echo
	echo "ERROR: System.exit call detected.. Please remove all System.exit calls and resubmit."
	exit 0
fi

lines=`ls | grep "2" | wc -l`
if [ $lines -lt 1 ] 
then
	echo
	echo "ERROR: no file with the name "2".
	echo "Please resubmit with the file."
fi

lines=`ls | grep "Aloha.java" | wc -l`
if [ $lines -lt 1 ] 
then
	echo
	echo "ERROR: no file with the name "Aloha.java".
	echo "Please resubmit with the file."
fi

lines=`ls | grep "Sayonara.java" | wc -l`
if [ $lines -lt 1 ] 
then
	echo
	echo "ERROR: no file with the name "Sayonara.java".
	echo "Please resubmit with the file."
fi

# --------------------
voccheck
echo
javac -d . 2
javac -d . Aloha.java
javac -d . Sayonara.java

javac -d . -cp .:$VLIB/java/voc-grader.jar:$VLIB/java/junit-4.12.jar:$VLIB/java/hamcrest-core-1.3.jar:$LIB/grading-tools-vocareum.jar $ASNLIB/1 $ASNLIB/GreetingGrader.javajava -cp .:$VLIB/java/voc-grader.jar:$VLIB/java/junit-4.12.jar:$VLIB/java/hamcrest-core-1.3.jar:$LIB/grading-tools-vocareum.jar GreetingGraderrm *.class