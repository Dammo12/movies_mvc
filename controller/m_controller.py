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
                self.eliminar_pelicula()
            elif o == '11':
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
            self.view.read_m_cast(out)    
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
        return
        
