from PIL import Image

ig = Image.open(".\\Py_project\\img\\pic.jpeg")

jpg = ig.convert("RGB")

jpg.save("pic.jpg")

print("Image converted Succesfully")           