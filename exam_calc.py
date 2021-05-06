#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program lets the user know if they are allowed to take the exam or not
#  by checking what percentage of classes they have attended


def main():
    # this function lets the user enter the amount of classes they have
    #   and then lets the user enter the amount of clsases they attended
    
    # input
    total_classes = input("Enter how many classes you had in total: ")
    attended_classes = input("Enter how many classes you attended: ")

    # process & output
    try:
        total_classes_int = int(total_classes)
        attended_classes_int = int(attended_classes)
        percent_of_attend = (attended_classes_int / total_classes_int) * 100
        print("\nYou have attended {0}% of your classes.".format(percent_of_attend))

        if percent_of_attend > 100:
          print("\nYou cannot attend {0}% of your classes! Quit lying!".format(percent_of_attend))

        elif percent_of_attend >= 75:
          print("\nYou can partake in the exam!")
        
        elif percent_of_attend < 75:
          print("\nYou cannot partake in the exam.")

    except Exception:
      print("\nYou have entered an invalid integer.")
    finally:
      print("\nDone")

if __name__ == "__main__":
    main()
    