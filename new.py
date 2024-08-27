import psycopg2

# Step 1: Connect to your PostgreSQL database on your local machine
try:
    conn = psycopg2.connect(
        dbname="nutrient",  # Replace with your database name
        user="postgres",  # Replace with your PostgreSQL username
        password="lusijia",  # Replace with your PostgreSQL password
        host="localhost",
        port="5432"  # Default port for PostgreSQL
    )
    print("Database connection successful.")
    
    # Step 2: Create a cursor object
    cursor = conn.cursor()

    # Step 3: Delete records for Alice and Bob
    cursor.execute('DELETE FROM users WHERE name IN (%s, %s)', ('Alice', 'Bob'))

    # Step 4: Commit the changes to apply the deletion
    conn.commit()
    print("Records for Alice and Bob have been deleted.")

    # Step 5: Query the data to confirm deletion
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    # Print the remaining results
    for row in rows:
        print(row)

except Exception as e:
    print("An error occurred while connecting to the database or executing SQL commands:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
