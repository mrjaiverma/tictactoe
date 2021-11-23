#Drawing shapes in PyGame 

import pygame

pygame.init() #this will initialise/start pygame 

screen = pygame.display.set_mode((600, 600)) #creates a screen to work with in pygame 
screen.fill((245, 136, 64))

running = True         #tells the loop that the program is still running 

image_X = pygame.image.load('X.png')
image_O = pygame.image.load('O.png')
count = 0 
winning = False
board = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def winning_or_not(): 
    global board, winning
    #win for cols
    for row in range(3): 
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != 0: 
            pygame.draw.line(screen, (0, 0, 0), (row*200 + 100, 0), (row*200 + 100, 600), 5)    
            winning = True
            break
    #win for rows
    for col in range(3): 
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0: 
            pygame.draw.line(screen, (0, 0, 0), (0, col*200+100), (600, col*200+100), 5)
            winning = True
            break
            
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0: 
        pygame.draw.line(screen, (0, 0, 0), (0, 0), (600, 600), 5)
        winning = True
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0: 
        pygame.draw.line(screen, (0, 0, 0), (600, 0), (0, 600), 5)
        winning = True        
        
while running: 
    for event in pygame.event.get():
        winning_or_not()
        pygame.display.flip()
        global count, winning
        if event.type == pygame.QUIT:
            running = False 
    #pygame.draw.rect(screen, (155,155,155), (200,200,200,200))
        pygame.draw.line(screen, (184, 82, 82), (200, 0), (200,600), 10)
        pygame.draw.line(screen, (184, 82, 82), (400, 0), (400,600), 10)
        pygame.draw.line(screen, (184, 82, 82), (0, 200), (600,200), 10)
        pygame.draw.line(screen, (184, 82, 82), (0, 400), (600,400), 10)
        if event.type == pygame.MOUSEBUTTONDOWN:
          x, y = pygame.mouse.get_pos()
          x = int(x/200)
          y = int(y/200)
          if x == 0 and y == 0 and board[x][y] == 0 and winning==False: 
               if count%2 == 0: 
                  screen.blit(image_X, (0, 0))
                  board[x][y] = '1'
               else: 
                  screen.blit(image_O, (0, 0))
                  board[x][y] = '2'
          elif x == 1 and y == 0 and board[x][y] == 0 and winning==False:
               if count%2 == 0: 
                  screen.blit(image_X, (200, 0))
                  board[x][y] = '1'
               else: 
                  screen.blit(image_O, (200, 0))
                  board[x][y] = '2'
          elif x == 2 and y == 0 and board[x][y] == 0 and winning==False: 
               if count%2 == 0: 
                  screen.blit(image_X, (400, 0))
                  board[x][y] = '1'
               else: 
                  screen.blit(image_O, (400, 0))  
                  board[x][y] = '2'
          elif x == 0 and y == 1 and board[x][y] == 0 and winning==False: 
               if count%2 == 0: 
                  board[x][y] = '1'
                  screen.blit(image_X, (0, 200))
               else: 
                  screen.blit(image_O, (0, 200))
                  board[x][y] = '2'
          elif x == 1 and y == 1 and board[x][y] == 0 and winning==False: 
               if count%2 == 0: 
                  board[x][y] = '1'  
                  screen.blit(image_X, (200, 200))
               else: 
                  screen.blit(image_O, (200, 200))
                  board[x][y] = '2'
          elif x == 2 and y == 1 and board[x][y] == 0 and winning==False: 
               if count%2 == 0:
                  board[x][y] = '1'
                  screen.blit(image_X, (400, 200))
               else: 
                  board[x][y] = '2'
                  screen.blit(image_O, (400, 200))  
          elif x == 0 and y == 2 and board[x][y] == 0 and winning==False:
               if count%2 == 0: 
                  board[x][y] = '1'
                  screen.blit(image_X, (0, 400))
               else: 
                  board[x][y] = '2'
                  screen.blit(image_O, (0, 400))  
          elif x == 1 and y == 2 and board[x][y] == 0 and winning==False: 
               if count%2 == 0: 
                  board[x][y] = '1'
                  screen.blit(image_X, (200, 400))
               else: 
                  board[x][y] = '2'
                  screen.blit(image_O, (200, 400))  
          elif x == 2 and y == 2 and board[x][y] == 0 and winning==False:  
               if count%2 == 0: 
                  board[x][y] = '1'
                  screen.blit(image_X, (400, 400))
               else: 
                  board[x][y] = '2'
                  screen.blit(image_O, (400, 400))  
          count = count + 1
    pygame.display.update()
    
pygame.quit()
