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
  def __init__(self):
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
  
  def renderPlayerImage(self):
    pass
    
    
class Game:
  def __init__(self):
    self.board = Board()
    self.playerX = Player('./assets/x.png' , 'X')
    self.playerO = Player("./assets/o.png" , 'O')
    self.end = False
    self.playerTurn = self.playerX
  
  def start_game(self):
    pass
  
  def check_winner(self):
    # 3 horizental, 3 vertical , 2 diagonal
    # horizental
      if (self.board.grid[0][0].value is not None and self.board.grid[0][0].value == self.board.grid[0][1].value and self.board.grid[0][0].value == self.board.grid[0][2].value or
        self.board.grid[1][0].value is not None and self.board.grid[1][0].value == self.board.grid[1][1].value and self.board.grid[1][0].value == self.board.grid[1][2].value or
        self.board.grid[2][0].value is not None and self.board.grid[2][0].value == self.board.grid[2][1].value and self.board.grid[2][0].value == self.board.grid[2][2].value):
          self.playerTurn.winner = True
          self.end = True
        
      
      # vertical
      elif (self.board.grid[0][0].value is not None and self.board.grid[0][0].value == self.board.grid[1][0].value and self.board.grid[0][0].value == self.board.grid[2][0].value or
        self.board.grid[0][1].value is not None and self.board.grid[0][1].value == self.board.grid[1][1].value and self.board.grid[0][1].value == self.board.grid[2][1].value or
        self.board.grid[0][2].value is not None and self.board.grid[0][2].value == self.board.grid[1][2].value and self.board.grid[0][2].value == self.board.grid[2][2].value):
          self.playerTurn.winner = True
          self.end = True
        
      # diagonale
      elif (self.board.grid[0][0].value is not None and self.board.grid[0][0].value == self.board.grid[1][1].value and self.board.grid[0][0].value == self.board.grid[2][2].value or
        self.board.grid[0][2].value is not None and self.board.grid[0][2].value == self.board.grid[1][1].value and self.board.grid[0][2].value == self.board.grid[2][0].value):
          self.playerTurn.winner = True
          self.end = True
      else:
        self.end = all(box.value is not None for row in self.board.grid for box in row)
        
      
  
  # def isEnd(self):
  #   self.end = all(box.value is not None for row in self.board.grid for box in row)
  
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
  



def render_text(screen, text, font, color, position):
    # Render the text and blit it to the screen at the given position
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)
if __name__ == "__main__":
    
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    text_font = pygame.font.SysFont(None ,30)
    clock = pygame.time.Clock()
    game = Game()
    while True:
      
      # print("end : " , game.end)
        
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
          if mouse_click[0] and not game.end: 
            if x_pos - 50 <= mouse_pos[0] <=  x_pos + 50 and y_pos - 50 <= mouse_pos[1] <=  y_pos + 50 :
              
              # if game.end:
              #   break
              # game.isEnd()
              # print(f"Mouse clicked at value{i}{j}")
              # print("end : " , game.end)
              if box.value is None: # so we dont replace existing value
                if game.playerTurn == game.playerX:
                  box.value =  "X"
                  game.playerX.boxes.append(box)
                  # game.switchTurn()
                else:
                  box.value =  "O"
                  game.playerO.boxes.append(box)
                  # game.switchTurn()
                
                game.check_winner()
                if not game.end:  # Only switch turn if game has not ended
                  game.switchTurn()
                else:
                  break  
      
          if box.value ==  "X" :
            x_img = pygame.image.load('./assets/x.png')
            x_img = pygame.transform.scale(x_img , (100,100))
            screen.blit(x_img, (x_pos - 50, y_pos - 50))
          if box.value == "O":
            o_img = pygame.image.load('./assets/o.png')
            o_img = pygame.transform.scale(o_img , (100,100))
            screen.blit(o_img, (x_pos - 50, y_pos - 50))
      
      if game.end:
        if game.playerX.winner:
          # print("Winner: X")
          render_text(screen, "X won", text_font, (0,0,255), (400,600))
        elif game.playerO.winner:
          # print("Winner: O")
          render_text(screen, "O won", text_font, (255,0,0), (400,600))
        else:
          # print("It's a tie!")
          render_text(screen, "tie", text_font, (0,0,0), (400,600))
        
        render_text(screen, "new game", text_font, (0,0,0), (400,650))
        if mouse_click[0]:
          if 400 - 100 <= mouse_pos[0] <=  400 + 100 and 650 - 30 <= mouse_pos[1] <=  650 + 30 :
            game = Game()
            # print("clikcedkkdkdkdkd")
      else:
        render_text(screen, f"{game.playerTurn.symbol} turn", text_font, (0,0,0), (400,550))
        
      
      # flip() the display to put your work on screen
      pygame.display.flip()
      clock.tick(60)  # limits FPS to 60