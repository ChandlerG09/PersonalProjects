class FindNumConnectedSinks:

    def __init__(self) -> None:
        self.tuples = []
        self.visitedIndexes = []
        self.ConnectedSinks = []

    def FindNumConnectedSinks(self, filePath):
        with open(filePath, 'r') as file:
            for line in file:
                self.tuples.append(line.strip().split(' '))
                
        source = self.FindSourcePosition()
        self.NavigatePipes(int(source[1]), int(source[2]))

        return self.ConnectedSinks

    #Recursive Function to search through the pipes for sinks connected
    def NavigatePipes(self, x, y):

        char = self.FindValueBasedOnPosition(x, y)[0]
        
        self.visitedIndexes.append((x,y))

        #Move .Up
        if(y > 0 and 'up' in self.DetermineDirections(char) and (x,y+1) not in self.visitedIndexes and
           self.FindValueBasedOnPosition(x,y+1) != []):
            self.NavigatePipes(x, y+1)
        #Move Right
        if('right' in self.DetermineDirections(char) and (x+1,y) not in self.visitedIndexes
           and self.FindValueBasedOnPosition(x+1,y) != []):
            self.NavigatePipes(x+1, y)
        #Move Left
        if(x > 0 and 'left' in self.DetermineDirections(char) and (x-1,y) not in self.visitedIndexes
           and self.FindValueBasedOnPosition(x-1,y) != []):
            self.NavigatePipes(x-1, y)
        #Move Down  
        if('down' in self.DetermineDirections(char) and (x,y-1) not in self.visitedIndexes
           and self.FindValueBasedOnPosition(x,y-1) != []):
            self.NavigatePipes(x, y-1)

        
        if(str.isupper(char)):
            self.ConnectedSinks.append(char)

    def FindSourcePosition(self):
        return next(filter(lambda n: n[0] == '*', self.tuples))

    def FindValueBasedOnPosition(self, x, y):
        tuple = [tup for tup in self.tuples if int(tup[1]) == x and int(tup[2]) == y]
        return tuple[0] if tuple else []


    def DetermineDirections(self, char):
        if(char == '═'):
            return ['left', 'right']
        if(char == '║'):
            return ['up', 'down']
        if(char == '╔'):
            return ['down', 'right']
        if(char == '╗'):
            return ['left', 'down']
        if(char == '╚'):
            return ['up', 'right']
        if(char == '╝'):
            return ['left', 'up']
        if(char == '╠'):
            return ['up', 'down', 'right']
        if(char == '╣'):
            return ['left', 'up', 'down']
        if(char == '╦'):
            return ['left', 'right', 'down']
        if(char == '╩'):
            return ['left', 'right', 'up']
        if(char.isupper() or char == '*'):
            return ['up', 'right', 'left', 'down']
        return ['Not Found']

if __name__ == '__main__':

    print(FindNumConnectedSinks().FindNumConnectedSinks('/Users/chandlerglowicki/Development/coding_qual_input.txt'))
    print('Done')
