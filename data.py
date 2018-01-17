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

def mapmenutext(text, lang):
    '''This function returns id of the requested label'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT field_id FROM labels
                      WHERE name=? AND lang=?''', (text, lang, ))
    raw = cursor.fetchone()
    return raw[0]

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
    '''This function will return lang_name based on lang_id'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM languages WHERE lang=?''', (lang, ))
    name = cursor.fetchone()
    return name[0]

def getstats():
    '''This function will return all stats for the characters'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM attributes WHERE disabled=0 ORDER BY pos''')
    raw = cursor.fetchall()
    return formatresult(raw)

def getvisiblestats():
    '''This function will return all stats which values should be printed in
    Character generation menu. Flag hidden is used for hiding attribute in case
    that it's a e.g. combobox that doesn't hold value in Label'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM attributes WHERE hidden IS NOT 1 ORDER BY pos''')
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
        langerror = getlangname(lang)
        print("Unable to get label in " + langerror)
        result = getraces("en")
    return result

def getrace(race_id, lang):
    '''This function will return race based on id in given language'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM races WHERE race_id=? AND lang=?''', (race_id, lang))
    raw = cursor.fetchone()
    try:
        race = raw[0]
    except TypeError:
        langerror = getlangname(lang)
        print("Unable to get label in " + langerror)
        race = getrace(race_id, "en")
    return race


def maprace(race, lang):
    '''This function will return race_id based on localized race string'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT race_id FROM races WHERE name=? AND lang=?''', (race, lang, ))
    race_id = cursor.fetchone()
    return race_id[0]

def formatresult(raw):
    '''This function will format the result into pretty list'''
    result = []
    result.append(raw[0])
    result = []
    for row in raw:
        result.append(row[0])
    return result

def setactive(lang):
    '''This function will set current language as active'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT lang FROM languages WHERE is_active="1"''')
    old_lang = None
    try:
        raw_old = cursor.fetchone()
        old_lang = raw_old[0]
    except TypeError:
        print("ERROR: No Language is active")
    if old_lang is not None:
        cursor.execute('''UPDATE languages SET is_active="0" WHERE lang=?''', (old_lang, ))
        DBASE.commit()
    cursor.execute('''UPDATE languages SET is_active=1 WHERE lang=?''', (lang, ))
    DBASE.commit()

def getactive():
    '''This function returns currently active language'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT lang FROM languages WHERE is_active="1"''')
    try:
        raw = cursor.fetchone()
        lang = raw[0]
    except TypeError:
        print("ERROR: No Language is active")
        lang = "en"
    return lang

def getgenders(lang):
    '''This function returns gender text description in given language'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM labels WHERE field_id
                      IN ("male","female") AND lang=?''', (lang, ))
    raw = cursor.fetchall()
    try:
        genders = formatresult(raw)
    except IndexError:
        print("Unable to get genders in current Language")
        genders = getgenders("en")
    return genders

def gethair(lang, color_id, race):
    '''This function will return request hair color name
    It checks language, color_id and race
    Returns a string with color name'''
    raceid = maprace(race, lang)
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM hair_color
                      WHERE race=? AND lang=?
                      AND color_id=?''', (raceid, lang, color_id, ))
    try:
        raw = cursor.fetchone()
        color = raw[0]
    except TypeError:
        print("ERROR: Invalid hair color value: " + str(color_id) + " Race: "
              + str(race) + " lang: " + str(lang))
        color = "Undefined"
    return color

def getage(lang, age_id, race):
    '''This function will return age based on age_id and race'''
    cursor = DBASE.cursor()
    race_id = maprace(race, lang)
    cursor.execute('''SELECT '''+ race_id +''' FROM character_age WHERE dice_value=?''', (age_id, ))
    raw = cursor.fetchone()
    return raw[0]

def geteye(lang, color_id, race):
    '''This function will return requested eye color based on race color_id and laguage.
    Returns string with a name'''
    raceid = maprace(race, lang)
    cursor = DBASE.cursor()
    cursor.execute('''SELECT color FROM eye_color
                      WHERE race=? AND lang=?
                      AND color_id=?''', (raceid, lang, color_id, ))
    try:
        raw = cursor.fetchone()
        color = raw[0]
    except TypeError:
        print("ERROR: Invalid eye color value: " + str(color_id) + " Race: "
              + str(race) + " lang: " + str(lang))
        color = "Undefined"
    return color

def getweight(lang, weight_id, race):
    '''This function will return weight based on weight_id and race'''
    cursor = DBASE.cursor()
    race_id = maprace(race, lang)
    cursor.execute('''SELECT '''+ race_id +''' FROM weight WHERE weight_id=?''', (weight_id, ))
    raw = cursor.fetchone()
    return raw[0]

def getmark(lang, mark_id):
    '''This function will return distinguishing mark based on id and language'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM distinguishing_marks WHERE lang=? AND mark_id=?''',
                   (lang, mark_id, ))
    raw = cursor.fetchone()
    try:
        mark = raw[0]
    except TypeError:
        print("ERROR: Mark not found for id: " + str(mark_id) + " and language: " + lang)
        mark = "Undefined"
    return mark

def getbirthplace(place_id, lang):
    '''Returns birthplaces from DB'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM birthplace
                      WHERE place_id=? AND lang=?''', (place_id, lang, ))
    raw = cursor.fetchone()
    try:
        result = raw[0]
    except TypeError:
        print("ERROR: Birthplace not found for language: " + lang)
        result = getbirthplace(place_id, "en")
    return result

def getbirthdetails(detail_id, lang):
    '''Return birthplace details for human birthplace'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM birthplace_detail
                      WHERE place_id=? AND lang=?''', (detail_id, lang, ))
    raw = cursor.fetchone()
    try:
        result = raw[0]
    except TypeError:
        print("ERROR: Birthplace detail not found for language: " + lang)
        result = getbirthdetails(detail_id, "en")
    return result

def getsiblings(race, sib_id):
    '''Returns number of siblings for given race'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT ''' + race + ''' FROM siblings
                      WHERE id=?''', (sib_id, ))
    result = cursor.fetchone()
    return result[0]

def getstar(star_id, lang):
    '''Returns star sign for the character in given language'''
    cursor = DBASE.cursor()
    cursor.execute('''SELECT name FROM star_sign WHERE lang=? AND sign_id=?''', (lang, star_id, ))
    raw = cursor.fetchone()
    try:
        result = raw[0]
    except TypeError:
        print("ERROR: Star sign not found for language: " + lang)
        result = getstar(star_id, "en")
    return result

def closedb():
    '''This functon closes db on app exit'''
    DBASE.close()
