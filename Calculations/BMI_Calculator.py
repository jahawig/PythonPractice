weight = float(input("What is your weight (pounds): "))
height = float(input("What is your height (inches): "))
BMI = 703 * weight / (height * height)


# Want to calculate how much weight you have to lose to move up/down a BMI bracket
def weight_change(original_weight, constant_height, target_BMI):
    new_weight = target_BMI * (constant_height * constant_height) / 703
    change_in_weight = abs(original_weight - new_weight)
    return change_in_weight


print("Hello, thank you for inputting your information, your BMI is: " + str(BMI))
if BMI < 16:
    print("Your BMI lands in the Severely Underweight range (0-16)")
    print("To get to the Underweight BMI range, you need to gain " + str(weight_change(weight, height, 16)) + " pounds.")
    print("To get to the Normal range, you need to gain " + str(weight_change(weight, height, 25)) + " pounds.")
    print("Here is a link with some resources on how you can raise your BMI.")
elif BMI < 18.5:
    print("You BMI lands in the Underweight range (16-18.5)")
    print("To get to the Normal range, you need to gain " + str(weight_change(weight, height, 25)) + " pounds.")
    print("Here is a link with some resources on how you can raise your BMI.")
elif BMI < 25:
    print("Your BMI lands in the normal range (18.5-25).")
    print("Keep it up!")
elif BMI < 30:
    print("Your BMI lands in the Overweight range (25-30).")
    print("To get to the Normal range, you need to lose " + str(weight_change(weight, height, 25)) + " pounds.")
    print("Here is a link with some resources on how you can lower your BMI.")
elif BMI > 30:
    print("Your BMI lands in the obese range (30+).")
    print("To get to the Overweight BMI range, you need to lose " + str(weight_change(weight,height,30)) + " pounds.")
    print("To get to the Normal range, you need to lose " + str(weight_change(weight, height, 25)) + " pounds.")
    print("Here is a link with some resources that can help lower your BMI.")
