#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pilas
import escena_menu


class HeadSoccer:
    '''Clase que llama a la escena menú para que comience el juego.'''
    
    def __init__(self):
        '''Inicia pilas con título "Head Soccer", y gravedad 0.'''
        pilas.iniciar(titulo='Head Soccer', gravedad=(0, 0))
        self.empezar()
        
    def empezar(self):
        '''Ejecuta la clase "Menu".'''
        escena_menu.EscenaMenu()
        pilas.ejecutar()
        

if __name__ == '__main__':
    '''El juego será ejecutado solo si se abre este achivo, al ser llamado por otro habrá que ejecutar la clase:
    
    >>> import HeadSoccer
    >>> HeadSoccer.HeadSoccer()
    '''
    HeadSoccer()
