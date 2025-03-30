from google.cloud import vision
import os

os.environ["lostandfoundAPI"] = r"C:\Users\Hp\Downloads\circular-light-447918-m1-4fef2ebfde18.json"

def get_image_labels(image_path):
    client = vision.ImageAnnotatorClient()

    with open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = [label.description for label in response.label_annotations]

    return labels
