import requests
import json

# CAT API PROGRAM - thecatapi.com

BASE_URL = "https://api.thecatapi.com/v1"


# STEP 1: Test the connection

print("=" * 55)
print("STEP 1: Testing Connection to The Cat API")
print("=" * 55)

response = requests.get(f"{BASE_URL}/breeds")
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    print("Connection successful!\n")
else:
    print("Connection failed.\n")


# STEP 2: Print raw (unformatted) response

print("=" * 55)
print("STEP 2: Raw (Unformatted) Response - First Breed")
print("=" * 55)

data = response.json()
# Show just the first breed entry raw
print(data[0])


# STEP 3: Print formatted response

print("\n" + "=" * 55)
print("STEP 3: Formatted Response - First 3 Breeds")
print("=" * 55)

def jprint(obj):
    """Pretty-print a JSON object."""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Show first 3 breeds formatted
for breed in data[:3]:
    jprint(breed)
    print("-" * 55)

# Summary
print(f"\nTotal breeds available: {len(data)}")
print("\nAll breed names:")
for breed in data:
    print(f"  - {breed['name']} (Origin: {breed.get('origin', 'Unknown')})")
