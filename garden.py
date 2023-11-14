roses = 5
dahlias = 3.80
tulips = 2.80
narcissus = 3
gladiolus = 2.50

flower_price = {}

flower_type = str(input())
flower_sum = int(input())
budget = int(input())

off = {}
up1 = {}

if flower_type == "roses":
    flower_price = roses * flower_sum

    if flower_sum > 80:
        discount = 0.10
        discounted_amount = flower_price * discount
        flower_price -= discounted_amount
elif flower_type == "dahlias":
    flower_price = dahlias * flower_sum

    if flower_sum > 90:
        discount = 0.15
        discounted_amount = flower_price * discount
        flower_price -= discounted_amount
elif flower_type == "tulips":
    flower_price = tulips * flower_sum

    if flower_sum > 80:
        discount = 0.15
        discounted_amount = flower_price * discount
        flower_price -= discounted_amount
elif flower_type == "narcissus":
    flower_price = narcissus * flower_sum

    if flower_sum < 120:
        discount = 0.15
        discounted_amount = flower_price * discount
        flower_price += discounted_amount
elif flower_type == "gladiolus":
    flower_price = gladiolus * flower_sum

    if flower_sum > 80:
        discount = 0.20
        discounted_amount = flower_price * discount
        flower_price += discounted_amount

leva_left = budget - flower_price
leva_needed = flower_price - budget

if flower_price < budget:
    print(f"Hey, you have a great garden with {flower_sum} {flower_type} and {leva_left} leva left.")
elif flower_price > budget:
    print(f"Not enough money, you need {leva_needed} leva more.")
