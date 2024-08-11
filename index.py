def calculate_bmi(weight, height):
    return weight / (height ** 2)

def categorize_bmi(bmi):
    if bmi < 16:
        return "Severely underweight", "Consider consulting a healthcare provider."
    elif 16 <= bmi < 18.5:
        return "Underweight", "A balanced diet and exercise may help."
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "Maintain your current lifestyle."
    elif 25 <= bmi < 29.9:
        return "Overweight", "A balanced diet and regular exercise are recommended."
    elif 30 <= bmi < 34.9:
        return "Obesity Class I", "Consult a healthcare provider for advice."
    elif 35 <= bmi < 39.9:
        return "Obesity Class II", "Professional medical guidance is advised."
    else:
        return "Obesity Class III (Morbid Obesity)", "Immediate medical intervention may be required."

def convert_height_to_meters(height_ft_in):
    feet, inches = map(float, height_ft_in.split('-'))
    height_in_meters = feet * 0.3048 + inches * 0.0254
    return height_in_meters

def main():
    while True:
        print("<----------- BMI Calculator ----------->\n")
        try:
            weight = float(input("Please enter your weight in kilograms: "))
            height_ft_in = input("\nPlease enter your height in feet-inches format (e.g., 5-8): ")

            if weight <= 0 or not height_ft_in:
                print("Weight must be positive, and height must be provided.")
                continue

            height = convert_height_to_meters(height_ft_in)
            bmi = calculate_bmi(weight, height)
            category, advice = categorize_bmi(bmi)

            print(f"\nYour BMI is: {bmi:.2f}")
            print(f"\nThis is considered: {category}")
            print(f"\nAdvice: {advice}")

        except ValueError:
            print("\nInvalid input! Please enter numeric values for weight and a valid height format.")

        choice = input("\nWould you like to calculate again? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("\nExiting the BMI Calculator. Stay healthy!\n")
            break

if __name__ == "__main__":
    main()
