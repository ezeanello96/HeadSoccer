#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pilas
from pilas.escenas import Escena

class EscenaAyuda(Escena):
    '''Representa a la escena que se desarrolla en la ayuda del juego'''

    def __init__(self):
        Escena.__init__(self)
        self.fondo = pilas.fondos.Fondo('Fondo/fondo_ayuda.png')
        self.fondo.escala = 0.50
        self.crear_texto_ayuda()
        pilas.eventos.pulsa_tecla_escape.conectar(self.cuando_pulsa_tecla)
        
    def crear_texto_ayuda(self):
        titulo = pilas.actores.Texto("Controles", magnitud=30, y=230)
        titulo.color = pilas.colores.negro
        texto1 = pilas.actores.Texto('Jugador 1 (derecha): se mueve con las flechas.', y=40, x=0)
        texto2 = pilas.actores.Texto('Jugador 2 (izquierda): se mueve con las letras WASD.', y=-40, x=0)
        texto3 = pilas.actores.Texto('Pulsa ESC para regresar al menu', y=-218, x=0)
        texto1.color = pilas.colores.amarillo
        texto2.color = pilas.colores.amarillo
        texto3.color = pilas.colores.negro

    def cuando_pulsa_tecla(self, *k, **kv):
        import escena_menu
        escena_menu.EscenaMenu()
