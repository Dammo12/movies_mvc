class View:
    def start(self):
        print("--------------------------------------")
        print("  BIENVENIDO AL SISTEMA DE PELICULAS  ")
        print("--------------------------------------")

    def menu(self):
        print("--------------------------------------")
        print("            MENU PELICULAS            ")
        print("--------------------------------------")
        print("1.- Peliculas")
        print("2.- Actores")
        print("3.- Directores")
        print("4.- Generos")
        print("5.- Clasificacion")

    #Submenus

    def menu_movies(self):
        print("--------------------------------------")
        print("          SUBMENU PELICULAS           ")
        print("--------------------------------------")
        print("1.- Agregar pelicula")
        print("2.- Ver catalogo de peliculas")
        print("3.- Buscar pelicula")
        print("4.- Ver detalles de pelicula")
        print("5.- Actualizar pelicula")
        print("6.- Eliminar pelicula")

    def menu_actors(self):
        print("--------------------------------------")
        print("           SUBMENU ACTORES            ")
        print("--------------------------------------")
        print("1.- Agregar actor")
        print("2.- Ver todos los actores")
        print("3.- Buscar actor")
        print("4.- Ver reparto de pelicula")
        print("5.- Actualizar actor")
        print("6.- Eliminar actor")

    def menu_directors(self):
        print("--------------------------------------")
        print("          SUBMENU DIRECTORES          ")
        print("--------------------------------------")
        print("1.- Agregar director")
        print("2.- Ver todos los directores")
        print("3.- Buscar director")
        print("4.- Ver directores de pelicula")
        print("5.- Actualizar director")
        print("6.- Eliminar director")

    def menu_genres(self):
        print("--------------------------------------")
        print("            SUBMENU GENEROS           ")
        print("--------------------------------------")
        print("1.- Agregar genero")
        print("2.- Ver generos registrados")
        print("3.- Buscar genero")
        print("4.- Buscar peliculas por generos")
        print("5.- Actualizar genero")
        print("6.- Eliminar genero")

    def menu_classification(self):
        print("--------------------------------------")
        print("        SUBMENU CLASIFICACION         ")
        print("--------------------------------------")
        print("1.- Agregar clasificacion")
        print("2.- Ver todas las clasificaciones")
        print("3.- Buscar clasificacion")
        print("4.- Buscar peliculas por clasificacion")
        print("5.- Actualizar clasificacion")
        print("6.- Eliminar clasificacion")

    #Movies

    def read_movies(self, movies):
        print('No:'.ljust(7)+'|'+'Nombre:'.ljust(40)+'|'+'Duracion:'.ljust(10)+'|'+'Estreno:'.ljust(15))
        print('-'*72)
        for record in movies:
            print(f'{record[0]:<7}|{record[1]:<40}|{record[2]:<40}|{record[3]:<40}')
        print('-'*72)

    def read_movie(self, movie):
        print("--------------------------------------")
        print("               PELICULA               ")
        print("--------------------------------------")
        print("Nombre: ", movie[1])
        print("Duracion: ", movie[2])
        print("Fecha de estreno: ", movie[3])   
        print("--------------------------------------")

    #MovieClassGen

    def read_a_m_det(self, movie_det):
        print("--------------------------------------")
        print("         DETALLES DE PELICULA         ")
        print("--------------------------------------")
        print("Nombre: ", movie_det[0])
        print("Clasificación: ", movie_det[1])
        print("Edad mínima: ", movie_det[2])
        print("Género: ", movie_det[3])
        print("Duracion: ", movie_det[4])
        print("Fecha de estreno: ", movie_det[5])   
        print("--------------------------------------")

    #MovieActor

    def read_a_m_cast(self, movie_cast):
        print('-'*85)
        print('ACTOR'.center(85))
        print('-'*85)
        print(("Pelicula: "+movie_cast[0][0]).center(85))
        print('-'*85)
        print('Nombre:'.ljust(35)+'Apellido:'.ljust(35)+'Salario:'.ljust(15))
        print('-'*85)
        for record in movie_cast:
            print(f'{record[1]:<35}{record[2]:<35}${record[3]:<15}')
        print('-'*85)

    #Actors

    def read_actor(self, actor):
        print("--------------------------------------")
        print("                ACTOR                 ")
        print("--------------------------------------")
        print("Nombre: ", actor[1])
        print("Apellido: ", actor[2] + ' ' + actor[3])
        print("Pais: ", actor[4])
        print("Telefono: ", actor[5])
        print("Edad: ", actor[6])
        print("--------------------------------------")


    def read_actors(self, actors):
        print('-'*171)
        print('ACTORES'.center(171))
        print('-'*171)
        print('No:'.ljust(7)+'Nombre:'.ljust(35)+'Apellido Paterno:'.ljust(35)+'Apellido Materno:'.ljust(35)+'Pais:'.ljust(30)+'Telefono:'.ljust(18)+'Edad:'.ljust(3))
        print('-'*171)
        for record in actors:
            print(f'{record[0]:<7}{record[1]:<35}{record[2]:<35}{record[3]:<35}{record[4]:<30}{record[5]:<18}{record[6]:<3}')
        print('-'*171)

    #MovieDirector

    def read_m_dir(self, movie_dir):
        print('-'*85)
        print('DIRECTOR'.center(85))
        print('-'*85)
        print(("Pelicula: "+movie_dir[0][0]).center(85))
        print('-'*85)
        print('Nombre:'.ljust(35)+'Apellido:'.ljust(35)+'Salario:'.ljust(15))
        print('-'*85)
        for record in movie_dir:
            print(f'{record[1]:<35}{record[2]:<35}${record[3]:<15}')
        print('-'*85)

    #Directors

    def read_director(self, director):
        print("--------------------------------------")
        print("               DIRECTOR               ")
        print("--------------------------------------")
        print("Nombre: ", director[1])
        print("Apellido: ", director[2] + ' ' + director[3])
        print("Pais: ", director[4])
        print("Telefono: ", director[5])
        print("Edad: ", director[6])
        print("--------------------------------------")


    def read_directors(self, directors):
        print('-'*171)
        print('DIRECTORES'.center(171))
        print('-'*171)
        print('No:'.ljust(7)+'Nombre:'.ljust(35)+'Apellido Paterno:'.ljust(35)+'Apellido Materno:'.ljust(35)+'Pais:'.ljust(30)+'Telefono:'.ljust(18)+'Edad:'.ljust(3))
        print('-'*171)
        for record in directors:
            print(f'{record[0]:<7}{record[1]:<35}{record[2]:<35}{record[3]:<35}{record[4]:<30}{record[5]:<18}{record[6]:<3}')
        print('-'*171)