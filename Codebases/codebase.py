# No.88
#Electricity-Bill-Calculator

#Energy counsumer units
def calculate_energy_charge(units):
    if units <= 100:
        return units * 3
    elif units <= 200:
        return 100 * 3 + (units - 100) * 5
    else:
        return 100 * 3 + 100 * 5 + (units - 200) * 8


def generate_bill(name, units):
    energy = calculate_energy_charge(units)
    fixed = 50
    tax = (energy + fixed) * 0.05
    total = energy + fixed + tax

    print("----- ELECTRICITY BILL -----")
    print("Consumer:", name)
    print("Units   :", units)
    print(f"Energy: {energy:.2f} | Fixed: {fixed:.2f} | Tax: {tax:.2f}")
    print(f"Total Bill: {total:.2f}")


name = input("Consumer name: ")

while True:
    try:
        units = float(input("Units consumed: "))
        if units >= 0:
            break
    except ValueError:
        pass
    print("Invalid units. Enter a non-negative number.")

generate_bill(name, units)