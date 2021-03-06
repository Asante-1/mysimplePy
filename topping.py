def top():
    print("Please enter your requested topping(s)")
    print("Please enter the toppings one at a time. ")

    num = int(input("Please enter the number of requested toppings you're about to add :"))

    k = 0
    requested_topping = []
    while k < num:

        topping = input("enter your topping:")

        requested_topping.append(topping)
        k += 1
    return requested_topping

x = top()
available_topppings = ['mushrooms', 'pepper', 'pepperoni', 'extra cheese']
for i in x:
    if i in available_topppings:
        print("\nwe are adding ", i , "in your pizza")
    else:
        print('\nOoops, we are out of ', i)
print('finished making your pizza')


