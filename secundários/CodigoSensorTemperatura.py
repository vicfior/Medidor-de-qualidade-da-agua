import serial

port = 'COM3'  
baud_rate = 9600 

ser = serial.Serial(port, baud_rate, timeout=0.5)

try:
    while True:
        line = ser.readline().strip()
        try:
            temperature = int(line)  
            print('Temperatura: {}ºC'.format(temperature))
        except ValueError:
            print('Dados inválidos recebidos: {}'.format(line))
except KeyboardInterrupt:
    ser.close()
