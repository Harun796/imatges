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
    ap=input("Seleccionar per amplada o alçada")
    if(ap == "alçada"):
      minim1=int(input("Quin es el mínim de pixels"))
      os.mkdir("seleccióH"+str(minim1))
      for g in fitxers:
        filename = path+"/"+g
        image = Image.open(filename)
        width, height = image.size
        if(height >= minim1):
          copyfile(path + "/"+ g ,"seleccióH" + str(minim1) + "/" + g)
    elif(ap == "amplada"):
      minim2=int(input("Quin és el mínim de pixels"))
      os.mkdir("seleccióW"+ str(minim2) )
      for t in fitxers:
        filename = path+"/"+t
        image = Image.open(filename)
        width, height = image.size
        if(width >= minim2):
          copyfile(path + "/" + t , "seleccióW" + str(minim2)+"/" + t)
  elif (opcioMenu == 2):
    h=int(input("Quina alçada vols?"))
    w=int(input("Quina amplada vols?"))
    os.mkdir("thumbnail")
    #Relative Path
    for z in fitxers: 
      img = Image.open(path+"/"+z) 
      #In-place modification 
      img.thumbnail((w,h)) 
      img.save("thumbnail"+"/"+ z) 
  #elif (opcioMenu == 3):
    #donde = input("On vols ")
    #if(donde == "dalt esquerre"):
    #elif(donde =="dalt dreta" ):
    #elif(donde == "baix esquerre"):
    #elif(donde == "baix dreta"):
  elif (opcioMenu == 4):
    path2 = "jpg"
    if(os.path.exists(path2)):
      print("Arxiu existent")
    else:
      os.mkdir("jpg")
      for r in fitxers:
        sapo = r[-3:]
        print(sapo)
        if(sapo == "png"):
          im = Image.open("images" + "/"+r)
          im = im.convert('RGB')
          im.save(path2+"/"+r[0:-4]+".jpg")
  #else:
      #opcioMenu = 5
#print("Adéu bon dia tinguis!")