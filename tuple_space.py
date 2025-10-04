"""
tuple_space.py
Implements a basic Linda-style Tuple Space for interprocess communication.

The TupleSpace acts as a shared data environment where components 
like the Product Owner UI and Developer UI can add, read, and remove 
structured data tuples safely across threads.

Each tuple represents a structured piece of information
reported bug: ("bug", bug_id, title, description, status).

We use thread locking to ensure that concurrent access
to the tuple space is thread-safe.
"""

import threading

class TupleSpace: 
    def __init__(self):
        self.tuples = []
        self.lock = threading.Lock()

    # Add a tuple to the tuple space (out operation)
    def out(self, tup):
        with self.lock:
            self.tuples.append(tup)
            print(f"Tuple added: {tup}")

    # Read (without removing) a tuple that matches the template (rd operation)
    def rd(self, template):
        with self.lock:
            for tup in self.tuples:
                if self.match(tup, template):
                    print(f"Tuple read: {tup}")
                    return tup
        print("No matching tuple found.")
        return None

    # Remove a tuple that matches the template (in operation)
    def inp(self, template):
        with self.lock:
            for i, tup in enumerate(self.tuples):
                if self.match(tup, template):
                    print(f"Tuple removed: {tuple}")
                    return self.tuples.pop(i)            #return the first matching Tuple
        print("No matching tuple found.")    
        return None
    
    # checks if tuple matches a given template
    # each element in the template must either:
    #   Be None or equal with the corresponding element
    # ex. match(("bug", 1, "open"), ("bug", None, None)) -> True
    #     match(("bug", 1, "open"), ("task", None, None)) -> False
    def match(self, tup, template):
        return all(t is None or t == v for t, v in zip(template, tup))