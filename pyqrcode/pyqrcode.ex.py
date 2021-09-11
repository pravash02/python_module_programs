import pyqrcode
from pyqrcode import QRCode

link = 'https://www.youtube.com/watch?v=lih75e6Rb8A'

url = pyqrcode.create(link)
url.svg('pyqrcode/random.svg', scale=5)
