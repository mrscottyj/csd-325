import requests
import json

# ============================================================
# PART 1: Test the connection to the Open Notify API
# ============================================================
print("=" * 50)
print("PART 1: Testing API Connection")
print("=" * 50)

response = requests.get("http://api.open-notify.org/astros.json")
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    print("Connection successful!\n")
else:
    print("Connection failed.\n")

# ============================================================
# PART 2: Retrieve current astronauts and format output
# ============================================================
print("=" * 50)
print("PART 2: Current Astronauts in Space")
print("=" * 50)

def jprint(obj):
    """Pretty-print a JSON object."""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

data = response.json()

print(f"\nTotal people in space: {data['number']}\n")
print("Formatted JSON Output:")
jprint(data)

print("\nAstronaut Names:")
for person in data['people']:
    print(f"  - {person['name']} aboard {person['craft']}")