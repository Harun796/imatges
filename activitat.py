import os
from PIL import Image
import shutil
from shutil import copyfile

path = "images"
fitxers = os.listdir(path)
formatsCorrectes = ["rgb","gif","tiff","jpeg","jpg","bmp","png"]
for f in fitxers:
   format =f[-3:]
   print(format)
   if(format not in formatsCorrectes):
    
     pregunta=input("Ho vols copiar?")
     if(pregunta == "si"):
       shutil.move(path+"/"+ f , "noimages"+"/"+f)
     else:
       os.remove(fitxers+"/"+f)
#TODO LListar tots els arxius de images

#TODO Mostrar el nom dels que no són imatge
#Borrar o copiar

opcioMenu =0
while (opcioMenu !=5):
  print("1- Seleccionar imatges per mida, amplada o alçada")
  print("2- Fer miniatures")
  print("3- Marca d'aigua")
  print("4- Convertir png a jpg")
  print("5- Sortir")
  opcioMenu = int(input("Quina opció vols?"))
  if (opcioMenu == 1):
      #TODO agafar si amplada o alçada
      ap=input("Seleccionar per amplada o alçada")
      if(ap == "alçada"):
        minim1=int(input("Quin es el mínim de pixels")
        os.mkdir(minim1)
            
      #TODO agafar la mida mínima de píxels
      
      #TODO crear carpeta dins la carpeta images
      
      #TODO llistar arxius, seleccionar per mida i copiar-los a la carpeta abans creada
  elif (opcioMenu == 2):
  elif (opcioMenu == 3):
  elif (opcioMenu == 4):
  else:
      opcioMenu = 5
print("Adéu bon dia tinguis!")