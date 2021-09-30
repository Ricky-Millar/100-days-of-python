from Herst_painter import HerstPainter
from Colour_list import ColourList
colourlist = ColourList('tyler.jpg',20)

list = colourlist.create_list_from_tupple(0,0)
print(list)
Painting = HerstPainter()
Painting.draw_dot_painting(15,list,40,20)
#Painting.draw_ordered_painting(list, 40, 20)