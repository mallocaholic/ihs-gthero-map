#!/usr/bin/python3

import os, sys
from fcntl import ioctl

# ioctl commands defined at the pci driver
RD_SWITCHES   = 24929
RD_PBUTTONS   = 24930
WR_L_DISPLAY  = 24931
WR_R_DISPLAY  = 24932
WR_RED_LEDS   = 24933
WR_GREEN_LEDS = 24934

mapping = {'0': '40', '1': '79', '2': '24', '3': '30', '4': '19', '5': '12', '6': '02', '7': '78', '8': '00', '9': '10'}

def retSS(val):
	val_str = str(val)
	str_emp = ""

	for number in val_str:
		str_emp += mapping[number] 

	while(len(str_emp) < 8):
		str_emp = mapping['0'] + str_emp

	return int(str_emp, 16)


def main():
    if len(sys.argv) < 2:
        print("Error: expected more command line arguments")
        print("Syntax: %s </dev/device_file>"%sys.argv[0])
        exit(1)

    fd = os.open(sys.argv[1], os.O_RDWR)

    # data to write
    data = retSS(int(input()))
    # data = hex(int_data)
    print(data)
    ioctl(fd, WR_R_DISPLAY)
    retval = os.write(fd, data.to_bytes(4, 'little'))
    print("wrote %d bytes"%retval)

    # data to write
    # data = 0xFFFFFFFF;
    # ioctl(fd, WR_RED_LEDS)
    # retval = os.write(fd, data.to_bytes(4, 'little'))
    # print("wrote %d bytes"%retval)

    os.close(fd)

if __name__ == '__main__':
    main()