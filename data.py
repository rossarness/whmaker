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
