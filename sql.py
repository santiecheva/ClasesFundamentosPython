import psycopg2

conn_params = {
        'dbname': 'dvdrental',
        'user': 'santiago', # or your PostgreSQL username
        'password': 'cofifi73', # replace with your password
        'host': 'localhost'
    }

def get_connection(conn_params):
    try:
        conn = psycopg2.connect(**conn_params)
        return conn
    except: 
        print('No se pudo establecer la conexión')


conn = get_connection(conn_params)
cur = conn.cursor()
cur.execute("SELECT title, description FROM film LIMIT 10;")
print(cur.fetchall())






def get_film_details():
    # Connection parameters
    conn_params = {
        'dbname': 'dvdrental',
        'user': 'santiago', # or your PostgreSQL username
        'password': 'cofifi73', # replace with your password
        'host': 'localhost'
    }
    
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**conn_params)
        
        # Create a cursor object
        cur = conn.cursor()
        
        # Execute a query
        cur.execute("SELECT title, description FROM film LIMIT 10;")
        
        # Fetch and print the results
        for row in cur.fetchall():
            print(f"Title: {row[0]}, Description: {row[1]}")
            
        # Close the cursor and connection
        cur.close()
        conn.close()
        
    except psycopg2.Error as e:
        print(f"Error: {e}")
        
