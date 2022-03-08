from cgi import test
from select import select
from movie_theatre import MovieTheatre

class Testing:
    def __init__(self) -> None:
        self.test = MovieTheatre()

    def testAll(self):
        print("\nExcecuting Test Cases:\n")
        self.checkFirstGroupSeat()
        self.checkReservationWithZeroRequirement()
        self.checkSufficientSeats()
        self.checkSeatAllocation()
        self.checkLargerGroup()

    def checkReservationWithZeroRequirement(self):
        if self.test.bookSeats("R001 0") == 1:
            print("Test:1 Passed")
        else:
            print("Test:1 Failed:: Reserved seats with 0 requirement of seats")
    
    def checkFirstGroupSeat(self):
        self.test.bookSeats("R002 4")
        ll = ["E1", "E2", "E3", "E4"]
        if self.test.getResults()["R002"] == ll:
            print("Test:1 Passed")
        else:
            print("Test:2 Failed:: Failed to reserve seats for first group at the middle row")

    def checkSufficientSeats(self):
        self.test.bookSeats("R003 250")
        if self.test.getSeatsNumber() > 0:
            print("Test:3 Passed")
        else:
            print("Test:3 Failed:: Allocated people out of theatre's capacity")

    def checkSeatAllocation(self):
        res = self.test.bookSeats("R004 25")
        if res == 0:
            print("Test:4 Passed")
        else:
            print("Test:4 Failed to reserve seats to a group")
    
    def checkLargerGroup(self):
        ll = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'E8', 'E9', 'E10', 'E11', 'E12']
        if self.test.getResults()["R004"] == ll:
            print("Test:5 Passed")
        else:
            print("Test:5 Failed to reserve seats to a group larger than number seats in a row")