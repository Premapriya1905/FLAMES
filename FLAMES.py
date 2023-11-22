# Get names from user
player1_name = input("Enter the name of the first person: ")
player2_name = input("Enter the name of the second person: ")

# Remove spaces and convert to uppercase
player1_name = player1_name.replace(" ", "").upper()
player2_name = player2_name.replace(" ", "").upper()

# Find common letters in the names
common_letters = set(player1_name) & set(player2_name)

# Determine relationship status
total_letters = len(player1_name) + len(player2_name) - len(common_letters)

# Display the result
if total_letters == 0:
    print("Invalid relation")
else:
    flames = "FLAMES"
    result_index = total_letters % len(flames) - 1
    relationship_status = {
        "F": "Friends",
        "L": "Lovers",
        "A": "Affectionate",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings",
    }[flames[result_index]]
    print(f"The relationship status is: {relationship_status}")



