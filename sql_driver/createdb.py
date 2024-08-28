import psycopg2


#creates basic relational database schema for the nutrient database
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

    #create units table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS units (
            unit_id SERIAL PRIMARY KEY,
            unit_name VARCHAR(20) NOT NULL UNIQUE
        );
    ''')

    #create food_categories table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS food_categories (
            category_id SERIAL PRIMARY KEY,
            category_name VARCHAR(100) NOT NULL UNIQUE
        );
    ''')

    #create food_items table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS food_items (
            food_id SERIAL PRIMARY KEY,
            food_name VARCHAR(255) NOT NULL,
            food_category_id INT,  -- References category_id from food_categories
            barcode VARCHAR(50) UNIQUE,
            brand_name VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (food_category_id) REFERENCES food_categories(category_id)
        );
    ''')

    #create nutrients table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nutrients (
            nutrient_id SERIAL PRIMARY KEY,
            food_id INT NOT NULL,
            calories FLOAT NOT NULL,
            calories_unit_id INT REFERENCES units(unit_id),
            protein FLOAT NOT NULL,
            protein_unit_id INT REFERENCES units(unit_id),
            fat FLOAT NOT NULL,
            fat_unit_id INT REFERENCES units(unit_id),
            carbohydrates FLOAT NOT NULL,
            carbohydrates_unit_id INT REFERENCES units(unit_id),
            fiber FLOAT,
            fiber_unit_id INT REFERENCES units(unit_id),
            sugar FLOAT,
            sugar_unit_id INT REFERENCES units(unit_id),
            sodium FLOAT,
            sodium_unit_id INT REFERENCES units(unit_id),
            vitamin_c FLOAT,
            vitamin_c_unit_id INT REFERENCES units(unit_id),
            iron FLOAT,
            iron_unit_id INT REFERENCES units(unit_id),
            calcium FLOAT,
            calcium_unit_id INT REFERENCES units(unit_id),
            potassium FLOAT,
            potassium_unit_id INT REFERENCES units(unit_id),
            vitamin_d FLOAT,
            vitamin_d_unit_id INT REFERENCES units(unit_id),
            cholesterol FLOAT,
            cholesterol_unit_id INT REFERENCES units(unit_id),
            FOREIGN KEY (food_id) REFERENCES food_items(food_id) ON DELETE CASCADE
        );
    ''')

    print("exectued")

except Exception as e:
    print("An error occurred while connecting to the database:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
