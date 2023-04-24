#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exercici 2 
#Realitza la següent consulta sobre la base de dades acabada de crear: 

#Has d'obtenir el nom, el país i la data de naixement d'aquelles persones per les quals no consti una data de mort i 
#ordenar les dades de la persona més vella a la persona més jove.

import mysql.connector

db=mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="",
    charset="utf8mb4",
    database="movies")

cursor = db.cursor(buffered=True)

cursor.execute("""

select person_name as nom, person_country as pais, person_dob as data_de_naixement
from tb_person
where person_dod is null
order by data_de_naixement desc;

""")

db.commit()

for x in cursor:
    print(x)
    
cursor.close()


# In[2]:


# Exercici 3
#Realitza la següent consulta sobre la base de dades acabada de crear: 

#Has d'obtenir el nom del gènere i el nombre total de pel·lícules d'aquest gènere i ordenar-ho per ordre descendent de nombre
#total de pel·lícules.  

import mysql.connector

db=mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="",
    charset="utf8mb4",
    database="movies")

cursor = db.cursor(buffered=True)

cursor.execute("""

select g.genre_name, count(*) from tb_movie t join tb_genre g 
on t.movie_genre_id=g.genre_id
GROUP by g.genre_name;

""")

db.commit()

for x in cursor:
    print(x)
    
cursor.close()


# In[3]:


#Has d'obtenir, per a cada persona, el seu nom i el nombre màxim de rols diferents que ha tingut en una mateixa pel·lícula. 

import mysql.connector

db=mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="",
    charset="utf8mb4",
    database="movies")

cursor = db.cursor(buffered=True)

cursor.execute("""

select movie_title, name, roles from (SELECT distinct m.movie_title, p.person_name as name, count(r.role_id) as roles 
from tb_movie m 
join tb_movie_person mp on mp.movie_id=m.movie_id 
join tb_person p on p.person_id=mp.person_id 
join tb_role r on r.role_id=mp.role_id 
group by name) t
where roles > 1
order by roles desc;

""")

#Posteriorment, mostra únicament aquelles persones que hagin assumit més d'un rol en una mateixa pel·lícula.

db.commit()

for x in cursor:
    print(x)
    
cursor.close()


# In[4]:


# Has de crear un nou gènere anomenat "Documental" el qual tingui com a identificador el nombre 69.

import mysql.connector

db=mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="",
    charset="utf8mb4",
    database="movies")

cursor = db.cursor(buffered=True)

try:  
    cursor.execute("""

    INSERT INTO tb_genre (genre_id, genre_name) VALUES (69,'Documental');

    """)
except: 
    print("Something´s wrong, maybe already there?")

db.commit()

cursor.close()


# In[5]:


import mysql.connector

db=mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="",
    charset="utf8mb4",
    database="movies")

cursor = db.cursor(buffered=True)

#Elimina la pel·lícula "La Gran Familia Española" de la base de dades.
try:
    cursor.execute("""
    ALTER TABLE tb_movie_person
    DROP CONSTRAINT `fk_movper_movie`;
    """)

    cursor.execute("""
    DELETE FROM tb_movie WHERE movie_title="La Gran Familia Española";
    """)
except:
    print("Something´s wrong, check again")
    
db.commit()

cursor.close()


# In[6]:


import mysql.connector

db=mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="",
    charset="utf8mb4",
    database="movies")

cursor = db.cursor(buffered=True)

#Canvia el gènere de la pel·lícula "Ocho apellidos catalanes" perquè consti com a comèdia i no com a romàntica.

try:
    cursor.execute("""
    UPDATE tb_movie 
    JOIN tb_genre on tb_genre.genre_id=tb_movie.movie_genre_id
    SET tb_movie.movie_genre_id=tb_genre.genre_id
    WHERE tb_movie.movie_title='Ocho apellidos catalanes'
    AND tb_genre.genre_name='Comedia'
    ;
    """)

except:
    print("Something´s wrong, check again")

db.commit()

cursor.close()


# In[ ]:




