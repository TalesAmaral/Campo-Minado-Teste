from PIL import ImageGrab
from PIL import Image
from PIL import ImageChops
import pyautogui
import random
def igual(im1, im2):
    return ImageChops.difference(im1, im2).getbbox() is None
def mouse(pos,botao):
    pyautogui.moveTo(pos)
    pyautogui.click(button= botao)
    pyautogui.moveTo(400,280)
def leitura(TALES):
    d=[]
    a = ImageGrab.grab()
    index =0
    for y in range(0,384,24):
        d.append([])
        for x in range(0,720,24):
            c = a.crop((415+x,286+y,439+x,310+y))
            for i in range(9):
                if igual(c,TALES[i]):
                    d[index].append(i)
                    break
        index+=1
    return d
def contagem(d,x,y,oq):
    contador = []
    for i in range(y-1,y+2):
                    if i!=-1 and i<16:
                        for g in range(x-1,x+2):
                            if g!=-1 and g<30:
                                if d[i][g]==oq:
                                    contador.append((i,g))
    return contador
def releitura(d,TALES):
    a = ImageGrab.grab()
    for y in range(0,384,24):
        holder1 = int(y/24)
        for x in range(0,720,24):
            holder2 = int(x/24)
            c = a.crop((415+x,286+y,439+x,310+y))
            if  not igual(c,TALES[(d[holder1][holder2])%8]):
                for i in range(9):
                    if i!=(d[holder1][holder2])%8:
                        if igual(c,TALES[i]):
                            d[holder1][holder2]=i
                            break
    return d
def verificacao_basica(d,y,x,TALES):
    coo = contagem(d,x,y,1)
    coa = len(contagem(d,x,y,8))
    if coa==(d[y][x]-1) and len(coo)>0:
        mouse((427+24*x,298+24*y),"left")
        d[y][x] = 8+d[y][x]
        d= releitura(d,TALES)
    else:
        if len(coo)+coa==(d[y][x]-1):
            for i in range(len(coo)):
                mouse((427+24*coo[i][1],298+24*coo[i][0]),"right")
                d[coo[i][0]][coo[i][1]]=8
    return d

def bomba(d,TALES):
    for y in range(0,16):
        for x in range(0,30):
            if d[y][x] not in (0,1,8) :
                d = verificacao_basica(d,y,x,TALES)   
    return d            
def main():
    TALES = (Image.open("0.png"),Image.open("1.png"),Image.open("2.png"),Image.open("3.png"),Image.open("4.png"),Image.open("5.png"),Image.open("6.png"),Image.open("7.png"),Image.open("8.png"))
#  for i in range(3):
   #     mouse((random.randint(415,1135),random.randint(286,670)),"left")
    d = leitura(TALES)
    while 1:    
        d = bomba(d,TALES)
    return 0
if __name__ == "__main__":
    main()
