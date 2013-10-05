# -*- coding: utf8 -*-

# This python script generates the extra files needed for the frames
# version of the manual. It generates the files:
# indexframes.html, contents.html and title.html
# Based on html files created by Michael Rhoades
# Script written by Andres Cabrera June 2006
# Licensed under the GPL licence version 3 or later

import sys
from xml.dom import minidom

version = sys.argv[1:]
if (len(version)==0):
    version=['']
indexframesFile = open('html/indexframes.html','w')
creditsFile = open('html/credits.html','w')
titleFile = open('html/title.html','w')
contentsFile = open('html/contents.html','w')

indexFile = open('html/index.html','r')
index = indexFile.read()
indexFile.seek(0)
indexparse = minidom.parse(indexFile)

frameLink = '''
          <div>
            <h2 class="title"><a href="indexframes.html">Version avec Cadres</a></h2>
          </div>'''
s = '''<div>
            <h1 class="title"><a id="index"></a>Le Manuel de Référence Canonique de Csound</h1>'''
titleEnd = index.find(s) + len(s) + 1
if (index[titleEnd:titleEnd+len(frameLink)]==frameLink):
    print '''**************************************
Warning: index.html already processed!
**************************************'''

# indexframes.html -----------------------------------------
indexframesFile.write('''<!-- généré par makeframes.py - NE PAS EDITER MANUELLEMENT-->\n<html>\n<head>
<link rel="stylesheet" href="csound.css" type="text/css" />
<title>Csound ''' +version[0]+ ''' Manuel - Version avec Cadres</title>
</head>
<frameset cols="275,*">
  <frame name="left" scrolling="auto" noresize target="rtop" src="contents.html">
  <frameset rows="90,*">
    <frame name="rtop" target="rbottom" src="title.html" scrolling="no" marginheight="6">
    <frame name="rbottom" src="credits.html">
  </frameset>
  <noframes>
  <body>

  <p>Cette page utilise des cadres, mais votre navigateur ne les supporte pas.</p>

  </body>
  </noframes>
</frameset>
</html>''')
indexframesFile.close()

# credits.html -----------------------------------------
creditsFile.write('''<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<!-- generated by makeframes.py -->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <link rel="stylesheet" href="csound.css" type="text/css" />
  </head>
  <body>\n    ''')
creditsFile.write(index[index.find('<div class="book"'):index.find('Massachusetts Institute of Technology</p>')+106])
creditsFile.write('</div>\n  </body>\n</html>')  
creditsFile.close()

# title.html -----------------------------------------

titleFile.write('''<!-- généré par makeframes.py -->\n<html>\n<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title>Le Manuel de Référence Canonique de Csound</title>\n
    <link rel="stylesheet" href="csound.css" type="text/css" />
    <base target="rbottom">
    </head>
<body alink="#0000ff" link="#0000ff" vlink="#0000ff">
<p align="center"><font size="6">Le Manuel de Référence Canonique de Csound
</font>
<font size="4">
<br>
|
<a href="contents.html#a" style="text-decoration: none;">A</a>
|
<a href="contents.html#b" style="text-decoration: none;">B</a>
|
<a href="contents.html#c" style="text-decoration: none;">C</a>
|
<a href="contents.html#d" style="text-decoration: none;">D</a>
|
<a href="contents.html#e" style="text-decoration: none;">E</a>
|
<a href="contents.html#f" style="text-decoration: none;">F</a>
|
<a href="contents.html#g" style="text-decoration: none;">G</a>
|
<a href="contents.html#h" style="text-decoration: none;">H</a>
|
<a href="contents.html#i" style="text-decoration: none;">I</a>
|
<a href="contents.html#j" style="text-decoration: none;">J</a>
|
<a href="contents.html#k" style="text-decoration: none;">K</a>
|
<a href="contents.html#l" style="text-decoration: none;">L</a>
|
<a href="contents.html#m" style="text-decoration: none;">M</a>
|
<a href="contents.html#n" style="text-decoration: none;">N</a>
|
<a href="contents.html#o" style="text-decoration: none;">O</a>
|
<a href="contents.html#p" style="text-decoration: none;">P</a>
|
<a href="contents.html#r" style="text-decoration: none;">R</a>
|
<a href="contents.html#s" style="text-decoration: none;">S</a>
|
<a href="contents.html#t" style="text-decoration: none;">T</a>
|
<a href="contents.html#u" style="text-decoration: none;">U</a>
|
<a href="contents.html#v" style="text-decoration: none;">V</a>
|
<a href="contents.html#w" style="text-decoration: none;">W</a>
|
<a href="contents.html#x" style="text-decoration: none;">X</a>
|
<a href="contents.html#z" style="text-decoration: none;">Z</a>
|
<br>
<a href="ScoregensTop.html" target="rbottom" style="text-decoration: none;">Instructions de Partition</a>
|
<a href="ScoreGenRef.html" target="rbottom" style="text-decoration: none;">Routines GEN</a>
|
<a href="MiscQuickref.html" target="rbottom" style="text-decoration: none;">Référence Rapide</a> 
</font></p>\n</body>\n</html>''')
titleFile.close()

# contents.html -----------------------------------------

contentsFile.write('''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- generated by makeframes.py -->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Contents</title>
    <link rel="stylesheet" href="csound.css" type="text/css" />
    <link rel="start" href="index.html" title="Le Manuel de Référence Canonique de Csound" />
    <link rel="next" href="PrefaceTop.html" title="Preface" />
    <base target="rbottom">
  </head>
  <body link="#0000FF" vlink="#0000FF" alink="#0000FF">
    <div class="navheader" style="width: 1137; height: 2">
      ''')

#routine to find the toc
navheader = indexparse.getElementsByTagName('div')
i = 0
while (navheader[i]!=''):
    #print navheader[i].attributes.keys()
    if (len(navheader[i].attributes.keys())!=0):
        if (navheader[i].attributes.keys()[0]=='class'):
            #print navheader[i].attributes['class'].value
            if(navheader[i].attributes['class'].value == 'toc'):
                break
    i += 1
    
toc = navheader[i]
sections = toc.getElementsByTagName('span')
a =  toc.getElementsByTagName('a')

for j in range(len(a)):
    if (a[j].attributes['href'].value=='OpcodesTop.html'):
        overview=a[j].parentNode.parentNode.nextSibling.nextSibling
    elif (a[j].attributes['href'].value=='ScoregensTop.html'):
        scoregens=a[j].parentNode.parentNode.nextSibling.nextSibling
        break


#print overview.toxml().encode('utf-8')

# Routine to make titles bigger and black, except Appendices
            
for j in range(len(sections)):
    #print "---------\n", sections[j].toxml()
    #raw_input()
    if ((sections[j].attributes['class'].value!='section') and
        (sections[j].attributes['class'].value!='chapter') and
        (sections[j].attributes['class'].value!='appendix') and
        (sections[j].attributes['class'].value!='refentrytitle') and
        (sections[j].attributes['class'].value!='refpurpose') and
        (sections[j].attributes['class'].value!='quote') and
        (sections[j].attributes['class'].value!='emphasis')):
        print "--------Title:", sections[j].childNodes[1].firstChild.toxml().encode('utf-8')
        font = minidom.Element('font')
        font.setAttribute('size','4')
        font.setAttribute('color','Black')
        font.appendChild(minidom.Element('br'))
        print str(j) + " ; " + sections[j].attributes['class'].value
        if (sections[j].childNodes[1].childNodes[0].toxml().encode('utf8')=='Glossaire'):
            font.appendChild(sections[j].childNodes[1].cloneNode(True))
        else:
            font.appendChild(sections[j].childNodes[1].childNodes[0].cloneNode(True))
        font.appendChild(minidom.Element('br'))
        #print sections[j].firstChild.toxml().encode('latin-1')
        #print font.toxml().encode('latin-1')
        parent = sections[j].parentNode
        parent.appendChild(font)
        parent.removeChild(sections[j])
        #spanElement = sections[j].getElementsByTagName('span')
        #try:
            #sections[j].removeChild(spanElement)
        #except:
            #print "No span for", sections[j].toxml()
        #print sections[j].toxml().encode('latin-1')
        #print font.toxml().encode('latin-1')
    elif (sections[j].attributes['class'].value=='appendix'):
        font = minidom.Element('font')
        font.setAttribute('size','4')
        font.appendChild(sections[j].childNodes[1].cloneNode(True))
        font.appendChild(minidom.Element('br'))
        #print sections[j].firstChild.toxml().encode('latin-1')
        #print font.toxml().encode('latin-1')
        parent = sections[j].parentNode
        parent.appendChild(font)
        parent.removeChild(sections[j])
        #print sections[j].toxml().encode('latin-1')
        #print font.toxml().encode('latin-1')
    else:
        #print sections[j].toxml().encode('latin-1')
        parent = sections[j].parentNode
        newNode = sections[j].getElementsByTagName('a')
        font = minidom.Element('font')
        font.setAttribute('size','2')
        #font.setAttribute('color','Black')
        #font.appendChild(minidom.Element('br'))
        #if (sections[j].attributes['class'].value!='refpurpose' and
            #sections[j].attributes['class'].value!='refentrytitle' and
            #sections[j].attributes['class'].value!='quote' and
            #sections[j].attributes['class'].value!='emphasis'):
        if newNode != []:
            #    font.appendChild(newNode[0].cloneNode(True))
            parent.appendChild(newNode[0].cloneNode(True))
#        parent.appendChild(font)
        parent.removeChild(sections[j])
        #print sections[j].toxml().encode('latin-1')
    

#print toc.toxml() #.encode('latin-1')

# routine to remove text description from opcode entries and
# add alphabetical references and letters
unwantedtext = overview.getElementsByTagName('dt')
alphabetcaps = []
alphabet = []

for num in range(65,93):
    alphabetcaps.extend(chr(num))
    alphabet.extend(chr(num+32))

count = -1
for text in unwantedtext:
    if count==15 or count==23:
        count = count + 1 #There is no 'Q' or 'Y'
    #print "text: ", text.toxml()
    text.removeChild(text.childNodes[0])
    #text.appendChild(minidom.Element('br'))
    #print "Unwanted: ", text.toxml()
    node = text.getElementsByTagName('a')
    if ((node[0].firstChild.toxml().encode('utf-8')[0]==alphabet[count+1])
        or(node[0].toxml().encode('utf-8')[0]==alphabetcaps[count+1])):
        count += 1
        string = '<b style="border:solid;"><a name="' + alphabet[count] + '">' + alphabetcaps[count] + '</a></b>'
        #print "string:", string
        letter = minidom.parseString(string)
        text.insertBefore(minidom.Element('br'), text.firstChild) 
        text.insertBefore(letter.firstChild, text.firstChild)
        print "unwanted2: ", text.firstChild
    #print text.toxml().encode('latin-1')


# routine to remove text description from score statement and GEN entries
unwantedtext = scoregens.getElementsByTagName('dt')
for text in unwantedtext:
    node = text.firstChild
    if node.nodeType == minidom.Node.ELEMENT_NODE and node.tagName == 'a':
        text.removeChild(text.childNodes[1])
        text.appendChild(minidom.Element('br'))
        

# Routines to remove indentation

#dt = toc.getElementsByTagName('dt')
#for j in range(len(dt)):
    #spanElement = dt.getElementsByTagName('span')
    #if spanElement.attributes['class'].value == 'section':
      #break
    #parent = dt[j].parentNode
    #print parent.toxml()
    #for k in range(len(dt[j].childNodes)):
        #parent.insertBefore(dt[j].firstChild ,dt[j])
    #parent.removeChild(dt[j])


#dl = toc.getElementsByTagName('dl')
#for j in range(len(dl)):
    #parent = dl[j].parentNode
    #for k in range(len(dl[j].childNodes)):
        #parent.insertBefore(dl[j].firstChild ,dl[j])
    #parent.removeChild(dl[j])
    
#dd = toc.getElementsByTagName('dd')
#for j in range(len(dd)):
    #parent = dd[j].parentNode
    #if (parent.nodeName!='dd'):
        #for k in range(len(dd[j].childNodes)):
            #parent.insertBefore(dd[j].firstChild ,dd[j])
        #parent.removeChild(dd[j])



#print toc
#print toc.toxml().encode('latin-1')
toc = toc.toxml().encode('utf-8')
contentsFile.write(toc)
contentsFile.close()

# Modify index.html to include a link to the frames version

if (index[titleEnd:titleEnd+len(frameLink)]!=frameLink):
    newindex = index[0:titleEnd]+ frameLink
    newindex += index[titleEnd:]
    indexFile.close()
    indexFile = open('html/index.html','w')
    indexFile.seek(0)
    indexFile.write(newindex)
    indexFile.close()


