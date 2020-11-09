import requests, json
import cv2 as cv
import time
import pyautogui
from operator import itemgetter
import random


league = "Heist"
account = "Lebaa"
sessid = "06eb90a33481fe625796c4fd67f4f8cc"
cfduid = "d83e779259a5de9bfe3ff2c4ad59fd9b31604933475"

global ID
ID = 0

inventory_x = [1295, 1355, 1405, 1455, 1505, 1555, 1605, 1660, 1725, 1775, 1825, 1875]
inventory_y = [615, 665, 715, 770, 825]

currencytab = []
currencytab2 = []
fragmenttab = []
fragmenttab2 = []
maptab = []
maptab2 = []
ylijäämä = []
essence = []
delve = []
divtab = []

def parse_currency(item):
    if "Incubation" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        ylijäämä.append(a)
    elif "Scarabs" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        if len(fragmenttab) < 60:
            fragmenttab.append(a)
        else:
            fragmenttab2.append(a)
    elif "Catalysts" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        ylijäämä.append(a)
    elif "Blueprint" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        ylijäämä.append(a)
    elif "Contract" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        ylijäämä.append(a)
    elif "Oils" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        if len(currencytab) < 60:
            currencytab.append(a)
        else:
            currencytab2.append(a)
    elif "Essence" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        essence.append(a)
    elif "Delve" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        delve.append(a)
    elif "Prophecy" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        ylijäämä.append(a)
    elif "Breach" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        if len(fragmenttab) < 60:
            fragmenttab.append(a)
        else:
            fragmenttab2.append(a)
    elif "Metamorph" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        ylijäämä.append(a)
    elif "Delirium" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        ylijäämä.append(a)
    elif "Splinter" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        if len(fragmenttab) < 60:
            fragmenttab.append(a)
        else:
            fragmenttab2.append(a)
    else:
        a = [item['typeLine'], item['x'], item['y']]
        if len(currencytab) < 60:
            currencytab.append(a)
        else:
            currencytab2.append(a)

def parse_map(item):
    if "Map" in item['typeLine']:
        a = [item['typeLine'], item['x'], item['y']]
        if len(maptab) < 60:
            maptab.append(a)
        else:
            maptab2.append(a)
    elif "Sacrifice" in item['typeLine']:
        a = [item['typeLine'], item['x'], item['y']]
        if len(fragmenttab) < 60:
            fragmenttab.append(a)
        else:
            fragmenttab2.append(a)
    elif "Mortal" in item['typeLine']:
        a = [item['typeLine'], item['x'], item['y']]
        if len(fragmenttab) < 60:
            fragmenttab.append(a)
        else:
            fragmenttab2.append(a)
    elif "Simulacrum" in item['typeLine']:
        a = [item['typeLine'], item['x'], item['y']]
        ylijäämä.append(a)
    elif "Splinter" in item['typeLine']:
        a = [item['typeLine'], item['x'], item['y']]
        if len(fragmenttab) < 60:
            fragmenttab.append(a)
        else:
            fragmenttab2.append(a)
    elif "Offering" in item['typeLine']:
        a = [item['typeLine'], item['x'], item['y']]
        if len(fragmenttab) < 60:
            fragmenttab.append(a)
        else:
            fragmenttab2.append(a)
    elif "Fragment" in item['typeLine']:
        a = [item['typeLine'], item['x'], item['y']]
        if len(fragmenttab) < 60:
            fragmenttab.append(a)
        else:
            fragmenttab2.append(a)


def parse_divination(item):
    a = [item['typeLine'], item['x'], item['y']]
    divtab.append(a)

def parse_armour(item):
    if len(item['sockets']) != 6:
        print("Eio 6s, mitä tekee?")
    else:
        sockets = item['sockets']
        groups = []
        for s in sockets:
            groups.append(s['group'])
        if all(g == groups[0] for g in groups):
            print("6l")
        else:
            print("ei oo 6l")

def parse_2h(item):
    if len(item['sockets']) != 6:
        print("Eio 6s, mitä tekee?")
    else:
        sockets = item['sockets']
        groups = []
        for s in sockets:
            groups.append(s['group'])
        if all(g == groups[0] for g in groups):
            print("6l")
        else:
            print("ei oo 6l")

def parse_flask(item):
    print("#"*50)
    print(item['typeLine'])
    try:
        if "increased Movement Speed" in item['utilityMods']:
            print("Quicksilver")
        if "increased Damage" in item['utilityMods']:
            print("Sulphur")
        if "to Evasion Rating" in item['utilityMods']:
            print("Jade")
        if "Armor" in item['utilityMods']:
            print("Granite")
        if "Elemental Resistances" in item['utilityMods']:
            print("Bismuth")
        if "increased Evasion Rating" in item['utilityMods']:
            print("Stibnite")
        if "Chaos Resistances" in item['utilityMods']:
            print("Amethyst")
        if "Fire Resistance" in item['utilityMods']:
            print("Ruby")
        if "Cold Resistance" in item['utilityMods']:
            print("Sapphire")
        if "Lightning Resistance" in item['utilityMods']:
            print("Topaz")
        if "Onslaught" in item['utilityMods']:
            print("Silver")
        if "Avoid Cold Damage" in item['utilityMods']:
            print("Aquamarine")
        if "Phasing" in item['utilityMods']:
            print("Quartz")
        if "Basalt" in item['utilityMods']:
            print("Physical damage reduction")
    except KeyError:
        print("Jotain meni vituiks")

    try:
        print(item['explicitMods'])
    except KeyError:
        print("Ei prefixiä?")

    try:
        print(item['implicitMods'])
    except KeyError:
        print("Ei suffixia")



def parse_amulet(item):
    '''todo'''

def parse_gem(item):
    '''todo'''

def parse_jewel(item):
    '''todo'''

def parse_belt(item):
    '''todo'''

def parse_ring(item):
    '''todo'''

def parse_quiver(item):
    '''todo'''

def parse_tab(tab):
    if len(tab['items']) != 0:
        itemit = tab['items']
        for item in itemit:
            if "Currency/Heist" in item ['icon']:
                print("Heisti paskaa")
            elif "Currency" in item['icon']:
                parse_currency(item)
            elif "Maps" in item['icon']:
                parse_map(item)
            elif "Map" in item['typeLine']:
                parse_map(item)
            elif "Divination" in item['icon']:
                parse_divination(item)
            elif "Armours" in item['icon']:
                '''parse_armour(item)'''
            elif not item['identified']:
                '''print("unid ei pysty")'''
            elif "TwoHandWeapons" in item['icon']:
                '''parse_2h(item)'''
            elif "Flask" in item['typeLine']:
                '''parse_flask(item)'''
            elif "Amulets" in item['icon']:
                '''parse_amulet(item)'''
            elif "Gems" in item['icon']:
                '''parse_gem(item)'''
            elif "Jewels" in item['icon']:
                '''parse_jewel(item)'''
            elif "Belts" in item['icon']:
                '''parse_belt(item)'''
            elif "Rings" in item['icon']:
                '''parse_ring(item)'''
            elif "Quivers" in item['icon']:
                '''parse_quiver(item)'''
            elif "Wand" in item['icon']:
                '''print("wandi")'''
            else:
                print(item)



def request_tabs():
    url = "https://www.pathofexile.com/character-window/get-stash-items?league="+league+"&accountName="+account+"&tabs=1"
    payload = {}
    headers = {
        "Cookie": "POESESSID="+sessid+"; __cfduid="+cfduid
    }

    resp = requests.request("GET", url, headers=headers, data=payload)
    json = resp.json()
    num = 1
    for x in range(num):

        tabiurl = url + "&tabIndex=" + str(x)
        tabi = requests.request("GET", tabiurl, headers=headers, data=payload)
        tabi_json = tabi.json()
        print(tabi_json)
        parse_tab(tabi_json)
        tabiurl = ""

def calc_clickpoint(x,y):
    x_coord = 30
    y_coord = 140
    return [(x_coord + int(x*26.3)), (y_coord + int(y*26.3))]

def draw_crosshairs(img, coordinates):

    for c in coordinates:
        cv.drawMarker(img, (c[0], c[1]), color=(255,0,255), markerType=cv.MARKER_CROSS, markerSize=10, thickness=2)

    return img

def stash_to_inventory(lista):

    lista.sort(key=itemgetter(2))
    lista.sort(key=itemgetter(1))

    pyautogui.moveTo(80,110,0.2)
    pyautogui.leftClick()
    pyautogui.keyDown('ctrl')
    for l in lista:

        coords = calc_clickpoint(l[1], l[2])
        pyautogui.moveTo(coords[0], coords[1], random.uniform(0.1, 0.25))
        pyautogui.leftClick()

    pyautogui.keyUp('ctrl')


def inventory_to_stash(tabi,string):

    if len(tabi) != 0:
        if string == "currencytab":
            pyautogui.moveTo(230,110,0.2)
            pyautogui.leftClick()
        elif string == "fragmenttab":
            pyautogui.moveTo(305,110,0.2)
            pyautogui.leftClick()
        elif string == "maptab":
            pyautogui.moveTo(170,110,0.2)
            pyautogui.leftClick()
        elif string == "divtab":
            pyautogui.moveTo(375, 110, 0.2)
            pyautogui.leftClick()
        elif string == "essencetab":
            pyautogui.moveTo(435, 110, 0.2)
            pyautogui.leftClick()
        elif string == "delve":
            pyautogui.moveTo(490, 110, 0.2)
            pyautogui.leftClick()
        elif string == "ylijäämä":
            pyautogui.moveTo(555, 110, 0.2)
            pyautogui.leftClick()

        pyautogui.keyDown('ctrl')
        counter = 0
        kiepit = 0

        print(tabi)
        for x in inventory_x:
            if(kiepit % 2) == 0 or (len(tabi)-counter) <6:
                kiepit += 1
                for y in inventory_y:
                    if len(tabi) != counter:
                        pyautogui.moveTo(x,y,random.uniform(0.01,0.05))
                        pyautogui.click(clicks=(random.randint(2,4)), interval=random.uniform(0.05,0.1))
                        counter += 1
                    else:
                        break

            elif (kiepit % 2) != 0:
                kiepit += 1
                for y in inventory_y[::-1]:
                    if len(tabi) != counter:
                        pyautogui.moveTo(x, y, random.uniform(0.01, 0.05))
                        pyautogui.click(clicks=(random.randint(3, 6)), interval=random.uniform(0.02, 0.005))
                        counter += 1
                    else:
                        break
        pyautogui.keyUp('ctrl')
        pyautogui.leftClick()

def countdown(n):
    print("Script starts in: ")
    while n > 0:
        print(str(n))
        n = n-1
        time.sleep(1)
        if n == 0:
            break

markers = []
request_tabs()
countdown(10)

while True:

    stash_to_inventory(currencytab)
    inventory_to_stash(currencytab, "currencytab")
    try:
        stash_to_inventory(currencytab2)
        inventory_to_stash(currencytab2,"currencytab")
    except:
        print("Jotain vituiks")
    stash_to_inventory(fragmenttab)
    inventory_to_stash(fragmenttab, "fragmenttab")
    try:
        stash_to_inventory(fragmenttab2)
        inventory_to_stash(fragmenttab2, "fragmenttab")
    except:
        print("Jotain vituiks")
    stash_to_inventory(maptab)
    inventory_to_stash(maptab, "maptab")
    try:
        stash_to_inventory(maptab2)
        inventory_to_stash(maptab2, "maptab")
    except:
        print("Jotain vituiks")
    stash_to_inventory(delve)
    inventory_to_stash(delve, "delve")
    stash_to_inventory(essence)
    inventory_to_stash(essence, "essencetab")
    stash_to_inventory(divtab)
    inventory_to_stash(divtab, "divtab")
    stash_to_inventory(ylijäämä)
    inventory_to_stash(ylijäämä, "ylijäämä")
    break

print("Done.")
