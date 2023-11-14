import serial

# Configurar a porta serial
ser = serial.Serial('COM3', 9600) 

try:
    while True:
        line = ser.readline().strip()
        if line.startswith("pH Val: "):
            try:
                ph_value = float(line.split(":")[1].strip())
                print("Valor de pH: %.2f" % ph_value)
            except ValueError:
                print("Valor de pH não pôde ser convertido para float:", line)
        else:
            print("Linha inesperada:", line)
except KeyboardInterrupt:
    ser.close()
