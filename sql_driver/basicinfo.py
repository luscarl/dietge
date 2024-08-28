import psycopg2


#adds basic information to the nutrient database
try:
    conn = psycopg2.connect(
        dbname="nutrient",  
        user="postgres",  
        password="lusijia",  
        host="localhost",
        port="5432"  
    )
    print("Database connection successful.")

    cursor = conn.cursor()

    categories = [
            'Fruit',
            'Vegetable',
            'Meat',
            'Dairy',
            'Grains',
            'Snacks',
            'Beverages',
            'Seafood',
            'Nuts and Seeds',
            'Oil',        
            'Sauce',
            'Spices',
            'Fast Food',
            'Frozen Food',
            'Canned Food',
            'Bakery',
            'Desserts',
        ]
    
    for i,c in enumerate(categories):
        cursor.execute(f'''
            INSERT INTO food_categories (category_id,category_name) VALUES ({i},'{c}')
            ON CONFLICT (category_name) DO NOTHING;
        ''')
    print("Food categories data inserted successfully.")
    conn.commit()
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
