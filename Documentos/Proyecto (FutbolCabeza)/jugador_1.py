#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pilas
from pilas.actores import Actor
from pilas.simbolos import *
from pilas.comportamientos import *

class Jugador_1(Actor):
    """Este seria uno de los jugadores"""

    def __init__(self, x=0, y=0):
        pilas.actores.Actor.__init__(self, x=x, y=y)
        """Ahora agregamos la imagen al actor"""
        self.imagen = pilas.imagenes.cargar('Personajes/CRISTIANO.png')
        """Le damos una escala apropiada para que no sea tan grande"""
        self.escala = 0.20
        """Le agrandamos su radio de colision"""
        self.radio_de_colision = 17
        """Le decimos que nunca salga de la pantalla"""
        self.aprender(pilas.habilidades.SeMantieneEnPantalla)
        """Se puede mover con las flechas del teclado"""
        self.aprender(self.MoverseConWSAD)
    
    class MoverseConWSAD(pilas.habilidades.Habilidad):
        '''Hace que un actor se pueda mover con las teclas:
        
        W --> arriba
        S --> abajo
        A --> izquierda
        D --> derecha
        
        Facilita el uso de un segundo mando, muy usado en juegos multiplayer'''

        def __init__(self, receptor):
            pilas.habilidades.Habilidad.__init__(self, receptor)
            self.w = False
            self.a = False
            self.d = False
            self.s = False
            self.receptor = receptor
            pilas.eventos.actualizar.conectar(self.pulsa_tecla)
            pilas.eventos.pulsa_tecla.conectar(self.cuando_pulsa_la_tecla)
            pilas.eventos.suelta_tecla.conectar(self.cuando_suelta_la_tecla)
            
        def pulsa_tecla(self, evento):
            velocidad = 5

            if self.w:
                self.receptor.y += velocidad
            elif self.s:
                self.receptor.y -= velocidad
                
            if self.d:
                self.receptor.x += velocidad
            elif self.a:
                self.receptor.x -= velocidad              

        def cuando_pulsa_la_tecla(self, evento):
            self.procesar_cambio_de_estado_en_la_tecla(evento.codigo, True)

        def cuando_suelta_la_tecla(self, evento):
            self.procesar_cambio_de_estado_en_la_tecla(evento.codigo, False)
                
        def procesar_cambio_de_estado_en_la_tecla(self, codigo, estado):
            mapa = {
                w: 'w',
                s: 's',
                a: 'a',
                d: 'd',
            }

            if mapa.has_key(codigo):
                setattr(self, mapa[codigo], estado)


