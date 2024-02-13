# Project-Pandita

ampy --port  /dev/ttyUSB0 run -n main.py

## Firmware instalation

### ESP32

´´´bash
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20190125-v1.10.bin
´´´

### ESP8266
´´´bash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin
´´´