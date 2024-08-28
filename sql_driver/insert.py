import psycopg2

def insert_food_item_with_nutrients():
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="nutrient",  # Replace with your database name
            user="postgres",  # Replace with your PostgreSQL username
            password="lusijia",  # Replace with your PostgreSQL password
            host="localhost",  # Or the host where your PostgreSQL server is running
            port="5432"  # Default port for PostgreSQL
        )
        print("Database connection successful.")
        
        # Create a cursor object
        cursor = conn.cursor()

        # Step 1: Get input from the user
        food_name = input("Enter food name: ")
        food_category = input("Enter food category (e.g., 'Fruit', 'Vegetable', etc.): ")
        barcode = input("Enter barcode (or press Enter to skip): ") or None
        brand_name = input("Enter brand name (or press Enter to skip): ") or None

        # Nutrient data
        nutrients = {}
        nutrients['calories'] = float(input("Enter calories (per 100g): "))
        nutrients['calories_unit'] = 'kcal'
        nutrients['protein'] = float(input("Enter protein (g per 100g): "))
        nutrients['protein_unit'] = 'g'
        nutrients['fat'] = float(input("Enter fat (g per 100g): "))
        nutrients['fat_unit'] = 'g'
        nutrients['carbohydrates'] = float(input("Enter carbohydrates (g per 100g): "))
        nutrients['carbohydrates_unit'] = 'g'
        nutrients['fiber'] = float(input("Enter fiber (g per 100g): "))
        nutrients['fiber_unit'] = 'g'
        nutrients['sugar'] = float(input("Enter sugar (g per 100g): "))
        nutrients['sugar_unit'] = 'g'
        nutrients['sodium'] = float(input("Enter sodium (mg per 100g): "))
        nutrients['sodium_unit'] = 'mg'
        nutrients['vitamin_c'] = float(input("Enter vitamin C (mg per 100g): "))
        nutrients['vitamin_c_unit'] = 'mg'
        nutrients['iron'] = float(input("Enter iron (mg per 100g): "))
        nutrients['iron_unit'] = 'mg'
        nutrients['calcium'] = float(input("Enter calcium (mg per 100g): "))
        nutrients['calcium_unit'] = 'mg'
        nutrients['potassium'] = float(input("Enter potassium (mg per 100g): "))
        nutrients['potassium_unit'] = 'mg'
        nutrients['vitamin_d'] = float(input("Enter vitamin D (IU per 100g): "))
        nutrients['vitamin_d_unit'] = 'IU'
        nutrients['cholesterol'] = float(input("Enter cholesterol (mg per 100g): "))
        nutrients['cholesterol_unit'] = 'mg'

        # Step 2: Insert the food item into the food_items table
        cursor.execute('''
            INSERT INTO food_items (food_name, food_category_id, barcode, brand_name)
            VALUES (%s, (SELECT category_id FROM food_categories WHERE category_name = %s), %s, %s)
            RETURNING food_id;
        ''', (food_name, food_category, barcode, brand_name))
        
        # Get the food_id of the newly inserted food item
        food_id = cursor.fetchone()[0]
        print(f"Inserted food item '{food_name}' with food_id {food_id}.")

        # Step 3: Insert nutrient data into the nutrients table
        cursor.execute('''
            INSERT INTO nutrients (
                food_id, calories, calories_unit_id, protein, protein_unit_id, fat, fat_unit_id, carbohydrates, carbohydrates_unit_id,
                fiber, fiber_unit_id, sugar, sugar_unit_id, sodium, sodium_unit_id, vitamin_c, vitamin_c_unit_id, iron, iron_unit_id,
                calcium, calcium_unit_id, potassium, potassium_unit_id, vitamin_d, vitamin_d_unit_id, cholesterol, cholesterol_unit_id
            ) VALUES (
                %s, %s, (SELECT unit_id FROM units WHERE unit_name = %s), %s, (SELECT unit_id FROM units WHERE unit_name = %s),
                %s, (SELECT unit_id FROM units WHERE unit_name = %s), %s, (SELECT unit_id FROM units WHERE unit_name = %s),
                %s, (SELECT unit_id FROM units WHERE unit_name = %s), %s, (SELECT unit_id FROM units WHERE unit_name = %s),
                %s, (SELECT unit_id FROM units WHERE unit_name = %s), %s, (SELECT unit_id FROM units WHERE unit_name = %s),
                %s, (SELECT unit_id FROM units WHERE unit_name = %s), %s, (SELECT unit_id FROM units WHERE unit_name = %s),
                %s, (SELECT unit_id FROM units WHERE unit_name = %s), %s, (SELECT unit_id FROM units WHERE unit_name = %s)
            );
        ''', (
            food_id, 
            nutrients['calories'], nutrients['calories_unit'], 
            nutrients['protein'], nutrients['protein_unit'],
            nutrients['fat'], nutrients['fat_unit'],
            nutrients['carbohydrates'], nutrients['carbohydrates_unit'],
            nutrients['fiber'], nutrients['fiber_unit'],
            nutrients['sugar'], nutrients['sugar_unit'],
            nutrients['sodium'], nutrients['sodium_unit'],
            nutrients['vitamin_c'], nutrients['vitamin_c_unit'],
            nutrients['iron'], nutrients['iron_unit'],
            nutrients['calcium'], nutrients['calcium_unit'],
            nutrients['potassium'], nutrients['potassium_unit'],
            nutrients['vitamin_d'], nutrients['vitamin_d_unit'],
            nutrients['cholesterol'], nutrients['cholesterol_unit']
        ))
        print(f"Nutrient data inserted for food_id {food_id}.")

        # Commit the changes
        conn.commit()
        print("Changes committed to the database.")

        cursor.close()
        conn.close()

    except Exception as e:
        print("An error occurred:", e)

    

# Run the function to insert a food item with its nutrient data from user input
insert_food_item_with_nutrients()
