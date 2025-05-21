# Main Program
def main():
    rate = None
    rate = province_selection(rate)
    pretax = float(input("Pre-Tax Sale: $"))
    GST = pretax * rate
    Total_Price = pretax + GST
    print(f"Total price is ${Total_Price:.2f}, GST is {GST:.2f} and pre-tax is {pretax:.2f}")
# Province Selection, Different provinces have different GST/HST rates. For example: ON has a 13% HST while AB has a lower rate of 5%.
def province_selection(r:float):
    selection = input("Please select your province. For Ontario, select 1, For
                      Atlantic provinces, select 2. For other provinces, select
                      3. ")
    match selection:
        case "1":
            print("You've selected Ontario")
            return 0.13
        case "2":
            ns=input("You've selected Atlantic Provinces, hmmm, there is a
                     change in HST for Nova Scotia, is this a sale that occured
                     in Nova Scotia?")
            if ns == "1":
                if input("Is this a sale that happened after April 1, 2025?") == "1":
                    pass
if __name__ == "__main__":
	main()
