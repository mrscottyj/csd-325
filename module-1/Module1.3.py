# Function to count down the bottles
def countdown_bottles(bottles):
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            if bottles - 1 == 1:
                print(f"Take one down, pass it around, 1 bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down, pass it around, 0 bottles of beer on the wall.\n")
        
        bottles -= 1


# Main program
bottles = int(input("Enter number of bottles: "))
countdown_bottles(bottles)
print("Time to buy more bottles of beer.")