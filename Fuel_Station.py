def fuel_station(choice_1, choice_1_1, choice_1_2, choice_2, choice_3, choice):
    global liter
    print('Welcome to our station!')
    if choice == choice_1.lower():
        Fuel_choice_f = input("\nWhich is your typr of petrol?\n")
        if Fuel_choice_f == choice_1_1.lower():  
            liter = int(input("\nHow much liter do you want?\n "))
            print(f"\nIt will be you cost {520 * liter}:")
        if Fuel_choice_f == choice_1_2.lower():  
            liter = int(input("\nHow much liter do you want?\n "))
            print(f"\nIt will be you cost {490 * liter}:")
    if choice == choice_2.lower():
        liter = int(input("\nHow much liter do you want?\n "))
        print(f"\nIt will be you cost {400 * liter}:")
    if choice == choice_3.lower():
        liter = int(input("\nHow much liter do you want?\n "))
        print(f"\nIt will be you cost {350 * liter}:")


choice_1 = "Fuel"
choice_1_1 = "Premium"
choice_1_2 = "Regular"
choice_2 = "Gas"
choice_3 = "Diesel"
choice = input('\nWhich is your typr of Fuel?\n')
fuel_station(choice_1, choice_1_1, choice_1_2, choice_2, choice_3, choice)

def your_choice(fuel_storage,budget, choice_1,choice_1_1, choice_1_2, choice_2, choice_3, choice):
    second_choice = input("\nDo you want to pour in your car.\n")
    if second_choice == "Yes".lower():
        if choice == choice_1.lower():
            if Fuel_choice_f == choice_1_1.lower():
                budget += 520 * liter 
                fuel_storage -= liter
                print(f"Our budget is equal to {budget}")
                print(f"fuel storage's reserve is equal to {fuel_storage}")
            if Fuel_choice_f == choice_1_2.lower():
                budget += 520 * liter 
                fuel_storage -= liter
                print(f"Our budget is equal to {budget}")
                print(f"fuel storage's reserve is equal to {fuel_storage}")
        if choice == choice_2.lower():
            budget += 400 * liter
            fuel_storage -= liter
            print(f"Our budget is equal to {budget}")
            print(f"fuel storage's reserve is equal to {fuel_storage}")
        if choice == choice_3.lower():
            budget += 350 * liter
            fuel_storage -= liter
            print(f"Our budget is equal to {budget}")
            print(f"fuel storage's reserve is equal to {fuel_storage}")
        print("Your car's tank is full.")
    elif second_choice == "No".lower():
        print("Please exit the zone of station.")
    else:
        print("Wrong command. Try again.")

fuel_storage = 100
budget = 0
your_choice(fuel_storage,budget, choice_1,choice_1_1, choice_1_2, choice_2, choice_3, choice)
