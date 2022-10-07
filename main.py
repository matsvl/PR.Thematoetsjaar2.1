

def main():
    file_name = "chr1.csv"
    data, gene_count = open_bestand(file_name)
    filter_50(data, gene_count)


def open_bestand(file_name):
    try:
        file = open(file_name, encoding="utf-8")
    except FileNotFoundError:
        print("Inputted file not corresponding with expected item, please check file name.")

    gene_count = -1
    gc_perc = []
    for line in file:
        gene_count += 1
        line = line.strip().split(",")
        gc_perc.append(line[-1])

    return gc_perc, gene_count


def filter_50(gc_perc, gene_count):

    del gc_perc[0]

    gc_perc_int = [eval(i) for i in gc_perc]
    gc_50_ls = filter(lambda x: x > 50, gc_perc_int)

    print(list(gc_50_ls))

    print(len(list(gc_50_ls)))

    # print("Out of:", gene_count, "GC percentages,", gc_higher_50, "have a percentage higher than 50%.")

    print("The number of counted genes is:", gene_count)


main()
