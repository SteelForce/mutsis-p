import config
x = 0
while x == 0:
  a = input('Syötä käyttäjätunnus: ')
  b = input('Syötä salasana: ')



  if a == config.login:
    if b == config.password:
      print('terve', config.login)
      x = x+1
    else:
      print('salasana väärin (0)')
  else:
    if a == config.login1:
      if b == config.password1:
        print('terve', config.login1)
        x = x+1
      else:
        print('salasana väärin (1)')  
    else:
      if a == config.login2:
        if b == config.password2:
          print('terve', config.login2)
          x= x+1
        else:
          print('salasana väärin (2)')
      else:
        print('käyttäjätunnus väärin')
        print(' ')
  #tiedän on melko sketch spagetti mutta toimii
    

