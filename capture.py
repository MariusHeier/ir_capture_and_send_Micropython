import utime
from machine import Pin


def get_binary():
    try:
        num1s = 0
        binary = 1
        command = []
        previous_value = 1
        ir_input = Pin(21, Pin.IN)

        while ir_input.value():
            value = ir_input.value()
            start_time = utime.ticks_us() 

        while True:
            if previous_value != value:
                now = utime.ticks_us()
                pulse_time = utime.ticks_diff(now, start_time)
                start_time = now
                command.append((previous_value, pulse_time))
            previous_value = value
            value = ir_input.value()
            if value:
                num1s += 1
            else:
                num1s = 0
            if num1s > 1000:
                break
        if len(command) > 10:
            for (typ, tme) in command:
                if typ == 1:
                    if tme > 1000:
                        binary = binary * 10 +1
                    else:
                        binary *= 10
            print(binary)
        return binary
    except Exception as e:
        print(e)
        return None

def convert_hex(binary_value):
    tmpB2 = int(str(binary_value), 2)
    return hex(tmpB2)

while True:
    binary_data = get_binary()
    
    if binary_data:        
        if len(str(binary_data)) > 10:
            hex_data = convert_hex(binary_data)
            print("Hex:", hex_data)
            print("Binary:", binary_data)
            print("Binary length:",len(str(binary_data)))
            print("\n")
