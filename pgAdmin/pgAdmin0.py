from weakref import ref
import psycopg2

def flascpr(login,password):
    conn = psycopg2.connect(
    dbname="Rproduc",
    user="postgres",
    password="Rus371m",
    host="localhost",
    port="4998"
)


    cursor = conn.cursor()
    cursor.execute(
    "SELECT registg.isbuy FROM registg, user_city WHERE registg.login = user_city.login AND registg.password = user_city.password AND registg.login = %s AND registg.password = %s",
    (login, password)
    )
    res = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    print(res[0][0])
    return res[0][0]





def tg_login(login):
    conn = psycopg2.connect(
    dbname="Rproduc",
    user="postgres",
    password="Rus371m",
    host="localhost",
    port="4998"
)


    cursor = conn.cursor()
    cursor.execute("SELECT password FROM registg where login = %s", (login,))
    res = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    print(res)
    return res[0][0]



def seve():
    conn = psycopg2.connect(
    dbname="Rproduc",
    user="postgres",
    password="Rus371m",
    host="localhost",
    port="4998"
)


    cursor = conn.cursor()
    cursor.execute("SELECT * FROM fruits")
    res = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return res

    
    
def add_order(id,name, price,data):
    try:
        a=1
        conn = psycopg2.connect(
            dbname="Rproduc",
            user="postgres",
            password="Rus371m",
            host="localhost",
            port="4998"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT balance from users WHERE user_id = 2")
        ball = cursor.fetchall()
        cursor.execute("UPDATE users SET balance = balance - %s WHERE user_id = 2 AND balance >= %s",(int(price),int(price)))
        conn.commit()
        cursor.close()
        conn.close()
        print(f'баланс:{ball[0][0]}')
        if ball[0][0] >= int(price):
            conn = psycopg2.connect(
                dbname="Rproduc",
                user="postgres",
                password="Rus371m",
                host="localhost",
                port="4998"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT counts from sclad WHERE id = %s", (int(id),))
            res = cursor.fetchall()
            print(f'количество:{res[0][0]}')
            cursor.execute("UPDATE sclad SET counts = counts - 1 WHERE id = %s AND counts > 0 ",(int(id),))
            conn.commit()
            cursor.close()
            conn.close()
            if res[0][0]>0:
                    conn = psycopg2.connect(
                    dbname="Rproduc",
                    user="postgres",
                    password="Rus371m",
                    host="localhost",
                    port="4998"
                )
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO orders VALUES (%s,%s, %s,%s)",
                        (id,name, price,data)
                    )
                    conn.commit()
                    cursor.close()
                    conn.close()
            else:
                print("net count")
        else:
            print("net balansa")
            
            
    except psycopg2.errors.UniqueViolation as e:
        print(f"Error: {e}")
        
    
def order():
    conn = psycopg2.connect(
        dbname="Rproduc",
        user="postgres",
        password="Rus371m",
        host="localhost",
        port="4998"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res