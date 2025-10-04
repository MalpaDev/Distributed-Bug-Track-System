"""
developer_ui.py
Developer interface for the distributed bug tracking system.

This UI allows a developer to:
  - Pick up bugs from the shared Tuple Space (status = "Open")
  - Mark them as "In Progress"
  - Resolve them when completed ("Resolved")
  - View all current bugs for debugging and testing purposes
"""

import tkinter as tk
from tuple_space import TupleSpace

class DeveloperUI:
    def __init__(self, root, ts, dev_name = "Dev1"):
        self.ts = ts
        self.dev_name = dev_name
        # Tracks which bug this developer is working on
        # Devs can only work on one bug at the moment
        self.current_bug = None
        # Text field for entering a bug ID
        tk.Label(root, text = "Enter Bug ID to pick: ").pack()
        self.bug_id_entry = tk.Entry(root)
        self.bug_id_entry.pack()
        # Buttons for developer actions
        tk.Button(root, text = "Pick Bug", command = self.pick_bug).pack()
        tk.Button(root, text = "Resolve Bug", command = self.resolve_bug).pack()
        tk.Button(root, text = "View All Bugs", command = self.view_all).pack()

    # Pick an unassigned, open bug and mark it as In Progress
    def pick_bug(self):
        try:
            bug_id = int(self.bug_id_entry.get())
        except ValueError:
            print("Please enter a valid bug ID")
            return
        # find and remove an open, unassigned bug that matches the given ID
        bug = self.ts.inp((bug_id, None, None, "Open", "Unassigned"))
        if bug:
            # update bugs status and assign it to the developer
            updated_bug = (bug[0], bug[1], bug[2], "In Progress", self.dev_name)
            self.ts.out(updated_bug)
            self.current_bug = updated_bug
            print(f"{self.dev_name} picked bug: ", updated_bug)
        else:
            print(f"No available bug with ID {bug_id} found or already taken")

    # Resolve the current bug and update its status
    def resolve_bug(self):
        if self.current_bug:
            # Remove the in-progress tuple and mark it as resolved
            bug = self.ts.inp(self.current_bug)
            if bug:
                resolved = (bug[0], bug[1], bug[2], "Resolved", self.dev_name)
                self.ts.out(resolved)
                print(f"{self.dev_name} resolved bug: ", resolved)
                self.current_bug = None
            else:
                print("No bug in progress")
    
    # Display all tuples currently stored in the tuple space (for debugging)
    def view_all(self):
        print("\n --- Current TupleSpace Contents ---")
        with self.ts.lock:
            if not self.ts.tuples:
                print("No bugs in tuple space")
            else:
                for bug in self.ts.tuples:
                    print(bug)
        print("--------------------------------------")
                    
# Run the Developer UI directly (for standalone testing)
if __name__ == "__main__":
    root = tk.Tk()
    ts = TupleSpace()
    app = DeveloperUI(root, ts, dev_name = "Dev1")
    root.mainloop()