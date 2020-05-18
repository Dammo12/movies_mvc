from mysql import connector

class Model: 
    def __init__(self, config_db_file='m_config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()
        
    def close_db(self):
        self.cnx.close()

    #::::::::::::::CRUD METHODS:::::::::::::::::::

    #Actors
    def create_actor(self, fn_a, ln1_a, ln2_a, a_country, phone_a, a_age ):
        try:
            sql = 'INSERT INTO actors (`fn_a`, `ln1_a`, `ln2_a`, `a_country`, `phone_a`,`a_age`) VALUES (%s,%s,%s,%s,%s,%s)' 
            vals = (fn_a, ln1_a, ln2_a, a_country, phone_a, a_age)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_actor(self,id_act):
        try:
            sql = 'SELECT * FROM actors WHERE id_act = %s' 
            vals = (id_act,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_actors(self):
        try:
            sql = 'SELECT * FROM actors'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_actors_country(self,a_country):
        try:
            sql = 'SELECT * FROM actors WHERE a_country = %s'
            vals = (a_country, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_actors_age(self,a_age):
        try:
            sql = 'SELECT * FROM actors WHERE a_age = %s'
            vals = (a_age, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_actor(self, fields, vals):
        try:
            sql = 'UPDATE actors SET ' + ','.join(fields)+' WHERE id_act = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_actor(self, id_act):
        try:
            sql = 'DELETE FROM actors WHERE id_act = %s'
            vals = (id_act,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Directors
    def create_director(self, fn_d, ln1_d, ln2_d, d_country, phone_d, d_age ):
        try:
            sql = 'INSERT INTO directors (`fn_d`, `ln1_d`, `ln2_d`, `d_country`, `phone_d`, `d_age`) VALUES (%s,%s,%s,%s,%s,%s)' 
            vals = (fn_d, ln1_d, ln2_d, d_country, phone_d, d_age)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True 
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_director(self,id_dir):
        try:
            sql = 'SELECT * FROM directors WHERE id_dir = %s' 
            vals = (id_dir,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_directors(self):
        try:
            sql = 'SELECT * FROM directors'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_directors_country(self,d_country):
        try:
            sql = 'SELECT * FROM directors WHERE d_country = %s'
            vals = (d_country, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_directors_age(self,d_age):
        try:
            sql = 'SELECT * FROM directors WHERE d_age = %s'
            vals = (d_age, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_director(self, fields, vals):
        try:
            sql = 'UPDATE directors SET ' + ','.join(fields)+' WHERE id_dir = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_director(self, id_dir):
        try:
            sql = 'DELETE FROM directors WHERE id_dir = %s'
            vals = (id_dir,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Classifications
    def create_classification(self, rate, recommended, min_age):
        try:
            sql = 'INSERT INTO classifications (`rate`, `recommended`, `min_age`) VALUES (%s,%s,%s)' 
            vals = (rate, recommended, min_age)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_classification(self,rate):
        try:
            sql = 'SELECT * FROM classifications WHERE rate = %s' 
            vals = (rate,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_classifications(self):
        try:
            sql = 'SELECT * FROM classifications'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_classifications_minage(self,min_age):
        try:
            sql = 'SELECT * FROM classifications WHERE min_age <= %s'
            vals = (min_age, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_m_class(self,id_class):
        try:
            sql = 'SELECT movies.*, classifications.rate FROM (movie_det) JOIN (movies, classifications) WHERE movie_det.id_class = %s and movie_det.id_class = classifications.rate and movie_det.id_movie = movies.id_movie' 
            vals = (id_class,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_classification(self, fields, vals):
        try:
            sql = 'UPDATE classifications SET ' + ','.join(fields)+' WHERE rate = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_classifications(self, rate):
        try:
            sql = 'DELETE FROM classifications  WHERE rate = %s'
            vals = (rate,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Genres
    def create_genre(self, gen):
        try:
            sql = 'INSERT INTO genres (`gen`) VALUES (%s)' 
            vals = (gen,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_genre(self,id_gen):
        try:
            sql = 'SELECT * FROM genres WHERE id_gen = %s' 
            vals = (id_gen,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_m_genre(self,id_gen):
        try:
            sql = 'SELECT movies.*, genres.gen FROM (movie_det) JOIN (movies, genres) WHERE movie_det.id_gen = %s and movie_det.id_gen = genres.id_gen and movie_det.id_movie = movies.id_movie' 
            vals = (id_gen,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_genres(self):
        try:
            sql = 'SELECT * FROM genres'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_genre(self, fields, vals):
        try:
            sql = 'UPDATE genres SET ' + ','.join(fields)+' WHERE id_gen = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_genre(self,id_gen):
        try:
            sql = 'DELETE FROM genres WHERE id_gen = %s'
            vals = (id_gen,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Movies
    def create_movie(self, m_title, duration, premiere_day):
        try:
            sql = 'INSERT INTO movies (`m_title`, `duration`, `premiere_day`) VALUES (%s,%s,%s)' 
            vals = (m_title, duration, premiere_day)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_movie(self,id_movie):
        try:
            sql = 'SELECT * FROM movies WHERE id_movie = %s' 
            vals = (id_movie,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_movies(self):
        try:
            sql = 'SELECT * FROM movies'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_movie(self, fields, vals):
        try:
            sql = 'UPDATE movies SET ' + ','.join(fields)+' WHERE id_movie = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_movie(self, id_movie):
        try:
            sql = 'DELETE FROM movies  WHERE id_movie = %s'
            vals = (id_movie,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Movie Details
    def create_m_det(self,id_movie,id_gen,id_class):
        try:
            sql = 'INSERT INTO movie_det(`id_movie`,`id_gen`,`id_class`) VALUES (%s,%s,%s)'
            vals = (id_movie, id_gen, id_class)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_m_det(self, id_movie):
        try:
            sql = 'SELECT movies.m_title, movie_det.id_class, classifications.min_age, genres.gen, movies.duration, movies.premiere_day FROM (movie_det) JOIN (genres, classifications, movies) ON movie_det.id_movie = movies.id_movie and movie_det.id_movie = %s and movie_det.id_class = classifications.rate and movie_det.id_gen = genres.id_gen'
            vals = (id_movie)
            self.cursor.execute(sql,(vals,))
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err


    def update_m_det(self, fields, vals):
        try:
            sql = 'UPDATE movie_det SET '+','.join(fields)+' WHERE id_movie = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err


    #Movie casting
    def create_m_casting(self,id_movie,id_act, salary_a):
        try:
            sql = 'INSERT INTO casting(`id_movie`,`id_act`, `salary_a`) VALUES (%s,%s,%s)'
            vals = (id_movie, id_act, salary_a)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_m_cast(self, id_movie):
        try:
            sql = 'SELECT movies.m_title, actors.fn_a, actors.ln1_a, casting.salary_a FROM casting JOIN (movies, actors) ON casting.id_movie = movies.id_movie and movies.id_movie = %s and casting.id_act = actors.id_act'
            vals = (id_movie,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Movie director
    def create_m_director(self,id_movie,id_dir, salary_d):
        try:
            sql = 'INSERT INTO movie_dir(`id_movie`,`id_dir`, `salary_d`) VALUES (%s,%s,%s)'
            vals = (id_movie, id_dir, salary_d)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_m_dir(self, id_movie):
        try:
            sql = 'SELECT movies.m_title, directors.fn_d, directors.ln1_d, movie_dir.salary_d FROM movie_dir JOIN (movies, directors) ON movie_dir.id_movie = movies.id_movie and movies.id_movie = %s and movie_dir.id_dir = directors.id_dir'
            vals = (id_movie,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err