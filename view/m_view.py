class View:
    def start(self):
        print("------------------------------------")
        print(" BIENVENIDO AL SISTEMA DE PELICULAS ")
        print("------------------------------------")
        
    def menu(self):
        print("1.- Mostrar peliculas")
        print("2.- Buscar peliculas")
        print("3.- Mostrar actores")
        print("4.- Buscar actores")
        print("5.- Mostrar directores")
        print("5.- Buscar directores")

    #Movies

    def read_movies(self, movies):
        print('No:'.ljust(7)+'|'+'Nombre:'.ljust(40))
        print('-'*47)
        for record in movies:
            print(f'{record[0]:<7}|{record[1]:<40}')
        print('-'*47)

    def read_movie(self, movie):
        print("--------------------------------------")
        print("               PELICULA               ")
        print("--------------------------------------")
        print("Nombre: ", movie[1])
        print("Clasificación: ", movie.rate)
        print("Género: ", movie.genre)
        print("Nombre: ", movie.m_title)
        print("--------------------------------------")

    def read_a_m_det(self, movie_det):
        print("--------------------------------------")
        print("         DETALLES DE PELICULA         ")
        print("--------------------------------------")
        print("Nombre: ", movie_det[0])
        print("Clasificación: ", movie_det[1])
        print("Edad mínima: ", movie_det[2])
        print("Género: ", movie_det[3])
        print("--------------------------------------")

    def read_a_m_cast(self, movie_cast):
        print("--------------------------------------")
        print("  Pelicula: "+movie_cast[0])
        print("--------------------------------------")
        print("Casting:")
        
        print("--------------------------------------")

    def show_actor(self, actor):
        print("--------------------------------------")
        print("                ACTOR                 ")
        print("--------------------------------------")
        print("Nombre: ", actor[1])
        print("Apellido: ", actor[2])
        print("Pais: ", actor[4])
        print("Edad: ", actor[5])
        print("--------------------------------------")


    def read_actors(self, actors):
        print('No:'.ljust(7)+'|'+'Nombre:'.ljust(40)+'|'+'Apellido:'.ljust(40)+'2a'.ljust(40)+'|')
        print('-'*127)
        for record in actors:
            print(f'{record[0]:<7}|{record[1]:<40}|{record[2]:<40}{record[4]:<40}')
        print('-'*127)