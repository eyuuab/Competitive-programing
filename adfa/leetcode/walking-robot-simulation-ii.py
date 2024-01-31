class Robot:
    def __init__(self, width: int, height: int):
        self.size = [width, height]
        self.current_position = [0, 0]
        self.current_direction = 'East'        

    def step(self, num: int) -> None:
        x, y = self.current_position
        direction = self.current_direction
        size = self.size
        
        # Calculate total moves available 
        total_moves = 2*(size[0]-1 + size[1]-1)
        
        # Speedup the process
        if num >= total_moves: num = num % total_moves
            
        # Handle EDGE CASE directions
        if num == 0 and x == 0 and y == 0: direction = 'South'
        elif num == 0 and x == size[0] -1 and y == 0: direction = 'East'
        elif num == 0 and x == size[0] -1 and y == size[1]-1: direction = 'North'
        elif num == 0 and x == 0 and y == size[1] -1: direction = 'West'
            
        # Travel remaining distance normally
        while num > 0:
            if direction == 'East': 
                if x < size[0] -1: 
                    x += 1
                    num -= 1
                else:
                    direction = 'North'
            
            elif direction == 'North': 
                if y < size[1] -1: 
                    y += 1
                    num -= 1
                else:
                    direction = 'West'
            
            elif direction == 'West': 
                if x > 0:
                    x -= 1
                    num -=1
                else:
                    direction = 'South'
            
            elif direction == 'South': 
                if y > 0: 
                    y -= 1
                    num -= 1
                else:
                    direction = 'East'
          
        self.current_position = [x, y]
        self.current_direction = direction

    def getPos(self) -> List[int]:
        return self.current_position

    def getDir(self) -> str:
        return self.current_direction