from model.m_model import Model
from view.m_view import View

v = View()
m = Model()
#m.create_movie('Azul Amanecer', '02:40:47', '2020-05-15')
#m.create_m_det(1, 2, 'G')
#m.create_m_casting(1,1,17000)
#t = m.create_actor('Alberto', 'Estrada', 'Rojas', 'Colombia', '6325874125', 32)
#t = m.create_director('Guillermo', 'Del Toro', 'Gomez', 'Mexico', '4842531478', 53)
#m.create_classification('PG', 'Parental Guidance Suggested', 7)
#m.create_genre('Ciencia Ficcion')
#t = m.create_movie('Rojo Amanecer', '02:30:25', '2020-05-16')
#t = m.create_m_director(1, 1, '40000')
#t = m.read_directors()
#t = m.read_classifications()
#t = m.read_genres()
#t = m.read_movies()
#t = m.read_m_cast(1)
#t = m.read_m_det(1)
#t = m.read_m_dir(1)

t = m.read_m_class('G')
v.read_m_class(t)

m.close_db()