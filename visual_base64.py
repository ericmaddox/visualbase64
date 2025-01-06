import os 
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import filedialog, messagebox
import base64

def on_drop(event):
    """
    Handle the drag-and-drop event.
    """
    file_path = event.data
    if file_path:
        file_path = file_path.replace("{", "").replace("}", "")  # Clean up the file path
        select_and_convert_image(file_path)

def select_and_convert_image(file_path):
    """
    Converts the selected image file to a Base64 string.
    """
    try:
        if not file_path:
            return  # No file path provided

        # Convert the selected image to Base64
        with open(file_path, "rb") as image_file:
            image_data = image_file.read()
            base64_encoded = base64.b64encode(image_data).decode('utf-8')

        # Display the Base64 string in the text widget
        output_text.delete("1.0", tk.END)  # Clear existing text
        output_text.insert(tk.END, base64_encoded)

        # Notify the user
        messagebox.showinfo("Success", "Image successfully converted to Base64!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def copy_to_clipboard():
    """
    Copy the Base64 string to the clipboard.
    """
    base64_text = output_text.get("1.0", tk.END).strip()
    if base64_text:
        app.clipboard_clear()
        app.clipboard_append(base64_text)
        app.update()  # Ensure the clipboard is updated
        messagebox.showinfo("Copied", "Base64 string copied to clipboard!")

# Create the main application window
app = TkinterDnD.Tk()
app.title("Image to Base64 Converter")
app.geometry("700x600")
app.config(bg="#F7F7F7")

# Title label
title_label = tk.Label(app, text="Image to Base64 Converter", font=("Arial", 18, "bold"), fg="#333333", bg="#F7F7F7")
title_label.pack(pady=20)

# Add a drag-and-drop area
drop_area = tk.Label(app, text="Drag and drop an image file here", font=("Arial", 14), fg="#555555", bg="#DDDDDD", width=40, height=10, relief="sunken")
drop_area.pack(pady=20)
drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind('<<Drop>>', on_drop)

# Add a text widget to display the Base64 string
output_text = tk.Text(app, wrap="word", font=("Arial", 12), height=10, bg="#FFFFFF", fg="#333333", padx=10, pady=10, bd=2, relief="sunken")
output_text.pack(expand=True, fill="both", padx=30, pady=10)

# Add a scrollbar for large outputs
scrollbar = tk.Scrollbar(app, command=output_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text.config(yscrollcommand=scrollbar.set)

# Add a button to copy the Base64 string to the clipboard
copy_button = tk.Button(
    app,
    text="Copy to Clipboard",
    command=copy_to_clipboard,
    font=("Arial", 14),
    bg="#2196F3",  # Blue background
    fg="white",
    relief="flat",
    width=20,
    height=2
)
copy_button.pack(pady=20)

# Run the application
try:
    app.mainloop()
except Exception as e:
    messagebox.showerror("Error", f"An error occurred: {e}")
    app.destroy()
