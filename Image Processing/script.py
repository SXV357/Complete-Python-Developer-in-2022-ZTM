from PIL import Image, ImageFilter

# img = Image.open(r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\Image Processing\Pokedex\bulbasaur.jpg")
# print(img, img.format, img.size, img.mode)
# filtered_img = img.filter(ImageFilter.BLUR) # applying blur filter
# filtered_img.save("blur.png", "png") # saving it with extension
# # filtered_img.show() # displaying
# grayscale = img.convert("L") # converting intro grayscale format
# grayscale.save("gray.png", "png")

img_arr = [r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\Image Processing\Pokedex\bulbasaur.jpg",
           r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\Image Processing\Pokedex\charmander.jpg",
           r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\Image Processing\Pokedex\pikachu.jpg",
           r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\Image Processing\Pokedex\squirtle.jpg"
           ]

# for index, path in enumerate(img_arr):
#     img = Image.open(path)
#     grayscale_img = img.convert("L")
#     grayscale_img.show()

new_img = Image.open(r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\Image Processing\Pokedex\pikachu.jpg")
grayed = new_img.convert("L")
smoothen = grayed.filter(ImageFilter.SMOOTH)
rotated = smoothen.rotate(180)
# rotated.save("final.png", "png")

print(rotated.size)
resized = rotated.resize((500, 500)) # resize method accepts tuple
resized.save("resize.png", "png")
print(resized.format, resized.size)

#cropping
crop_box = (125, 200, 320, 320)
cropped = resized.crop(crop_box)
cropped.save("cropped.png", "png")
cropped.show()

