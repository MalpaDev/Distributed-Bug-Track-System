"""
product_owner_ui.py
Product Owner interface for the distributed bug tracking system

This UI allows the Product Owner to:
  - Submit new bugs into the shared Tuple Space
  - Specify a title and priority for each bug
  - Automatically assign default values:
        status = "Open"
        assigned_to = "Unassigned"
"""

import tkinter as tk
from tuple_space import TupleSpace
# Allows the product owner to submit new bugs into the tuple space
class ProductOwnerUI:
    def __init__(self, root, ts):
        self.ts = ts
        self.bug_id = 1             # Tracks bug IDs locally
        # Input for bug title
        self.title_entry = tk.Entry(root)
        self.title_entry.pack()
        # Dropdown menu for bug priority
        self.priority_var = tk.StringVar(value="Low")
        tk.OptionMenu(root, self.priority_var, "Low", "Medium", "High").pack()
        # Button to submit a new bug
        tk.Button(root, text = "Submit Bug", command = self.submit_bug).pack()

    # Called when submit bug is clicked
    def submit_bug(self):
        title = self.title_entry.get()
        priority = self.priority_var.get()
        bug = (self.bug_id, title, priority, "Open", "Unassigned")
        # Add to the tuple space
        self.ts.out(bug)
        print("Bug Submitted: ", bug)
        self.bug_id += 1

# Run the Product Owner UI directly (standalone testing)
if __name__ == "__main__":
    root = tk.Tk()
    ts = TupleSpace()
    app = ProductOwnerUI(root, ts)
    root.mainloop()