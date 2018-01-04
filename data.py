'''This file contains SQL helpers for data manipulation'''
import sqlite3 as sql

DBASE = sql.connect('data/whdb')

def getmenutext(text, lang):
    '''This function will fetch menu text for menu entry
    It will return only first value and one column'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM menus WHERE field_id=? AND lang=?''',
                   (text, lang))
    new_text = cursor.fetchone()
    return new_text[0]

def getstatsdesc(lang):
    '''This function will return Array with all stats names in requested language'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM menus
                    WHERE field_id IN ('ws','bs','s','t','ag','int','wp','fel') 
                    AND lang=? ORDER BY position ASC;''', (lang,))
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(row[0])
    return result

def getlanguages():
    '''This function will return all languages supported by the application'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT lang from languages''')
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(row[0])
    return result

def closedb():
    '''This functon closes db on app exit'''
    DBASE.close()
