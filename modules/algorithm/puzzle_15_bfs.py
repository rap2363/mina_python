class State:
    def __init__(self, initial_state):
        self.initial_state = tuple(initial_state)

    def __eq__(self, other):
        return self.initial_state == other.initial_state
    
    def __hash__(self):
        return hash(tuple(self.initial_state))
    
        
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
                new_initial_state = list(first_state) # converting to list to modify
                new_initial_state[index],new_initial_state[new_index] =  new_initial_state[new_index], new_initial_state[index]
                neighbour.append(tuple(new_initial_state)) #making it hashable
        return neighbour

    def breadth_first_search(self,goal_state):
        goal_state = tuple(goal_state)
        queue = [] # or could be a deque
        queue.append(self.initial_state)
        visited_states = set([self.initial_state])
        
        steps = {}  # To track the different states

        while len(queue) > 0:
            current_state = queue.pop(0)
            if current_state == goal_state:
                # reconstruct the path path if goal state is reached
                path = [current_state]
                while current_state in steps:
                    current_state = steps[current_state]
                    path.append(current_state)
                path.reverse() # to see the path from initial to goal state
                print('The puzzle has been solved. Steps:')
                for i in path:
                    print(i)
                return path
                
            
            current = State(current_state)
            neighbors = current.generate_neighbours()
            for n in neighbors:
                    if n not in visited_states:
                        
                        visited_states.add(n)
                        queue.append(n)
                        steps[n] = current_state
        print(f'Puzzle not solvable')

        return self.initial_state
    
