"""
Naam: Mats van Leuken
Klas: Bin-1a
Datum: 17-10-2022
Toets: BI1a-T
Docent: Thijn van Kempen
"""


def main():
    file_name = 'chr1.vcf'
    aantal_a_t_mutaties(file_name)
    quality_lager_dan(file_name)


def aantal_a_t_mutaties(file_name):
    try:
        file = open(file_name, encoding="utf-8")  # Opening and renaming file
        # using utf-8 interpreter

        mutation_count = 1
        for line in file:
            line = line.strip().split("\t")
            if line[3] == 'A' and line[4] == 'T':
                mutation_count += 1

        print("The number of counted 'A' to 'T' mutations is:", mutation_count)
        return mutation_count

    except FileNotFoundError:  # Intercepting possible occurring errors
        print("Inputted file not corresponding with expected item, please "
              "check file name.")


def quality_lager_dan(file_name, quality=35):
    try:
        file = open(file_name, encoding="utf-8")  # Opening and renaming file using utf-8 interpreter

        exc_count = 0
        quality_low_35_count = 0
        for line in file:
            line = line.strip().split("\t")
            try:
                if int(line[5]) < quality:
                    quality_low_35_count += 1
            except ValueError:
                print("Called on value does not qualify as integer (column headings).")
                exc_count += 1

        print("The number of counted point mutations is:", quality_low_35_count)



        # for line in quality_ls

    except FileNotFoundError:  # Intercepting possible occurring errors
        print("Inputted file not corresponding with expected item, please check file name.")


main()
