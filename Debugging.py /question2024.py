flag = True  # 3. Change False to True
while flag:
	length = float(input("What is the length of the parcel?"))
	width = float(input("What is the width of the parcel?"))
	depth = float(input("What is the depth of the parcel?"))
	if length > 50 and width > 50 and depth > 50: # 6. change second length to width
		parcel_size = "large"
	elif length > 50 and width > 50 and depth <= 50: # 7. should be <= for depth, # 9. change or to and
		parcel_size = "medium"  # 8. Should be parcel_size
	else: # 1. change elif to else
		parcel_size = "small"
		
	print(f"The size of the parcel is {parcel_size}") # testing only. to remove later 
	more_parcel = input("Do you want to enter another parcel? Y or N") 
	if more_parcel == "N": # 2. Should be double equal, # 4. should be "N"
		flag = False # 5. Change it to false to exit loop
		
