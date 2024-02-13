from lcd.ST7735 import TFT,TFTColor

class Catalog:
        
    def __init__(self,repo:str,start:int,end:int,exclude:list):
        spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(13))
        self.__tft=TFT(spi,4,22,5)
        self.__tft.initr()
        self.__tft.rgb(True)
        self.__tft.rotation(0)
        self.__tft.fill(TFT.BLACK)
        self.__start=start
        self.__end=end
        self.__exclude=exclude
        self.__cursor=start
        self.__repo=repo
        
    def __printImage(self)->None:
        f=open("photo.bmp", 'rb')
        if f.read(2) == b'BM':  #header
            dummy = f.read(8) #file size(4), creator bytes(4)
            offset = int.from_bytes(f.read(4), 'little')
            hdrsize = int.from_bytes(f.read(4), 'little')
            width = int.from_bytes(f.read(4), 'little')
            height = int.from_bytes(f.read(4), 'little')
            if int.from_bytes(f.read(2), 'little') == 1: #planes must be 1
                depth = int.from_bytes(f.read(2), 'little')
                if depth == 24 and int.from_bytes(f.read(4), 'little') == 0:#compress method == uncompressed
                    print("Image size:", width, "x", height)
                    rowsize = (width * 3 + 3) & ~3
                    if height < 0:
                        height = -height
                        flip = False
                    else:
                        flip = True
                    w, h = width, height
                    if w > 128: w = 128
                    if h > 160: h = 160
                    self.__tft._setwindowloc((0,0),(w - 1,h - 1))
                    for row in range(h):
                        if flip:
                            pos = offset + (height - 1 - row) * rowsize
                        else:
                            pos = offset + row * rowsize
                        if f.tell() != pos:
                            dummy = f.seek(pos)
                        for col in range(w):
                            bgr = f.read(3)
                            self.__tft._pushcolor(TFTColor(bgr[2],bgr[1],bgr[0]))
                            
    def __downloadImage(self,imageName:str):
        pass
        
    def next(self):
        if self.__cursor not in self.__exclude:
            self.__downloadImage(f"{self.__cursor}.bmp")
        self.__printImage()
        self.__cursor = self.__cursor + 1 if self.__cursor <= self.__end else self.__start
    
    def changeConfig(self,repo:str,start:int,end:int,exclude:list)->None:
        self.__repo=repo
        self.__start=start
        self.__end=end
        self.__exclude=exclude
        self.__cursor=start
            
        