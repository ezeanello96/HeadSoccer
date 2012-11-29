#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pilas


class Puntaje1(pilas.actores.Puntaje):
    '''Representa el puntaje del jugador rojo'''

    def __init__(self, x=-70, y=210):
        pilas.actores.Puntaje.__init__(self, x=x, y=y)
        self.color = pilas.colores.blanco
        self.escala = 1.75
        
        
class Puntaje2(pilas.actores.Puntaje):
    '''Representa el puntaje del jugador azul'''

    def __init__(self, x=70, y=210):
        pilas.actores.Puntaje.__init__(self, x=x, y=y)
        self.color = pilas.colores.blanco
        self.escala = 1.75
