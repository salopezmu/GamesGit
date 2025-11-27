#Autor: Sebastian Triana

#Caso de uso: Aprender a usar hilos por medio de un jueguito

import pygame
import threading
import random
import time


pygame.init()

COLOR_FONDO = (10, 10, 30)
COLOR_METEORO = (255, 80, 80)
COLOR_JUGADOR = (80, 200, 255)

#tamaño de la ventana
ANCHO = 1280
ALTO = 720

#posicion inicial de la navesita
# (estos valores ahora los maneja la clase Jugador)

#la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))

#creacion del reloj
reloj = pygame.time.Clock()
FPS = 60

juego_activo = True
perdiste = False  # <-- NUEVO

meteoros = [] 


#clase navesita
class Jugador:
    def __init__(self):
        #posición inicial de la navesita
        self.x = ANCHO / 2
        self.y = ALTO - 100
        self.ancho = 50
        self.alto = 50
        self.velocidad = 5

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidad

        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidad

        # Evitar que se salga del lado izquierdo
        if self.x < 0:
            self.x = 0

        # Evitar que se salga del lado derecho
        if self.x > ANCHO - self.ancho:
            self.x = ANCHO - self.ancho

    def dibujar(self, pantalla):
        #dibujo de la nave
        pygame.draw.rect(
            pantalla,
            COLOR_JUGADOR,  # color de la navesita
            (self.x, self.y, self.ancho, self.alto)  # tamaño de la navesita
        )


#Clase meteorito
class Meteoro(threading.Thread):
    def __init__(self):
        super().__init__()
        self.x = random.randint(0, ANCHO)
        self.y = -50
        self.velocidad = random.randint(3, 7)
        self.vivo = True

    def run(self):
        while self.vivo and juego_activo:
            self.y += self.velocidad

            if self.y > ALTO + 50:
                self.vivo = False  

            time.sleep(0.02) 

    def generador_meteoros():
        while juego_activo:
            nuevo = Meteoro()
            meteoros.append(nuevo)
            nuevo.start()  # inicia el hilo del meteoro

            time.sleep(0.7)  # cada cuanto se generan las piedras esas


# iniciar el generador de peñones
hilo_generador = threading.Thread(target=Meteoro.generador_meteoros)
hilo_generador.start()

# Crear jugador
jugador = Jugador()


#manejo de las colisiones
def hay_colision(jugador, meteoro):
    nave_rect = pygame.Rect(jugador.x, jugador.y, jugador.ancho, jugador.alto)
    meteoro_rect = pygame.Rect(meteoro.x - 20, meteoro.y - 20, 40, 40)
    return nave_rect.colliderect(meteoro_rect)


#loop principal
while juego_activo:
    reloj.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_activo = False

    pantalla.fill(COLOR_FONDO)

    if not perdiste:

        teclas = pygame.key.get_pressed()
        jugador.mover(teclas)
        jugador.dibujar(pantalla)

        for m in meteoros:
            if m.vivo:
                pygame.draw.circle(pantalla, COLOR_METEORO, (int(m.x), int(m.y)), 20)

                # DETECCION DE COLISION
                if hay_colision(jugador, m):
                    perdiste = True
                    juego_activo = False  # detener generador
                    break

    pygame.display.flip() #Se muestra todo lo dibujado


#Jajajaja, perdistes
pantalla.fill((0, 0, 0))

fuente = pygame.font.Font(None, 100)
texto = fuente.render("Jajajajaj, que malo eres!", True, (255, 0, 0))
pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, ALTO//2 - texto.get_height()//2))

pygame.display.flip()

time.sleep(3)

pygame.quit()


