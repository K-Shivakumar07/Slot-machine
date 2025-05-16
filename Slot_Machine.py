#Python Slot Machine Game
import random

def spin_row():
    symbols = ["🍒","🍓","🍑","🍊","🍋"]
    
    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("****************")
    print(" | ".join(row))
    print("****************")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍓":
            return bet * 4
        elif row[0] == "🍑":
            return bet * 5
        elif row[0] == "🍊":
            return bet * 6
        elif row[0] == "🍋":
            return bet * 7
        
    return 0       

def main():
    balance = 100
    
    print("****************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒  🍓 🍑 🍊 🍋")
    print("****************")
    
    
    while balance > 0:
        print(f"Current balnace : ${balance}")
        
        bet = input("Enter your bet amount: $")
        
        if not bet.isdigit():
            print("Invalid bet amount. Please enter a number.")
            continue
        
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient balance. Please enter a valid bet amount.")
            continue
        elif bet <= 0:
            print("Bet amount must be greater than 0")
            continue
        
        balance -= bet
        
        row = spin_row()
        print("Spinning...\n")
        print_row(row)
        
        payout = get_payout(row, bet)
        
   
        
        if payout > 0:
            print("Congratulations!")
            print(f"You won ${payout}! Your new balance is ${balance + payout}")
            
            
        else:
            print(f"You lost ${bet}. Your new balance is ${balance}")
            
        balance += payout
        
        play_again = input("Do you want to play again? (Y/N): ").upper()
        print("---------------------------------------")
        
        if play_again != "Y":
            print("***** Thank You for playing *****")
            break
            
        
    
if __name__ == "__main__":
    main()