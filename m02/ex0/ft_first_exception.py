def check_temperature(temp_str: str) -> int:
    print(f"Testing temperature: {temp_str}")
    try:
        temp = (int)temp_str
    except:
        print(f"Error: '{temp_str}' is not a valid number\n")
    if temp >= 0 and temp <= 40:
        print(f"Temperature {temp}°C is perfect for plants!\n")
        return temp
    if temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        return temp
    if temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
        return temp
    

def test_temperature_input() -> None:
        print("Testing temperature: 25")
        check_temperature("25")
        print("Testing temperature: abc")
        check_temperature("abc")
        print("Testing temperature: 100")
        check_temperature("100")
        print("Testing temperature: -50")
        check_temperature("-50")
        print("All tests completed - program didn't crash!")


def __


