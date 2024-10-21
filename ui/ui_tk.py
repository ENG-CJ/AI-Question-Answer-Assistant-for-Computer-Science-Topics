import tkinter as tk
from tkinter import Button
from PIL import Image, ImageTk

def app_main_loop(start_command=None,stop_command=None):
    # Create the root window
    root = tk.Tk()
    # Set window title
    root.title("Ai Assistant")

    # Adjust window width and height
    root.geometry("500x500")  # You can change the width and height as per your requirement

    # Load the image (ensure your image is in the same directory or provide the correct path)
    image_path = "listen.png"  # Replace with the path to your image
    image = Image.open(image_path)
    image = image.resize((300, 300))  # Resize image to fit the window

    # Convert the image to PhotoImage for Tkinter
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    image_label = tk.Label(root, image=photo)
    image_label.pack(pady=10)  # Add some padding to center the image vertically

    # Create a frame for buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)  # Add padding between the image and buttons

    # Add buttons to the frame
    btn1 = Button(button_frame, text="Start",command=start_command)
    btn1.pack(side="left", padx=10)  # Add padding between buttons

    btn2 = Button(button_frame, text="Stop",command=stop_command)
    btn2.pack(side="left", padx=10)

    return root
