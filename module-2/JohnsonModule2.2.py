#Scott Johnson
#Module 2.2
#12/11/25

# Function to convert miles to kilometers
def miles_to_km(miles):
    return miles * 1.60934

# Get miles from user
try:
    # Ask for input
    miles = float(input("Enter miles: "))
    
    # Convert using function
    km = miles_to_km(miles)
    
    # Show results
    print(f"Miles: {miles}")
    print(f"Kilometers: {km:.2f}")
    
except ValueError:
    # Handle bad input
    print("Please enter a number.")