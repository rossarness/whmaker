'''This file contains SQL helpers for data manipulation'''
import sqlite3 as sql

DBASE = sql.connect('data/whdb')

def getmenutext(text, lang):
    '''This function will fetch menu text for menu entry
    It will return only first value and one column'''
    result = []
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM labels WHERE field_id=? AND lang=?''',
                   (text, lang))
    try:
        new_text = cursor.fetchone()
        result.append(new_text[0])
    except TypeError:
        print("Description for menu " + text + " not found")
        result.append(text)
    return result[0]

def getstatsdesc(lang):
    '''This function will return Array with all stats names in requested language'''
    stats = getstats()
    cursor = DBASE.cursor()
    result = []
    for stat in stats:
        try:
            cursor.execute('''SELECT name FROM labels
                        WHERE field_id=?
                        AND lang=? ORDER BY position ASC;''', (stat, lang,))
            raw = cursor.fetchone()
            result.append(raw[0])
        except TypeError:
            print("Unable to get label in " + lang + " for: " + stat)
            result.append(stat)
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
    try:
        result = formatresult(raw)
    except TypeError:
        print("Unable to get label in English")
        result = getraces("en")
    return result

def formatresult(raw):
    '''This function will format the result into pretty list'''
    result = []
    for row in raw:
        result.append(row[0])
    return result

def setactive(lang):
    '''This function will set current language as active'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM languages WHERE is_active="1"''')
    raw_old = cursor.fetchone()
    old_lang = raw_old[0]
    if raw_old != lang:
        cursor.execute('''UPDATE languages SET is_active="0" WHERE is_active="1"''')
        cursor.execute()

def closedb():
    '''This functon closes db on app exit'''
    DBASE.close()
