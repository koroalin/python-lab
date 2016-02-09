#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""

Tuxy cauta in fiecare zi cate o problema de matematica complet noua pentru el.

Rezolvand problema 101, a observat ca are nevoie de cateva formule mai vechi.
A revenit la fisierul lui de teoreme "teoreme1.txt" pentru ajutor. S-a bucurat 
ca a reusit sa il gaseasca la timp ,fisierul fiind in /tmp/ciorne. 
Uitandu-se prin el,a observat ca folosea o regula cand scria teoreme noi:

    [Index].[Spatiu][Spatiu][Numele Teoremei]
    [Numele scurt]
    [Rand nou]
    [Rand nou]
    [Teorema]
    [Rand nou]
    [Rand nou]

Exemplu: 
    1.  The Irrationality of the Square Root of 2  
        SQRT_2_IRRATIONAL 
       
        
     |- ~rational(sqrt(&2))


"""


"""
Stiind limbajul de programare python si fiind un fan al liniei de comanda,
el doreste sa implementeze un utilitar inteligent de cautat formule. 
Functionalitatile care doreste sa le implementeze sunt:
    [1] cautare indiferent de caz (ex. 'a'=='A' ) [-i]
    [2] cautare exacta ( nu ia in considere parti ale cuvintelor) [-e] 
    [3] cautare si schimbare a sirurilor de caractere [-s]
    [4] numararea aparitiilor unui sir de caractere [-n]
    [5] cautare recursiva a fisierelor prin director [-r]
    [6] introducerea parametrilor din linia de comanda:
    ex: python utilitar.py -in "CARD" teoreme1.txt
    sirul "CARD" (insensitiv) apare de 44 de ori in teoreme1.txt
    [7] afisarea unui mesaj de ajutor daca parametrii introdusi sunt gresiti

P.S. Prin inteligent se refera ca v-a returna tot ce stie despre teorema(nume,
nume scurt siteorema). Daca sirul de caractere cautat apare in mai multe
teoreme, utilitarul returneaza doar numele complet si cel scurt al teoremelor.
"""


"""

Oare cum a implementat Tuxy acest utilitar?

Posibila documentatie:
    - http://linux.die.net/man/1/grep
    - http://git.savannah.gnu.org/cgit/grep.git/snapshot/grep-2.22.tar.gz
    - din cadrul arhivei amintite anterior, folderul "src"
    - https://github.com/heyhuyen/python-grep
"""
def main(*args):
    try:
        path=args[-1]
        fisier=open(path,"r")
        teoreme=fisier.read()
        fisier.close()
    except IOError:
        print "Eroare de I/O"
        return
    sir=args[-2] """aici am sirul"""
    ar=args[-3]
    checkArguments(ar)

 def checkArguments(ar):
 	alfabet="-iesnr"
 	for litera in ar:


