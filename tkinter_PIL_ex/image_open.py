import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from urllib.parse import urlparse


# Create a function to open the image in a pop-up window
def open_image(link):
    # Create a new window
    window = tk.Toplevel()

    # Check if the link is a local file path or an HTTP URL
    scheme = urlparse(link).scheme

    if scheme == 'file':
        # Extract the file path from the link
        path = urlparse(link).path
        # Load the image using Pillow
        image = Image.open(path)
    elif scheme == 'http' or scheme == 'https':
        # Download the image using requests
        response = requests.get(link)
        # Load the image from the response using Pillow
        image = Image.open(BytesIO(response.content))
    else:
        print(f'Unsupported URL scheme: {scheme}')
        return

    # Resize the image to fit the window
    width, height = image.size
    if width > 800:
        ratio = 800 / width
        width *= ratio
        height *= ratio
    if height > 600:
        ratio = 600 / height
        width *= ratio
        height *= ratio
    image = image.resize((int(width), int(height)), Image.ANTIALIAS)

    # Convert the image to a format that tkinter can use
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    label = tk.Label(window, image=photo)
    label.image = photo  # keep a reference to the image to prevent it from being garbage-collected

    # Add the label to the window and center it
    label.pack(expand=True, fill='both')
    window.geometry(f'{int(width)}x{int(height)}+100+100')  # center the window on the screen
    window.title(link)
    window.focus_set()
    window.grab_set()
    window.wait_window()

# Create a tkinter window with links
root = tk.Tk()
root.title("Image Viewer")

# Add a label and links to the window
tk.Label(root, text="Click a link to open the image in a pop-up window").pack()
image_links = ["https://i.stack.imgur.com/8lOtO.png",
               "https://imgs.xkcd.com/comics/helium_reserve.png",
               "https://i.stack.imgur.com/gPtbt.jpg"]
for link in image_links:
    tk.Label(root, text=link).pack()
    tk.Button(root, text="Open Image", command=lambda l=link: open_image(l)).pack()

root.mainloop()
