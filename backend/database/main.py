import oracledb

connection = oracledb.connect(
    user="willianUsertestes",
    password="senha",
    dsn="localhost/xe")

print("\n\nSuccessfully connected to Oracle Database\n")

cursor = connection.cursor()
# DROP TABLE AMOSTRAS PURGE;
try:
    cursor.execute("""
        create table amostras (
        id number generated always as identity,
        mp10 number(*),mp25 number(*),o3 number(*), co number(*),no2 number(*),so2 number(*), classification varchar2(30),
        primary key (id))""") # CRIADA A COLUNA DE CLASSIFICATION 
    print("Table created")
except:
    print("Table already created\n")

def insertSamplesDb(co, so2, no2, o3, mp25, mp10, classification):
    query = (f"insert into amostras(co, so2, no2, o3, mp25, mp10,classification) values ({co}, {so2}, {no2}, {o3}, {mp25},{ mp10}, '{classification}')")
    try:
        cursor.execute(query)
        connection.commit()
    except Exception as err:
        print({err})

def deleteSamplesDb(id):
    try:
        query = (f'DELETE from amostras where ID={id}')
        cursor.execute(query)
        connection.commit()
        return "Success"
    except Exception as err:
        print({err})  

def updateSamplesDb(id,co, so2, no2, o3, mp25, mp10, classification):
    try:
        query = (f"UPDATE amostras set co={co}, so2={so2}, no2={no2}, o3={o3}, mp25={mp25}, mp10={mp10}, classification='{classification}' where id={id}") 
        cursor.execute(query)
        connection.commit()
    except Exception as err:
        print({err})

def getSamplesDb():
    samplesDb=[]
    for row in cursor.execute('SELECT * from amostras order by id asc'):
        samplesDb.append(row)
    return samplesDb

def averageSamples():
    cursor.execute("select round(avg(mp10),2),round(avg(mp25),2),round(avg(o3),2),round(avg(co),2),round(avg(no2),2),round(avg(so2),2) from amostras")
    avg = cursor.fetchone()
    if None in avg : avg = False # AVG = FALSE CASO NÃO POSSUA AMOSTRAS REGISTRADAS NO BANCO
    return avg
