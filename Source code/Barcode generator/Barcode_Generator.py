from barcode import EAN8
import barcode
from barcode.writer import ImageWriter

text="Barcode created in Python"
code=barcode.get_barcode_class("code128")
image=code(text,writer=ImageWriter())
image.save("Python barcode 1")
