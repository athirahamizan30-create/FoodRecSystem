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

intro ()
choose_cuisine ()