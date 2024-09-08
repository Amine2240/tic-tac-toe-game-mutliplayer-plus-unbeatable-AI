import pygame
import sys

class Box:
  def __init__(self , i , j):
    rect_width = 50
    rect_height = 50
    rect_position = (i * 150 + 300, j * 150 + 100)
    self.image_space_rect = pygame.Rect(rect_position[0], rect_position[1], rect_width, rect_height)
    self.value = None
    # self.image = ""
    # self.img_rect = self.image.get_rect()
    
class Board:
  def __init__(self , font):
    self.image = pygame.image.load('./assets/board.png')
    self.grid = [
       [0,0,0],
       [0,0,0],
       [0,0,0]
      ]
    for i in range(3):
        for j in range(3):
          box = Box(i , j)
          self.grid[i][j] = box
          # self.image.blit(box.text_surface, box.text_rect)
    

  def getBoardImage(self):
    return self.image
  # def getBoardGrid(self):
  #   return self.grid
  
  def showBoardGrid(self):
    pass
  
  def renderPlayerImage(self , player):
    pass
    
    
class Game:
  def __init__(self , font):
    self.board = Board(font)
    self.playerX = Player('./assets/x.png' , 'X')
    self.playerO = Player("./assets/o.png" , 'O')
    self.end = False
    self.playerTurn = self.playerX
  
  def start_game(self):
    pass
  
  def check_winner(self):
    pass
  
  def isEnd(self):
    self.end = all(box.value is not None for row in self.board.grid for box in row)
  
  def switchTurn(self):
    if self.end == False:
      if self.playerTurn == self.playerX:
        self.playerTurn = self.playerO
      else:
        self.playerTurn = self.playerX
  
  
  
    

class Player:
  def __init__(self , text , symbol):
    self.image = pygame.image.load(text)
    self.symbol = symbol
    self.winner = False
    self.boxes = []
  
  def play(self):
    # check the nature of the player in order to render the right symbol
    pass  
  




if __name__ == "__main__":
    
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    text_font = pygame.font.SysFont(None ,30)
    clock = pygame.time.Clock()
    game = Game(text_font)
    while True:
        
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          
            

      screen.fill("white")
      # RENDER YOUR GAME HERE
      
      screen.blit(game.board.getBoardImage() , (0,0))
      mouse_pos = pygame.mouse.get_pos()
      mouse_click = pygame.mouse.get_pressed()
      for i in range(3):
        for j in range(3): 
          box = game.board.grid[i][j]
          x_pos = game.board.grid[i][j].image_space_rect.x
          y_pos = game.board.grid[i][j].image_space_rect.y
          if mouse_click[0]: 
            if x_pos - 50 <= mouse_pos[0] <=  x_pos + 50 and y_pos - 50 <= mouse_pos[1] <=  y_pos + 50 :
              game.isEnd()
              print(f"Mouse clicked at value{i}{j}")
              print("end : " , game.end)
              if box.value is None: # so we dont replace existing value
                if game.playerTurn == game.playerX:
                  box.value =  "X"
                  game.playerX.boxes.append(box)
                  game.switchTurn()
                else:
                  box.value =  "O"
                  game.playerO.boxes.append(box)
                  game.switchTurn()
                
                
      
          if box.value ==  "X":
            x_img = pygame.image.load('./assets/x.png')
            x_img = pygame.transform.scale(x_img , (100,100))
            screen.blit(x_img, (x_pos - 50, y_pos - 50))
          if box.value == "O":
            o_img = pygame.image.load('./assets/o.png')
            o_img = pygame.transform.scale(o_img , (100,100))
            screen.blit(o_img, (x_pos - 50, y_pos - 50))

      # flip() the display to put your work on screen
      pygame.display.flip()
      clock.tick(60)  # limits FPS to 60