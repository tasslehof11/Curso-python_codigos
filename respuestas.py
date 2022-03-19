# -*- coding: utf-8 -*-
astr = 'Hello Bob'
istr = int(astr)
print('First', istr)
astr = '123'
istr = int(astr)
print('Second', istr)

#%%
score = float(input("Enter Score: "))

try:
    if 0.9<=score and score<=1:
    	print("A")
        
    elif 0.8<=score and score<0.9:
    	print("B")
        
    elif 0.7<=score and score<0.8:
    	print("C")
        
    elif 0.6<=score and score<0.7:
    	print("D")	
        
    elif 0<=score and score<0.6:
    	print("F")	

    
except:
    print("Debe estar entre 0.0 - 1.0")

#%%
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')

#%%
def computepay(h,r):
    if h<=40:
    	op = h*r
    
    else:
    	one = h*r
    	two = (h-40)*r*0.5
    
    	op = one + two
        
    return op

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate: "))

p = computepay(hrs,rate)
print("Pay",p)

#%%
con = []
while True:
    num = input("Enter a number: ")
    if num == "done" : break
   
    try:
    	con.append(float(num))
    except:
        print("Invalid input")
        continue

largest = max(con)
smallest = min(con)
print("Maximum is ", largest)
print("Minimun is ", smallest)

#%%
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
     print('Happy New Year:',  friend)
print('Done!')

#%%
text = "X-DSPAM-Confidence:    0.8475"

for i in text:
    if i.isnumeric():
        one = text.find(i)
        break

for idx in text:
    if idx == text[-1]:
        two = text.find(idx)
    
num = text[one:two+1]

print(float(num))

#%%
# Use words.txt as the file name
fname = input("Enter file name: ")
with open(fname, encoding = 'utf-8') as file:
    text = file.read()
    
print(text.upper())

#%%
fname = input("Enter file name: ")
lista = []
lista1 = []

with open(fname) as file:
    text = file.read()
    
    lista = text.split()
    lista = set(lista)
    
    for a in lista:
        lista1.append(a)
        
lista1.sort()
print(lista1)

#%%
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
a = str()
fh = open(fname)
count = 0
imprenta = []

for line in fh:
    if not line.startswith("From") : continue
    a = a + line
    
lista = a.split("\n")
lista.remove('')

for i in lista:
    n = i.split()
    print(n[1])
    count = count+1

print("There were", count, "lines in the file with From as the first word")

#%%
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
a = str()
fh = open(fname)
count = 0
imprenta = []
letras = {}

for line in fh:
    if not line.startswith("From:") : continue
    a = a + line
    
lista = a.split("\n")
lista.remove('')

for i in lista:
    n = i.split()
    imprenta.append(n[1])

for idx in imprenta:
    letras.setdefault(idx, 0)
    letras[idx] = letras[idx] + 1
    
largest = -1
theword = None
for k,v in letras.items():
    if v>largest:
        largest = v
        theword = k
    
print(theword, largest)

#%%
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
a = str()
fh = open(fname)
lista = []
horas_e, horas = [], []
dicc = {}


for line in fh:
    if not line.startswith("From") : continue
    a = a + line
    
lista = a.split("\n")
lista.remove('')

for i in lista:
    n = i.split()
    if len(n) >= 5:
        horas_e.append(n[5])

for char in horas_e:
    x = char.split(":")
    horas.append(x[0])
    
print(horas)

for idx in horas:
    dicc.setdefault(idx, 0)
    dicc[idx] = dicc[idx] + 1
    
for i in sorted(dicc):
    print(i, dicc[i])
    
#%%
orden = int(input("Ingrese el orden del cuadrado : "))
n = int(input("Ingrese el numero superior izquierdo: "))
while n > orden:
    print("El numero superior izquierdo debe de ser menor o igual al orden del cuadrado")
    n = int(input("Ingrese el numero superior izquierdo: "))

lista = []
cuadrado = []
inicialF = n
for i in range(0, orden):
    inicialC = inicialF
    for j in range(0, orden):
        lista.append(inicialC)
        inicialC = inicialC + 1
        if inicialC > orden:
             inicialC = 1
    cuadrado.append(lista)
    inicialF = inicialF + 1
    if inicialF > orden:
        inicialF = 1
    lista = []

for i in range(0, orden):
    for j in range(0, orden):
        print(cuadrado[i][j], end=" ")
    print(end="\n")

#%%
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if line.startswith("From: "):
        print(line)


#%%
import re
lista_s = []
fname = input("Enter file name: ")
with open(fname, encoding = 'utf-8') as file:
    text = file.read()
    lista = re.findall("[0-9]+", text)
    
    for i in lista:
        lista_s.append(int(i))

    print(sum(lista_s))
#%%
import re
def telegrafo(message):
    '''telegrafo(mensaje)     Funcion que retorna el costo de enviar un mensaje bajo ciertos criterios
                - Letra (alfabeto inglés): 1.00
                - Caracteres especiales (incluye letras especial del español): 2.50
                - Digitos: 1.50
                
                Los espacios en blanco no tiene un costo
                
    Argumento:
        message: str
        
    Uso: 
        telegrafo("Mensaje 123") -> 11.50
    '''
    #Genero variable acumulativa
    t = 0
    
    #Encuentro los numeros y luego hallo el valor de t
    numeros = re.findall("[0-9]+", message)
    t = 1.50 * len(numeros)
    
    for i in message:
        
        for idx in ["ñ", "á", "é", "í", "ó", "ú", "@", "#", "&", "$", "%"]:
            if i == idx:
                t = t + 2.50        
            
        for idx in ["-", ",", "."]:
            if i == idx:
                t = t + 1.50
            
        if i == " ":
            t = t
            
        else:
            t = t + 1.00
                
    return t
                
        
print(telegrafo("En el futuro, el correo del administrador será admin@mail.org"))
#%%
def res_paralelo(*tupla):
    '''res_paralelo()      Retorna la resistencia equivalente de un número indeterminado de resistencias
    
    Parametros:
        ? : int, float
    
    Uso:
    res_equiv_paralelo(50, 50) ->  25.0
    res_equiv_paralelo(10, 20, 30) ->  5.454545454545454
    '''
    suma_inv = 0
    for i in list(tupla):
        suma_inv = suma_inv +(1/i)

    return (1/suma_inv)

print(res_paralelo(10, 20, 30))

#%%
def reverse(n):
    '''reverse(n)    Retorna un entero con los dígitos en sentido inverso
    
    Argumentos:
        n : int
        
    Uso: reverse(36) -> 63
    
    '''
    revertir = 0
    while n > 0:
        residuo = n % 10
        revertir = (revertir * 10) + residuo
        n //= 10
        
    return revertir

def all_odds(n):
    '''all_odds(n)     Retorna True/False si todos los dígitos del número n son impares
    
    Argumentos:
        n: int
        
    Uso: all_odds(1313) -> True
    '''
    
    while int(n) > 0:
        residuo = n % 10
        if residuo%2 == 0:
            return False
        n//=10
        
    return True

acum = 0
for i in range(1000000000):
    if i%10 != 0:
        if all_odds(i+reverse(i)):
            acum +=1
                
print(acum)

#%%
def es_primo(n):
    '''es_primo(n)          Retorna True/False si un numero es primo o no
    
    Argumentos:
        n: int
        
    Uso: 
        es_primo(13) -> True
    '''
    if n < 1:
        return False
    
    elif n == 2:
        return True
    
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True   


def rotar_num(n):
    '''rotar_num(n)      Retorna una lista con todos los posibles números de la rotación
                         de los digitos de n
                         
    Arguementos:
        n: int
        
    Uso:
        rotar_num(197) -> [197, 917, 719]
    '''
    varia = str(n)
    lista_num = []
    num_ini = 0
    while num_ini < len(varia):
        varia = varia[1:] + varia[0]
        num_ini += 1
        lista_num.append(int(varia))
        
    return lista_num

print(rotar_num(97831))

#%%
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
#%%
abc = "With three words"
stuff = abc.split()
print(len(stuff))

#%%
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

#%%
a,b,c,d = 108, 105, 110, 101
print(chr(a),chr(b),chr(c),chr(d))
print(chr(42))
print(ord("G"))

#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup("tr")

acum=0
ac=0

for tag in tags:
    text = tag.decode()
    text=text.replace(">"," ")
    text=text.replace("<"," ")
    k = [int(Numero) for Numero in text.split() if Numero.isdigit()]
    if len(k)==1:
        acum = k[0]+acum
        ac+=1
        
print("Count",ac)
print("Sum",acum)

#%%
Texto="la casa 24 roja es de otra propiedad."
Lista=[int(Numero) for Numero in Texto.split() if Numero.isdigit()]
print(Lista)
#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
count = int(input("Enter count: "))
pos = int(input("Enter position: "))

print("Retrieving:",url)
for i in range(count):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    var = tags[pos-1].get("href", None)
    print("Retrieving:",var)
    url=var
            
#%%
import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

#%%
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print('Retrieving', url)
data = urlopen(url).read()

tree = ET.fromstring(data)
counts = tree.findall('.//count')
print('Retrieving',len(data),'characters')
print('Count:',len(counts))
acum = 0
for i in counts:
    acum = acum+int(i.text)
    
print('Sum:', acum)
#%%
import json
from urllib.request import urlopen
import ssl

x=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print('Retrieving', url)

data = urlopen(url).read()
info = json.loads(data)

print('Retrieved', len(data) ,'characters')
print('Count:',len(info['comments']))
for i in info["comments"]:
    x=x+int(i['count'])
    
print('Sum:',x)

#%%
a=[108, 105, 115, 116]
for i in a:
    print(chr(i))
#%%
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    org = email.split("@")[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
   
cur.close()
#%%
import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')


fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None : 
        continue


    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id,len,rating,count) 
        VALUES ( ?, ?, ?,?, ?, ? )''', 
        (name, album_id, genre_id, length, rating, count))

    conn.commit()

#%%

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]
    genre = entry[2]

    print(str(name)+'|'+str(title)+'|'+str(genre))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        (user_id, course_id, genre))

    conn.commit()

#%%
from collections import Counter

fh = open('datos.txt')
lista = []

for i in fh:
    d = i.strip()
    lista.append(float(d))
    
count = dict(Counter(lista))
print(count)

#%%
import numpy as np
L = [3,4,5]

L.extend([3,3])
























