def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("Celsius|Fahrenheit")
    print("__________________")
    print("                  ")

    for celsius in range(0, 101, 10):
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(celsius, "    |    ", fahrenheit)

main()
