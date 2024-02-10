import os
from flask import Flask, render_template, request, url_for
from ascii_gen import load_image, resize_image, pixel_to_ascii

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'  # Define a folder to store uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/create", methods=['GET', 'POST'])
def create():
    file = None  # Initialize file variable

    if request.method == 'POST':
        # Check if the POST request has a file part
        if 'file' not in request.files:
            return render_template("create.html", error="No file part")

        file = request.files['file']

        # If the user does not select a file, browser may submit an empty file
        if file.filename == '':
            return render_template("create.html", error="No selected file")

        # If file is selected and valid, save it to disk
        if file:
            # Create a path to save the uploaded file
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Load the image from the saved filepath
            image = load_image(filepath)
            if image is None:
                return render_template("create.html", error="Error loading image")

            # Resize the image
            image = resize_image(image)

            # Convert the image to ASCII art
            ascii_art = pixel_to_ascii(image)

            image_width = image.shape[1]

            # Render the create.html template with the ASCII art
            return render_template("create.html", ascii_art=ascii_art, image_width=image_width, file=file)

    # Render the create.html template for GET requests
    return render_template("create.html", file=file)






# @app.route("/create", methods=['GET', 'POST'])
# def create():
#     if request.method == 'POST':
#         # Check if the POST request has a file part
#         if 'file' not in request.files:
#             return render_template("create.html", error="No file part")

#         file = request.files['file']

#         # If the user does not select a file, browser may submit an empty file
#         if file.filename == '':
#             return render_template("create.html", error="No selected file")

#         # If file is selected and valid, save it to disk
#         if file:
#             # Create a path to save the uploaded file
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#             file.save(filepath)

#             # Load the image from the saved filepath
#             image = load_image(filepath)
#             if image is None:
#                 return render_template("create.html", error="Error loading image")

#             # Resize the image
#             image = resize_image(image)

#             # Convert the image to ASCII art
#             ascii_art = pixel_to_ascii(image)

#             image_width = image.shape[1]
#             print(f'Image Width in views: {image_width}')


#             # Render the create.html template with the ASCII art
#             return render_template("create.html", ascii_art=ascii_art, image_width=image_width)

    # Render the create.html template for GET requests
    return render_template("create.html")



if __name__ == "__main__":
    app.run(debug=True)