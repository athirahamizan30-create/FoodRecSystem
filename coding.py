def intro ():
    print ("=" * 60)
    print ("               FOOD RECOMMENDATION SYSTEM ")
    print ("=" * 60)
    print ()
    print ("Welcome!")
    print ("Let's help you find something delicious.")
    print ()

def choose_cuisine ():
    print ("Choose your cuisine:")
    print ()
    print ("    1 → Malay")
    print ("    2 → Chinese")
    print ("    3 → Indian")
    print ("    4 → Western")
    print ("    5 → Korean")
    print ("    6 → Japanese")
    print ()
    item1 = input("\nCuisine (Enter number 1-6): ")
    print ()
    cuisine = {
        "1":"Malay",
        "2":"Chinese",
        "3":"Indian",
        "4":"Western",
        "5":"Korean",
        "6":"Japanese"
        }
    choice = cuisine.get(item1)
    print (f"✓ *{choice}* cuisine selected!")
    print ()

def choose_spiciness ():
    print ("-" * 60)
    print ("                  CHOOSE YOUR SPICY LEVEL")
    print ("-" * 60)
    print ()
    print ("    1 → Spicy")
    print ("    2 → Non-Spicy") 
    print ()
    item2 = input("\nSpiciness (Enter number 1/2): ")
    print ()
    spiciness = {
        "1":"spicy",
        "2":"non-spicy"
    }
    spicy_level = spiciness.get(item2)
    print (f"✓ Your spicy level is *{spicy_level}*")
    print ()

def set_budget ():
    print ("-" * 60)
    print ("                     SET YOUR BUDGET")
    print ("-" * 60)
    print ()
    budget = input("\nBudget (Enter your budget 5.00 - 40.00): ")
    print ()
    print (f"✓ Your budget is *{budget}*.")
    print ()

intro ()
choose_cuisine ()
choose_spiciness ()
set_budget ()