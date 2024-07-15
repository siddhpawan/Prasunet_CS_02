from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog

class ImageEncryptionTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption Tool")

        # Create input fields
        self.image_label = tk.Label(root, text="Select Image:")
        self.image_label.pack()
        self.image_entry = tk.Entry(root, width=40)
        self.image_entry.pack()
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_image)
        self.browse_button.pack()

        self.key_label = tk.Label(root, text="Enter Encryption Key:")
        self.key_label.pack()
        self.key_entry = tk.Entry(root, width=40)
        self.key_entry.pack()

        # Create buttons
        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt_image)
        self.encrypt_button.pack()
        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt_image)
        self.decrypt_button.pack()

        # Create output field
        self.output_label = tk.Label(root, text="Output:")
        self.output_label.pack()
        self.output_text = tk.Text(root, height=10, width=40)
        self.output_text.pack()

    def browse_image(self):
        image_path = filedialog.askopenfilename()
        self.image_entry.delete(0, "end")
        self.image_entry.insert(0, image_path)

    def encrypt_image(self):
        image_path = self.image_entry.get()
        key = int(self.key_entry.get())

        # Open the image
        image = Image.open(image_path)
        # Convert the image to a numpy array
        pixels = np.array(image)

        # Perform XOR operation on each pixel value
        encrypted_pixels = pixels ^ key

        # Convert the encrypted pixels back to an image
        encrypted_image = Image.fromarray(encrypted_pixels)

        # Save the encrypted image
        encrypted_image.save('encrypted_image.png')

        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", "Image encrypted successfully. Encrypted image saved as 'encrypted_image.png'")

    def decrypt_image(self):
        image_path = self.image_entry.get()
        key = int(self.key_entry.get())

        # Open the encrypted image
        encrypted_image = Image.open(image_path)
        # Convert the encrypted image to a numpy array
        encrypted_pixels = np.array(encrypted_image)

        # Perform XOR operation on each pixel value to decrypt
        decrypted_pixels = encrypted_pixels ^ key

        # Convert the decrypted pixels back to an image
        decrypted_image = Image.fromarray(decrypted_pixels)

        # Save the decrypted image
        decrypted_image.save('decrypted_image.png')

        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", "Image decrypted successfully. Decrypted image saved as 'decrypted_image.png'")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptionTool(root)
    root.mainloop()