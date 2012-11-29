#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pilas
from pilas.actores import Actor
from pilas.simbolos import *
from pilas.comportamientos import *

class Jugador_2(Actor):
    """Este seria uno de los jugadores"""

    def __init__(self, x=0, y=0):
        pilas.actores.Actor.__init__(self, x=x, y=y)
        """Ahora agregamos la imagen al actor"""
        self.imagen = pilas.imagenes.cargar('Personajes/messi.png')
        """Le damos una escala apropiada para que no sea tan grande"""
        self.escala = 0.20
        """Le agrandamos su radio de colision"""
        self.radio_de_colision = 17
        """Le decimos que nunca salga de la pantalla"""
        self.aprender(pilas.habilidades.SeMantieneEnPantalla)
        """Se puede mover con las flechas del teclado"""
        self.aprender(pilas.habilidades.MoverseConElTeclado)
        
   

