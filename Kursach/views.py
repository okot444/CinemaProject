from django.shortcuts import render
import json
import hashlib
from pathlib import Path
import datetime


def hallsize(hall):
    if hall == "Большой":
          return 100
    if hall == "Малый":
        return 50


def login(request):
    return render(request, 'login.html', {})

def index(request):
    today = str(datetime.datetime.date(datetime.datetime.now()).day) + "." + str(
        datetime.datetime.date(datetime.datetime.now()).month) + "." + str(
        datetime.datetime.date(datetime.datetime.now()).year)
    with open("Kursach/data.json", 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        films=list()
        date=list(data["Timetable"])
        try:
            hlist=list(data["Timetable"][today])
            for i in range(0,len(hlist)):
                flist=list(data["Timetable"][today][hlist[i]])
                for j in range(0,len(flist)):
                    film=list()
                    time = str(data["Timetable"][today][hlist[i]][flist[j]]["start"]) +"-" +str(
                        data["Timetable"][today][hlist[i]][flist[j]]["end"])
                    film.append(time)
                    film.append(data["Timetable"][today][hlist[i]][flist[j]]["film"])
                    film.append(data["Timetable"][today][hlist[i]][flist[j]]["price"])
                    film.append(str(hlist[i]))
                    film.append(data["Timetable"][today][hlist[i]][flist[j]]["id"])
                    films.append(film)
        except:
            pass
    #films.sort()
    name = data["Cinema"]["name"]
    address = data["Cinema"]["address"]
    tel = data["Cinema"]["tel"]
    maplink = data["Cinema"]["location"]
    worktime = data["Cinema"]["time of work"]
    return render(request, 'index.html', {"films": films,"name": name,"tel": tel,"address": address,"maplink": maplink, "today": today,"worktime": worktime})


def contacts(request):
    with open("Kursach/data.json", 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        name = data["Cinema"]["name"]
        address = data["Cinema"]["address"]
        tel = data["Cinema"]["tel"]
        ctel = data["Cinema"]['ctel']
        maplink = data["Cinema"]["location"]
        worktime = data["Cinema"]["time of work"]
    return render(request, 'contacts.html', {"name": name,"tel": tel,"address": address, "ctel": ctel, "maplink": maplink,"worktime": worktime})


def timetable(request):
    with open("Kursach/data.json", 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        date = list(data["Timetable"])
        table=list()
        for l in range(0, len(date)):
            films=list()
            films.append(date[l])
            hlist = list(data["Timetable"][date[l]])
            for i in range(0, len(hlist)):
                flist = list(data["Timetable"][date[l]][hlist[i]])
                for j in range(0, len(flist)):
                    film = list()
                    time = str(data["Timetable"][date[l]][hlist[i]][flist[j]]["start"]) + "-" + str(
                        data["Timetable"][date[l]][hlist[i]][flist[j]]["end"])
                    film.append(time)
                    film.append(data["Timetable"][date[l]][hlist[i]][flist[j]]["film"])
                    film.append(data["Timetable"][date[l]][hlist[i]][flist[j]]["price"])
                    film.append(str(hlist[i]))
                    film.append(data["Timetable"][date[l]][hlist[i]][flist[j]]["id"])
                    films.append(film)
            table.append(films)
        name = data["Cinema"]["name"]
        address = data["Cinema"]["address"]
        tel = data["Cinema"]["tel"]
        maplink = data["Cinema"]["location"]
        worktime = data["Cinema"]["time of work"]
    return render(request, 'timetable.html', {"name": name, "tel": tel, "address": address, "maplink": maplink,
                                              "table": table,"worktime": worktime})




def film(request):
    if request.method == "GET":
        filmname = request.GET["film"]
        id=request.GET["id"]
    with open("Kursach/data.json", 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        description =data["Films"][id]["Description"]
        postsrc=data["Films"][id]["poster"]
        genre=data["Films"][id]["Genre"]
        length=data["Films"][id]["length"]+" минут"

        name = data["Cinema"]["name"]
        address = data["Cinema"]["address"]
        tel = data["Cinema"]["tel"]
        maplink = data["Cinema"]["location"]
        worktime = data["Cinema"]["time of work"]
    return render(request, 'film.html', {"name": name, "tel": tel, "address": address, "maplink": maplink,
                                         "description":description,"postsrc":postsrc,"filmname":filmname,"genre":genre,"worktime": worktime,"length":length})


def edit(request):
    if request.method == "GET":
        login = request.GET["login"]
        password=request.GET["password"]
    with open("Kursach/data.json", 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        mlist=list(data["Users"]["Admins"])
        for i in mlist:
            if login == data["Users"]["Admins"][i]["login"]:
                if hashlib.sha256((password + login).encode()).hexdigest() == data["Users"]["Admins"][i]["password"]:
                    return table(request)
        alist=list(data["Users"]["Admins"])
        for i in alist:
            if login == data["Users"]["Admins"][i]["login"]:
                if hashlib.sha256((password + login).encode()).hexdigest() == data["Users"]["Admins"][i]["password"]:
                    return Users(request)
        return render(request, "login.html", {"wrong": "Wrong login or password"})

#edit timetable
def table(request):

    with open("Kursach/data.json", 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        date = list(data["Timetable"])
        table=list()
        for l in range(0, len(date)):
            films=list()
            films.append(date[l])
            hlist = list(data["Timetable"][date[l]])
            for i in range(0, len(hlist)):
                flist = list(data["Timetable"][date[l]][hlist[i]])
                for j in range(0, len(flist)):
                    film = list()
                    time = str(data["Timetable"][date[l]][hlist[i]][flist[j]]["start"]) + "-" + str(
                        data["Timetable"][date[l]][hlist[i]][flist[j]]["end"])
                    film.append(time)
                    film.append(data["Timetable"][date[l]][hlist[i]][flist[j]]["film"])
                    film.append(data["Timetable"][date[l]][hlist[i]][flist[j]]["price"])
                    film.append(str(hlist[i]))
                    film.append(flist[j])
                    films.append(film)
            table.append(films)
        fk=list(data["Films"])
        filmlist = list()
        for i in fk:
            filmlist.append(data["Films"][i]["name"])
    return render(request, 'EDITtimetable.html', {"table": table,"filmlist":fk})


def add(request):
    path = Path("Kursach/data.json")
    data = json.loads(path.read_text(encoding='utf-8'))
    if request.method == "GET":
        filmid = request.GET["fname"]
        time = request.GET["time"]
        price = request.GET["price"]
        hall = request.GET["hall"]
        date = request.GET["date"]
    filmname = data["Films"][filmid]["name"]
    timet = time.split("-")
    if len(timet[0]) == 4:
        time = "0"+time
    try:
        data["Timetable"][date][hall]={**data["Timetable"][date][hall], **{time:""}}
    except:
        data["Timetable"][date]={**data["Timetable"][date],**{hall:""}}
        data["Timetable"][date][hall]={time:""}


    data["Timetable"][date][hall][time] = {"end": timet[1],
                    "film": filmname,
                    "number": hallsize(hall),
                    "price": price,
                    "start": timet[0],
                    "id": filmid
                    }
    path.write_text(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')), encoding='utf-8')
    return table(request)


def EDTable(request):
    if request.method == "GET":
        id=request.GET["id"]
        filmid = request.GET["fname"]
        time = request.GET["time"]
        price = request.GET["price"]
        hall = request.GET["hall"]
    temp = id.split("$")
    id = temp[0]
    date = temp[1]
    path = Path("Kursach/data.json")
    data = json.loads(path.read_text(encoding='utf-8'))
    timet = time.split("-")
    filmname=data["Films"][filmid]["name"]
    data["Timetable"][date][hall][id] = {"end": timet[1],
                                               "film": filmname,
                                               "number": hallsize(hall),
                                               "price": price,
                                               "start": timet[0]}
    path.write_text(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')), encoding='utf-8')
    return table(request)


def delTable(request):
    if request.method == "GET":
        id=request.GET["id"]
    temp = id.split("$")
    id = temp[0]
    date = temp[1]
    hall=temp[2]
    path = Path("Kursach/data.json")
    data = json.loads(path.read_text(encoding='utf-8'))
    del(data["Timetable"][date][hall][id])
    path.write_text(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')), encoding='utf-8')
    return table(request)


def DelDate(request):
    if request.method == "GET":
        date = request.GET["date"]
    path = Path("Kursach/data.json")
    data = json.loads(path.read_text(encoding='utf-8'))
    del (data["Timetable"][date])
    path.write_text(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')), encoding='utf-8')
    return table(request)


def AddDate(request):
    if request.method == "GET":
        date = request.GET["date"]
    if(len(date)>0):
        path = Path("Kursach/data.json")
        data = json.loads(path.read_text(encoding='utf-8'))
        data["Timetable"] = {**data["Timetable"], **{date: {}}}
        path.write_text(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')), encoding='utf-8')
    return table(request)


#edit films functions
def films(request):
    with open("Kursach/data.json", 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        fk=list(data["Films"])
        flist=list()
        for i in range(0,len(fk)):
            film=list()
            film.append(data["Films"][fk[i]]["name"])
            film.append(data["Films"][fk[i]]["Genre"])
            film.append(data["Films"][fk[i]]["Description"])
            postersrc=str(data["Films"][fk[i]]["poster"]).replace("images/posters/", "")
            film.append(postersrc)
            film.append(fk[i])
            '''length=data["Films"][fk[i]]["length"]+" мин"
            film.append(length)'''
            flist.append(film)
    return render(request, 'EDITfilm.html', {"flist":flist})


def addFilm(request):
    if request.method == "GET":
        name=request.GET["name"]
        dis=request.GET["dis"]
        poster=request.GET["poster"]
        genre=request.GET["genre"]
        length=request.GET["length"]
    path = Path("Kursach/data.json")
    data = json.loads(path.read_text(encoding='utf-8'))
    n = len(list(data["Films"]))-1
    idf = list(data["Films"])
    if len(idf)==0:
        n=0
    else:
        n = int(idf[n])+1
    data["Films"] = {**data["Films"], **{str(n): ""}}
    postersrc="images/posters/"+str(poster)
    data["Films"][n] = {"name": name, "Description": dis, "Genre": genre, "poster":postersrc ,"length":length}
    path.write_text(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')), encoding='utf-8')
    return films(request)


def EDFilm(request):
    if request.method == "GET":
        name=request.GET["name"]
        dis=request.GET["dis"]
        poster=request.GET["poster"]
        genre=request.GET["genre"]
        id=request.GET["ID"]
    path = Path("Kursach/data.json")
    data = json.loads(path.read_text(encoding='utf-8'))
    n = id
    postersrc="images/posters/"+str(poster)
    data["Films"][n] = {"name": name, "Description": dis, "Genre": genre, "poster":postersrc }
    path.write_text(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')), encoding='utf-8')
    return films(request)


def delFilm(request):
    if request.method == "GET":
        id=request.GET["ID"]
    path = Path("Kursach/data.json")
    data = json.loads(path.read_text(encoding='utf-8'))
    del(data['Films'][id])
    path.write_text(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')), encoding='utf-8')
    return films(request)
'''

#edit users list functions
def Users(request):
    with open("Kursach/data.json", 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        adminlist=list(data["Users"]["Admins"])
        managerlist = list(data["Users"]["Managers"])
        userlist=list()
        for i in adminlist:
            user=list()
            user.append(data["Users"]["Admins"][i]["login"])
            password="******"
            user.append(password)
            user.append("Admin")
            user.append(i)
            userlist.append(user)
        for i in managerlist:
            user=list()
            user.append(data["Users"]["Managers"][i]["login"])
            password ="******"
            user.append(password)
            user.append("Manager")
            user.append(i)
            userlist.append(user)
    return render(request, 'users.html', {"userlist": userlist})


def EditUser(request):
    if request.method == "GET":
        login = request.GET["login"]
        password = request.GET["password"]
        role = request.GET["role"]
        id=request.GET["id"]
    path = Path("Kursach/data.json")
    data = json.loads(path.read_text(encoding='utf-8'))
    if role == "Admin":
        n = id
        if password == "******":
            data["Users"]["Admins"][n] = {
                "login": login,
                "password": data["Users"]["Adnins"][n]["password"]
            }
        else:
            data["Users"]["Admins"][n] = {
                "login": login,
                "password": hashlib.sha256((password + login).encode()).hexdigest()
            }
    if role == "Manager":
        n = id
        if password == "******":
            data["Users"]["Managers"][n] = {
                "login": login,
                "password": data["Users"]["Managers"][n]["password"]
            }
        else:
            data["Users"]["Managers"][n] = {
                "login": login,
                "password": hashlib.sha256((password + login).encode()).hexdigest()
            }
    path.write_text(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')), encoding='utf-8')
    return Users(request)


def AddUser(request):
    if request.method == "GET":
        login = request.GET["login"]
        password = request.GET["password"]
        role = request.GET["role"]
    path = Path("Kursach/data.json")
    data = json.loads(path.read_text(encoding='utf-8'))
    if role == "Admin":
        n = len(list(data["Users"]["Admins"]))
        data["Users"]["Admins"] = {**data["Users"]["Admins"], **{n: ""}}
        data["Users"]["Admins"][n] = {
            "login": login,
            "password": hashlib.sha256((password+login).encode()).hexdigest()
        }
    if role == "Manager":
        n = len(list(data["Users"]["Managers"]))
        data["Users"]["Managers"] = {**data["Users"]["Managers"], **{n: ""}}
        data["Users"]["Managers"][n] = {
            "login": login,
            "password": hashlib.sha256((password+login).encode()).hexdigest()
        }
    path.write_text(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')), encoding='utf-8')
    return Users(request)


def DelUser(request):
    if request.method == "GET":
        id = request.GET["id"]
    temp = id.split("$")
    id = temp[0]
    role = temp[1]+"s"
    path = Path("Kursach/data.json")
    data = json.loads(path.read_text(encoding='utf-8'))
    del (data["Users"][role][id])
    path.write_text(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')), encoding='utf-8')
    return Users(request)

'''