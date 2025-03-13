from tkinter import Label, Button, filedialog, Checkbutton, Entry, BooleanVar, Canvas, Scale
from tkinter.constants import HORIZONTAL
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking")
        self.root.geometry("800x500")
        self.root.configure(bg="#555c5c")

        # Variables
        self.image_path = None
        self.watermark_path = None
        self.text_watermark = BooleanVar()
        self.image_watermark = BooleanVar()
        self.image = None
        self.original_image = None  # Store the original image

        # UI Elements
        self.choose_image_btn = Button(root, text="Choose a Picture", command=self.load_image)
        self.choose_image_btn.place(x=50, y=50)

        self.image_watermark_checkbox = Checkbutton(root, text="Picture Watermark", variable=self.image_watermark)
        self.image_watermark_checkbox.place(x=50, y=100)

        self.choose_watermark_btn = Button(root, text="Choose a Watermark", command=self.load_watermark)
        self.choose_watermark_btn.place(x=50, y=150)

        self.text_watermark_checkbox = Checkbutton(root, text="Text Watermark", variable=self.text_watermark)
        self.text_watermark_checkbox.place(x=50, y=200)

        self.watermark_text_label = Label(root, text="Watermark Text:", bg="#555c5c", fg="white")
        self.watermark_text_label.place(x=50, y=250)

        self.text_entry = Entry(root)
        self.text_entry.place(x=150, y=250, width=100)

        self.add_watermark_btn = Button(root, text="Add Watermark", command=self.apply_watermark)
        self.add_watermark_btn.place(x=50, y=300)

        self.clear_btn = Button(root, text="Clear Watermark", command=self.clear_watermark)
        self.clear_btn.place(x=150, y=300)

        self.save_btn = Button(root, text="Save Picture", command=self.save_image)
        self.save_btn.place(x=500, y=450)

        self.canvas = Canvas(root, width=400, height=300, bg="white")
        self.canvas.place(x=300, y=50)

        self.image_display = None

        # Positioning UI for watermark
        self.canvas_x_label = Label(root, text="Position X", bg="#555c5c", fg="white")
        self.canvas_x_label.place(x=80, y=350)
        self.canvas_x_entry = Scale(root, from_=0, to=100, orient=HORIZONTAL)
        self.canvas_x_entry.place(x=150, y=350, width=100)

        self.canvas_y_label = Label(root, text="Position Y", bg="#555c5c", fg="white")
        self.canvas_y_label.place(x=80, y=400)
        self.canvas_y_entry = Scale(root, from_=0, to=100, orient=HORIZONTAL)
        self.canvas_y_entry.place(x=150, y=400, width=100)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if self.image_path:
            self.original_image = Image.open(self.image_path)  # Store the original image
            self.image = self.original_image.copy()
            self.display_image(self.image)

            # Update Scale widget ranges based on the image size
            self.canvas_x_entry.config(from_=0, to=self.image.width)
            self.canvas_y_entry.config(from_=0, to=self.image.height)

    def load_watermark(self):
        self.watermark_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])

    def clear_watermark(self):
        """ Reset the image to the original state, removing all watermarks. """
        if self.original_image:
            self.image = self.original_image.copy()
            self.display_image(self.image)

    def apply_watermark(self):
        """ Clear previous watermarks and apply a new one. """
        if not self.original_image:
            return

        self.clear_watermark()  # Reset to original image before adding a new watermark
        watermarked_image = self.image.copy()
        draw = ImageDraw.Draw(watermarked_image)

        pos_x = self.canvas_x_entry.get()
        pos_y = self.canvas_y_entry.get()

        # Add text watermark
        if self.text_watermark.get():
            font = ImageFont.load_default()
            draw.text((pos_x, pos_y), self.text_entry.get(), fill="black", font=font)

        # Add image watermark
        if self.image_watermark.get() and self.watermark_path:
            watermark = Image.open(self.watermark_path).convert("RGBA")

            # Scale the watermark to the image size
            w_ratio = self.image.width / 4  # Adjust size relative to the image
            h_ratio = self.image.height / 4
            watermark = watermark.resize((int(w_ratio), int(h_ratio)))

            watermarked_image.paste(watermark, (pos_x, pos_y), watermark)

        self.display_image(watermarked_image)
        self.image = watermarked_image  # Update image with watermark

    def display_image(self, img):
        img.thumbnail((400, 300))
        self.image_display = ImageTk.PhotoImage(img)
        self.canvas.create_image(200, 150, image=self.image_display)

    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")])
            if file_path:
                self.image.save(file_path)