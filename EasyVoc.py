import os


# define colored print formats using ANSI color codes
def print_red(text): print("\x1B[91m {}\x1B[00m".format(text))


def print_green(text): print("\x1B[92m {}\x1B[00m".format(text))


def print_yellow(text): print("\x1B[93m {}\x1B[00m".format(text))


def print_light_purple(text): print("\x1B[94m {}\x1B[00m".format(text))


def print_purple(text): print("\x1B[95m {}\x1B[00m".format(text))


def print_cyan(text): print("\x1B[96m {}\x1B[00m".format(text))


def print_gray(text): print("\x1B[97m {}\x1B[00m".format(text))


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

    if not os.path.exists(os.path.join(os.getcwd(), '/', assignment_properties[0],
                                       '/', assignment_properties[1], '/asnlib')):
        put_dir = os.path.join(os.getcwd(), '/', assignment_properties[0], '/', assignment_properties[1], '/asnlib')
        os.mkdir(put_dir)

    if not os.path.exists(os.path.join(os.getcwd(), '/', assignment_properties[0],
                                       '/', assignment_properties[1], '/scripts')):
        put_dir = os.path.join(os.getcwd(), '/', assignment_properties[0], '/', assignment_properties[1], '/scripts')
        os.mkdir(put_dir)

    if assignment_type == "LB":
        # assignment is a lab
        print_green("Because the assignment is a LAB, it is worth 100 points. It is split into three categories: "
                    "Debugging, Walkthrough, and Challenge. How would you like these points distributed?")

        while True:
            debugging_points = input(print_light_purple("How many points is the debugging?"))
            walkthrough_points = input(print_light_purple("How many points is the walkthrough?"))
            challenge_points = input(print_light_purple("How many points is the challenge?"))

            if debugging_points + walkthrough_points + challenge_points == 100:
                break
            else:
                print_red("The numbers did not add up to 100. Input the values again!")

        debugging_categories = input(print_green("How many categories are in the debugging section?"))
        walkthrough_categories = input(print_green("How many categories are in the walkthrough section?"))
        challenge_categories = input(print_green("How many categories are in the challenge section?"))

        debugging_categories_names = [debugging_categories]
        debugging_categories_points = [debugging_categories]
        walkthrough_categories_names = [walkthrough_categories]
        walkthrough_categories_points = [walkthrough_categories]
        challenge_categories_names = [challenge_categories]
        challenge_categories_points = [challenge_categories]

        print_green("\nStarting with Debugging categories...")
        for i in range(0, int(debugging_categories)):
            debugging_categories_names.append(input(print_cyan("What is category {}'s name?".format(i))))
            debugging_categories_points.append(int(input(print_cyan("How many points is the category named {} worth?".
                                                                    format(debugging_categories_names[i])))))

        print_green("\nNow, let's do walkthrough categories...")
        for i in range(0, int(walkthrough_categories)):
            walkthrough_categories_names.append(input(print_cyan("What is category {}'s name?".format(i))))
            walkthrough_categories_points.append(int(input(print_cyan("How many points is the category named {} worth?".
                                                                      format(walkthrough_categories_names[i])))))

        print_light_purple("\nFinally, let's do the challenge category...")
        for i in range(0, int(challenge_categories)):
            challenge_categories_names.append(input(print_cyan("What is category {}'s name?".format(i))))
            challenge_categories_points.append(int(input(print_cyan("How many points is the category named {} worth?".
                                                                    format(challenge_categories_names[i])))))

    else:
        print("work in progress...")


# assignment is a homework or project


if __name__ == "__main__":
    easy_voc()
