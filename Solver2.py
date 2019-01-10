import copy
def solve_ff(starting_state):
    reached = set()
    reached.add(starting_state)
    nextmove = [[[],starting_state]]

    while len(nextmove) > 0:
        #search through all possible moves
        
        #sort to search boards that have the most covered pancakes first
        nextmove.sort(key = bitcount, reverse = True)
        
        current = nextmove.pop(0)
        for i in range(25):
            current_board = current[1]

            #center
            current_board = current_board ^ (1 << i)
            #above
            if i > 4:
                current_board = current_board ^ (1 << (i - 5))
            #below
            if i < 20:
                current_board = current_board ^ (1 << (i + 5))
            #left
            if i % 5 != 0:
                current_board = current_board ^ (1 << (i - 1))
            #right
            if (i + 1) % 5 != 0:
                current_board = current_board ^ (1 << (i + 1))
            
            if current_board == 33554431:
                #winning moves found (25 least significant bits are 1)
                current[0].append(i)
                return remove_dups(current[0])
            if current_board not in reached:
                current_moves = copy.copy(current[0])
                current_moves.append(i)
                nextmove.append([current_moves,current_board])
                reached.add(current_board)

    return ["no winning combination found"] 

def bitcount(moveitem):
    return bin(moveitem[1]).count('1')

def remove_dups(solution):
    
    #any flapjack should be clicked 0 or 1 times, but
    #solver runs faster if allowed to explore unnecessary extra clicks
    
    #remove unnecessary extra clicks (remove pairs of same number, leaving
    #  0 or 1 of each number)
    
    if len(solution) < 2:
        return solution
    solution.sort()
    i = 1
    remove_i = []
    while(i < len(solution)):
        if solution[i] == solution[i-1]:
            remove_i.append(i-1)
            remove_i.append(i)
            i += 2
        else:
            i += 1
    
    while len(remove_i) > 0:
        del solution[remove_i.pop()]

    return solution


print("enter the buttered states of the pancakes as a string of 1s and 0s")
print("start at the top left row, move right, then go to the next row")
print("for example: 1011111111000001111111111")
print("is the input for a board that looks like this:")
print("|b| |b|b|b|")
print("|b|b|b|b|b|")
print("| | | | | |")
print("|b|b|b|b|b|")
print("|b|b|b|b|b|")
puzzle_str = input("please enter the current board state:")
puzzle = 0
for i in range(25):
    puzzle = puzzle^(int(puzzle_str[i]) << i)

solution = solve_ff(puzzle)
print("with 0 as the top-left pancake, and 24 as the bottom-right pancake like this:")
print("| 0| 1| 2| 3| 4|")
print("| 5| 6| 7| 8| 9|")
print("|10|11|12|13|14|")
print("|15|16|17|18|19|")
print("|20|21|22|23|24|")
print("click the following cakes in the following order:")
print(solution)