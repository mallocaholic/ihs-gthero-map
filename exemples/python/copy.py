#!/usr/bin/python3

import os, sys, time
from fcntl import ioctl

# ioctl commands defined at the pci driver
RD_SWITCHES   = 24929
RD_PBUTTONS   = 24930
WR_L_DISPLAY  = 24931
WR_R_DISPLAY  = 24932
WR_RED_LEDS   = 24933
WR_GREEN_LEDS = 24934

def main():
    if len(sys.argv) < 2:
        print("Error: expected more command line arguments")
        print("Syntax: %s </dev/device_file>"%sys.argv[0])
        exit(1)

    fd = os.open(sys.argv[1], os.O_RDWR)

    # data to write
    data = 0x40404040;
    ioctl(fd, WR_R_DISPLAY)
    retval = os.write(fd, data.to_bytes(4, 'little'))
    print("wrote %d bytes"%retval)

    # data to write
    data = 0x40404040;
    ioctl(fd, WR_L_DISPLAY)
    retval = os.write(fd, data.to_bytes(4, 'little'))
    print("wrote %d bytes"%retval)

    # data to write
    data = 0x00000000;
    ioctl(fd, WR_GREEN_LEDS)
    retval = os.write(fd, data.to_bytes(4, 'little'))
    print("wrote %d bytes"%retval)

    # data to write
    data = 0x00000000;
    ioctl(fd, WR_RED_LEDS)
    retval = os.write(fd, data.to_bytes(4, 'little'))
    print("wrote %d bytes"%retval)

    # 
    ioctl(fd, RD_SWITCHES)
    switch = os.read(fd, 4);
    print("Switch: 0x%X"%int.from_bytes(switch, 'little'))
    
    ioctl(fd, RD_PBUTTONS)
    button = os.read(fd, 4);
    print("0x%X"%int.from_bytes(button, 'little'))

    os.close(fd)

if __name__ == '__main__':
    main()

