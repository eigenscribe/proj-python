#I found the "base" code for this at https://www.webucator.com/article/python-color-constants-module/

from collections import OrderedDict, namedtuple

Color = namedtuple('RGB','red, green, blue')
colors = {} #dict of colors

class RGB(Color):
  def hex_format(self):
    #'''Returns color in hex format'''
    return '#{:02X}{:02X}{:02X}'.format(self.red,self.green,self.blue)

# Define the RGB class before using it to create color constants
BLUE = RGB(0,0,255)
BLUE2 = RGB(0, 0, 238)
BLUE3 = RGB(0, 0, 205)
BLUE4 = RGB(0, 0, 139)
BLUEVIOLET = RGB(138, 43, 226)

# Add colors to the colors dictionary
colors['blue'] = BLUE
colors['blue2'] = BLUE2
colors['blue3'] = BLUE3
colors['blue4'] = BLUE4
colors['blueviolet'] = BLUEVIOLET
colors = OrderedDict(sorted(colors.items(), key=lambda t: t[0]))
