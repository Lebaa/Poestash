import requests, json
import MySQLdb as mysql
import sshtunnel

league = "Harvest"
account = "Lebaa"
sessid = "6a8442d5e716cfc0cfd7e9da7c657d4d"
cfduid = "d362a63b151b7f74c6b8f9bf4efc8a31f1594966418"

global ID
ID = 0

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

def db_command(command, variables):
    with sshtunnel.SSHTunnelForwarder(
        ("ssh.eu.pythonanywhere.com"),
        ssh_username="Leba",
        ssh_password="Lebalol123",
        remote_bind_address=("Leba.mysql.eu.pythonanywhere-services.com", 3306),
    ) as tunnel:
        connection = mysql.connect(
            user="Leba",
            password="superpassu",
            host="127.0.0.1",
            port=tunnel.local_bind_port,
            database="Leba$PoeStash",
        )

        cur = connection.cursor()
        cur.execute(command, variables)
        result = cur.fetchall()
        connection.commit()
        connection.close()
        return result

def parse_currency(item):
    if "Scarabs" in item['icon']:
        print("Seo scrarabi")
    elif "Catalysts" in item['icon']:
        value = item['properties'][0]['values'][0][0].strip().split('/')[0]
        print(value + " x " + item['typeLine'])
    elif "Oils" in item['icon']:
        value = item['properties'][0]['values'][0][0].strip().split('/')[0]
        print(value + " x " + item['typeLine'])
    elif "Essence" in item['icon']:
        value = item['properties'][0]['values'][0][0].strip().split('/')[0]
        print(value + " x " + item['typeLine'])
    elif "Delve" in item['icon']:
        value = item['properties'][0]['values'][0][0].strip().split('/')[0]
        print(value + " x " + item['typeLine'])
    elif "Prophecy" in item['icon']:
        print("ennustuksia")
    elif "Incubation" in item['icon']:
        print("Inkubaattori")
    elif "Breach" in item['icon']:
        value = item['properties'][0]['values'][0][0].strip().split('/')[0]
        print(value + " x " + item['typeLine'])
    elif "Metamorph" in item['icon']:
        print("Sisäelin")
    elif "Delirium" in item['icon']:
        value = item['properties'][0]['values'][0][0].strip().split('/')[0]
        print(value + " x " + item['typeLine'])
    else:
        value = item['properties'][0]['values'][0][0].strip().split('/')[0]
        print(value + " x " + item['typeLine'])

def parse_map(item):
    if "Map" in item['typeLine']:
        value = item['properties'][0]['values'][0][0].strip().split('/')[0]
        print(item['typeLine'] + " tier: " + value)
    elif "Sacrifice" in item['typeLine']:
        print(item['typeLine'])
    elif "Mortal" in item['typeLine']:
        print("Mortal fragment")

def parse_divination(item):
    value = item['properties'][0]['values'][0][0].strip().split('/')[0]
    print(value + " x " + item['typeLine'])

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
                '''parse_currency(item)'''
            elif "Maps" in item['icon']:
                print(item)
                parse_map(item)
            elif "Map" in item['typeLine']:
                parse_map(item)
            elif "Divination" in item['icon']:
                '''parse_divination(item)'''
                '''print(item)'''
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
    num = json['numTabs']

    for x in range(num):

        tabiurl = url + "&tabIndex=" + str(x)
        tabi = requests.request("GET", tabiurl, headers=headers, data=payload)
        tabi_json = tabi.json()
        parse_tab(tabi_json)
        tabiurl = ""

def insert_account(accountName, sessionID):
    command = "INSERT INTO poe_account (account_name, session_id) VALUES (%s, %s)"
    db_command(command, (accountName, sessionID))

def insert_stash_tab(accountID,tabName):
    command = "INSERT INTO stash_tab (account_id, tab_name) VALUES (%s, %s)"
    db_command(command(accountID,tabName))

request_tabs()

