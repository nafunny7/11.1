import pandas as pd
from PIL import Image, ImageFilter

print("PANDAS")
df = pd.read_excel("пайтон.xlsx")
print(df.head(5))
print("Изменим первую строчку")
edit_names = ["Counrty", "Square", "population", "density", "%"]
df1 = df.set_axis(edit_names, axis="columns", copy=None)
print(df1.head(3))

defolt = Image.open("oto52.jpg")
defolt.thumbnail((800, 600))
defolt.filter(ImageFilter.SMOOTH)
defolt.save("loto52.jpg")
defolt.show()
