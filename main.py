"""
Naam: Mats van Leuken
Klas: Bin-1a
Datum: 17-10-2022
Toets: BI1a-T
Docent: Thijn van Kempen
"""


def main():
    file_name = 'chr1.vcf'  # Renaming file name
    aantal_a_t_mutaties(file_name)  # Calling on function
    quality_lager_dan(file_name)  # Calling on function
    unieke_filters(file_name)  # Calling on function


def aantal_a_t_mutaties(file_name):
    try:
        file = open(file_name, encoding="utf-8")  # Opening and renaming file
        # using utf-8 interpreter

        mutation_count = 0  # Starting counter at 0
        for line in file:  # Looping trough file
            line = line.strip().split("\t")  # Splitting line at \t
            try:
                if line[3] == 'A' and line[4] == 'T':  # Checking if 'A' and 'T' are in the same line
                    mutation_count += 1  # Adding 1 to counter
            except ValueError:  # Intercepting error for not corresponding values
                print("Value found not corresponding with intended value.")  # Printing occurred problem

        print("The number of counted 'A' to 'T' mutations is:", mutation_count)  # Printing outcome

        return mutation_count  # Returning value to main

    except FileNotFoundError:  # Intercepting error if file is not found
        print("Inputted file not corresponding with expected item, please "
              "check file name.")  # Printing occurred error
    except IOError:  # Intercepting error if file is not readable
        print("Inputted file could not be read.")  # Printing occurred error


def quality_lager_dan(file_name, quality=35):
    try:
        file = open(file_name, encoding="utf-8")  # Opening and renaming file using utf-8 interpreter

        exc_count = 0  # Starting counter at 0
        quality_low_35_count = 0  # Starting counter at 0
        for line in file:  # Looping trough file
            line = line.strip().split("\t")  # Splitting line at \t
            try:
                if int(line[5]) < quality:  # Checking if value is lower than inputted value
                    quality_low_35_count += 1  # Adding 1 to counter
            except ValueError:  # Intercepting error for not corresponding values
                print("Called on value does not qualify as integer (column headings).")  # Printing occurred error
                exc_count += 1  # Adding 1 to counter
                if exc_count > 1:  # Checking if counter is bigger than 1
                    print("Number of occurred ValueErrors is higher than expected, check for strings in column 'QUAL'.")  # Printing the occurred problem

        print("The number of counted point mutations is:", quality_low_35_count)  # Printing outcome

    except FileNotFoundError:  # Intercepting error if file is not found
        print("Inputted file not corresponding with expected item, please check file name.")  # Printing occurred error
    except IOError:  # Intercepting error if file is not readable
        print("Inputted file could not be read.")  # Printing occurred error


def unieke_filters(file_name):
    try:
        file = open(file_name, encoding="utf-8")  # Opening and renaming file using utf-8 interpreter

        unique_ls = []  # Creating an empty list
        next(file)  # Skipping first line in file
        for line in file:  # Looping trough file
            line = line.strip().split("\t")  # Splitting line at \t
            try:
                if line[6] not in unique_ls:  # Checking if item is not in list
                    unique_ls.append(line[6])  # Adding item to list
            except ValueError:  # Intercepting error for not corresponding values
                print("Value found not corresponding with intended value.")  # Printing occurred problem

        return unique_ls  # Returning value to main

    except FileNotFoundError:  # Intercepting error if file is not found
        print("Inputted file not corresponding with expected item, please check file name.")  # Printing occurred error
    except IOError:  # Intercepting error if file is not readable
        print("Inputted file could not be read.")  # Printing occurred error


main()  # Calling on main function
