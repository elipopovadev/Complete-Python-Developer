from PIL import Image, ImageFilter

img = Image.open("fox.png")
print(img)
print(img.format)  # PNG
print(img.size)  # (295, 287)

filtred_img = img.filter(ImageFilter.BLUR)
filtred_img.save("blur.png", "png")

filtred_img2 = img.filter(ImageFilter.SMOOTH)
filtred_img2.save("smooth.png", "png")

filtred_img3 = img.filter(ImageFilter.SHARPEN)
filtred_img3.save("sharpen.png", "png")

converted_img = img.convert("L")
converted_img.save("grey.png", "png")
converted_img.show()

crooked_img = img.rotate(90)
crooked_img.save("crooked_img.png", "png")

img.thumbnail((200, 200))
img.save("resized_img.png", "png")
