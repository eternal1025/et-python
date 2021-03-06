#!/usr/bin/env python
# author:  Hua Liang [ Stupid ET ]
# email:   et@everet.org
# website: http://EverET.org
#
import Image

color = 'MNHQ$OC?7>!:-;.'

def to_html(func):
    html_head = '''
            <html>
              <head>
                <style type="text/css">
                  body {font-family:Monospace; font-size:5px; font-weight:bold;}
                </style>
              </head>
            <body> '''
    html_tail = '</body></html>'

    def wrapper(img):
        pic_str = func(img)
        pic_str = ''.join(l + ' <br/>' for l in pic_str.splitlines())
        return html_head + pic_str + html_tail

    return wrapper

@to_html
def make_char_img(img):
    pix = img.load()
    pic_str = ''
    width, height = img.size
    for h in xrange(height):
        for w in xrange(width):
            pic_str += color[int(pix[w, h]) * 14 / 255] 
        pic_str += '\n'
    return pic_str

def preprocess(img_name):
    img = Image.open(img_name)

    w, h = img.size
    m = max(img.size)
    delta = m / 180.0 
    w, h = int(w / delta), int(h / delta)
    img = img.resize((w, h))
    img = img.convert('L')

    return img

def make_save_char_img(filename, outfilename):
    save_to_file(outfilename, make_char_image(filename))

def save_to_file(filename, pic_str):
    outfile = open(filename, 'w')
    outfile.write(pic_str)
    outfile.close()

def make_char_image(filename):
    img = preprocess(filename) 
    pic_str = make_char_img(img) 
    return pic_str

class CharImg:
    def __init__(self):
        self.handlers = {'load':{}, 'preprocess':{}, 'process':{}, 'pixel_process':{}}
        self.data = {'img':None}
    def load_img(self, filename):
        self.data['img'] = Image.open(filename)
        return [func(self.data['img']) for func in self.handlers['load']]
    def preprocess(self):
        return [func(self.data['img']) for func in self.handlers['preprocess']]
    def pixel_process(self):
        return [func(self.data['img']) for func in self.handlers['pixel_process']]
    def process(self):
        return [func(self.data['img']) for func in self.handlers['process']]
    
def main():
    pass


if __name__ == '__main__':
    main()
