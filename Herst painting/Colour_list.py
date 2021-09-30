import colorgram
class ColourList():
    def __init__(self,image,num_of_colours):
        self.colours = colorgram.extract(image, num_of_colours)
        self.num_of_colours = num_of_colours
        self.colour_list = []
        self.exlude_common = 0
        self.exlude_rare = 0

    def create_list_from_tupple(self, exlude_common_colour_num, exlude_rare_colour_num):
        '''Creates list from the Colours in the pallet, with most common colours coming first'''
        self.exlude_common = exlude_common_colour_num
        self.exlude_rare = exlude_rare_colour_num


        for i in range(self.exlude_common ,self.num_of_colours-exlude_rare_colour_num):
            r = self.colours[i].rgb.r
            g = self.colours[i].rgb.g
            b = self.colours[i].rgb.b
            colour_rgb_value = (r,g, b)
            self.colour_list.append(colour_rgb_value)
        return self.colour_list

