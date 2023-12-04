import tkinter as tk

def on_click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Window dimensions        
width = 400
height = 400

# Main window
root = tk.Tk()
root.title("Thanasis Calculator")
root.geometry(f"{width}x{height}")

# Entry widget for input and display
entry = tk.Entry(root, width=20, bg = 'white', font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4)

# Calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create and place the buttons in the grid
row_val = 1
col_val = 0

for button_text in buttons:
    tk.Button(root, text=button_text, width=5, height=2,bg = 'grey',
              command=lambda bt=button_text: on_click(bt)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the Tkinter event loop
root.mainloop()
