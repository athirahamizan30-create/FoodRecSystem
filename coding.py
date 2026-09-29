food_data = {  #list of food based on category, spiciness level and average price in Cyberjaya (survey area)
    "Malay": [
        {"food": "Nasi Lemak Ayam", "spiciness": "spicy",  "price": 10.00},
        {"food": "Mee Goreng Mamak", "spiciness": "spicy",  "price": 9.00},
        {"food": "Nasi Goreng Kampung", "spiciness": "spicy",  "price": 9.00},
        {"food": "Laksa Johor", "spiciness": "spicy",  "price": 12.00},
        {"food": "Nasi Kerabu", "spiciness": "spicy",  "price": 12.00},
        {"food": "Nasi Ayam Penyet", "spiciness": "spicy", "price": 9.00},
        {"food": "Nasi Dagang", "spiciness": "non-spicy", "price": 10.00},
        {"food": "Nasi Minyak Ayam", "spiciness": "non-spicy", "price": 11.00},
        {"food": "Mee Rebus", "spiciness": "non-spicy", "price": 8.00},
        {"food": "Lontong", "spiciness": "non-spicy", "price": 8.00}
    ],

    "Chinese": [
            {"food": "Sichuan Dan Dan Noodles", "spiciness": "spicy",  "price": 10.00},
            {"food": "Spicy Beef Noodles", "spiciness": "spicy",  "price": 9.00},
            {"food": "Mala Fried Rice", "spiciness": "spicy",  "price": 9.00},
            {"food": "Kung Pao Chicken Rice", "spiciness": "spicy",  "price": 12.00},
            {"food": "Spicy Sichuan Chicken Rice", "spiciness": "spicy",  "price": 12.00},
            {"food": "Hainanese Chicken Rice", "spiciness": "non-spicy", "price": 9.00},
            {"food": "Char Siew Rice", "spiciness": "non-spicy", "price": 10.00},
            {"food": "Wantan Mee", "spiciness": "non-spicy", "price": 11.00},
            {"food": "Fried Rice with Egg", "spiciness": "non-spicy", "price": 8.00},
            {"food": "Beef Hor Fun", "spiciness": "non-spicy", "price": 8.00}
        ],

    "Indian": [
            {"food": "Chicken Biryani", "spiciness": "spicy",  "price": 13.00},
            {"food": "Chicken Curry Rice", "spiciness": "spicy",  "price": 12.00},
            {"food": "Fish Curry Rice", "spiciness": "spicy",  "price": 12.00},
            {"food": "Mutton Biryani", "spiciness": "spicy",  "price": 16.00},
            {"food": "Chicken Masala Rice", "spiciness": "spicy",  "price": 13.00},
            {"food": "Chicken Tandoori with Naan", "spiciness": "non-spicy", "price": 15.00},
            {"food": "Roti Canai with Dhal", "spiciness": "non-spicy", "price": 5.00},
            {"food": "Cheese Naan with Chicken Tikka", "spiciness": "non-spicy", "price": 15.00},
            {"food": "Masala Dosa", "spiciness": "non-spicy", "price": 8.00},
            {"food": "Vegetable Biryani", "spiciness": "non-spicy", "price": 10.00}
        ],

    "Korean": [
        {"food": "Soondubu Jjigae (Spicy Soft Tofu Stew)", "spiciness": "spicy", "price": 25.00},
        {"food": "Tteokbokki (Spicy Rice Cakes)", "spiciness": "spicy", "price": 21.00},
        {"food": "Dakgalbi (Spicy Stir-Fried Chicken)", "spiciness": "spicy", "price": 28.50},
        {"food": "Kimchi Bokkeumbap (Kimchi Fried Rice)", "spiciness": "spicy", "price": 21.00},
        {"food": "Bibimbap (Mixed Rice Bowl)", "spiciness": "non-spicy", "price": 25.50},
        {"food": "Bulgogi Rice Sets (Marinated Beef/Chicken)", "spiciness": "non-spicy", "price": 26.50},
        {"food": "Japchae (Stir-Fried Glass Noodles)", "spiciness": "non-spicy", "price": 19.00},
        {"food": "Kimbap (Korean Seaweed Rice Rolls)", "spiciness": "non-spicy", "price": 16.50},
        {"food": "Korean Fried Chicken (Soy Garlic / Honey Butter)", "spiciness": "non-spicy", "price": 22.50},
        {"food": "Korean Fried Chicken (Large Sharing Platter)", "spiciness": "non-spicy", "price": 50.00},
        {"food": "Korean Burgers (Modern Fusion)", "spiciness": "non-spicy", "price": 18.50}
    ],

    "Japanese": [
        {"food": "Creamy Salmon Mentai Pasta", "spiciness": "spicy", "price": 28.00},
        {"food": "Takoyaki", "spiciness": "non-spicy", "price": 10.50},
        {"food": "Salmon Mentai Sushi", "spiciness": "non-spicy", "price": 6.40},
        {"food": "Chicken Katsu Curry Don", "spiciness": "non-spicy", "price": 22.00},
        {"food": "Gyudon (Mangkuk Daging Lembu)", "spiciness": "non-spicy", "price": 20.00},
        {"food": "Chicken Teriyaki Bento", "spiciness": "non-spicy", "price": 26.00},
        {"food": "California Roll", "spiciness": "non-spicy", "price": 15.00},
        {"food": "Salmon Poke Bowl", "spiciness": "non-spicy", "price": 28.00},
        {"food": "Sushi (Set)", "spiciness": "non-spicy", "price": 18.00},
        {"food": "Tori Paitan Ramen", "spiciness": "non-spicy", "price": 24.00},
        {"food": "Beef Nabeyaki Udon", "spiciness": "non-spicy", "price": 22.50},
        {"food": "Okonomiyaki", "spiciness": "non-spicy", "price": 18.50}
    ],

    "Western": [
        {"food": "Spicy Seafood Aglio Olio", "spiciness": "spicy", "price": 24.00},
        {"food": "Buffalo Chicken Wings", "spiciness": "spicy", "price": 17.00},
        {"food": "Big Breakfast", "spiciness": "non-spicy", "price": 23.00},
        {"food": "Egg Benedict", "spiciness": "non-spicy", "price": 20.00},
        {"food": "Croissant Sandwich", "spiciness": "non-spicy", "price": 18.50},
        {"food": "Grilled Chicken Chop", "spiciness": "non-spicy", "price": 20.00},
        {"food": "Beef Burger / Crispy Chicken Burger", "spiciness": "non-spicy", "price": 18.00},
        {"food": "Fish & Chips", "spiciness": "non-spicy", "price": 22.00},
        {"food": "Ribeye / Striploin Beef Steak", "spiciness": "non-spicy", "price": 65.00},
        {"food": "Carbonara Pasta", "spiciness": "non-spicy", "price": 23.00},
        {"food": "Beef Lasagna", "spiciness": "non-spicy", "price": 24.00}
    ]
}

def intro (): #introduction to the system function
    print ("=" * 60)
    print ("               FOOD RECOMMENDATION SYSTEM ")
    print ("=" * 60)
    print ()
    print ("Welcome!")
    print ("Let's help you find something delicious.")
    print ()

def choose_cuisine ():  #function to choose cuisine
    print ("Choose your cuisine:")
    print ()
    print ("    1 → Malay")
    print ("    2 → Chinese")
    print ("    3 → Indian")
    print ("    4 → Western")
    print ("    5 → Korean")
    print ("    6 → Japanese")
    print ()
    print ()
    cuisine = {
        1:"Malay",
        2:"Chinese",
        3:"Indian",
        4:"Western",
        5:"Korean",
        6:"Japanese"
        }
    while True:
        item1 = input("\nCuisine (Enter number 1-6): ")

        if item1.isdigit():
            item1 =int(item1)

            if 1 <= item1 <= len(cuisine):  #only accept input 1-6 for cuisine selection
                choice = cuisine.get(item1)
                print()
                print (f"✓ *{choice}* cuisine selected!")
                print ()
                return choice
            else:
                print ("Invalid input! Please enter the number within the range") #if the input is not within the range of 1-6
        else:
            print ("Invalid input! Please enter a number.")

def choose_spiciness ():  #function to choose spiciness level
    print ("-" * 60)
    print ("                  CHOOSE YOUR SPICY LEVEL")
    print ("-" * 60)
    print ()
    print ("    1 → Spicy")
    print ("    2 → Non-Spicy") 
    print ()
    spiciness = {
        1:"spicy",
        2:"non-spicy"
    }

    while True:
        item2 = input("\nSpiciness (Enter number 1/2): ")
        print ()

        if item2.isdigit():
            item2 = int(item2)

            if 1 <= item2 <= len(spiciness):                        #only accept input 1 or 2 for spiciness level
                spicy_level = spiciness.get(item2)                  #fetching the value of the key from the dictionary "spiciness"
                print (f"✓ Your spicy level is *{spicy_level}*")
                print ()
                return spicy_level

            else: 
                print("Invalid input! Please enter 1 or 2")         #if the input is not within the range of 1-2

        else:
            print ("Invalid input! Please enter 1 or 2")            #if the input is not a number

def set_budget ():                                                  #function to set budget based on the price range of the food in the system
    print ("-" * 60)
    print ("                     SET YOUR BUDGET")
    print ("-" * 60)
    print ()
    while True:
        try:
            budget = float(input("\nBudget (Enter your budget 5.00 - 65.00): "))

            if 5.00 <= budget <= 80.00:
                print ()
                print (f"✓ Your budget is *RM{budget:.2f}*.")
                print ()
                return budget
            else:
                print("\n*Out of range! Please enter your budget within the range.*")
        except ValueError:
            print("\n*Invalid Input! Please enter a valid input.*")

def rec_food (cuisine, budget, spicy_level):
    menu = food_data.get(cuisine, [])
    
    recommendations = []
    for item in menu:
        if item["spiciness"] == spicy_level and item["price"] <= budget:
            recommendations.append(item)
            
    return recommendations

def show_food_loop(user_cuisine, user_budget, user_spicy):          #function to show matching available food recommendation based on the user input
    matches = rec_food(user_cuisine, user_budget, user_spicy)
    
    if not matches:
        print("*No food matches your criteria. Try increasing your budget or changing preferences!*")
        print()
        rerun = input("Would you like to try again? (y/n): ").lower()

        if rerun == "no" or rerun =="n":
            print ("Thank you for using our system. Have a great day") 
            print()
            print ("=" * 60)
            print("                     THANK YOU")
            print ("=" * 60) 
            return "exit"

        return "retry"

    else:
        print("Recommended Options:")
        print ()
        for i, dish in enumerate(matches, start = 1):
            print(f"{i}. {dish['food']} - RM {dish['price']:.2f}")

        return matches
 
def price_loop(recommendations):                                #function to calculate the estimated price of the selected food recommendation (food price (subtotal), delivery fee, total price)
    while True:
        print()
        cal_price = input("Would you like to know the estimated price? (y/n): ").lower()
        print()

        if cal_price in ["no","n"]:
            print ("Thank you for using our system. Have a great day") 
            print()
            print ("=" * 60)
            print("                     THANK YOU")
            print ("=" * 60) 
            return "exit"

        elif cal_price in ["yes", "y"]:
            break

        else: 
            print ("Invalid input! Please enter 'y' or 'n' to continue")

    while True:
        foodnum = input ("Which meal would you like to have? (Enter a number) :")

        if foodnum.isdigit():
            index = int(foodnum) - 1
            if 0 <= index < len(recommendations):
                choice = recommendations[index]
                print()
                print(f"*You selected: {choice['food']} which costs RM {choice['price']:.2f}*")
                print()
                break

            else:
                print("Invalid choice number.")

        else:
            print("Please enter a valid number.")


    print ("-" * 60)
    print("                 CALCULATING ESTIMATED PRICE")
    print ("-" * 60)
    print (f"Subtotal : RM {choice['price']:.2f}")
    print ("Estimated Delivery Fee : RM 3.00")
    print (f"Total price : RM {choice['price']+3:.2f}")

    while True:
        print()
        cal_price = input("Would you like to know continue? (y/n): ").lower()

        if cal_price in ["no","n"]:
            print ()
            print ("Thank you for using our system. Have a great day") 
            print()
            print ("=" * 60)
            print("                     THANK YOU")
            print ("=" * 60)
            return "exit"

        elif cal_price in ["yes", "y"]:
            return "retry"

        else: 
            print ("Invalid input! Please enter 'y' or 'n' to continue")
        

while True:
    intro ()

    user_cuisine = choose_cuisine()
    user_spicy = choose_spiciness()
    user_budget = set_budget()

    matches = show_food_loop(user_cuisine, user_budget, user_spicy)
    
    if matches == "exit":
        break  
    elif matches == "retry":
        continue 

    rerun2 = price_loop(recommendations=matches)
    if rerun2 == "exit":
        break
    elif rerun2 == "retry":
        continue
        



