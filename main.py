# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()

  dt = 0
  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  Player.containers = (updateable,drawable)
  Asteroid.containers = (updateable,drawable,asteroids)
  AsteroidField.containers = (updateable)
  Shot.containers = (updateable,drawable,shots)


  clock = pygame.time.Clock()
  screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

  player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
  asteroidfield = AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    pygame.Surface.fill(screen,(0,0,0))
    for item in drawable:
      item.draw(screen)
    updateable.update(dt)
    for shot in shots:
      for asteroid in asteroids:

        if shot.collide(asteroid):

          shot.kill()
          asteroid.split()

    for asteroid in asteroids:
      if player.collide(asteroid):
        print("Game Over!")
        return
    pygame.display.flip()
    dt=clock.tick(60)/1000
  

if __name__== "__main__":
  main()