from collections import OrderedDict, deque
from sortedcontainers import SortedDict
class MovieTheatre:
    def __init__(self):
        self.rows = 10
        self.cols = 20
        self.num_seats = self.rows * self.cols
        self.res = OrderedDict()    # result hashmap
        self.unallocated_seats = SortedDict()
        self.unallocated_seats[self.cols] = deque()
        self.seats = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.initHashMap()
        
    def initHashMap(self):
        flag = True
        jump_row = 1
        row = (self.rows//2)-1
        while row >= 0 and row < self.rows:
            temp = {chr(row+65):(0,self.cols-1)}
            self.unallocated_seats[self.cols].append(temp)
            if flag:
                row += jump_row
                flag = False
            else:
                row -= jump_row
                flag = True
            jump_row += 1
        # print(self.unallocated_seats)
    
    def bookSeats(self, reservation:str) -> int:
        input = reservation.split(" ")
        rsrv_no = input[0]
        group_count = int(input[1])
        ret_val = 0
        if group_count > 0:
            if self.num_seats >= group_count:
                if group_count > self.cols:
                    while group_count > self.cols:
                        ret_val = self.allocateSeats(rsrv_no, self.cols)
                        group_count -= self.cols
                    ret_val = self.allocateSeats(rsrv_no, group_count)
                else:
                    ret_val = self.allocateSeats(rsrv_no, group_count)
                return ret_val
            else:
                return -1
        else:
            return 1

    def findKey(self, group_count):
        for key in self.unallocated_seats:
            if key >= group_count:
                return key
        return -1

    def allocateSeats(self, rno:str, group_count:int) -> int:
        key = self.findKey(group_count)
        if key == -1:
            return -1
        row = self.unallocated_seats[key].popleft()
        if not self.unallocated_seats[key]:
            del self.unallocated_seats[key]
        row_key, col_start, col_end = None, None, None
        for k, val in row.items():
            row_key = k
            col_start, col_end = val
        for i in range(group_count):
            if col_start < self.cols:
                self.seats[ord(row_key)-ord('A')][col_start] = rno
                if rno not in self.res:
                    self.res[rno] = []
                self.res[rno].append(row_key+str(col_start+1))
                self.num_seats -= 1
            col_start += 1
        for _ in range(3):
            if col_start < self.cols:
                # storing XXXX to reserve seats for the public safety
                self.seats[ord(row_key)-65][col_start] = "XXXX"
                self.num_seats -= 1
            col_start += 1
        if col_end-col_start+1 > 0:
            if col_end-col_start+1 not in self.unallocated_seats:
                self.unallocated_seats[col_end-col_start+1] = deque()
            temp = {row_key: (col_start, col_end)}
            self.unallocated_seats[col_end-col_start+1].append(temp)
        return 0

    def displaySeatingArrangement(self) -> None:
        print("\nRESERVATIONS\n")
        print("*********************************************[[ SCREEN ]]********************************************\n")
        for row in range(self.rows):
            print(chr(row+65) + "", end=" ")
            for col in range(self.cols):
                print(self.seats[row][col], end=" ")
            print("\n")

    def getResults(self) -> OrderedDict:
        return self.res

    def getSeatsNumber(self) -> int:
        return self.num_seats
