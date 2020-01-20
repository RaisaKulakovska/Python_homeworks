# ----------------------Ex 1----------------------
def calculate_cost():
    """Calculate the cost of a car trip in both direction"""
    S=int(input("Enter a distance, km: "))
    amount_fuel_100km=int(input("Enter amount of fuel on 100km: ")) 
    price_1l=int(input("Enter a price of 1 liter of fuel, UA: "))

    cost=round(S/100*amount_fuel_100km*price_1l*2)
    print ("\nCost of your trip is",cost, "UA.\n")
# calculate_cost()

# ----------------------Ex 2----------------------
def show_holiday():     
    """Sow which holiday is in entered date"""     
    try:
        day=int(input("Enter a day (1....31): "))
        month=int(input("Enter a month (1....12): "))  
        if day==1 and month==1:
            print("It is a New Year!\n")
        elif day==7 and month==1:
            print("It is a Christmas!\n")
        elif day==7 and month==1:
            print("It is a Christmas!\n")
        elif day==28 and month==6:
            print("It is a Сonstitution day!\n")
        elif day==24 and month==8:
            print("It is an Independence day!\n")
        else:
            print("On this date a program hasn't any holiday...\n") 
    except ValueError:
        print("Invalid choice, enter a number.\n")
        exit
#show_holiday()

# ----------------------Ex 3----------------------
def speed():
    """Calculate a speed of sportsman"""
    try:
        S=int(input("enter a distanse, m: "))
        t=int(input("enter a time, s: "))
        v=round(S/t, 1)
        print("A speed of sportsman is", v, "m/s\n")
    except ValueError:
        print("Enter a number, please!\n")
#speed()

# ----------------------Ex 4----------------------
from random import randint
def game():
    """Play with dice, eatch player throws 2 dice, if they are the same, +2 points"""
    N = int(input("enter N (to which to whsch account the game lasts): \n"))
    plaing = True
    my_total_score = 0
    pc_total_score = 0
    while plaing:       
        input("Your turn:")
        rand_my_1 = randint(1, 6)
        rand_my_2 = randint(1, 6)
        print(rand_my_1)    
        print(rand_my_2)
        my_score = rand_my_1 + rand_my_2
        if rand_my_1 == rand_my_2:
            my_total_score += 2
            print("Double! Your got +2 points")           
        input("PC turn")
        rand_pc_1 = randint(1, 6)
        print(rand_pc_1)
        rand_pc_2 = randint(1, 6)
        print(rand_pc_2)
        pc_score = rand_pc_1 + rand_pc_2
        if rand_pc_1 == rand_pc_2:
            pc_total_score += 2
            print("Double! Computer got +2 points")        
        
        if my_score > pc_score:
            my_total_score +=1
        elif pc_score > my_score:
            pc_total_score +=1
        print("Total score: Your:",my_total_score, " PC:", pc_total_score, "\n")

        if my_total_score >= N or pc_total_score >= N:
            plaing = False
            if my_total_score > pc_total_score:
                print("You win!\n")    
            elif pc_total_score > my_total_score:
                print("Computer win!\n")
            elif my_total_score == pc_total_score:
                print("Dead heat!\n")
game()

