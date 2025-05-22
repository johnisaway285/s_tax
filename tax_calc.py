import re
# Main Program
def main():
    rate = None
    rate = rate_selection(rate)
    pretax = float(input("Pre-Tax Sale: $"))
    GST = pretax * rate
    Total_Price = pretax + GST
    print(f"Total price is ${Total_Price:.2f}, GST is {GST:.2f} and pre-tax is {pretax:.2f}")
# Province Selection, Different provinces have different GST/HST rates. For example: ON has a 13% HST while AB has a lower rate of 5%.
def rate_selection(r:float):
    while True:
        selection = input("Please select your province. For Ontario, select 1, For Atlantic provinces, select 2. For other provinces, select 3. ")
        if re.search(r"^[1-3]$",selection):
            break
        print("Wrong!")
    
    match selection:
        case "1":
            print("You've selected Ontario")
            return 0.13
        case "2":
            while True:
                ns=input("You've selected Atlantic Provinces, hmmm, there is a change in HST for Nova Scotia, is this a sale that occured in Nova Scotia?")
                if re.search(r"^[0-1]$",ns):
                    break
                print("No!")
            # NS changed their GST rate to 14% for sales on or after April 1, 2025
            if ns == "1":
                while True:
                    selection_2 = input("Is this a sale that happened after April 1, 2025? If yes, put 1 here, if not press 0 ") 
                    if selection_2 == "1":
                        return 0.14
                    elif selection_2 == "2":
                        return 0.15
                return 0.15
        #For provinces that are not atlantic and Ontario.
        case "3":
            return 0.05
if __name__ == "__main__":
	main()
