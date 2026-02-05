"""
George Athanasopoulos
Feb 5, 2026
Lab 4, Ditionary
"""

print("\n----- Example 1: Dictionary -----")
contacts = {
    'Bill': '718-111-2222',
    'Rick': '917-000-1111',
    'Mary': '800-222-3333',
}
print(f"Original Dictionary: {contacts}")

# Update a value of a dictionary
contacts['Rick'] = '347-000-1111'
print(f"Updated Dictionary:  {contacts}")

# Add a new key-value pair
contacts['Peter'] = '888-000-1111'
print(f"Updated Dictionary with new key/value pair: {contacts}")


print("\n----- Example 2: Loop through a dictionary -----")
# For loop to print each key in the dictionary
for v in contacts:
    print(v)

# For loop to print each value in the dictionary
for v in contacts:
    print(contacts[v])

# For loop to print each key-value in the dictionary
for v in contacts:
    print(f"{v} phone number is {contacts[v]}")


print("\n----- Example 3: items(), keys(), values() methods in a dictionary -----")
# Items() method returns all the key-value pairs in the dictionary
print(f"Items in the dictionary {contacts.items()}")
# Keys() method returns all the keys in the dictionary
print(f"Keys in the dictionary {contacts.keys()}")
# Values() method returns all the values in the dictionary
print(f"Values in the dictionary {contacts.values()}")


print("\n----- Example 4: Check if a key is 'in' or 'not in' a dictionary  -----")
check_name = 'Lucy'
check = check_name in contacts
print(f"Is {check_name} in the dictionary? {check}")


print("\n----- Example 5: Length of a dictionary  -----")
print(f"Contacts has {len(contacts)} key-value pairs")


print("\n----- Example 6: Remove a pair  -----")
print(f"Original Dictionary: {contacts}")
contacts.pop('Mary')
print(f"Updated Dictionary: {contacts}")


print("\n----- Example 7: Get() method  -----")
# Get() method returns the value pair of a key
print(f"Bill's Number: {contacts.get('Bill')}")


print("\n----- Example 8: Update() method  -----")
# Can be used to update a value of a key or to add a new key-value pair
contacts.update({'Annie': '718-888-9999'})
print(f"{contacts}")


print("\n----- EXERCISE  -----")
