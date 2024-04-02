# insurance-cost-calculator

def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
    print(f"The estimated insurance cost for {name} is {estimated_cost} dollars")
    return estimated_cost


def get_user_input():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    sex = int(input("Enter your sex (0 for female, 1 for male): "))
    bmi = float(input("Enter your BMI: "))
    num_of_children = int(input("Enter the number of children: "))
    smoker = int(input("Are you a smoker? (0 for non-smoker, 1 for smoker): "))
    return name, age, sex, bmi, num_of_children, smoker


def convert_currency(amount, from_currency, to_currency, requests=None):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    rate = float(data[to_currency])
    return amount * rate


def main():
    print("Welcome to the Insurance Cost Calculator!")
    name, age, sex, bmi, num_of_children, smoker = get_user_input()
    calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker)



if __name__ == "__main__":
    main()