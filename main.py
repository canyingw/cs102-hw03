import sys
import csv
from statistics import mean


def main():
    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")

    # TODO: Fill in the actual logic here!
    with open(input_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            newlist = []
            for numbers in row:
                newlist.append(float(numbers))
            mean(newlist)
            print(f"{mean(newlist)}")


if __name__ == "__main__":
    main()

