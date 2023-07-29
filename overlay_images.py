from PIL import Image
import math
def overlay_images(shirt_image, pants_image):
    # Load images
    human_model = Image.open("static/humans/human_model_3.png")

    # Convert human model to 'RGBA' mode to preserve alpha channel (if present)
    human_model = human_model.convert("RGBA")

    # Get image sizes
    human_width, human_height = human_model.size
    shirt_width, shirt_height = shirt_image.size
    pants_width, pants_height = pants_image.size

    # Proportions for the human model
    legs_proportion = 0.5
    torso_proportion = 0.33
    head_proportion = 0.12

    # Calculate dimensions based on the proportions
    head_height = int(human_height * head_proportion)
    torso_height = int(human_height * torso_proportion)
    legs_height = int(human_height * legs_proportion)

    # Calculate the remaining height available for the shirt and pants
    shirt_available_height = torso_height
    pants_available_height = legs_height

    # Resize the shirt to fit the torso
    shirt_aspect_ratio = shirt_width / shirt_height
    shirt_height = shirt_available_height+int(0.2*shirt_available_height)
    shirt_width = int(shirt_height * shirt_aspect_ratio)
    shirt = shirt_image.resize((shirt_width, shirt_height))

    # Resize the pants to fit the legs
    pants_aspect_ratio = pants_width / pants_height
    pants_height = pants_available_height+int(pants_available_height*0.1)
    pants_width = int(pants_height * pants_aspect_ratio) + int(0.2*pants_height * pants_aspect_ratio)
    pants = pants_image.resize((pants_width, pants_height))

    # Find center coordinates of the resized human model
    center_x = human_width // 2
    center_y = human_height // 2

    # Position the shirt on the torso
    shirt_x = center_x - shirt_width // 2
    shirt_y = head_height  # Start the shirt at the top of the torso
    human_model.paste(shirt, (shirt_x, shirt_y), mask=shirt)

    # Position the pants on the legs
    pants_x = center_x - pants_width // 2
    pants_y = shirt_y + shirt_height - math.floor(0.2*shirt_height)   # Place the pants below the shirt
    
    print(pants_y)
    human_model.paste(pants, (pants_x, pants_y), mask=pants)

    # Save the composite image with the same color mode as the original human model
    human_model.save("static/outfit_composite.png", format='PNG', subsampling=0, quality=100)

# The rest of the code (Flask app setup and URL routes) remains the same.
