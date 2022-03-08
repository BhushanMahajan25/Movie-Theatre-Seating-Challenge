import sys
from file_processing import FileHandling
from movie_theatre import MovieTheatre
from tests import Testing
def main():
    try:
        try:
            input_filename = sys.argv[1]
        except IndexError:
            print("Please specify the input filename in the command line argument")
            exit(0)
        fileObj = FileHandling()
        lines = fileObj.readFile(input_filename)
        if not lines:
            raise FileNotFoundError
        theatreObj = MovieTheatre()
        for line in lines:
            ret_val = theatreObj.bookSeats(line)
            if ret_val == 1:
                print("Invalid number of seats")
            if ret_val == -1:
                print("Insufficient seats")
        result = theatreObj.getResults()
        # print(result)
        fileObj.writeFile(result)
        theatreObj.displaySeatingArrangement()

        testObj = Testing()
        testObj.testAll()

    except FileNotFoundError:
        pass   


if __name__ == "__main__":
    main()