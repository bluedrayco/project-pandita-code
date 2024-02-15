import time
from mp3.DFPlayer import DFPlayer
from lcd.ST7735 import TFT,TFTColor
from machine import Pin,SPI
from lcd.fonts import sysfont
import math

start_mp3=1
end_mp3=44
step_mp3=start_mp3

start_fotos=1
end_fotos=7
step_fotos=start_fotos
time_fotos=5000

df=DFPlayer(uart_id=2)
print("empezo")
time.sleep(0.2)
df.volume(25)
time.sleep(0.2)
df.play(1,step_mp3)
time.sleep(1)
print(df.is_playing())


spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(13))
tft=TFT(spi,4,22,5)
tft.initr()
tft.rgb(True)

#test_main()
#time.sleep(2)
v = 0
tiempoTexto=5000
tft.fill(TFT.BLACK)
tft.text((0, v), "Gracias porsiempre    apoyarme,  creer en miy ver en   mi interiorlo que     otros no   ven en mi", TFT.WHITE, sysfont, 2, nowrap=False)
time.sleep_ms(tiempoTexto)
tft.fill(TFT.BLACK)
tft.text((0, v), "Gracias porser mi     companera  de vida y  tener      grandes    aventuras  juntos", TFT.GREEN, sysfont, 2, nowrap=False)
time.sleep_ms(tiempoTexto)
tft.fill(TFT.BLACK)
tft.text((0, v), "Gracias porque juntos estamos    formando   una hermosafamilia", TFT.FOREST, sysfont, 2, nowrap=False)
time.sleep_ms(tiempoTexto)
tft.fill(TFT.BLACK)
tft.text((0, v), "Este       pequeno    proyecto espara       demostrartetodo lo quesignificas para mi", TFT.YELLOW, sysfont, 2, nowrap=False)
time.sleep_ms(tiempoTexto)
tft.fill(TFT.BLACK)
tft.text((0, v), "Gracias mi amor por   estar todo este tiempoa mi lado             Te ama           tu BB", TFT.RED, sysfont, 2, nowrap=False)
time.sleep_ms(tiempoTexto)


while True:
    tft.fill(TFT.BLACK)
    filePath=f"fotos/{step_fotos}.bmp"
    print(filePath)
    f=open(filePath, 'rb')
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
                tft._setwindowloc((0,0),(w - 1,h - 1))
                for row in range(h):
                    if flip:
                        pos = offset + (height - 1 - row) * rowsize
                    else:
                        pos = offset + row * rowsize
                    if f.tell() != pos:
                        dummy = f.seek(pos)
                    for col in range(w):
                        bgr = f.read(3)
                        tft._pushcolor(TFTColor(bgr[2],bgr[1],bgr[0]))
    time.sleep_ms(time_fotos)
    step_fotos=step_fotos+1 if step_fotos<end_fotos else start_fotos
    if not df.is_playing():
        step_mp3=step_mp3+1 if step_mp3<end_mp3 else start_mp3
        df.play(1,step_mp3)