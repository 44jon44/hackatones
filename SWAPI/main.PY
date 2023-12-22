API_BASE_URL = 'https://swapi.dev/api/ee'
import requests


def testConnection(self):
    ok = None
    try:
        req = requests.request('GET', API_BASE_URL)
        print(req)

        if req.status_code == requests.codes.ok:
            print("Conexion correcta")
            ok = True
        elif req.status_code == requests.codes.not_found:
            print("No se ha encontrado")
            ok = False
    except requests.exceptions.ConnectionError:
        print("Error en la conexion")
        ok = False
    return ok


def getRoot():
    repuesta = requests.get('https://swapi.dev/api/')

    root = repuesta.json()
    return root


def getData(opc):
    # th = getRoot()
    # for nombre, valor in th.items():
    #    print(nombre)

    try:
        if opc == "people":
            people = requests.request('GET', "https://swapi.dev/api/people/")
            return people
        elif opc == "planet":
            planet = requests.request('GET', "https://swapi.dev/api/planets/")
            return planet
        elif opc == "films":
            films = requests.request('GET', "https://swapi.dev/api/films/")
            return films
        elif opc == "species":
            species = requests.request('GET', "https://swapi.dev/api/species/")
            return species
        elif opc == "vehicles":
            vehicles = requests.request('GET', "https://swapi.dev/api/vehicles/")
            return vehicles
        elif opc == "starships":
            starships = requests.request('GET', "https://swapi.dev/api/starships/")
            return starships
        else:
            return None

    except requests.exceptions.ConnectionError:
        print("Error en la conexion")


def getData2(url):
    try:
        data = requests.request('GET', url)
        return data
    except requests.exceptions.ConnectionError:
        print("Error en la conexion")


def getPersonajes():
    people = getData("people").json()
    next1 = people["next"]
    del people["count"]
    del people["next"]
    del people["previous"]
    print(people)

    while next1 is not None:
        people = getData2(next1).json()
        next1 = people["next"]
        del people["count"]
        del people["next"]
        del people["previous"]
        print(people)


def getPeopleByName(name="Luke Skywalker"):
    enc = False
    people = getData("people").json()
    next1 = people["next"]
    del people["count"]
    del people["next"]
    del people["previous"]

    if people['name'] == name:
        enc = True
        print(people)

    while not enc:
        people = getData2(next1).json()
        next1 = people["next"]
        del people["count"]
        del people["next"]
        del people["previous"]
        if people["name"] == name:
            enc = True
            print(people)


getPeopleByName()
