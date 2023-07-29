from flask import Flask, render_template, request, send_file
from PIL import Image
import io
from overlay_images import overlay_images

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    composite_image_path = "static/outfit_composite.png"

    if request.method == "POST":
        # Get the selected clothing items from the form
        shirt_choice = request.form.get("shirt")
        pants_choice = request.form.get("pants")

        # Load the images based on the selected choices
        blue_shirt = Image.open(f"static/shirts/{shirt_choice}.png")
        brown_pants = Image.open(f"static/pants/{pants_choice}.png")

        # Call the overlay_images function with the selected images
        overlay_images(blue_shirt, brown_pants)

        # Return the path to the composite image
        return render_template("index.html", composite_image_path=composite_image_path)

    # Render the index.html template with the drop-down list
    return render_template("index.html")

@app.route("/get_composite_image")
def get_composite_image():
    composite_image_path = "static/outfit_composite.png"
    return send_file(composite_image_path, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)