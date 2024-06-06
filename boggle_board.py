import random

class BoggleBoard_gen1:
  
  ltr_dict = {
    1:"A", 
    2:"B",
    3:"C", 
    4:"D",
    5:"E",
    6:"F",
    7:"G",
    8:"H", 
    9:"I",
    10:"J",
    11:"K",
    12:"L",
    13:"M",
    14:"N",
    15:"O",
    16:"P",
    17:"Q",
    18:"R",
    19:"S",
    20:"T",
    21:"U",
    22:"V",
    23:"W",
    24:"X",
    25:"Y",
    26:"Z"
  }


  def __init__(self, name):
    self.name = name
    for num in range(4):
      print("____")
  
  @classmethod
  def shake(self):
    print("------")
    brd_lst = []
    for i in range(4):
      rdm_num = random.randint(1,26)
      brd_lst.append(self.ltr_dict[rdm_num])
      for j in range(3):
        srdm_num = random.randint(1,26)
        brd_lst[i] += f" {self.ltr_dict[srdm_num]}"
        if j == 2:
          print(brd_lst[i])
    print("------")
    


# game1 = BoggleBoard_gen1("game1")
# game1.shake()
# BoggleBoard_gen1.shake()
      
class BoggleBoard_gen2(BoggleBoard_gen1):

  ltr_dict = {
    1: list("AAEEGN"),
    2: list("ELRTTY"),
    3: list("AOOTTW"),
    4: list("ABBJOO"),
    5: list("EHRTVW"),
    6: list("CIMOTU"),
    7: list("DISTTY"),
    8: list("EIOSST"),
    9: list("DELRVY"),
    10: list("ACHOPS"),
    11: list("HIMNQU"),
    12: list("EEINSU"),
    13: list("EEGHNW"),
    14: list("AFFKPS"),
    15: list("HLNNRZ"),
    16: list("DEILRX")  
    }


  

  def __init__(self, name):
    super().__init__(name)
    self.list = random.sample(range(1, 17), 16)
    self.board = []


  def shake(self):
    tick = 0
    for i in range(0,16,4):
      num = random.randint(0,5)
      self.board.append(self.ltr_dict[self.list[i]][num])
      
      for j in range(i+1,i+4):
        num = random.randint(0,5)
        self.board[tick] += f" {self.ltr_dict[self.list[j]][num]}"
      tick += 1
    for k in range(0,4):
      print(self.board[k])


game1 = BoggleBoard_gen2("game1")
game1.shake()