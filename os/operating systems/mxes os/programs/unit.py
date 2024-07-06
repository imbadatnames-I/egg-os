end=False
CONVERSIONS = {
"length": {
    "m_to_km": 0.001,
    "km_to_m": 1000,
    "cm_to_m": 0.01,
    "m_to_cm": 100,
    "ft_to_m": 0.3048,
    "m_to_ft": 3.28084,
},
"weight": {
    "kg_to_g": 1000,
    "g_to_kg": 0.001,
    "lb_to_kg": 0.453592,
    "kg_to_lb": 2.20462,
},
"temperature": {
    "c_to_f": lambda c: c * 9/5 + 32,  # Corrected formula
    "f_to_c": lambda f: (f - 32) * 5/9,
},
}
def display_menu():
    print("> Unit Converter")
    print("> Select a conversion type:")
    print("> 1. Length")
    print("> 2. Weight")
    print("> 3. Temperature")
    print("> 4. Exit")
def convert_length():
    # Display conversion options for length
    print("> Length Conversion")
    print("> Choose an option:")
    print("> 1. Meters to Kilometers")
    print("> 2. Kilometers to Meters")
    print("> 3. Centimeters to Meters")
    print("> 4. Meters to Centimeters")
    print("> 5. Feet to Meters")
    print("> 6. Meters to Feet")
    
    # Validate user choice and the value to convert
    try:
        choice = int(input("> Enter your choice (1-6): \n> "))
        if not 1 <= choice <= 6:
            raise ValueError("Invalid choice.")
        value = float(input("> Enter the value to convert: \n> "))
    except ValueError as e:
        print(f"> Error: {e}")
        return
    
    # Perform conversion based on user choice
    CONVERSIONS = {
        1: value * CONVERSIONS["length"]["m_to_km"],
        2: value * CONVERSIONS["length"]["km_to_m"],
        3: value * CONVERSIONS["length"]["cm_to_m"],
        4: value * CONVERSIONS["length"]["m_to_cm"],
        5: value * CONVERSIONS["length"]["ft_to_m"],
        6: value * CONVERSIONS["length"]["m_to_ft"],
    }
    
    # Display the converted value
    result = CONVERSIONS.get(choice)
    if result:
        print(f"> Converted value: {result}")
    else:
        print("> Invalid choice.")
def convert_weight():
    # Display conversion options for weight
    print("> Weight Conversion")
    print("> Choose an option:")
    print("> 1. Kilograms to Grams")
    print("> 2. Grams to Kilograms")
    print("> 3. Pounds to Kilograms")
    print("> 4. Kilograms to Pounds")
    
    # Validate user choice and the value to convert
    try:
        choice = int(input("> Enter your choice (1-4): \n> "))
        if not 1 <= choice <= 4:
            raise ValueError("Invalid choice.")
        value = float(input("> Enter the value to convert: \n> "))
    except ValueError as e:
        print(f"> Error: {e}")
        return
    
    # Perform conversion based on user choice
    conversions = {
        1: value * CONVERSIONS["weight"]["kg_to_g"],
        2: value * CONVERSIONS["weight"]["g_to_kg"],
        3: value * CONVERSIONS["weight"]["lb_to_kg"],
        4: value * CONVERSIONS["weight"]["kg_to_lb"],
    }
    
    result = conversions.get(choice)
    if result:
        print(f"> Converted value: {result}")
    else:
        print("> Invalid choice.")
def convert_temperature():
    # Display conversion options for temperature
    print("> Temperature Conversion")
    print("> Choose an option:")
    print("> 1. Celsius to Fahrenheit")
    print("> 2. Fahrenheit to Celsius")
    
    # Validate user choice and the value to convert
    try:
        choice = int(input("> Enter your choice (1-2): \n> "))
        value = float(input("> Enter the value to convert: \n> "))
    except ValueError as e:
        print(f"> Error: {e}")
        return
    
    # Perform conversion based on user choice
    conversions = {
        1: CONVERSIONS["temperature"]["c_to_f"](value),
        2: CONVERSIONS["temperature"]["f_to_c"](value),
    }
    
    result = conversions.get(choice)
    if result:
        print(f"> Converted value: {result}")
    else:
        print("> Invalid choice.")
def main():
    while True:
        display_menu()  # Display the menu
        try:
            choice = int(input("> Choose an option: \n> "))  # Get user choice
            
            # Perform actions based on the choice
            if choice == 1:
                convert_length()  # Length conversions
            elif choice == 2:
                convert_weight()  # Weight conversions
            elif choice == 3:
                convert_temperature()  # Temperature conversions
            elif choice == 4:
                print("> Exiting the program.")
                exit()
            else:
                print("> Invalid choice. Try again.")
        except ValueError:
            print("> Please enter a valid number.")
while not end:
    main()  # Start the main loop