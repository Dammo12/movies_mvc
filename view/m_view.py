from datetime import datetime

class View:
    def start(self):
        print('--------------------------------------')
        print(' ¡BIENVENIDO AL SISTEMA DE PELICULAS! ')
        print('--------------------------------------')

    def end(self):
        print('--------------------------------------')
        print('       ¡GRACIAS, VUELVA PRONTO!       ')
        print('--------------------------------------')

    def option(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end = '')

    def no_valid_option(self):
        print('Opcion no valida\nIntenta de nuevo')

    def ask(self, output):
        print(output, end = '')

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('='*(len(str(id))+len(op)+24))
        print(('¡ '+str(id)+' se '+ op +' correctamente !').center(len(str(id))+len(op)+24))
        print('='*(len(str(id))+len(op)+24))

    def error(self, err):
        print('¡ERROR!'.center(len(err)+4))
        print(err.center(len(err)+4))
        print('-'*(len(err)+4))

    #Menus

    def menu(self):
        print('--------------------------------------')
        print('            MENU PELICULAS            ')
        print('--------------------------------------')
        print('1.- Peliculas')
        print('2.- Actores')
        print('3.- Directores')
        print('4.- Generos')
        print('5.- Clasificacion')
        print('6.- Salir')


    #Movies

    def menu_movies(self):
        print('--------------------------------------')
        print('          SUBMENU PELICULAS           ')
        print('--------------------------------------')
        print('1.- Agregar pelicula')
        print('2.- Agregar detalle a pelicula')
        print('3.- Agregar reparto a pelicula')
        print('4.- Ver catalogo de peliculas')
        print('5.- Buscar pelicula')
        print('6.- Ver detalles de pelicula')
        print('7.- Ver reparto de pelicula')
        print('8.- Ver directores de pelicula')
        print('9.- Actualizar pelicula')
        print('10.- Eliminar pelicula')
        print('11.- Regresar')

    def read_movies(self, movies):
        print('-'*97)
        print('PELICULAS'.center(92))
        print('-'*97)
        print('No:'.ljust(7)+'Película:'.ljust(60)+'Duracion:'.ljust(15)+'Estreno:'.ljust(15))
        print('-'*97)
        for record in movies:
            print(f'{record[0]:<7}{record[1]:<60}{str(record[2]):<15}{str(record[3]):<15}')
        print('-'*97)

    def read_movie(self, movie):
        print('----------------------------------------')
        print('                PELICULA                ')
        print('----------------------------------------')
        print('Nombre: '.ljust(20), movie[1])
        print('Duracion: '.ljust(20), movie[2])
        print('Fecha de estreno: '.ljust(20), movie[3])   
        print('----------------------------------------')

    def read_m_det(self, movie_det):
        print('------------------------------------------')
        print('           DETALLES DE PELICULA           ')
        print('------------------------------------------')
        print('Nombre: '.ljust(20), movie_det[0])
        print('Clasificación: '.ljust(20), movie_det[1])
        print('Edad mínima: '.ljust(20), movie_det[2])
        print('Género: '.ljust(20), movie_det[3])
        print('Duracion: '.ljust(20), movie_det[4])
        print('Fecha de estreno: '.ljust(20), movie_det[5])   
        print('------------------------------------------')


    #Actors

    def menu_actors(self):
        print('--------------------------------------')
        print('           SUBMENU ACTORES            ')
        print('--------------------------------------')
        print('1.- Agregar actor')
        print('2.- Ver todos los actores')
        print('3.- Buscar actor')
        print('4.- Ver reparto de pelicula')
        print('5.- Actualizar actor')
        print('6.- Eliminar actor')
        print('7.- Regresar')

    def read_actor(self, actor):
        print('--------------------------------------')
        print('                ACTOR                 ')
        print('--------------------------------------')
        print('Nombre: '.ljust(12), actor[1])
        print('Apellido: '.ljust(12), actor[2] + ' ' + actor[3])
        print('Pais: '.ljust(12), actor[4])
        print('Telefono: '.ljust(12), actor[5])
        print('Edad: '.ljust(12), actor[6])
        print('--------------------------------------')

    def read_actors(self, actors):
        print('-'*171)
        print('ACTORES'.center(171))
        print('-'*171)
        print('No:'.ljust(7)+'Nombre:'.ljust(35)+'Apellido Paterno:'.ljust(35)+'Apellido Materno:'.ljust(35)+'Pais:'.ljust(30)+'Telefono:'.ljust(18)+'Edad:'.ljust(3))
        print('-'*171)
        for record in actors:
            print(f'{record[0]:<7}{record[1]:<35}{record[2]:<35}{record[3]:<35}{record[4]:<30}{record[5]:<18}{record[6]:<3}')
        print('-'*171)

    def read_m_cast(self, movie_cast):
        print('-'*85)
        print('ACTORES'.center(85))
        print('-'*85)
        print(('Pelicula: '+movie_cast[0][0]).center(85))
        print('-'*85)
        print('Nombre:'.ljust(35)+'Apellido:'.ljust(35)+'Salario:'.ljust(15))
        print('-'*85)
        for record in movie_cast:
            print(f'{record[1]:<35}{record[2]:<35}${record[3]:<15}')
        print('-'*85)


    #Directors

    def menu_directors(self):
        print('--------------------------------------')
        print('          SUBMENU DIRECTORES          ')
        print('--------------------------------------')
        print('1.- Agregar director')
        print('2.- Ver todos los directores')
        print('3.- Buscar director')
        print('4.- Ver directores de pelicula')
        print('5.- Actualizar director')
        print('6.- Eliminar director')
        print('7.- Regresar')

    def read_director(self, director):
        print('--------------------------------------')
        print('               DIRECTOR               ')
        print('--------------------------------------')
        print('Nombre: '.ljust(12), director[1])
        print('Apellido: '.ljust(12), director[2] + ' ' + director[3])
        print('Pais: '.ljust(12), director[4])
        print('Telefono: '.ljust(12), director[5])
        print('Edad: '.ljust(12), director[6])
        print('--------------------------------------')

    def read_directors(self, directors):
        print('-'*171)
        print('DIRECTORES'.center(171))
        print('-'*171)
        print('No:'.ljust(7)+'Nombre:'.ljust(35)+'Apellido Paterno:'.ljust(35)+'Apellido Materno:'.ljust(35)+'Pais:'.ljust(30)+'Telefono:'.ljust(18)+'Edad:'.ljust(3))
        print('-'*171)
        for record in directors:
            print(f'{record[0]:<7}{record[1]:<35}{record[2]:<35}{record[3]:<35}{record[4]:<30}{record[5]:<18}{record[6]:<3}')
        print('-'*171)

    def read_m_dir(self, movie_dir):
        print('-'*85)
        print('DIRECTOR'.center(85))
        print('-'*85)
        print(('Pelicula: '+movie_dir[0][0]).center(85))
        print('-'*85)
        print('Nombre:'.ljust(35)+'Apellido:'.ljust(35)+'Salario:'.ljust(15))
        print('-'*85)
        for record in movie_dir:
            print(f'{record[1]:<35}{record[2]:<35}${record[3]:<15}')
        print('-'*85)


    #Genres

    def menu_genres(self):
        print('--------------------------------------')
        print('            SUBMENU GENEROS           ')
        print('--------------------------------------')
        print('1.- Agregar genero')
        print('2.- Ver generos registrados')
        print('3.- Buscar genero')
        print('4.- Buscar peliculas por genero')
        print('5.- Actualizar genero')
        print('6.- Eliminar genero')
        print('7.- Regresar')

    def read_genre(self, genre):
        print('------------------------------------------')
        print('                 GENERO                   ')
        print('------------------------------------------')
        print('No: '.ljust(10), genre[0])
        print('Genero: '.ljust(10), genre[1])
        print('------------------------------------------')

    def read_genres(self, classifications):
        print('-'*35)
        print('GENEROS'.center(35))
        print('-'*35)
        print('No:'.ljust(10)+'Genero:'.ljust(25))
        print('-'*35)
        for record in classifications:
            print(f'{record[0]:<10}{record[1]:<25}')
        print('-'*35)

    def read_m_genre(self, movies):
        print('-'*122)
        print('PELICULAS - GENERO'.center(122))
        print('-'*122)
        print('No:'.ljust(7)+'Película:'.ljust(60)+'Duracion:'.ljust(15)+'Estreno:'.ljust(15)+'Genero:'.ljust(25))
        print('-'*122)
        for record in movies:
            print(f'{record[0]:<7}{record[1]:<60}{str(record[2]):<15}{str(record[3]):<15}{record[4]:<25}')
        print('-'*122)


    #Classification

    def menu_classification(self):
        print('--------------------------------------')
        print('        SUBMENU CLASIFICACION         ')
        print('--------------------------------------')
        print('1.- Agregar clasificacion')
        print('2.- Ver todas las clasificaciones')
        print('3.- Buscar clasificacion')
        print('4.- Buscar peliculas por clasificacion')
        print('5.- Actualizar clasificacion')
        print('6.- Eliminar clasificacion')
        print('7.- Regresar')

    def read_classification(self, classification):
        print('----------------------------------------------')
        print('                CLASIFICACION                 ')
        print('----------------------------------------------')
        print('Rating: '.ljust(14), classification[0])
        print('Preferente: '.ljust(14), classification[1])
        print('Edad minima: '.ljust(14), classification[2])
        print('----------------------------------------------')

    def read_classifications(self, classifications):
        print('-'*55)
        print('CLASIFICACIONES'.center(55))
        print('-'*55)
        print('Rating:'.ljust(10)+'Preferente:'.ljust(30)+'Edad minima:'.ljust(10))
        print('-'*55)
        for record in classifications:
            print(f'{record[0]:<10}{record[1]:<30}{record[2]:<10}')
        print('-'*55)

    def read_m_class(self, movies):
        print('-'*112)
        print('PELICULAS - CLASIFICACION'.center(112))
        print('-'*112)
        print('No:'.ljust(7)+'Película:'.ljust(60)+'Duracion:'.ljust(15)+'Estreno:'.ljust(15)+'Clasificacion:'.ljust(15))
        print('-'*112)
        for record in movies:
            print(f'{record[0]:<7}{record[1]:<60}{str(record[2]):<15}{str(record[3]):<15}{record[4]:<15}')
        print('-'*112)