import psycopg2

conn_params = {
        'dbname': 'dvdrental',
        'user': 'santiago', # or your PostgreSQL username
        'password': 'cofifi73', # replace with your password
        'host': 'localhost'
    }

def get_connection(conn_params):
    """Esta función me genera una conexión para alguna base de datos postgres dada

    Args:
        conn_params (dict): parametros de conexion, con host, usuario y contraseña

    Returns:
        conn: Conexión
    """
    try:
        conn = psycopg2.connect(**conn_params)
        return conn
    except: 
        print('No se pudo establecer la conexión')


conn = get_connection(conn_params)
cur = conn.cursor()

def read(query: str,cur):
    try:
        cur.execute(query)
        return cur.fetchall()
    except:
        print("No se pudo ejecutar el query")

query_read = "SELECT title, description FROM film LIMIT 10;"

#data = read(query,cur)


#for value in data:
#    print(f"EL título de la película es {value[0]} y trata de {value[1]}")

query_create = "insert into actor (first_name, last_name) values ('Santiago', 'echeverri')"

def create(query,cur):
    try:
        cur.execute(query)
        conn.commit()
    except psycopg2.Error as error:
        print(error)

query_update = "update actor set last_name = 'Echeverri' where actor_id = 202"

def update(query,cur):
    cur.execute(query)
    conn.commit()

update(query_update, cur)

query_delete = "delete from actor where actor_id = 202"

def delete(query,cur):
    cur.execute(query)
    conn.commit()

delete(query_delete,cur)