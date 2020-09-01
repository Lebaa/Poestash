import requests, json
import cv2 as cv
import time
import pyautogui
from operator import itemgetter
import random


league = "Harvest"
account = "Lebaa"
sessid = "6a8442d5e716cfc0cfd7e9da7c657d4d"
cfduid = "d362a63b151b7f74c6b8f9bf4efc8a31f1594966418"

global ID
ID = 0

inventory_x = [1295, 1355, 1405, 1455, 1505, 1555, 1605, 1660, 1725, 1775, 1825, 1875]
inventory_y = [615, 665, 715, 770, 825]

currencytab = []
fragmenttab = []
maptab = []
ylijäämä = []
essence = []
delve = []
divtab = []

def parse_currency(item):
    if "Scarabs" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        fragmenttab.append(a)
    elif "Catalysts" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        ylijäämä.append(a)
    elif "Oils" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        currencytab.append(a)
    elif "Essence" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        essence.append(a)
    elif "Delve" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        delve.append(a)
    elif "Prophecy" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        ylijäämä.append(a)
    elif "Incubation" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        ylijäämä.append(a)
    elif "Breach" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        fragmenttab.append(a)
    elif "Metamorph" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        ylijäämä.append(a)
    elif "Delirium" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        ylijäämä.append(a)
    elif "Splinter" in item['icon']:
        a = [item['typeLine'], item['x'], item['y']]
        fragmenttab.append(a)
    else:
        a = [item['typeLine'], item['x'], item['y']]
        currencytab.append(a)

def parse_map(item):
    if "Map" in item['typeLine']:
        a = [item['typeLine'], item['x'], item['y']]
        maptab.append(a)
    elif "Sacrifice" in item['typeLine']:
        a = [item['typeLine'], item['x'], item['y']]
        fragmenttab.append(a)
    elif "Mortal" in item['typeLine']:
        a = [item['typeLine'], item['x'], item['y']]
        fragmenttab.append(a)
    elif "Splinter" in item['typeLine']:
        a = [item['typeLine'], item['x'], item['y']]
        fragmenttab.append(a)
    elif "Offering" in item['typeLine']:
        a = [item['typeLine'], item['x'], item['y']]
        fragmenttab.append(a)


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
            if "Currency" in item['icon']:
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
    print(resp.status_code)
    json = resp.json()
    num = 1
    for x in range(num):

        tabiurl = url + "&tabIndex=" + str(x)
        tabi = requests.request("GET", tabiurl, headers=headers, data=payload)
        tabi_json = tabi.json()
        parse_tab(tabi_json)
        tabiurl = ""

def calc_clickpoint(x,y):
    x_coord = 30
    y_coord = 175
    return [(x_coord + int(x*26.3)), (y_coord + int(y*26.3))]

def draw_crosshairs(img, coordinates):

    for c in coordinates:
        cv.drawMarker(img, (c[0], c[1]), color=(255,0,255), markerType=cv.MARKER_CROSS, markerSize=10, thickness=2)

    return img

def stash_to_inventory(lista):

    lista.sort(key=itemgetter(2))
    lista.sort(key=itemgetter(1))
    pyautogui.moveTo(80,140,0.2)
    pyautogui.leftClick()
    pyautogui.keyDown('ctrl')
    for l in lista:
        coords = calc_clickpoint(l[1], l[2])
        pyautogui.moveTo(coords[0], coords[1], random.uniform(0.15, 0.30))
        pyautogui.leftClick()

    pyautogui.keyUp('ctrl')


def inventory_to_stash(tabi):
    if tabi == currencytab:
        pyautogui.leftClick(230,140,0.2)
    if tabi == fragmenttab:
        pyautogui.leftClick(305,140,0.2)
    if tabi == maptab:
        pyautogui.leftClick(170,140,0.2)

    pyautogui.keyDown('ctrl')
    for y in inventory_y:
        for x in inventory_x:
            pyautogui.moveTo(x,y,random.uniform(0.05,0.15))
            pyautogui.leftClick()
    pyautogui.keyUp('ctrl')

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
    inventory_to_stash(currencytab)
    break
    stash_to_inventory(fragmenttab)
    inventory_to_stash(fragmenttab)
    stash_to_inventory(maptab)
    inventory_to_stash(maptab)
    stash_to_inventory(delve)
    inventory_to_stash(delve)
    stash_to_inventory(essence)
    inventory_to_stash(essence)
    stash_to_inventory(divtab)
    inventory_to_stash(divtab)
    #click_items(essence)
    #click_items(divtab)

    screenshot = window_capture()
    screenshot = np.array(screenshot)
    output = draw_crosshairs(screenshot, markers)
    cv.imshow("Matches", output)

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break

print("Done.")
