import random
cards = "Diamonds", "Spades", "Heart", "Clubs" #declaring my card types
numbers = 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace" #declaring my card numbers/special cards

def card_Pick(): #my function to do everything so I can just print out the fuction 
    card = random.choices (cards)
    number = random.choices (numbers)
    
    return(f"The {number} of {card}" )

print(card_Pick()) #Giving the person their result