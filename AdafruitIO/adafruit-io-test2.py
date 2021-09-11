from Adafruit_IO import *

aio = Client('csn495', 'aio_VLmr90d31e3xNDl07HJ36ojN4joF')

numb = 42
aio.send("number", numb)
