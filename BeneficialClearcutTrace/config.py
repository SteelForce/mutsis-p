tiedosto=open('salasanat.txt', 'r')
sanat = tiedosto.readline().split('/')
iedosto=open('tunnukset.txt', 'r')
anat = iedosto.readline().split('/')



login =anat[0]
password =sanat[0]

login1 =anat[1]
password1 =sanat[1]

login2 =anat[2]
password2 =sanat[2]