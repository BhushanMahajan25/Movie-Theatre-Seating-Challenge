from asyncore import write
import string

class FileHandling:
    def __init__(self)->None:
        self.filename = None

    def readFile(self, filename:str) -> str:
        input_file = None
        try:
            input_file = open(filename, 'r')
            return input_file.readlines()
        except FileNotFoundError:
            print("File not found")
        finally:
            if input_file:
                input_file.close()
    def writeFile(self, result:dict) -> None:
        try:
            filename = "output.txt"
            writer = open(filename, 'w')
            for rno, seats in result.items():
                writer.write("{}: ".format(rno))
                for s in seats:
                    writer.write("{} ".format(s))
                writer.write("\n")
        except Exception as e:
            print(e.with_traceback())
        finally:
            writer.close()
