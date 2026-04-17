# ============================================================
#         🌡️  INTERACTIVE TEMPERATURE CONVERTER 🌡️
#              Built with Python | Beginner Friendly
# ============================================================

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def get_temperature_category(celsius):
    """Return a category and fun message based on Celsius temperature."""
    if celsius <= 0:
        return "🥶 Freezing", "Bundle up! It's freezing out there!"
    elif celsius <= 10:
        return "❄️  Very Cold", "Wear a heavy coat — it's bitterly cold!"
    elif celsius <= 18:
        return "🌬️  Cold", "A jacket is definitely recommended."
    elif celsius <= 25:
        return "😊  Comfortable", "Perfect weather — enjoy your day!"
    elif celsius <= 32:
        return "☀️  Warm", "Nice and warm outside. Stay comfortable!"
    elif celsius <= 40:
        return "🔥  Hot", "Stay hydrated and wear sunscreen! 🥵"
    else:
        return "🌋  Extremely Hot", "Danger zone! Avoid going out if possible! 🚨"


def print_banner():
    """Print the welcome banner."""
    print("\n" + "=" * 55)
    print("       🌡️   TEMPERATURE CONVERTER PROGRAM   🌡️")
    print("=" * 55)
    print("   Convert temperatures between Celsius & Fahrenheit")
    print("=" * 55)


def print_menu():
    """Display the main conversion menu."""
    print("\n┌─────────────────────────────────────┐")
    print("│         CHOOSE CONVERSION TYPE       │")
    print("├─────────────────────────────────────┤")
    print("│  1️⃣   Celsius  ➡️  Fahrenheit         │")
    print("│  2️⃣   Fahrenheit  ➡️  Celsius          │")
    print("│  3️⃣   Exit Program                   │")
    print("└─────────────────────────────────────┘")


def get_numeric_input(prompt):
    """Prompt user for a numeric temperature value with error handling."""
    while True:
        user_input = input(prompt).strip()
        try:
            value = float(user_input)
            return value
        except ValueError:
            print(f"\n  ⚠️  Oops! '{user_input}' is not a valid number.")
            print("  👉 Please enter a numeric value (e.g., 25 or -10.5)\n")


def get_menu_choice():
    """Prompt user for a menu option with validation."""
    while True:
        choice = input("\n  👉 Enter your choice (1 / 2 / 3): ").strip()
        if choice in ("1", "2", "3"):
            return choice
        else:
            print(f"\n  ⚠️  '{choice}' is not a valid option.")
            print("  👉 Please enter 1, 2, or 3.")


def display_result(original_value, original_unit, converted_value, converted_unit):
    """Display the conversion result in a formatted box."""
    # Determine Celsius value for category
    if original_unit == "°C":
        celsius_val = original_value
    else:
        celsius_val = fahrenheit_to_celsius(original_value)

    category, message = get_temperature_category(celsius_val)

    print("\n" + "─" * 45)
    print("   📊  TEMPERATURE CONVERSION RESULT")
    print("─" * 45)
    print(f"   Input   :  {original_value:.2f}{original_unit}")
    print(f"   Output  :  {converted_value:.2f}{converted_unit}")
    print()
    print(f"   ✅  {original_value:.1f}{original_unit} = {converted_value:.2f}{converted_unit}")
    print()
    print(f"   🌡️  Category  :  {category}")
    print(f"   💬  Tip       :  {message}")
    print("─" * 45)


def ask_continue():
    """Ask the user if they want to perform another conversion."""
    while True:
        again = input("\n  🔄  Do you want to convert another temperature? (yes / no): ").strip().lower()
        if again in ("yes", "y"):
            return True
        elif again in ("no", "n"):
            return False
        else:
            print("  ⚠️  Please type 'yes' or 'no'.")


def main():
    """Main program loop."""
    print_banner()
    print("\n  Welcome! Let's convert some temperatures. 🌍")

    while True:
        print_menu()
        choice = get_menu_choice()

        if choice == "1":
            print("\n  🌡️  CELSIUS → FAHRENHEIT")
            temp = get_numeric_input("  Enter temperature in Celsius (°C): ")
            result = celsius_to_fahrenheit(temp)
            display_result(temp, "°C", result, "°F")

        elif choice == "2":
            print("\n  🌡️  FAHRENHEIT → CELSIUS")
            temp = get_numeric_input("  Enter temperature in Fahrenheit (°F): ")
            result = fahrenheit_to_celsius(temp)
            display_result(temp, "°F", result, "°C")

        elif choice == "3":
            print("\n" + "=" * 55)
            print("   👋  Thanks for using the Temperature Converter!")
            print("   🌤️  Stay comfortable out there. Goodbye!")
            print("=" * 55 + "\n")
            break

        if choice in ("1", "2"):
            if not ask_continue():
                print("\n" + "=" * 55)
                print("   👋  Thanks for using the Temperature Converter!")
                print("   🌤️  Stay comfortable out there. Goodbye!")
                print("=" * 55 + "\n")
                break


# ── Entry Point ──────────────────────────────────────────────
if __name__ == "__main__":
    main()
