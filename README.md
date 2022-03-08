# Movie Theatre Seating Challenge
## Development Environment:
1. Python (3.8.9)
2. VS Code 
3. Apple M1 Silicon

## Project Overview
* This project takes an input file from command line, reads the file line by line and processes the requests to reserve the seats for a given movie theatre having 10 rows x 20 seats, 
* As per the requirements, this projects efficiently allocates seats to maximize the customer satisfaction and public safety.
* Test cases are excuted automatically.

## Algorithm's brief description:
1. A hashmap is used to store number of remaining seats and deque of the interval per row.
   1. eg. Let's say, row A has empty 20 seats. Then the hashmap will contain `key=20` and `value=[{A:(0,19)}]`
   2. A row which has greater than or equal to the count of people in group is selected to reseve the seats.
   3. If group size is greater than total seats in a row then group is partitioned in two parts to maximize the safety and satisfaction.
   4. The hashmap is updated each time when seats are allocated to a group


## Assumptions:
* Assuming that there is only one theatre with one screen, seats can be reserved for a group that has size less than theatre capacity
* To ensure public safety, adding 3 empty seats between each group, while allocating the seats

## How are the goals of the problem statememts acheived?
### Customer Satisfaction:
* To ensure customer satisfaction, the algorithm allocates seats for a group such that every customer in the group can seat next to each other so that they can enjoy a movie together.
* Accoding to a survey, best experience to watch a movie comes from the middle row of a theatre. Hence, those customers who come first will be allocated to middle row.
### Public Safety:
* To ensure public safety, the algoithm leaves 3 seats empty from both left and right direction of a group.

## Steps to run the project:
1. Navigate to the project directory.
2. execute the project by running following command:
    `python3 main.py <input-filename>`

**NOTE**: Make sure you have installed python3
