def main():
	pretax = float(input("Pre-Tax Sale: $"))
	GST = pretax * 0.05
	Total_Price = pretax + GST
	print(f"Total price is ${Total_Price:.2f}, GST is {GST:.2f} and pre-tax is {pretax:.2f}")
if __name__ == "__main__":
	main()
