import pygame
import threading
import random
from threading import *


class Game:
    def __init__(self):
        self.jug = Player(320, 700, 10, 10)
        self.clock = pygame.time.Clock()
        self.enemya = Enemya(random.randint(0, 640), -30)
        self.enemya2 = Enemya(random.randint(0, 640), -30)
        self.enemya3 = Enemya(random.randint(0, 640), -20)
        self.internalclock = 0
        self.play = Spritep()
        self.bg = pygame.image.load("Img/bg.png")
        self.puntaje = Puntaje()
        
    def inicializar_ventana(self):
        self.ventana = pygame.display.set_mode((640, 720))
        pygame.display.set_caption("Tuhu")
        pygame.mixer.music.load("Sounds/bgsong.ogg")
        pygame.mixer.music.play(-1)
    def crear_bucle(self):
        self.bucle = True
        while self.bucle == True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.bucle = False
            
            self.ventana.fill((0,0,0))
            
            self.internalclock += 1
            
            #Player----------------------
            
            self.jug.crear_jugador(self.ventana)
            self.jug.mover_jugador()
            self.jug.disparar(self.ventana)
            
            #Bullets---------------------------------
            self.jug.mostrar_disparo(self.ventana)
            self.jug.esperar_disparo()
            
            
            #Basic_enemyA----------------------------
            
            #EnemyA1---------------------------------------------------------------
            if self.internalclock >= 60:
                self.hil1 = threading.Thread(target= self.enemya.esperar_movimiento(), daemon= True)
                self.hil1.start()
                if self.enemya.cooldownp == 0:
                    self.enemya.mover_enemigo()
                self.enemya.crear_enemigo(self.ventana)
                
                self.hil2 = threading.Thread(target=self.enemya.disparar(), daemon= True)
                self.hil2.start()
                self.hil3 = threading.Thread(target=self.enemya.esperar_disparo(), daemon= True)
                self.hil3.start()
                self.enemya.mostrar_disparo(self.ventana)
                self.hil9 = threading.Thread(target=self.enemya.esperar_reaparecer(), daemon=True)  
                self.hil9.start()
            
            #EnemyA2----------------------------------------------------------------
            if self.internalclock >= 120:
                self.hil4 = threading.Thread(target= self.enemya2.esperar_movimiento(), daemon= True)
                self.hil4.start()
                if self.enemya2.cooldownp == 0:
                    self.enemya2.mover_enemigo()
                self.enemya2.crear_enemigo(self.ventana)
                
                self.hil5 = threading.Thread(target=self.enemya2.disparar(), daemon= True)
                self.hil5.start()
                self.hil6 = threading.Thread(target=self.enemya2.esperar_disparo(), daemon= True)
                self.hil6.start()
                self.enemya2.mostrar_disparo(self.ventana)
                self.hil12 = threading.Thread(target=self.enemya2.esperar_reaparecer(), daemon=True)  
                self.hil12.start()
            
            #EnemyA3-----------------------------------------------------------------
            if self.internalclock >= 130:
                self.hil13 = threading.Thread(target= self.enemya3.esperar_movimiento(), daemon= True)
                self.hil13.start()
                if self.enemya3.cooldownp == 0:
                    self.enemya3.mover_enemigo()
                self.enemya3.crear_enemigo(self.ventana)
                
                self.hil14 = threading.Thread(target=self.enemya3.disparar(), daemon= True)
                self.hil14.start()
                self.hil15 = threading.Thread(target=self.enemya3.esperar_disparo(), daemon= True)
                self.hil15.start()
                self.enemya3.mostrar_disparo(self.ventana)
                self.hil16 = threading.Thread(target=self.enemya3.esperar_reaparecer(), daemon=True)  
                self.hil16.start()
                
            #--------------------------Colision-----------------------------
            for b in self.jug.balas:
                if b.collision.colliderect(self.enemya.collision) and self.internalclock > 100:
                    self.hil7 = threading.Thread(target=self.enemya.crear_poder(), daemon=True)
                    self.hil7.start()
                    self.jug.balas.remove(b)
                    self.puntaje.puntaje += 2
            for b in self.jug.balas:
                if b.collision.colliderect(self.enemya2.collision) and self.internalclock > 120:
                    self.hil11 = threading.Thread(target=self.enemya2.crear_poder(), daemon=True)
                    self.hil11.start()
                    self.jug.balas.remove(b)
                    self.puntaje.puntaje += 2
            for b in self.jug.balas:
                if b.collision.colliderect(self.enemya3.collision) and self.internalclock > 120:
                    self.hil17 = threading.Thread(target=self.enemya3.crear_poder(), daemon=True)
                    self.hil17.start()
                    self.jug.balas.remove(b)
                    self.puntaje.puntaje += 2
                    
                    
                    
            self.enemya.soltar_poder(self.ventana)
            self.enemya2.soltar_poder(self.ventana)
            self.enemya3.soltar_poder(self.ventana)
            
            
            for p in self.enemya.power:
                if self.jug.collision.colliderect(p.collision) and self.jug.powcooldown <= 0:
                    self.jug.powcooldown = 10
                    if self.jug.power < 40: 
                        self.jug.aumentar_power()
                    print(self.jug.power)
                    self.enemya.power.remove(p)
                    self.puntaje.puntaje += 5
                    
            for p in self.enemya2.power:
                if self.jug.collision.colliderect(p.collision) and self.jug.powcooldown <= 0:
                    self.jug.powcooldown = 10
                    if self.jug.power < 40: 
                        self.jug.aumentar_power()
                    print(self.jug.power)
                    self.enemya2.power.remove(p)
                    self.puntaje.puntaje += 5
                    
            for p in self.enemya3.power:
                if self.jug.collision.colliderect(p.collision) and self.jug.powcooldown <= 0:
                    self.jug.powcooldown = 10
                    if self.jug.power < 40: 
                        self.jug.aumentar_power()
                    self.enemya3.power.remove(p)
                    self.puntaje.puntaje += 5
                    
                    
                    
            self.jug.powcooldown -= 1
            
            for b in self.enemya.balas:
                if self.jug.collision.colliderect(b.collision):
                    self.terminar_aplicacion()
            
            for b in self.enemya2.balas:
                if self.jug.collision.colliderect(b.collision):
                    self.terminar_aplicacion()
                    
            for b in self.enemya3.balas:
                if self.jug.collision.colliderect(b.collision):
                    self.terminar_aplicacion()
            
            #---------------------Sprites-------------------------------------------------------------
            
            self.hil8 = threading.Thread(target = self.play.definir_sprite(), daemon=True)
            self.hil8.start()
            #-------------------------Puntaje-------------------------------
            if self.internalclock % 60 == 0:
                self.puntaje.puntaje += 1
                
            #---------------------Terminan todos los eventos que requieran actualizacion--------------
            self.actualizar_pantalla()
            

    def actualizar_pantalla(self):
        self.ventana.blit(self.bg, (0, 0))
        self.jug.cargar_sprite(self.ventana)
        self.enemya.mostrar_sprite(self.ventana)
        self.enemya2.mostrar_sprite(self.ventana)
        self.enemya3.mostrar_sprite(self.ventana)
        self.enemya.mostrar_spritep(self.ventana)
        self.enemya2.mostrar_spritep(self.ventana)
        self.enemya3.mostrar_spritep(self.ventana)
        self.ventana.blit(self.puntaje.mostrar_puntaje(), self.puntaje.textrect)
        pygame.display.update()
        self.clock.tick(60)
        
    def terminar_aplicacion(self):
        pygame.quit()
        
        
        
        
        
#----------------Logica de pygame------------^^^^^^


class Player():
    def __init__(self, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 4
        self.balas = []
        self.cooldown = 0
        self.power = 0
        self.powcooldown = 0
        
    def crear_jugador(self, juego):    
        pygame.draw.rect(juego, (255, 0, 0), (self.x, self.y, self.ancho, self.alto))
        self.collision = pygame.Rect(self.x, self.y, self.ancho, self.alto)
    def mover_jugador(self):
        self.teclas = pygame.key.get_pressed()
        if self.teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocidad
        if self.teclas[pygame.K_RIGHT] and self.x < 640:
            self.x += self.velocidad
        if self.teclas[pygame.K_UP] and self.y > 0:
            self.y -= self.velocidad
        if self.teclas[pygame.K_DOWN] and self.y < 720:
            self.y += self.velocidad
        # Movimiento normal------------------
        if self.teclas[pygame.K_LSHIFT]:
            self.velocidad = 6
        elif self.teclas[pygame.K_LCTRL]:
            self.velocidad = 2
        else:
            self.velocidad = 4
        # Movimiento rapido o lento--------------------
        
    def disparar(self, ventana):
        if self.teclas[pygame.K_z] and self.cooldown <= 0:
            self.bala = Playerproyectile(self.x + 3, self.y)
            self.balas.append(self.bala)
            self.cooldown = 50 - self.power
    
    def esperar_disparo(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        
    def mostrar_disparo(self, ventana):
        for b in self.balas:
            b.desplazar_bala()
            b.crear_bala(ventana)
        self.balas = [b for b in self.balas if b.y >= -10]

    def cargar_sprite(self, ventana):
        self.play = Spritep()
        self.hil = threading.Thread(target = self.play.definir_sprite(), daemon=True)
        self.hil.start()
        for b in self.balas:
            ventana.blit(b.image, (b.x, b.y))
        ventana.blit(self.play.image, (self.x- 20, self.y - 30))
    def aumentar_power(self):
        self.power += 2

#------------Logica jugador--------^^^^

class Playerproyectile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 10
        self.alto = 10
        self.velocidad = 12
        self.image = pygame.image.load("Img/playerbull.png")
        
    def crear_bala(self, juego):
        self.bala = pygame.draw.rect(juego, (255, 255, 255), (self.x, self.y, self.ancho, self.alto))
    def desplazar_bala(self):
        self.y -= self.velocidad
        self.collision = pygame.Rect(self.x, self.y, 10, 10)
        
#-----------Logica balas------------^^^^^^

class Enemya():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 0
        self.esperar = 100
        self.direccionx = 320
        self.direcciony = -20
        self.balas = []
        self.cooldown = 100
        self.collision = pygame.Rect(self.x, self.y, 20, 20)
        self.power = []
        self.cooldownp = 0
    def mover_enemigo(self):
        if self.esperar <= 0:
            self.direccionx = random.randint(10, 630)
            self.direcciony = random.randint(10, 200)
            
            self.esperar = 100
        
        self.x += (self.direccionx - self.x)/10
        self.y += (self.direcciony - self.y)/5
        
        self.collision = pygame.Rect(self.x, self.y, 20, 20)

    def esperar_movimiento(self):
        if self.esperar > 0:
            self.esperar -= 1
    def crear_enemigo(self, venatana):
        pygame.draw.rect(venatana, (0, 255, 0), (self.x, self.y, 20, 20))
        
    def esperar_disparo(self):
        if self.cooldown > 0 :
            self.cooldown -= 1
        
    def disparar(self):
        if self.cooldown <= 0 and self.cooldownp <= 0:
            self.bullet = Enemyabullet(self.x, self.y, 2)
            self.bullet2 = Enemyabullet(self.x, self.y, 0)
            self.bullet3 = Enemyabullet(self.x, self.y, -2)
            self.balas.append(self.bullet)
            self.balas.append(self.bullet2)
            self.balas.append(self.bullet3)
            self.cooldown = random.randint(10, 40)
        
    def mostrar_disparo(self,ventana):
        for b in self.balas:
            b.crear(ventana)
            b.mover_bala()
            
            
        self.balas = [b for b in self.balas if b.y < 730]
        self.balas = [b for b in self.balas if b.x > 0 and b.x < 640]
        
    def crear_poder(self):
        if self.cooldownp <= 0:
            self.cooldownp = random.randint(60, 120)
            self.powers = Power_up(self.x, self.y)
            self.power.append(self.powers)
            self.x = random.randint(0, 640)
            self.y = -30
        
    def soltar_poder(self, ventana):    
        for p in self.power:
            p.crear_power(ventana)
            p.mover_power()
            
            
        self.power = [p for p in self.power if p.y < 730]
        
    def mostrar_spritep(self, ventana):
        for p in self.power:
            ventana.blit(p.image, (p.x, p.y))
            
    def esperar_reaparecer(self):
        if self.cooldownp > 0:
            self.cooldownp -= 1        
    
    def mostrar_sprite(self, ventana):
        self.sprit = Spritea()
        for b in self.balas:
            ventana.blit(b.image, (b.x, b.y))
        ventana.blit(self.sprit.image, (self.x- 5, self.y- 4))
    
#-------------Enemigo A (movimiento aleatorio alrededor y disparo)------------^^^^^^


class Enemyabullet(pygame.sprite.Sprite):
    def __init__ (self , x, y, velocidad):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.collision = pygame.Rect(self.x, self.y, 7, 7)
        self.image = pygame.image.load("Img/enemyabull.png")
    def crear(self, ventana):
        pygame.draw.rect(ventana,(255, 255, 255), (self.x + 5, self.y + 13, 7, 7))
        
    def mover_bala(self):
        self.y += 4
        self.x -= self.velocidad 
        self.collision = pygame.Rect(self.x, self.y, 7, 7)
        

        
        
        
#-----------------------EnemyA bullet---------------^^^^^^

class Power_up(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x  
        self.y = y
        self.ancho = 15
        self.alto = 15
        self.velocidad = random.randint(2, 10)
        self.collision = pygame.Rect(self.x, self.y, 15, 15)
        self.image = pygame.image.load("img/power.png")
    def crear_power(self, ventana):
        pygame.draw.rect(ventana, (0, 0, 255), (self.x,self.y, self.ancho, self.alto))
    def mover_power(self):
        self.y += self.velocidad
        self.collision = pygame.Rect(self.x, self.y, 15, 15)

#-------------------------Power up------------------------^^^^^^

class Spritep(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("Img/rc.png")
    def definir_sprite(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_LEFT]:
            self.image = pygame.image.load("Img/rl.png")
        elif self.keys[pygame.K_RIGHT]:
            self.image = pygame.image.load("Img/rr.png")
        else:
            self.image = pygame.image.load("Img/rc.png")
            

class Spritea(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("Img/ena.png")


#-----------------------Sprites ^^^^^^^^-------------------------


class Puntaje():
    def __init__(self):
        self.font = pygame.font.SysFont("Comic_sans", 24)
        self.puntaje = 0
        self.textrect = pygame.Rect(50, 640, 10, 10)
    def mostrar_puntaje(self):
                self.texto = self.font.render(f"Puntaje: {self.puntaje}", True, (255, 255, 255))
                return self.texto
            



#------------------------------Puntaje----------------^^^^^^^^
def main():
    pygame.init()
    tuhu = Game()
    tuhu.inicializar_ventana()
    tuhu.crear_bucle()
    
if __name__ == "__main__":
    main()