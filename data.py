'''This file contains SQL helpers for data manipulation'''
import sqlite3 as sql

DBASE = sql.connect('data/whdb')

def getmenutext(text, lang):
    '''This function will fetch menu text for menu entry
    It will return only first value and one column'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM labels WHERE field_id=? AND lang=?''',
                   (text, lang))
    new_text = cursor.fetchone()
    return new_text[0]

def getstatsdesc(lang):
    '''This function will return Array with all stats names in requested language'''
    stats = getstats()
    cursor = DBASE.cursor()
    result = []
    for stat in stats:
        cursor.execute('''SELECT name FROM labels
                    WHERE field_id=?
                    AND lang=? ORDER BY position ASC;''', (stat, lang,))
        raw = cursor.fetchone()
        result.append(raw[0])
    return result

def getlanguages():
    '''This function will return all languages supported by the application'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name from languages''')
    raw = cursor.fetchall()
    return formatresult(raw)

def maplanguage(name):
    '''This function will return lang_id based on name'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT lang FROM languages WHERE name=?''', (name, ))
    lang = cursor.fetchone()
    return lang[0]

def getlangname(lang):
    '''This function will return lang_name based on lang'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM languages WHERE lang=?''', (lang, ))
    name = cursor.fetchone()
    return name[0]

def getstats():
    '''This function will return all stats for the characters'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM attributes ORDER BY pos''')
    raw = cursor.fetchall()
    return formatresult(raw)

def getraces(lang):
    '''This function will return all races'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM races WHERE lang=?''', (lang, ))
    raw = cursor.fetchall()
    return formatresult(raw)

def formatresult(raw):
    '''This function will format the result into pretty list'''
    result = []
    for row in raw:
        result.append(row[0])
    return result

def closedb():
    '''This functon closes db on app exit'''
    DBASE.close()
