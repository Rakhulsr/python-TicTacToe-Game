from ipywidgets import widget, HBox, VBox, Layout
from IPython.display import display
from functools import partial
import numpy as np

#import tictactoe algorithm
import ttt as minimax_helper
  
#game
class general_function(object) :
    def _init_(self, matrix, actual_turn) :
      self.N = 3
      self.button_list = None
      self.text_box = matrix
      self.game_finished = False
      self.actual_turn = actual_turn
    def display_matrix(self):
       N = self.N
       childs = []
       for i in range (N):
          for j in range (N):
             if self.matrix[i,j] == 1:
                self.button_list[i * N + j].description = 'o'
                if self.matrix[i,j] == 1:
                    self.button_list[i * N + j].description = 'x'
    def on_button_clicked(self,index, button) : 
       N = self.N
       if self.game_finished:
          return
       
       y = index%N
       x = int(index/N)
       if self.matrix[x,y]!= 0:
          self.text_box.value = 'Anda tidak bisa membuat input disana!'
          return
       button.desctription =  self.actual_turn[0]
       if self.actual_turn == 'o':
          self.matrix[x,y] = 1
          self.game_finished, status = minimax_helper.game_over(self.matrix)
          if self.game_finished:
             if (status!=0):
                self.text_box.value= 'o wins'
             else :
                self.text_box.value = 'draw'
          else :
             self.actual_turn = 'x'
             self.text_box.value = 'Juega '+ self.actual_turn
    def draw_box(self):
       self.text_box = widget.Text(value='Juega '+self.actual_turn, layout=Layout(width='129px', height='40px'))
       self.button_list = []
       for i in range (9):
          button = widget.Button(description= '',
                                 disabled = False,
                                 button_style='',
                                 #'success', 'info', 'warning', 'danger' or ''
                                 tooltip = "Click me",
                                 icon = '',
                                 layout=Layout(width='40px', height='40px')
                                 )
          self.button_list.append(button)
          button.on_click(partial(self.on_button_clicked, i))
          tic_tac_toe_board = VBox([HBox([self.button_list[0],self.button_list[1],self.button_list[2]])],
                                 HBox([self.button_list[3],self.button_list[4],self.button_list[5]]),
                                 HBox([self.button_list[6],self.button_list[7],self.button_list[8]]))
       display(VBox([self.text_box, tic_tac_toe_board]))
    def computer_play(self):
       if self.game_finished:
          return
       if self.actual_turn=='x':
          turn = -1
          next_turn = 'o'
       if self.actual_turn=='o':
          turn = 1
          next_turn = 'x'
       self.matrix = self.get_best_play(turn)
       self.display_matrix()
       self.actual_turn = next_turn
       self.text_box.value = 'juega' +self.actual_turn
       self.game_finished, status = minimax_helper.game_over(self.matrix)
       if self.game_finished:
          if(status!=0):
             self.text_box.value = 'computer wins'
          else :
             self.text_box.value = 'draw'
    def get_best_olat(self, turn) :
       # 100 is an infinite value compared with highest cost of 10 we can get
       choice, points, nodes_visited = minimax_helper.minimax(self.matrix, turn)
       print('point:', points)
       print('noted_visited: ', nodes_visited)
       return choice

          
          


          

      
