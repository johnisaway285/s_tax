# Main Program
def main():
    province_selection()
    pretax = float(input("Pre-Tax Sale: $"))
    GST = pretax * 0.05
    Total_Price = pretax + GST
    print(f"Total price is ${Total_Price:.2f}, GST is {GST:.2f} and pre-tax is {pretax:.2f}")
# Province Selection, Different provinces have different GST/HST rates. For example: ON has a 13% HST while AB has a lower rate of 5%.
def province_selection():
    selection = input("Please select your province. For Ontario, select 1, For Atlantic provinces, select 2. For other provinces, select 3")
    print(selection)
if __name__ == "__main__":
	main()
