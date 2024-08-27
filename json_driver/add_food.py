import json
import json

# Prompt the user for input
food_data = {
    "id": input("Enter the food ID: "),
    "name": input("Enter the food name: "),
    "nutrition-per-100g": {
        "energy": float(input("Enter the energy value (kcal): ")),
        "protein": float(input("Enter the protein value (g): ")),
        "fat": float(input("Enter the fat value (g): ")),
        "saturated-fat": float(input("Enter the saturated fat value (g): ")),
        "omega-3-fatty-acid": float(input("Enter the omega-3 fatty acid value (g): ")),
        "carbohydrate": float(input("Enter the carbohydrate value (g): ")),
        "sugars": float(input("Enter the sugars value (g): ")),
        "dietary-fibre": float(input("Enter the dietary fibre value (g): ")),
        "sodium": float(input("Enter the sodium value (mg): "))
    },
    "tags": input("Enter the tags (separated by commas): ").split(",")
}

# Load existing data from food.json
with open("food.json", "r") as file:
    existing_data = json.load(file)

# Add the new food entry to the existing data
existing_data.append(food_data)

# Write the updated data back to food.json
with open("food.json", "w") as file:
    json.dump(existing_data, file, indent=4)

print("Food entry added successfully!")