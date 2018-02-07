
# Python
## * Getting Started


## What do you think about ‘Python’?
![image](http://www.voidspace.org.uk/ironpython/silverlight/images/python.gif)
# <center><b>This?</b></center>
![image](https://images-na.ssl-images-amazon.com/images/I/A1HRKSKsafL._SL1000_.png)
# <center><b>Or This?</b></center>
## <center>It doesn’t matter, coz we are going to talk about the second one!</center>


# So What Python Actually Is ?
## Python is a programming language.<br>
* An Open Source language which is very powerful but easy to learn.
* Python is designed to be readable, and hence maintainable.
* Developed by Guido van Rossum In early 1990’s!



# Why Should We Care To Use Python?
<br>
* ## Python has very short and precise syntax



```python
x = 34 -23
y = "Hello"
z = 3.45
print(x)
print(y)
print(z)
```

    11
    Hello
    3.45


* ## It has variety of applications

* ## You can do system programming!

* ## Game development

* ## Web Development

* ## GUI (Graphical user Interface) applications

* ## And Internet Scripting, Database Programming, Images, artificial Intelligence, XML, etc.



# It is used in?

>Anki spaced repetition Bazaar BitTorrent Blender 3D (software) BuildBot Calibre Chandler Cinema 4D Deluge GNOME Dropbox emesene MSN/WLM Exaile Gajim XMPP GRAMPS genealogy software Gwibber microblogging Image Packaging System package management system Solaris operating system OpenSolaris Juice Mercurial Miro internet television Morpheus MusicBrainz Picard MusicBrainz Nicotine PyGTK Soulseek OpenLP OpenShot Video Editor OpenStack PiTiVi non-linear video editor Portage Quake Army Knife Quake engine Quod Libet Resolver One spreadsheet SABnzbd Sage SCons Sublime Text Tryton Ubuntu Software Center package manager Ubuntu Wammu Wicd Linux WikidPad YUM OpenERP ERP5 GNU Mailman MoinMoin Planet Plone content management system Roundup ViewVC CVS SVN Trac Turntable.fm CherryPy Django Flask Google App Engine Pylons Pyramid Quixote Topsite Templating System TurboGears SQLObject SQLAlchemy Kid Genshi CherryPy Pylons web2py Zope content management systems edit Pygame SDL Panda3D Python Imaging Library Python-Ogre Soya3D edit PyGTK GNOME PyQt KDE PySide wxPython wxWidgets edit Biopython graph-tool NetworkX complex networks SciPy SymPy Veusz VisTrails edit Matplotlib MATLAB NumPy Sage free software SymPy edit Cheetah IPython Jinja Django mod python Apache PYthon Remote Objects PyObjC Sphinx (documentation generator) reStructuredText HTML PDF EPub Man pages Twisted VPython edit ADvantage Framework Amarok ArcGIS Autodesk Maya 3D modeler MEL Autodesk MotionBuilder Autodesk Softimage Blender Boxee home theater PC Cinema 4D Corel Paint Shop Pro Claws Mail DSHub ERDAS

# And

>Imagine EventScripts Valve Source engine FreeCAD gedit GIMP GNAT Houdini Inkscape vector graphics editor MeVisLab Modo MSC.Software Notepad++ Nuke ParaView Poser 3D rendering animation PyMOL QGIS Rhinoceros 3D Rhythmbox Scribus 3DSlicer SPSS statistical software Totem GNOME Vim VisIt WeeChat IRC edit CCP hf Stackless Python MMO Eve Online Google Google Groups Gmail Google Maps NASA CAD CAE PDM reddit Common Lisp Enthought edit CPython Cython IronPython .NET Mono Jython Java Parrot Psyco JIT compiler PyPy Stackless Python coroutines Unladen Swallow Google Python CLPython CPython Jython IronPython PyPy Python for S60 Psyco Stackless Python Unladen Swallow Boa IDLE SPE Youtube Yahoo Groups

## This was a list of the famous Applications which use Python

>## Okay..Let me be serious
### It is used by Google, Yahoo, 
### Youtube, reddit, NASA, 
### BattleField 2(game),
### Notepad++, GIMP, VIM, gedit,
### Autodesk Maya, Corel Paint
### And many more..

## What was that creepy image about in the start of the slide?
>It was from a British Comedy show ‘Monty Python and Flying Circus’ from which the Programming Language ‘Python’ got its name.


# So, Let's Start With Python


* ## Printing


```python
print("Hello World!")
```

    Hello World!



```python
print("Hello ACM VIT")
```

    Hello ACM VIT


* ## Input


```python
a = input("Enter A Number: ")
print(a)
```

    Enter A Number: 11
    11


* ## Comments


```python
#This Is A Comment
```

* ## Keywords & Identifiers
><b>Keywords</b> are names given to variables, functions, classes etc.
<br><br><b>Identifiers</b> are names used by a programming itself for
some predefined functions or operators etc.


* ## Lines/Identation

> Python unlike C/C++ do not use curly braces to specify a block of
statements, instead it uses indentation.
<br><b>Note:</b>
Spaces in indentation may vary but for statements to be in a same
block or suite should be indented by same number of spaces.


* ## Variables

> Variable Names Are Case-Sensetive i.e. Name is not equal to name


```python
integer = 7
floating_point = 7.7
string_val = "Hello ACM VIT"

print(integer)
print(floating_point)
print(string_val)
```

    7
    7.7
    Hello ACM VIT


* ## Assignment Of Vairables


```python
a = 1
b = c = a

print(b)
print(c)
```

    1
    1


* ## Datatypes
    <br>
    * Numbers
    * Strings
    * Lists
    * Tuples
    * Dictionaries
    * Boolean

* ## Numbers

>Numbers are used to numerical data, these are immutable data
types ie. These cannot be updated, if updated location is
Changed.
    * Integer
    * Floating Point
    * Complex


```python
print(7) #integer
print(7.11) #float
print(1+2j) #complex
```

    7
    7.11
    (1+2j)


> # Function On Numbers


```python
print(pow(2,3)) #power

print(min(-72,2,3,54,56,67)) #minimum

print(max(563,4357)) #maximum

import math

print(math.ceil(1.2)) #Smallest Integer

print(math.floor(2.3)) #Greatest Integer

print(math.sqrt(4)) #Square Root

print(math.degrees(3.14)) #radian to degree

print(math.radians(180)) #degree to radian

print(math.sin(3.14)) #sine

print(math.cos(3.14)) #cosine

print(math.tan(3.14)) #tangent
```

    8
    -72
    4357
    2
    2
    2.0
    179.9087476710785
    3.141592653589793
    0.0015926529164868282
    -0.9999987317275395
    -0.001592654936407223


* ## Arithmetic Operators


```python
print(1 + 2)

print(1 * 2)

print(3 / 2)

print(3 // 2) #integer division

print(2 ** 3) #exponential

print(3 % 2) #modulo
```

    3
    2
    1.5
    1
    8
    1


* ## Comparison Operators


```python
print(1 == 2)

print(1 < 2)

print(1 <= 1)

print(1 > 2)

print(2 >= 1)

print(2 != 1)
```

    False
    True
    True
    False
    True
    True


> ## Order of Evaluation!
When we string operators together - Python must know which one to do first, Known as `Operator Precedence`


```python
x = 1 + 2 ** 3 / 4 * 5

print(x)
```

    11.0


![image.png](attachment:image.png)

-------------

![image.png](attachment:image.png)

* ## Strings

>String is a data type which is implicitly picked up by a variable
storing a text.!


```python
x = "Hello ACM VIT"

print(x) #single line
```

    Hello ACM VIT



```python
x = """Hello
ACM VIT"""

print(x) #multi line
```

    Hello
    ACM VIT


>Operators on strings


```python
x = "Hello "
y = "ACM VIT "

print(x + y)

print(y * 7)
```

    Hello ACM VIT 
    ACM VIT ACM VIT ACM VIT ACM VIT ACM VIT ACM VIT ACM VIT 


>String Functions


```python
x = "Hello ACM VIT"

print(x.count('H')) #count

print(x.find('H')) #find (give index)

print(x.find('t'))

print(x.index('H')) #gives index

#NOTE: Find returns -1 when character is not found whereas index throws an error.

print(min("ACM"))

print(max(x))

print('12'.isdigit())

print(x.isalpha())

print(x.lower())

print(x.upper())

print(x.split(' '))

print(x.join('***'))
```

    1
    0
    -1
    0
    A
    o
    True
    False
    hello acm vit
    HELLO ACM VIT
    ['Hello', 'ACM', 'VIT']
    *Hello ACM VIT*Hello ACM VIT*


> ## String Slicing


```python
x = "Hello ACM VIT"

print(x[:])

print(x[2:])

print(x[:3])

print(x[::-1])

print(x[::2]) #third one is the step
```

    Hello ACM VIT
    llo ACM VIT
    Hel
    TIV MCA olleH
    HloAMVT


* ## Lists

>Lists are used to store collection of data.



```python
x = [1,2,3,4,5,6,7]

print(x)

print(x[0])

print(x[5])

y = "Hello ACM VIT"

print(list(y))

x[1] = -1

print(x)

print(y)

z = [x,list(y)]

print(x+list(y))

print(z[0][0]) #0 of x

print(z[1][4]) #2 of y

```

    [1, 2, 3, 4, 5, 6, 7]
    1
    6
    ['H', 'e', 'l', 'l', 'o', ' ', 'A', 'C', 'M', ' ', 'V', 'I', 'T']
    [1, -1, 3, 4, 5, 6, 7]
    Hello ACM VIT
    [1, -1, 3, 4, 5, 6, 7, 'H', 'e', 'l', 'l', 'o', ' ', 'A', 'C', 'M', ' ', 'V', 'I', 'T']
    1
    o


* ## Tuples

>Tuples are just like lists but these are immutable i.e. cannot be updated.


```python
t = (1,2,3,4,5,6,7)

print(t)

print(t[0])

print(t[5])

t[0] = 1
```

    (1, 2, 3, 4, 5, 6, 7)
    1
    6



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-110-800801a1e6e7> in <module>()
          7 print(t[5])
          8 
    ----> 9 t[0] = 1
    

    TypeError: 'tuple' object does not support item assignment



```python
l = [1,2,3,-1,0,-2]

print(sorted(l))

print(l.count(1))

print(l)

l.reverse()

print(l)

l.append(7)

print(l)
```

    [-2, -1, 0, 1, 2, 3]
    1
    [1, 2, 3, -1, 0, -2]
    [-2, 0, -1, 3, 2, 1]
    [-2, 0, -1, 3, 2, 1, 7]



```python
l = [1,2,3,4,5,6,7]

print(l[:])

print(l[::-1])

print(l[2:5])

```

    [1, 2, 3, 4, 5, 6, 7]
    [7, 6, 5, 4, 3, 2, 1]
    [3, 4, 5]


* ## Set

    * Set is another data type which is mutable but stores immutable data.
    * Set do not contain duplicate elements.
    * Represented using {}.
    * Declared using set().


```python
l = [1,2,3,1,1,3]

s = set(l)

print(s)
```

    {1, 2, 3}



```python
s1 = {1,2,3,4,5,56,6}

s2 = {1,2,3,6,7}

print(s1.intersection(s2))

print(s1.union(s2))

print(s1.isdisjoint(s2))

s3 = {-1,-2}

print(s1.isdisjoint(s3))

print(s2.issubset(s2))

print(s3.issubset(s1))
```

    {1, 2, 3, 6}
    {1, 2, 3, 4, 5, 6, 7, 56}
    False
    True
    True
    False


* ## Dictionaries

Dictionary are like lists but instead of indexes values are accessed
using unique key. Dictionary is collection of key value pairs.
Values can be anything:

    * Lists
    * Numbers
    * Tuples
    * Even Dictionaries

<b>Note:</b> Declared using curly braces ‘{}’ and keys are immutable.


```python
d = {1:2,3:4,"one":1}

print(d["one"])

print(d[1])


```

    1
    2



```python
d = {"one":1,"two":2}

l = d

print(d)

l["one"] = -1

print(d)

d = {"one":1,"two":2}

l = d.copy()

l["one"] = -1

print(d)

print(l)

print(d.items())

print(d.values())

print(d.get(2,0)) #used to get a valued when you are not sure if key exists or when you want a default value for a key
```

    {'one': 1, 'two': 2}
    {'one': -1, 'two': 2}
    {'one': 1, 'two': 2}
    {'one': -1, 'two': 2}
    dict_items([('one', 1), ('two', 2)])
    dict_values([1, 2])
    0


* ## Conditionals


```python
if(1 == 2):
    print("True")
else:
    print("False")
```

    False



```python
if(1 == 2):
    print("1 = 2")
elif(1<2):
    print("1 < 2")
else:
    print("1 > 2")
```

    1 < 2



```python
if(1 < 2 and 2 == 2):
    print("True")
else:
    print("False")
```

    True



```python
if(1 > 2 or 2 == 2):
    print("True")
else:
    print("False")
```

    True



```python
if(not 1 > 2):
    print("False")
else:
    print("True")
```

    False


* ## Range And Loops


```python
for i in range(1,10):
    print(i,end=" ")
```

    1 2 3 4 5 6 7 8 9 


```python
for i in range(1,10,2):
    print(i,end=" ")
```

    1 3 5 7 9 


```python
i = 0
while(i < 7):
    print(i,end=" ")
    i += 1
```

    0 1 2 3 4 5 6 


```python
for i in range(1,10):
    if(i == 4):
        break
    print(i,end=" ")
```

    1 2 3 


```python
for i in range(1,10):
    if(i == 4):
        continue
    print(i,end=" ")
```

    1 2 3 5 6 7 8 9 


```python
def add(x,y):
    return x + y
print(add(2,5))
```

    7



```python
def print_list(l):
    for i in l:
        print(i,end=",")
val_list = [16,25,34,47,52,92,106]
print_list(val_list)
```

    16,25,34,47,52,92,106,

* ## Type Conversions


```python
x = 7  #Integer

y = 7.7 #Floating Point

z = "Hello World" #String

print(x)

print(y)

print(int(y))

print(x + y)

print(x + int(y))

print(z + str(x) + str(y))

print(z + str(x) + str(int(y)))

z = "99"

print(z + str(x))

print(x + int(z))
```

    7
    7.7
    7
    14.7
    14
    Hello World77.7
    Hello World77
    997
    106

