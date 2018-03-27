#
# CS1010S --- Programming Methodology
#
# Sidequest 10.1 Template
#
# Note that written answers are commented out to allow us to run your #
# code easily while grading your problem set.

from random import *
from puzzle import GameGrid
import pdb
###########
# Helpers #
###########

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0],
                  accumulate(fn, initial, seq[1:]))

def flatten(mat):
    return [num for row in mat for num in row]



###########
# Task 1  #
###########
def new_game_matrix(n):
    "Your answer here"
    matrix = []
    for i in range(n):
        matrix.append([0]*n)
    return matrix

def new_game_matrix1(n):
    empty_nest = []
    full_stack = []
    for i in range(0,n):
        empty_nest.append(0)
    for i in range(0,n):
        full_stack.append(empty_nest)
    return full_stack

def has_zero(mat):
    flatten_mat = flatten(mat)
    return 0 in flatten_mat

def add_two(mat):
    positions = ()
    if has_zero(mat) == True:
        for i in range(0,len(mat)):
            for j in range(0,len(mat)):
                if mat[i][j] == 0:
                    positions += ((i,j),)

        random_num = randint(0,len(positions)-1)
        chosen_positions = positions[random_num]
        i= chosen_positions[0]
        j = chosen_positions[1]
        print(i,j)
        mat[i][j] = 2
        return mat
    
    else:
        return mat




def add_two123(mat):
    "Your answer here"
    a = randint(0, len(mat)-1)
    b = randint(0, len(mat)-1)
    while (mat[a][b] !=0):
        a = randint(0, len(mat)-1)
        b = randint(0, len(mat)-1)
    print(a,b)
    mat[a][b] = 2
    return mat

a = (new_game_matrix(3))
#print(new_game_matrix1(3) == new_game_matrix(3))
#print(add_two123(a))


#rubbish = [[0,0,0],[0,0,0],[0,0,0]]
#rubbish[0][1] = 2

#print(rubbish)


###########
# Task 2  #
###########

def game_status(mat):
    flatten_mat = flatten(mat)
    if 2048 in flatten_mat:
       return "win"
    for each_row in mat:
        for j in range(len(each_row)-1): #exclude last element:
            if each_row[j] == each_row[j+1]:
                return "not over"
    for i in range(1,len(mat)-1):
        for j in range(len(mat)):
            if mat[i][j] == mat[i-1][j] or mat[i][j] == mat[i+1][j]:
                return "not over"
    for each_row in mat:
        if 0 in each_row:
            return "not over"
    return "lose"
            
#print(4 in [2, 4, 16, 4, 4, 2, 2, 2, 2, 4, 2, 4, 4, 2, 4, 8])
#print(game_status([[2, 0, 2, 2], [0, 0, 0, 4], [4, 0, 8, 4], [2, 0, 0, 2048]]))
#print(game_status([[2, 0, 2, 4], [0, 2, 4, 2], [2, 4, 0, 4], [4, 2, 4, 0]]))
#print(game_status([[2, 4, 16, 4], [4, 2, 2, 2], [2, 4, 2, 4], [4, 2, 4, 8]]))
#print(game_status([[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 2]]))
###########
# Task 3a #
###########

def transpose1(mat):
    m = len(mat)
    n = len(mat[0])
    flatten_mat = flatten(mat)
    
    row_length = len(mat[0])
    total = []
    for index in range(row_length):
        result = [] #capture nested lists
        for each_row in mat:
            result.append(each_row[index])
        total.append(result) #add nested  list to overall list while still  in the for loop
    return total




def transpose(mat):
   
    result = []
    length = len(mat[0])
    for i in range (length):
        add = []
        for entry in mat:
            add = add + [entry[i]]
        result = result + [add]
    return result
print("hey")
print(transpose([[1, 2, 3], [4, 5, 6]]))

###########
# Task 3b #
###########

def reverse(mat):
    result = []
    for each_row in mat:
        each_row = each_row[::-1]
        result.append(each_row)
    return result

print("what")
print(reverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

def reverse1(mat):
    mat_copy = mat.copy()
    #print(mat_copy)
    result = []
    wip = [] 
    for each_row in mat_copy:
        while each_row:
            maximum = each_row[0]
            for i in range(len(each_row)):
                if each_row[i] > maximum:
                    maximum = each_row[i]
            each_row.pop(each_row.index(maximum))
            wip.append(maximum) #needs to be out of the  for loop but in the while loop to pop at every iteration of the element within the row
        result.append(wip) #this needs to be out of the while loop to capture the sorted WIP into the final results
        wip = [] #need to clear the WIP for each row
        
    return result
            



############
# Task 3ci #
############




def merge_left(mat):
    mat_copy = mat.copy()
    new_matrix = new_game_matrix(len(mat[0])) #create  empty matrix of size m
    total_score = 0
    for row_index in range(len(mat)): #index of row
        current_row = mat[row_index] #current row processing
        element_index = 0
        
        while element_index < len(current_row):
            current_element = current_row[element_index] #set value of the current element you are inspecting
            if current_element ==0: #exclude zero elements
                element_index = element_index + 1 #skip
            else:
                if element_index == (len(current_row)-1): #last element
                    nearest_zero = new_matrix[row_index].index(0)
                    new_matrix[row_index][nearest_zero] = current_element
                    element_index = element_index + 1
                    
                elif current_row[element_index+1] == 0: #if there is no element on the right is empty
                    nearest_zero = new_matrix[row_index].index(0)
                    new_matrix[row_index][nearest_zero] = current_element
                    element_index = element_index + 1
                    
                elif current_element == current_row[element_index+1]:
                    nearest_zero = new_matrix[row_index].index(0)
                    new_matrix[row_index][nearest_zero] = current_element*2
                    total_score += current_element*2
                    element_index = element_index + 2
                    
                elif current_element != current_row[element_index+1]:
                    nearest_zero = new_matrix[row_index].index(0)
                    new_matrix[row_index][nearest_zero] = current_element
                    element_index = element_index + 1
       # pdb.set_trace()
    return tuple( (new_matrix,mat!=new_matrix,total_score))
    
#a= [[2, 2, 0, 2], [4, 0, 0, 0], [4, 8, 0, 4], [0, 0, 0, 2]]
#print(a[2].index(0))
#print("up")                
#print(merge_left([[2, 2, 0, 2], [4, 0, 0, 0], [4, 8, 0, 4], [0, 0, 0, 2]]))       
mat = [[2, 0], [0, 0]]
new_mat = merge_left(mat)
#print (new_mat)

#print( ([[4, 2, 0, 0], [4, 0, 0, 0], [4, 8, 4, 0], [2, 0, 0, 0]], True, 4) == ([[4, 2, 0, 0], [4, 0, 0, 0], [4, 8, 4, 0], [2, 0, 0, 0]], True, 4) )
#############
# Task 3cii #
#############

def merge_right(mat):
    reverse_mat = reverse(mat)
#    print(reverse_mat)
    result = merge_left(reverse_mat)
  #  print (result)
    actual = reverse(result[0])
 #   print("final")
    return tuple((actual,result[1],result[2]))

print("merge right")

test = [[2, 2, 0, 2], [4, 0, 0, 0], [4, 8, 0, 4], [0, 0, 0, 2]]
#print("trans")
#print(transpose(test))
#print("t2")
#print(transpose(merge_left(transpose(test))[0]))
def merge_up(mat):
    transpose_mat = transpose(mat)
    result = merge_left(transpose_mat)
    wip = merge_left(transpose_mat)[0]
    actual = transpose(wip)
    return tuple((actual,result[1],result[2]))



def merge_down(mat):
    transpose_mat = transpose(mat)
    print (transpose_mat)
    result = merge_right(transpose_mat)
    wip_right = merge_right(transpose_mat)[0]
    print (wip_right)
    actual = transpose(wip_right)
    return tuple((actual,result[1],result[2]))


#print("up")
#print (merge_down(test))
###########
# Task 3d #
###########

def text_play():
    def print_game(mat, score):
        for row in mat:
            print(''.join(map(lambda x: str(x).rjust(5), row)))
        print('score: ' + str(score))
    GRID_SIZE = 4
    score = 0
    mat = add_two(add_two(new_game_matrix(GRID_SIZE)))
    print_game(mat, score)
    while True:
        move = input('Enter W, A, S, D or Q: ')
        move = move.lower()
        if move not in ('w', 'a', 's', 'd', 'q'):
            print('Invalid input!')
            continue
        if move == 'q':
            print('Quitting game.')
            return
        move_funct = {'w': merge_up,
                      'a': merge_left,
                      's': merge_down,
                      'd': merge_right}[move]
        mat, valid, score_increment = move_funct(mat)
        if not valid:
            print('Move invalid!')
            continue
        score += score_increment
        mat = add_two(mat)
        print_game(mat, score)
        status = game_status(mat)
        if status == "win":
            print("Congratulations! You've won!")
            return
        elif status == "lose":
            print("Game over. Try again!")
            return

# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR GAME
#text_play()


# How would you test that the winning condition works?
# Your answer: I don't know I never won before haha
#


##########
# Task 4 #
##########

def make_state(matrix, total_score):
    return [matrix, total_score]
def get_matrix(state):
    return state[0]
    
def get_score(state):
    return state[1]
    
def make_new_game(n):
    "Your answer here"
    matrix =  add_two(add_two(new_game_matrix(n)))
    return make_state(matrix, 0)
#helper for higher order function
def helper(merge, state):
    mat = get_matrix(state)
    score = get_score(state)
    result = merge(mat)
    result_mat = result[0]
    score = score + result[2]
    if result[1] == True:
        result_mat = add_two(result_mat)
    return (make_state(result_mat,score), result[1])
    
def left(state):
    return helper(merge_left, state)
    
def right(state):
    return helper(merge_right, state)
    
def up(state):
    return helper(merge_up, state)
    
def down(state):
    return helper(merge_down, state)

# Do not edit this #
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': lambda state: (state, False)
}

# UNCOMMENT THE FOLLOWING LINE TO START THE GAME (WITHOUT UNDO)
gamegrid = GameGrid(game_logic)




#################
# Optional Task #
#################

###########
# Task 5i #
###########

def make_new_record(mat, increment):
    "Your answer here"

def get_record_matrix(record):
    "Your answer here"

def get_record_increment(record):
    "Your answer here"

############
# Task 5ii #
############

def make_new_records():
    "Your answer here"

def push_record(new_record, stack_of_records):
    "Your answer here"

def is_empty(stack_of_records):
    "Your answer here"

def pop_record(stack_of_records):
    "Your answer here"

#############
# Task 5iii #
#############

# COPY AND UPDATE YOUR FUNCTIONS HERE
def make_state(matrix, total_score, records):
    "Your answer here"

def get_matrix(state):
    "Your answer here"

def get_score(state):
    "Your answer here"

def make_new_game(n):
    pass

def left(state):
    "Your answer here"

def right(state):
    "Your answer here"

def up(state):
    "Your answer here"

def down(state):
    "Your answer here"

# NEW FUNCTIONS TO DEFINE
def get_records(state):
    "Your answer here"

def undo(state):
    "Your answer here"


# UNCOMMENT THE FOLLOWING LINES TO START THE GAME (WITH UNDO)
##game_logic = {
##    'make_new_game': make_new_game,
##    'game_status': game_status,
##    'get_score': get_score,
##    'get_matrix': get_matrix,
##    'up': up,
##    'down': down,
##    'left': left,
##    'right': right,
##    'undo': undo
##}
#gamegrid = GameGrid(game_logic)
