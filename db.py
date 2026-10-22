from mysql import connector


def get_connexion():
    # connexion à la base de données (écrite une seule fois ici)
    return connector.connect(
        user="root",
        password="",
        database="bdd_flasksql",
        host="localhost"
    )


def lister_users():
    db = get_connexion()
    ma_bdd = db.cursor()
    ma_bdd.execute("SELECT * FROM users")
    resultat = ma_bdd.fetchall()
    db.close()
    return resultat


def ajouter_user(nom, prenom, mail):
    db = get_connexion()
    ma_bdd = db.cursor()
    req_add = "INSERT INTO users (nom, prenom, mail) VALUES (%s, %s, %s)"
    ma_bdd.execute(req_add, (nom, prenom, mail))
    db.commit()
    db.close()


def supprimer_user(id):
    db = get_connexion()
    ma_bdd = db.cursor()
    req_del = "DELETE FROM users WHERE id = %s"
    ma_bdd.execute(req_del, (id,))
    db.commit()
    db.close()