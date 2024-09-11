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
    
    
class Game:
  def __init__(self):
    self.board = Board()
    self.playerX = Player('./assets/x.png' , 'X')
    self.playerO = AiPlayer(self,"./assets/o.png" , 'O')
    self.end = False
    self.playerTurn = self.playerX
  
  def check_winner(self):
    # Check horizontals
    for row in range(3):
        if self.board.grid[row][0].value is not None and \
           self.board.grid[row][0].value == self.board.grid[row][1].value == self.board.grid[row][2].value:
            self.end = True
            if self.board.grid[row][0].value == "O":
              self.playerO.winner = True
              return 1
            else:
              self.playerX.winner = True
              return -1

    # Check verticals
    for col in range(3):
        if self.board.grid[0][col].value is not None and \
           self.board.grid[0][col].value == self.board.grid[1][col].value == self.board.grid[2][col].value:
            self.end = True
            if self.board.grid[0][col].value == "O":
              self.playerO.winner = True
              return 1
            else:
              self.playerX.winner = True
              return -1

    # Check diagonals
    if self.board.grid[0][0].value is not None and \
       self.board.grid[0][0].value == self.board.grid[1][1].value == self.board.grid[2][2].value:
        self.end = True
        if self.board.grid[0][0].value == "O":
          self.playerO.winner = True
          return 1
        else:
          self.playerX.winner = True
          return -1

    if self.board.grid[0][2].value is not None and \
       self.board.grid[0][2].value == self.board.grid[1][1].value == self.board.grid[2][0].value:
        self.end = True
        if self.board.grid[0][2].value == "O":
          self.playerO.winner = True
          return 1
        else:
          self.playerX.winner = True
          return -1

    # Check for a tie
    if all(box.value is not None for row in self.board.grid for box in row):
        self.end = True
        self.playerX.winner = False
        self.playerO.winner = False
        return 0  # Tie

    # Game is still ongoing
    self.end = False
    return None

  
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
  

class AiPlayer:
  # ai plays with O
  def __init__(self , game , text  , symbol):
    self.image = pygame.image.load(text)
    self.symbol = symbol
    self.winner = False
    self.boxes = [] 
    self.game = game
  
  def minimax(self , board , depth , isMaximazing ):
    winner = self.game.check_winner()
    # if self.game.end:
    if winner == 1:
      return 10 - depth
    elif winner == - 1:
      return -10
    elif winner == 0 and all(cell.value is not None for row in board.grid for cell in row):  # Tie
      return 0
    
    
    if isMaximazing:
      bestscore = -float("inf") # -linfini
      
      for i in range(3):
        for j in range(3):
          if board.grid[i][j].value is None:
            board.grid[i][j].value = "O"
            bestscore = max(bestscore , self.minimax(board , depth+1 , False ))
            board.grid[i][j].value = None
      
      return bestscore
              
    else:
      bestscore = float("inf")
      
      for i in range(3):
        for j in range(3):
          if board.grid[i][j].value is None:
            board.grid[i][j].value = "X"
            bestscore = min(bestscore , self.minimax(board ,depth + 1 , True))
            board.grid[i][j].value = None
      
      return bestscore
    
    
  def findBestMove(self , board):
    bestscore = -1000
    bestmove = (-1,-1)
    
    for i in range(3):
      for j in range(3):
        if board.grid[i][j].value is None:
          board.grid[i][j].value = "O"
          score = self.minimax(board , 0 , False)
          board.grid[i][j].value = None
          if score > bestscore:
            bestscore = score
            bestmove = (i ,j)
            
    return bestmove
  

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
        
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          
            

      screen.fill("white")
      # RENDER YOUR GAME HERE
      
      screen.blit(game.board.getBoardImage() , (0,0))
      mouse_pos = pygame.mouse.get_pos()
      mouse_click = pygame.mouse.get_pressed()# Always render the boxes (X's and O's)
      for i in range(3):
          for j in range(3):
              box = game.board.grid[i][j]
              x_pos = box.image_space_rect.x
              y_pos = box.image_space_rect.y

              # Draw the images for X and O based on their value
              if box.value == "X":
                  x_img = pygame.image.load('./assets/x.png')
                  x_img = pygame.transform.scale(x_img, (100, 100))
                  screen.blit(x_img, (x_pos - 50, y_pos - 50))
              elif box.value == "O":
                  o_img = pygame.image.load('./assets/o.png')
                  o_img = pygame.transform.scale(o_img, (100, 100))
                  screen.blit(o_img, (x_pos - 50, y_pos - 50))
      
      
      if not game.end:            
        for i in range(3):
          for j in range(3): 

            if game.playerTurn == game.playerX:
              box = game.board.grid[i][j]
              x_pos = box.image_space_rect.x
              y_pos = box.image_space_rect.y
              if mouse_click[0] and not game.end: 
                if x_pos - 50 <= mouse_pos[0] <=  x_pos + 50 and y_pos - 50 <= mouse_pos[1] <=  y_pos + 50 :
                  
                  if box.value is None: # so we dont replace existing value
                    box.value =  "X"
                    game.playerX.boxes.append(box)
                    game.check_winner()
                    if not game.end:  # Only switch turn if game has not ended
                      game.switchTurn()
                    else:
                      break 
            else:
              if game.playerTurn == game.playerO:
                (k,l) = game.playerO.findBestMove(game.board)
                box = game.board.grid[k][l]
                x_pos = box.image_space_rect.x
                y_pos = box.image_space_rect.y
                box.value = "O"
                game.playerO.boxes.append(box)
                game.check_winner()
                if not game.end:  # Only switch turn if game has not ended
                  game.switchTurn()
                else:
                  break
        
      if game.end:
        if game.playerO.winner:
          # print("Winner: X")
          render_text(screen, "O won", text_font, (255,0,0), (400,600))
        elif game.playerX.winner:
          # print("Winner: O")
          render_text(screen, "X won", text_font, (0,0,255), (400,600))
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