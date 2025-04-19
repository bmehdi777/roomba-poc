import serial
import time

def main():
    ser = serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=0.5)

    print(ser.name)

    start = bytearray([128])
    ser.write(start)
    print('Starting...')

    time.sleep(0.25)

    # no restrictions 
    fullmode = bytearray([132])
    ser.write(fullmode)

    time.sleep(2)

    go = bytearray([137, 0,100,0,0])
    ser.write(go)
    print('Driving...')

    time.sleep(5)

    print('Stop')
    stop = bytearray([173])
    ser.write(stop)

    ser.close()


if __name__ == "__main__":
    main()
