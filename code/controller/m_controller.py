from model.m_model import Model
from view.m_view import View
from datetime import datetime

class Controller:    
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.main_menu()

    def main_menu(self):
        o='0'
        while o!=6:
            self.view.menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.peliculas_menu()
            elif o == '2':
                self.actores_menu()
            elif o == '3':
                self.directores_menu()
            elif o == '4':
                self.generos_menu()
            elif o == '5':
                self.clasificacion_menu()
            elif o == '6':
                self.view.end()
                return
            else:
                self.view.no_valid_option()
        return

    def update_lists(self,fs,vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields,vals

    #Metodos peliculas
    def peliculas_menu(self):
        o = '0'
        while o != 11:
            self.view.menu_movies()
            self.view.option('11')
            o = input()
            if o == '1':
                self.agregar_pelicula()
            elif o == '2':
                self.agregar_detalle_pelicula()
            elif o == '3':
                self.agregar_reparto()
            elif o == '4':
                self.ver_catalogo_peliculas()
            elif o == '5':
                self.buscar_pelicula()
            elif o == '6':
                self.ver_detalles_pelicula()
            elif o == '7':
                self.ver_reparto_pelicula()
            elif o == '8':
                self.ver_directores_pelicula()
            elif o == '9':
                self.actualizar_pelicula()
            elif o == '10':
                self.actualizar_detalle_pelicula()
            elif o == '11':
                self.eliminar_pelicula()
            elif o == '12':
                return
            else:
                self.view.no_valid_option()
        return

    def ask_pelicula(self):
        self.view.ask('Titulo: ')
        titulo = input()
        self.view.ask('Duracion: ')
        duracion = input()
        self.view.ask('Fecha de estreno (YYYY-MM-DD): ')
        estreno = input()
        return [titulo,duracion,estreno]

    def ask_detalle_pelicula(self):
        self.view.ask('ID Pelicula: ')
        id_m = input()
        self.view.ask('ID Genero: ')
        gen = input()
        self.view.ask('ID Clasificacion: ')
        classif = input()
        return [id_m,gen,classif]

    def ask_reparto(self):
        self.view.ask('ID Pelicula: ')
        id_m = input()
        self.view.ask('ID Actor: ')
        id_a = input()
        self.view.ask('Salario: ')
        sal = input()
        return [id_m,id_a,sal]
    
    def agregar_pelicula(self):
        titulo, duracion, estreno = self.ask_pelicula()
        out = self.model.create_movie(titulo,duracion,estreno)
        if out == True:
            self.view.ok(titulo,'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL TITULO ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR LA PELICULA. REVISA.')
        return
    
    def agregar_detalle_pelicula(self):
        id_m, gen, classif = self.ask_detalle_pelicula()
        out = self.model.create_m_det(id_m,gen,classif)
        if out == True:
            self.view.ok(id_m,'agrego detalle')
        else:
            self.view.error('NO SE PUDO AGREGAR DETALLES A LA PELICULA. REVISA.')
        return

    def agregar_reparto(self):
        id_m, id_a, sal = self.ask_reparto()
        out = self.model.create_m_casting(id_m, id_a, sal)
        if out == True:
            self.view.ok(id_a,'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL ACTOR ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR AL REPARTO. REVISA.')
        return

    def ver_catalogo_peliculas(self):
        out = self.model.read_movies()
        if type(out) == list:
            self.view.read_movies(out)    
        else:
            self.view.error('PROBLEMA AL VER CATALOGO. REVISA.')
        return

    def buscar_pelicula(self):
        self.view.ask('ID Pelicula: ')
        id_m = input()
        out = self.model.read_movie(id_m)
        if type(out) == tuple:
            self.view.read_movie(out)    
        else:
            if out == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER PELICULA. REVISA.') 
        return
    
    def ver_detalles_pelicula(self):
        self.view.ask('ID Pelicula: ')
        id_m = input()
        out = self.model.read_m_det(id_m)
        if type(out) == tuple:
            self.view.read_m_det(out)    
        else:
            if out == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL DETALLE DE PELICULA. REVISA.')
        return

    def ver_reparto_pelicula(self):
        self.view.ask('ID Pelicula: ')
        id_m = input()
        out = self.model.read_m_cast(id_m)
        if type(out) == list:
            if out:
                self.view.read_m_cast(out)    
            else:
                self.view.error('LA PELICULA NO TIENE REPARTO')
        else:
            if out == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL REPARTO DE PELICULA. REVISA.')
        return

    def ver_directores_pelicula(self):
        self.view.ask('ID Pelicula: ')
        id_m = input()
        out = self.model.read_m_dir(id_m)
        if type(out) == list:
            self.view.read_m_dir(out)    
        else:
            if out == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LOS DIRECTORES DE PELICULA. REVISA.')
        return

    def actualizar_pelicula(self):
        self.view.ask('ID Pelicula: ')
        id_m = input()
        out = self.model.read_movie(id_m)
        if type(out) == tuple:
            self.view.read_movie(out)    
        else:
            if out == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER PELICULA. REVISA.') 
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_pelicula()
        fields, vals = self.update_lists(['m_title','duration','premiere_day'],whole_vals)
        vals.append(id_m)
        vals = tuple(vals)
        out = self.model.update_movie(fields,vals)
        if out == True:
            self.view.ok(id_m,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA PELICULA')
        return
    
    def actualizar_detalle_pelicula(self):
        self.view.ask('ID Pelicula: ')
        id_m = input()
        out = self.model.read_movie(id_m)
        if type(out) == tuple:
            self.view.read_movie(out)    
        else:
            if out == None:
                self.view.error('DETALLE DE PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER PELICULA. REVISA.') 
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_detalle_pelicula()
        fields, vals = self.update_lists(['id_movie','id_gen','id_class'],whole_vals)
        vals.append(id_m)
        vals = tuple(vals)
        out = self.model.update_m_det(fields,vals)
        if out == True:
            self.view.ok(id_m,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL DETALLE')
        return

    def eliminar_pelicula(self):
        self.view.ask('ID Pelicula: ')
        id_m = input()
        count = self.model.delete_movie(id_m)
        if count != 0:
            self.view.ok(id_m,'borro')
        else:
            if count == 0:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA PELICULA. REVISA.')
        return

    #Metodos actor
    
    def actores_menu(self):
        o = '0'
        while o != 8:
            self.view.menu_actors()
            self.view.option('8')
            o = input()
            if o == '1':
                self.agregar_actor()
            elif o == '2':
                self.ver_actores()
            elif o == '3':
                self.buscar_actor()
            elif o == '4':
                self.buscar_actor_edad()
            elif o == '5':
                self.buscar_actor_pais()
            elif o == '6':
                self.actualizar_actor()
            elif o == '7':
                self.eliminar_actor()
            elif o == '8':
                return
            else:
                self.view.no_valid_option()
        return
    
    def ask_actor(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Primer Apellido: ')
        ln1 = input()
        self.view.ask('Segundo Apellido: ')
        ln2 = input()
        self.view.ask('Pais: ')
        pais = input()
        self.view.ask('Telefono: ')
        tel = input()
        self.view.ask('Edad: ')
        edad = input()
        return [name,ln1,ln2,pais,tel,edad]

    def agregar_actor(self):
        name, ln1, ln2, pais, tel, edad = self.ask_actor()
        out = self.model.create_actor(name, ln1, ln2, pais, tel, edad)
        if out == True:
            self.view.ok(name,'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL ACTOR ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL ERROR. REVISE.')
        return

    def ver_actores(self):
        out = self.model.read_actors()
        if type(out) == list:
            self.view.read_actors(out)
        else:
            self.view.error('PROBLEMA AL VER ACTORES. REVISA.')
        return

    def buscar_actor(self):
        self.view.ask('ID Actor: ')
        id_a = input()
        out = self.model.read_actor(id_a)
        if type(out) == tuple:
            self.view.read_actor(out)    
        else:
            if out == None:
                self.view.error('EL ACTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER ACTOR. REVISA.') 
        return

    def buscar_actor_edad(self):
        self.view.ask('Edad: ')
        edad = input()
        out = self.model.read_actors_age(edad)
        if type(out) == list:
            self.view.read_actors(out)    
        else:
            self.view.error('PROBLEMA AL LEER ACTORES. REVISA.') 
        return

    def buscar_actor_pais(self):
        self.view.ask('Pais: ')
        pais = input()
        out = self.model.read_actors_country(pais)
        if type(out) == list:
            self.view.read_actors(out)    
        else:
            self.view.error('PROBLEMA AL LEER ACTORES. REVISA.') 
        return

    def actualizar_actor(self):
        self.view.ask('ID Actor: ')
        id_a = input()
        out = self.model.read_actor(id_a)
        if type(out) == tuple:
            self.view.read_actor(out)    
        else:
            if out == None:
                self.view.error('EL ACTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER ACTOR. REVISA.') 
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_actor()
        fields, vals = self.update_lists(['fn_a','ln1_a','ln2_a','a_country','phone_a','a_age'],whole_vals)
        vals.append(id_a)
        vals = tuple(vals)
        print (fields, vals)
        out = self.model.update_actor(fields,vals)
        if out == True:
            self.view.ok(id_a,'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL ACTOR')
        return

    def eliminar_actor(self):
        self.view.ask('ID Actor: ')
        id_a = input()
        count = self.model.delete_actor(id_a)
        if count != 0:
            self.view.ok(id_a,'borro')
        else:
            if count == 0:
                self.view.error('EL ACTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL ACTOR. REVISA.')
        return

    
    #Metodos Directores
    def directores_menu(self):
        o = '0'
        while o != 8:
            self.view.menu_directors()
            self.view.option('8')
            o = input()
            if o == '1':
                self.agregar_director()
            elif o == '2':
                self.ver_directores()
            elif o == '3':
                self.buscar_director()
            elif o == '4':
                self.buscar_director_edad()
            elif o == '5':
                self.buscar_director_pais()
            elif o == '6':
                self.actualizar_director()
            elif o == '7':
                self.eliminar_director()
            elif o == '8':
                return
            else:
                self.view.no_valid_option()
        return

    def ask_director(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Primer Apellido: ')
        ln1 = input()
        self.view.ask('Segundo Apellido: ')
        ln2 = input()
        self.view.ask('Pais: ')
        pais = input()
        self.view.ask('Telefono: ')
        tel = input()
        self.view.ask('Edad: ')
        edad = input()
        return [name,ln1,ln2,pais,tel,edad]

    def agregar_director(self):
        name, ln1, ln2, pais, tel, edad = self.ask_director()
        out = self.model.create_director(name, ln1, ln2, pais, tel, edad)
        if out == True:
            self.view.ok(name,'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL DIRECTOR ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL DIRECTOR. REVISE.')
        return

    def ver_directores(self):
        out = self.model.read_directors()
        if type(out) == list:
            self.view.read_directors(out)
        else:
            self.view.error('PROBLEMA AL VER DIRECTORES. REVISA.')
        return

    def buscar_director(self):
        self.view.ask('ID Director: ')
        id_d = input()
        out = self.model.read_director(id_d)
        if type(out) == tuple:
            self.view.read_director(out)    
        else:
            if out == None:
                self.view.error('EL DIRECTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER DIRECTOR. REVISA.') 
        return

    def buscar_director_edad(self):
        self.view.ask('Edad: ')
        edad = input()
        out = self.model.read_directors_age(edad)
        if type(out) == list:
            self.view.read_directors(out)    
        else:
            self.view.error('PROBLEMA AL LEER DIRECTORES. REVISA.')
        return

    def buscar_director_pais(self):
        self.view.ask('Pais: ')
        pais = input()
        out = self.model.read_directors_country(pais)
        if type(out) == list:
            self.view.read_directors(out)    
        else:
            self.view.error('PROBLEMA AL LEER DIRECTORES. REVISA.')
        return

    def actualizar_director(self):
        self.view.ask('ID Director: ')
        id_d = input()
        out = self.model.read_director(id_d)
        if type(out) == tuple:
            self.view.read_director(out)    
        else:
            if out == None:
                self.view.error('EL DIRECTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER DIRECTOR. REVISA.') 
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_director()
        fields, vals = self.update_lists(['fn_d','ln1_d','ln2_d','d_country','phone_d','d_age'],whole_vals)
        vals.append(id_d)
        vals = tuple(vals)
        out = self.model.update_director(fields,vals)
        if out == True:
            self.view.ok(id_d,'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL DIRECTOR')
        return

    def eliminar_director(self):
        self.view.ask('ID Director: ')
        id_d = input()
        count = self.model.delete_director(id_d)
        if count != 0:
            self.view.ok(id_d,'borro')
        else:
            if count == 0:
                self.view.error('EL DIRECTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL DIRECTOR. REVISA.')
        return

    #Metodos Generos
    def generos_menu(self):
        o = '0'
        while o != 7:
            self.view.menu_genres()
            self.view.option('7')
            o = input()
            if o == '1':
                self.agregar_genero()
            elif o == '2':
                self.ver_generos()
            elif o == '3':
                self.buscar_genero()
            elif o == '4':
                self.buscar_peliculas_genero()
            elif o == '5':
                self.actualizar_genero()
            elif o == '6':
                self.eliminar_genero()
            elif o == '7':
                return
            else:
                self.view.no_valid_option()
        return

    def agregar_genero(self):
        self.view.ask('Genero: ')
        gen = input()
        out = self.model.create_genre(gen)
        if out == True:
            self.view.ok(gen,'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL GENERO ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL GENERO. REVISE.')
        return

    def ver_generos(self):
        out = self.model.read_genres()
        if type(out) == list:
            self.view.read_genres(out)
        else:
            self.view.error('PROBLEMA AL VER GENEROS. REVISA.')
        return

    def buscar_genero(self):
        self.view.ask('ID Genero: ')
        id_g = input()
        out= self.model.read_genre(id_g)
        if type(out) == tuple:
            self.view.read_genre(out)    
        else:
            if out == None:
                self.view.error('EL GENERO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER GENERO. REVISA.') 
        return

    def buscar_peliculas_genero(self):
        self.view.ask('ID Genero: ')
        id_g = input()
        out= self.model.read_m_genre(id_g)
        if type(out) == list:
            self.view.read_movies(out)    
        else:
            if out == None:
                self.view.error('EL GENERO NO TIENE PELICULAS')
            else:
                self.view.error('PROBLEMA AL LEER PELICULAS POR GENERO. REVISA.') 
        return

    def actualizar_genero(self):
        self.view.ask('ID Genero: ')
        id_g = input()
        out = self.model.read_genre(id_g)
        if type(out) == tuple:
            self.view.read_genre(out)    
        else:
            if out == None:
                self.view.error('EL GENERO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER GENERO. REVISA.') 
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        self.view.ask('Genero: ')
        whole_vals = []
        whole_vals.append(input())
        fields, vals = self.update_lists(['gen'],whole_vals)
        vals.append(id_g)
        vals = tuple(vals)
        out = self.model.update_genre(fields,vals)
        if out == True:
            self.view.ok(id_g,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL GENERO')
        return

    def eliminar_genero(self):
        self.view.ask('ID Genero: ')
        id_g = input()
        count = self.model.delete_genre(id_g)
        if count != 0:
            self.view.ok(id_g,'borro')
        else:
            if count == 0:
                self.view.error('EL GENERO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL GENERO. REVISA.')
        return

    
    #Metodos Clasificacion
    def clasificacion_menu(self):
        o = '0'
        while o != 7:
            self.view.menu_classification()
            self.view.option('7')
            o = input()
            if o == '1':
                self.agregar_clasificacion()
            elif o == '2':
                self.ver_clasificaciones()
            elif o == '3':
                self.buscar_clasificacion()
            elif o == '4':
                self.buscar_peliculas_clasificacion()
            elif o == '5':
                self.actualizar_clasificacion()
            elif o == '6':
                self.eliminar_clasificacion()
            elif o == '7':
                return
            else:
                self.view.no_valid_option()
        return

    def ask_classi(self):
        self.view.ask('Grado: ')
        grad = input()
        self.view.ask('Recomendado: ')
        rec = input()
        self.view.ask('Edad minima: ')
        emin = input()
        return [grad,rec,emin]
    
    def agregar_clasificacion(self):
        grad, rec, emin= self.ask_classi()
        out = self.model.create_classification(grad, rec, emin)
        if out == True:
            self.view.ok(grad,'agrego')
        else:
            if out.errno == 1062:
                self.view.error('LA CLASIFICACION ESTA REPETIDA')
            else:
                self.view.error('NO SE PUDO AGREGAR LA CLASIFICACION. REVISE.')
        return

    def ver_clasificaciones(self):
        out = self.model.read_classifications()
        if type(out) == list:
            self.view.read_classifications(out)
        else:
            self.view.error('PROBLEMA AL VER CLASIFICACIONES. REVISA.')
        return

    def buscar_clasificacion(self):
        self.view.ask('ID Clasificacion: ')
        id_c = input()
        out = self.model.read_classification(id_c)
        if type(out) == tuple:
            self.view.read_classification(out)    
        else:
            if out == None:
                self.view.error('LA CLASIFICACION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER CLASIFICACION. REVISA.') 
        return

    def buscar_peliculas_clasificacion(self):
        self.view.ask('ID Clasificacion: ')
        id_c = input()
        out= self.model.read_m_class(id_c)
        if type(out) == list:
            self.view.read_movies(out)    
        else:
            if out == None:
                self.view.error('LA CLASIFICACION NO TIENE PELICULAS')
            else:
                self.view.error('PROBLEMA AL LEER PELICULAS POR CLASIFICACION. REVISA.')
        return

    def actualizar_clasificacion(self):
        self.view.ask('ID Clasificacion: ')
        id_c = input()
        out = self.model.read_classification(id_c)
        if type(out) == tuple:
            self.view.read_classification(out)    
        else:
            if out == None:
                self.view.error('LA CLASIFICACION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER CLASIFICACION. REVISA.') 
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_classi()
        fields, vals = self.update_lists(['rate','recommended','min_age'],whole_vals)
        vals.append(id_c)
        vals = tuple(vals)
        out = self.model.update_classification(fields,vals)
        if out == True:
            self.view.ok(id_c,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA CLASIFICACION')
        return

    def eliminar_clasificacion(self):
        self.view.ask('ID Clasificacion: ')
        id_c = input()
        count = self.model.delete_classifications(id_c)
        if count != 0:
            self.view.ok(id_c,'borro')
        else:
            if count == 0:
                self.view.error('LA CLASIFICACION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA CLASIFICACION. REVISA.')
        return
