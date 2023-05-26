import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect

def create_table(table_name:str, host, user, pwd, db):
    engine = create_engine(f"mysql+pymysql://{user}:{pwd}@{host}:3306/{db}")
    inspector=inspect(engine)
    if not table_name in inspector.get_table_names():


        # Initialisation des colonnes.
        df = pd.DataFrame({'expediteur':[] , 'objet':[], "message":[], "spam":[]})

        # Typage des colonnes de la Table SQL.
        df['expediteur']  = df['expediteur'].astype('str')
        df['objet']  = df['objet'].astype('str')
        df['message']  = df['message'].astype('str')
        df['spam']  = df['spam'].astype('str')

        # envoie du DataFrame sur SQL.
        df.to_sql(name=table_name, con=engine, if_exists='fail', index=False)

### Fonction permettent d'enregistrer le formulaire en BDD (la target et les features).
### Les paramètres : la connexion à la BDD, et une liste des features.
def save_formulaire(conn, features:list):
    cursor = conn.cursor()
    sql = "INSERT INTO resultat (expediteur, objet, message, spam) VALUES (%s,%s,%s,%s)"
    cursor.execute(sql, features)
    conn.commit()
    conn.close()
