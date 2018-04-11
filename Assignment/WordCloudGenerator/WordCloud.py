#Ariq Naufal Satria
#1706027414
import string
import random
import htmlFunctions

#=====================================
#Opening program, minta inputan user dan buka file-file
print("Program to create word cloud from a text file")
print("The result is stored as an HTML file\n")
ayy = input("Please enter the file name: ")
print("")
text = open(ayy,"r")
illegals = open("stopWords.txt", "r")

#=====================================
#bikin list yangg nanti kepake
word =[]
noword =[]
txt =[]  

#Masukin semua kata stopwords ke dalam list noword
for i in illegals :
    z = i.strip()
    noword.append(z)
noword.append("") #kalau ini ga dimasukkin ntar bakal ada '' yang keitung

#baca text nya, kemudian di split biar jadi list
tmp = text.read()
tmp1 = tmp.split()

#for yang bagian ini untuk menghilangkan punctuation sekaligus me lowercase semua kata
for i in tmp1 :
    tmp2 = i.strip(string.punctuation)
    tmp3=tmp2.strip().lower()

    #bagian ini untuk menyeleksi apakah kata tersebut ada di noword(stopword) atau tidak
    #bila ada, jangan di append ke list txt
    jelek = False
    for j in noword :
        if tmp3 == j :
            jelek = True
            break
    if not jelek :
        txt.append(tmp3)

#====================================

#disini bagian untuk counting jumlah dari masing masing kata
for i in txt : 
    udah = False    #boolean yang ini buat ngecek, apakah kata tersebut udah pernah masuk ke list word atau belum
    for j in range(len(word)) :
        if i == word[j][1] :    
            udah = True
            cnt = j
            break

    #Disini maksudnya, kalau udah pernah masuk, tambahin aja counternya
    #kalau belum, di append ke list terus counternya ditambah 1
    if not udah :
        word.append([1,i])
        
    else :
        word[cnt][0] += 1

#====================================

#disini maksudnya ngesort dari besar ke kecil
word = sorted(word,reverse = True)

#bagian ini untuk membatasi yang muncul hanya 50 tertinggi saja
#bila kurang dari 50 yasudah keluarin semua
panjang= len(word)
if panjang > 50 :
    panjang = 50

#mencari maksimum dan minimum dari freq yang ada
maxc = word[0][0]
minc = word[panjang-1][0]

#buat ngeprint dengan formatting
print(ayy,":")
print(panjang,"words in frequency order as (count:word) pairs\n")
samping = 0
for i in range(panjang) :
    print("{:3d}:{:15s}".format(word[i][0],str(word[i][1])),end ="")
    samping +=1
    if samping == 4 :
        print("")
        samping = 0
print("\n")
input("Please type Enter to continue ")

#=====================================
boi = ''

#karena yang masuk hanya 50 teratas, maka delete saja selain yang 50 pertama di list
#kalau kurang dari 50, for ini ga jalan kok
for i in range(50,len(word)) :
    del word[50]

#mensort sesuatu dengan menggunakan key lambda
#lambda itu function gitu seperti ini yang dipake :
"""
def lambda (i) :
    return i[1]
"""
word = sorted(word, key = lambda i:i[1])

#bagian ini untuk membuat html yang diminta
for i in range(panjang) :
   boi += " "+ htmlFunctions.make_HTML_word(word[i][1],word[i][0],maxc,minc)
box = htmlFunctions.make_HTML_box(boi)
htmlFunctions.print_HTML_file(box,'a word cloud of '+ayy)
