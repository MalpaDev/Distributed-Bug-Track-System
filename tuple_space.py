
# Basic Tuple Space class
class TupleSpace: 
    def __init__(self):
        self.space = []

    # Add a tuple to the tuple space (out operation)
    def out(self, t):
        self.space.append(t)
        print(f"Tuple added: {t}")

    # Read a tuple without removing it (rd operation)
    def rd(self, t):
        for tuple in self.space:
            if tuple[:len(t)] == t:
                print(f"Tuple read: {tuple}")
                return tuple
        print("No matching tuple found.")
        return None

    # Remove and return a matching tuple (in operation)
    def inp(self, t):
        for tuple in self.space:
            if tuple[:len(t)] == t:     #matches the poster and the topic
                self.space.remove(tuple)
                print(f"Tuple removed: {tuple}")
                return tuple            #return the first matching Tuple
        print("No matching tuple found.")    
        return None