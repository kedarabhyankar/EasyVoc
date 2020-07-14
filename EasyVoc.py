import os


# define colored print formats using ANSI color codes
def print_red(text): print("\x1B[91m {}\x1B[00m".format(text))


def print_green(text): print("\x1B[92m {}\x1B[00m".format(text))


def print_yellow(text): print("\x1B[93m {}\x1B[00m".format(text))


def print_light_purple(text): print("\x1B[94m {}\x1B[00m".format(text))


def print_purple(text): print("\x1B[95m {}\x1B[00m".format(text))


def print_cyan(text): print("\x1B[96m {}\x1B[00m".format(text))


def print_gray(text): print("\x1B[97m {}\x1B[00m".format(text))


def path_joiner(pathlist):
    finalpath = ""
    for path in pathlist:
        print("appending {}".format(path))
        finalpath += path

    return os.path.join('', finalpath)


def create_scripts(filenames, assignment_type, path):
    script_base = "source $LIB/public/vocTerminalInit.sh\n" \
                  "#Initial Setup Checks\n" \
                  "lines=`grep -R \".*package.*;.*\" *.java | wc -l`\n" \
                  "if [ $lines -gt 0 ]\n" \
                  "then\n" \
                  "\techo\n" \
                  "\techo \"ERROR: package statement detected. Please remove all package statements from your " \
                  "classes\"" \
                  "and resubmit.\n" \
                  "\texit 0\n" \
                  "fi\n" \
                  "lines=`grep -R \"System.exit\" *.java | wc -l`\n" \
                  "if [ $lines -gt 0 ]\n" \
                  "then\n" \
                  "\techo\n" \
                  "\techo \"ERROR: System.exit call detected.. Please remove all System.exit calls and resubmit.\"\n" \
                  "\texit 0\n" \
                  "fi\n\n"
    script = script_base
    for filename in filenames:
        script += "lines=`ls | grep \"{}\" | wc -l`\n" \
                  "if [ $lines -lt 1 ] \n" \
                  "then\n" \
                  "\techo\n" \
                  "\techo \"ERROR: no file with the name \"{}\".\n" \
                  "\techo \"Please resubmit with the file.\"\n" \
                  "fi\n\n".format(filename, filename)

    script += "# --------------------\n"
    if assignment_type != "LB":
        script += "voccheck\n"
        run_file = open(os.path.join(path, 'scripts/run.sh'), "w")
        run_file.write(script)
        run_file.close()

        check_line = "java -jar $LIB/checkstyle-vocareum.jar -c $LIB/checkstyle.xml *.java\n"
        check_file = open(os.path.join(path, 'scripts/check.sh'), "w")
        check_file.write(check_line)
        check_file.close()

    script += "echo\n"
    for filename in filenames:
        script += "javac -d . {}\n".format(filename)

    script += "\n"

    test_file_count = int(input(print_cyan("How many test files are there? These are "
                                           "files that contain the JUnit Tests.")))
    test_file_names = [test_file_count]

    i = 0
    while i < test_file_count:
        test_file_names.append(input(print_cyan("What is the name of test file {}?".format(i))))
        i += 1

    test_compile_string = "javac -d . -cp .:$VLIB/java/voc-grader.jar:$VLIB/java/junit-4.12.jar:$VLIB/java/hamcrest" \
                          "-core-1.3.jar:$LIB/grading-tools-vocareum.jar "

    grader_file_name = input(print_cyan("What is the name of the grader file? This is the file which has the "
                                        "Vocareum references. Do not include the extension for this file name."))

    i = 0
    while i < test_file_count:
        test_compile_string += "$ASNLIB/{} ".format(test_file_names[i])
        i += 1

    test_compile_string += "$ASNLIB/{}.java".format(grader_file_name)

    run_string = "java -cp .:$VLIB/java/voc-grader.jar:$VLIB/java/junit-4.12.jar:$VLIB/java/hamcrest-core-1.3.jar" \
                 ":$LIB/grading-tools-vocareum.jar {}".format(grader_file_name)
    del_string = "rm *.class"

    script += test_compile_string
    script += run_string
    script += del_string

    grade_script = open(os.path.join(path, 'scripts/grade.sh'), "w")
    submit_script = open(os.path.join(path, 'scripts/submit.sh'), "w")
    grade_script.write(script)
    submit_script.write(script)
    grade_script.close()
    submit_script.close()


def easy_voc():
    assignment_name = input(print_green("What is the name of your assignment?\n"
                                        "This should be in the assignment format, for example "
                                        "FA20-HW08-SomethingInJava."))
    if assignment_name.count('-') != 2:
        print_red("The assignment name is in the wrong format!")
        exit(1)

    assignment_properties = assignment_name.split("-")
    assignment_semester = assignment_properties[0][:2]
    assignment_type = assignment_properties[1][:2]

    if assignment_semester != "FA" and assignment_semester != "SP" and assignment_semester != "SU":
        print_red("The assignment semester is in the wrong format!")
        exit(1)

    if assignment_type != "HW" and assignment_type != "LB" and assignment_type != "PJ":
        print_red("The assignment type is in the wrong format!")
        exit(1)

    script_path = path_joiner("{},/,{},/,{},/scripts".format(os.getcwd(), assignment_properties[0],
                                                             assignment_properties[1]).split(","))
    asnlib_path = path_joiner("{},/,{},/,{},/scripts".format(os.getcwd(), assignment_properties[0],
                                                             assignment_properties[1]).split(","))

    if not os.path.exists(asnlib_path):
        put_dir = asnlib_path
        os.mkdir(put_dir)

    if not os.path.exists(script_path):
        put_dir = script_path
        os.mkdir(put_dir)

    assignment_points = int(input(print_green("How many points is this assignment worth?")))
    assignment_categories_num = int(input(print_yellow("How many categories are in this assignment?")))

    assignment_categories = [assignment_categories_num]
    assignment_category_points = [assignment_categories_num]

    i = 0
    while i < assignment_categories_num:
        assignment_categories.append(input(print_cyan("What is the name of this category?")))
        assignment_category_points.append(input(print_green("How many points is this category worth?")))
        i += 1

    number_of_file_to_submit = int(input(print_yellow("How many files should the student be submitting?")))
    filenames = [number_of_file_to_submit]

    i = 0
    while i < number_of_file_to_submit:
        filenames.append(input(print_light_purple("What is the name of the file? Make sure to include the "
                                                  "extension.")))
        i += 1

    root_path = path_joiner("{},/,{},/,{},/".format(os.getcwd(),
                                                    assignment_properties[0], assignment_properties[1]).split(","))
    create_scripts(filenames, assignment_type, root_path)


if __name__ == "__main__":
    easy_voc()
