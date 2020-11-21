MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def select_coffee(coffee_type):
    water_use = MENU[coffee_type]["ingredients"]["water"]
    milk_use = MENU[coffee_type]["ingredients"]["milk"]
    coffee_use = MENU[coffee_type]["ingredients"]["coffee"]
    coffee_cost = MENU[coffee_type]["cost"]
    return [water_use, milk_use, coffee_use, coffee_cost]


def payment_process(quarter_num, dime_num, nickle_num, penny_num):
    payment_paid = quarter_num * 0.25 + dime_num * 0.1 + nickle_num * 0.05 + penny_num * 0.01
    if payment_paid >= coffee_detail[3]:
        payment_remain = round(payment_paid - coffee_detail[3], 2)
        return payment_remain
    else:
        return "payment_insufficent"


machine = True
water_remain = resources["water"]
milk_remain = resources["milk"]
coffee_remain = resources["coffee"]
total_payment = 0

while machine:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_type == "report":
        print(f"Water : {water_remain} ml, Milk: {milk_remain} ml, Coffee: {coffee_remain} g, Total sale: $ {total_payment}")
        machine = False
    elif coffee_type == "off":
        machine = False
    else:
        coffee_detail = select_coffee(coffee_type)
        if water_remain < coffee_detail[0] or milk_remain < coffee_detail[1] or coffee_remain < coffee_detail[2]:
            print("There is no enough resources.")
            machine = False
        else:
            print("Please insert coins.")
            quarter_num = int(input("How many quarters?: "))
            dime_num = int(input("How many dimes?: "))
            nickle_num = int(input("How many nickles?: "))
            penny_num = int(input("How many pennies?: "))

            change = payment_process(quarter_num, dime_num, nickle_num, penny_num)

            if change == "payment_insufficent":
                print("Sorry, there is no enough coins.")
            else:
                print(f"Here is your {coffee_type}, and change: {change}")

    water_remain = water_remain - coffee_detail[0]
    milk_remain = milk_remain - coffee_detail[1]
    coffee_remain = coffee_remain - coffee_detail[2]
    total_payment = total_payment + coffee_detail[3]