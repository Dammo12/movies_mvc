from model.m_model import Model
from view.m_view import View

v = View()
m = Model()
#m.create_movie("Rojo Amanecer")
#print(t[0][1])
#t = m.create_actor('Juan', 'Romero', 'Salinas', 'Mexico', '4658812321', 21)
#print(t)
#t = m.create_director('Guillermo', 'Del Toro', 'Gomez', 'Mexico', '4842531478', 53)
#print(t)
#t = m.create_classification('A', 1)
#print(t)
#t = m.create_genre('Romance')
#print(t)
#t = m.create_movie('Rojo Amanecer', '02:30:25', '2020-05-16')
#t = m.create_m_director(1, 1, '40000')
#print(t)


#t = m.read_actors()
#print(t)
#t = m.read_directors()
#print(t)
#t = m.read_classifications()
#print(t)
#t = m.read_genres()
#print(t)
#t = m.read_movies()
#print(t)
#t = m.read_m_cast(1)
#print(t)
#t = m.read_m_det(1)
#print(t)
#t = m.read_m_dir(1)
#print(t)


m.close_db()