import pygame
import sys

class Board:
  def __init__(self):
    self.image = pygame.image.load('./assets/board.png')
    self.grid = [
       [0,0,0],
       [0,0,0],
       [0,0,0]
      ]
    
  def getBoardImage(self,font):
    value1 = font.render(str(self.grid[0][0]) , True , (0,0,0))
    self.image.blit(value1 , (300,100))
    return self.image
  
  def showBoardGrid(self):
    pass
  
  def renderPlayerImage(self , player):
    pass
    
    
class Game:
  def __init__(self):
    self.board = Board()
    self.player1 = Player('./assets/o.png' , 'X')
    self.player2 = Player("./assets/o.png" , 'O')
    self.end = False
    
  def getBoard(self):
    return self.board
  
  def getPlayer1(self):
    return self.player1
  
  def getPlayer2(self):
    return self.player2
  
  def getEnd(self):
    return self.end
  
  def start_game(self):
    pass
  
  def check_winner(self):
    pass
  
  
  
    

class Player:
  def __init__(self , text , symbol):
    self.image = pygame.image.load(text)
    self.symbol = symbol
    self.winner = False
  
  def getPlayerImage(self):
    return self.image
  
  def getPlayerSymbol(self):
    return self.symbol
  
  def getIsWinner(self):
    return self.winner
  
  def play(self):
    # check the nature of the player in order to render the right symbol
    pass  
  




if __name__ == "__main__":
    
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    text_font = pygame.font.SysFont(None ,30)
    clock = pygame.time.Clock()
    

    while True:
        
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
            

      screen.fill("white")
      # RENDER YOUR GAME HERE
      game = Game()
      screen.blit(game.getBoard().getBoardImage(text_font) , (0,0))
    
      
      

      # flip() the display to put your work on screen
      pygame.display.flip()
      clock.tick(60)  # limits FPS to 60