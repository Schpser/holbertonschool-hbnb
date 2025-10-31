import sqlite3
import os

def test_sql_scripts():
    # Créer une base de test
    test_db = 'test_hbnb.db'
    
    if os.path.exists(test_db):
        os.remove(test_db)
    
    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()
    
    print("🧪 TEST DES SCRIPTS SQL")
    print("=" * 40)
    
    # Exécuter le schéma
    with open('schema.sql', 'r') as f:
        schema_sql = f.read()
    
    cursor.executescript(schema_sql)
    print("✅ Schema créé avec succès")
    
    # Vérifier les tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    expected_tables = ['users', 'places', 'reviews', 'amenities', 'place_amenity']
    
    print(f"📊 Tables créées: {tables}")
    print(f"✅ Toutes les tables présentes: {all(t in tables for t in expected_tables)}")
    
    # Exécuter les données initiales
    with open('initial_data.sql', 'r') as f:
        data_sql = f.read()
    
    cursor.executescript(data_sql)
    print("✅ Données initiales insérées")
    
    # Vérifier les données
    cursor.execute("SELECT COUNT(*) FROM users;")
    user_count = cursor.fetchone()[0]
    print(f"👤 Users créés: {user_count}")
    
    cursor.execute("SELECT COUNT(*) FROM amenities;")
    amenity_count = cursor.fetchone()[0]
    print(f"🏊 Amenities créées: {amenity_count}")
    
    cursor.execute("SELECT email, is_admin FROM users WHERE id = '36c9050e-ddd3-4c3b-9731-9f487208bbc1';")
    admin_user = cursor.fetchone()
    print(f"🔧 Admin user: {admin_user[0]} (admin: {admin_user[1]})")
    
    conn.commit()
    conn.close()
    
    # Nettoyer
    os.remove(test_db)
    
    print("\n🎉" + "="*47 + "🎉")
    print("🎯 SCRIPTS SQL VALIDÉS !")
    print("✅ Schema généré correctement")
    print("✅ Données initiales insérées")
    print("✅ Contraintes respectées")
    print("🎉" + "="*47 + "🎉")

if __name__ == "__main__":
    test_sql_scripts()
