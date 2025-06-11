class State:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        
    def generate_neighbours(self):
        first_state = self.initial_state
        neighbour = []

        moves = {
            'up':-3,
            'down':+3,
            'left':-1,
            'right':+1
        }
        invalid_left = [0,3,6]
        invalid_right = [2,5,8]

        #finding the first instance of 0
        index = first_state.index(0)


        for direction, v in moves.items():
            new_index = index + v
            if direction == 'left' and index in invalid_left:
                continue
            if direction == 'right' and index in invalid_right:
                continue
            if 0 <= new_index < 9:
                new_initial_state = first_state[:]
                new_initial_state[index],new_initial_state[new_index] =  new_initial_state[new_index], new_initial_state[index]
                neighbour.append(new_initial_state)
        return neighbour

    def breadth_first_search(self,initial_state,goal_state):

        queue = [] # or could be a deque
        queue.append(initial_state)
        visited_states = set()
        visited_states.add(tuple(initial_state))
        steps = {}  # To track the different states

        while len(queue) > 0:
            current_state = queue.pop(0)
            if current_state == goal_state:
                print(f'The puzzule has been sovle. {current_state}')
                return current_state
            
            current = State(current_state)
            neighbors = current.generate_neighbours()
            for n in neighbors:
                    if tuple(n) not in visited_states:
                        
                        visited_states.add(tuple(n))
                        queue.append(n)
            
        print(f'Puzzle not solvable')
        return initial_state
    
    