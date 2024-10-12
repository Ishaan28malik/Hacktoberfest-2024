import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# File to save expenses
EXPENSE_FILE = 'expenses.json'

def load_expenses():
    """Load expenses from a JSON file."""
    try:
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    """Save expenses to a JSON file."""
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def is_valid_date(date_string):
    """Check if the date string is valid."""
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_expense(expenses):
    """Add a new expense from GUI input."""
    try:
        amount = float(amount_entry.get())
        if amount < 0:
            raise ValueError("Amount must be a positive number.")
        
        category = category_var.get()
        date = date_entry.get() if date_entry.get() else datetime.now().strftime("%Y-%m-%d")

        if not category:
            raise ValueError("Category cannot be empty.")
        
        if date and not is_valid_date(date):
            raise ValueError("Date must be in YYYY-MM-DD format.")
        
        expense = {
            "amount": amount,
            "category": category,
            "date": date
        }
        expenses.append(expense)
        save_expenses(expenses)
        messagebox.showinfo("Success", "Expense added successfully!")
        clear_entries()
        update_treeview(expenses)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def update_treeview(expenses):
    """Update the treeview to show current expenses with a delete option."""
    for i in tree.get_children():
        tree.delete(i)  # Clear the treeview

    for idx, expense in enumerate(expenses):
        tree.insert("", tk.END, values=(expense['date'], expense['category'], f"${expense['amount']:.2f}", "Delete"),
                    tags=('row',), iid=idx)

def delete_expense(index, expenses):
    """Delete the selected expense."""
    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this expense?"):
        expenses.pop(index)
        save_expenses(expenses)
        update_treeview(expenses)
        messagebox.showinfo("Success", "Expense deleted successfully!")

def clear_entries():
    """Clear input fields."""
    amount_entry.delete(0, tk.END)
    category_var.set('')  # Reset the category selection
    date_entry.delete(0, tk.END)

def on_treeview_click(event):
    """Handle click events in the treeview."""
    item = tree.identify_row(event.y)  # Get the row clicked
    if item:  # If a row was clicked
        column = tree.identify_column(event.x)  # Get the column clicked
        if column == "#4":  # If the delete column was clicked
            index = int(item)
            delete_expense(index, expenses)

def plot_graph_window():
    """Open a new window for plotting the graph."""
    graph_window = tk.Toplevel(root)
    graph_window.title("Plot Graph")
    graph_window.config(bg="#1e1e2e")

    tk.Label(graph_window, text="Select Graph Type:", bg="#1e1e2e", fg="#FFFFFF").pack(pady=5)
    
    graph_type_var = tk.StringVar()
    graph_type_dropdown = ttk.Combobox(graph_window, textvariable=graph_type_var, 
                                        values=["Bar", "Line", "Pie"])
    graph_type_dropdown.pack(pady=5)
    
    plot_button = tk.Button(graph_window, text="Plot", bg="#00ffcc", fg="#1a1a1a",
                            command=lambda: plot_graph(graph_type_var.get(), graph_window))
    plot_button.pack(pady=10)

    # Frame to hold the graph
    global graph_frame
    graph_frame = tk.Frame(graph_window, bg="#2d2d3f")
    graph_frame.pack(pady=10, fill=tk.BOTH, expand=True)

def plot_graph(graph_type, window):
    """Generate the graph based on selected type and display it in the new window."""
    if not expenses:
        messagebox.showerror("Error", "No expenses to plot.")
        return

    # Aggregate expenses by category
    categories = {}
    for expense in expenses:
        categories[expense['category']] = categories.get(expense['category'], 0) + expense['amount']

    # Clear previous figure
    for widget in graph_frame.winfo_children():
        widget.destroy()

    # Create a new figure
    fig, ax = plt.subplots()

    if graph_type == "Bar":
        ax.bar(categories.keys(), categories.values(), color='#1f77b4')
        ax.set_title("Expenses by Category (Bar Chart)", color="white")
    elif graph_type == "Line":
        ax.plot(categories.keys(), categories.values(), marker='o', color='#ff7f0e')
        ax.set_title("Expenses by Category (Line Chart)", color="white")
    elif graph_type == "Pie":
        ax.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', colors=['#ff9999', '#66b3ff', '#99ff99'])
        ax.set_title("Expenses by Category (Pie Chart)", color="white")
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    else:
        messagebox.showerror("Error", "Invalid graph type selected.")
        return

    ax.set_xlabel("Categories", color="white")
    ax.set_ylabel("Amount ($)", color="white")
    fig.patch.set_facecolor("#2d2d3f")
    ax.set_facecolor("#2d2d3f")
    ax.tick_params(colors="white")

    # Embed the plot in the new window
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Load existing expenses
expenses = load_expenses()

# Create GUI
root = tk.Tk()
root.title("Personal Expense Tracker")
root.state('zoomed')  # Fullscreen mode
root.config(bg="#282A36")  # Background color

# Create left frame for all content
left_frame = tk.Frame(root, bg="#282A36")
left_frame.pack(fill=tk.BOTH, expand=True)

# Entry fields for expenses
tk.Label(left_frame, text="Amount ($):", bg="#282A36", fg="#F8F8F2", font=('Courier New', 12)).pack(pady=5)
amount_entry = tk.Entry(left_frame, bg="#44475a", fg="#F8F8F2", insertbackground="white")
amount_entry.pack(pady=5)

tk.Label(left_frame, text="Category:", bg="#282A36", fg="#F8F8F2", font=('Courier New', 12)).pack(pady=5)
category_var = tk.StringVar()
category_entry = ttk.Combobox(left_frame, textvariable=category_var, values=["Food", "Transport", "Entertainment", "Utilities", "Other"])
category_entry.pack(pady=5)

tk.Label(left_frame, text="Date (YYYY-MM-DD, optional):", bg="#282A36", fg="#F8F8F2", font=('Courier New', 12)).pack(pady=5)
date_entry = tk.Entry(left_frame, bg="#44475a", fg="#F8F8F2", insertbackground="white")
date_entry.pack(pady=5)

# Add Expense Button
add_button = tk.Button(left_frame, text="Add Expense", bg="#50fa7b", fg="#1a1a1a", font=('Courier New', 12),
                       command=lambda: add_expense(expenses))
add_button.pack(pady=10)

# Plot Graph Button
plot_button = tk.Button(left_frame, text="Plot Graph", bg="#bd93f9", fg="#1a1a1a", font=('Courier New', 12),
                        command=plot_graph_window)
plot_button.pack(pady=10)

# Treeview to display expenses with delete option
tree = ttk.Treeview(left_frame, columns=("Date", "Category", "Amount", "Delete"), show="headings")
tree.heading("Date", text="Date")
tree.heading("Category", text="Category")
tree.heading("Amount", text="Amount")
tree.heading("Delete", text="Action")
tree.pack(pady=10, fill=tk.BOTH, expand=True)

# Bind click event to handle delete action
tree.bind("<Button-1>", on_treeview_click)  # Single click to check if delete column is clicked

# Exit button
exit_button = tk.Button(left_frame, text="Exit", bg="#ff5555", fg="#1a1a1a", font=('Courier New', 12), command=root.quit)
exit_button.pack(pady=10)

# Update treeview initially
update_treeview(expenses)

# Run the GUI
root.mainloop()
