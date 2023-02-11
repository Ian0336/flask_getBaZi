from flask import Flask, render_template, request, send_file, redirect, url_for
from flask_bootstrap import Bootstrap
import getBaZiFromNet as bz
import glob
import io
import os
name = " "
year = 0
mon = 2
day = 3
hr = 0
isMan = True
isLunar = False
isLeapMonth = False
mainStar = []
bornDay = []
eightword_f = []
eightword_s = []
eightword_f_elem = []
eightword_s_elem = []
bury = [[], [], [], []]
secondStar = [[], [], [], []]
fate = []
shansha = [[], [], [], []]
othershansha = []
bigFate = ""
bigFateYears = []
bigFateText = ""
flowYears = []
flowYears.append(" ")  # index 1
loveGod = ""
body = ""
personality = {}
horseFlower = {}
shanshaExplain = {}
couterAnimal = 0
yourAnimal = 0
sixCan = ""

app = Flask(__name__)
bs = Bootstrap(app)
def init():
    global name 
    global year 
    global mon 
    global day
    global hr
    global isMan 
    global isLunar 
    global isLeapMonth 
    global mainStar 
    global bornDay 
    global eightword_f 
    global eightword_s 
    global eightword_f_elem 
    global eightword_s_elem 
    global bury 
    global secondStar
    global fate 
    global shansha
    global othershansha 
    global bigFate 
    global bigFateYears 
    global bigFateText
    global flowYears 
    global loveGod
    global body 
    global personality
    global horseFlower 
    global shanshaExplain 
    global couterAnimal 
    global yourAnimal 
    global sixCan
    name = " "
    year = 0
    mon = 2
    day = 3
    hr = 0
    isMan = True
    isLunar = False
    isLeapMonth = False
    mainStar = []
    bornDay = []
    eightword_f = []
    eightword_s = []
    eightword_f_elem = []
    eightword_s_elem = []
    bury = [[], [], [], []]
    secondStar = [[], [], [], []]
    fate = []
    shansha = [[], [], [], []]
    othershansha = []
    bigFate = ""
    bigFateYears = []
    bigFateText = ""
    flowYears = []
    flowYears.append(" ")  # index 1
    loveGod = ""
    body = ""
    personality = {}
    horseFlower = {}
    shanshaExplain = {}
    couterAnimal = 0
    yourAnimal = 0
    sixCan = ""
@app.route('/')
def index():
    init()
    return render_template('index.html', title = "haha")
@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        for file in glob.glob("*.docx"):
            os.remove(file)
        """ for file in glob.glob("*.pdf"):
            os.remove(file) """
        global name,year,mon,day,hr,isMan,isLunar,isLeapMonth
        name = request.values['name']
        year = int(request.values['date'].split("-")[0])
        mon = int(request.values['date'].split("-")[1])
        day = int(request.values['date'].split("-")[2])
        hr = int(request.values['hour'])
        isMan = (request.values['gender'] == "man")
        isLunar = (request.values['lunar'] == "Lunar")
        isLeapMonth = (request.values['lunarMonth'] == "LunarMonth")
        print(name, year, mon, day, hr, isMan, isLunar, isLeapMonth)
        return render_template('generate.html', name=name, year=year, mon=mon, day=day, hr=hr, isMan=isMan, isLunar=isLunar, isLeapMonth=isLeapMonth)
@app.route('/ok')
def ok():
    bz.generate(nam=name, yea=year, mo=mon, da=day, h=hr, isMa=isMan, isLuna=isLunar, isLeapMont=isLeapMonth)
    return render_template('ok.html', name=name, year=year, mon=mon, day=day, hr=hr, isMan=isMan, isLunar=isLunar, isLeapMonth=isLeapMonth)
@app.route('/download/<name>')
def download(name):
    with open(f"./data/{name}.pdf", 'rb') as bites:
        return send_file(
            io.BytesIO(bites.read()),
            mimetype='application/pdf'
        )      
@app.route('/send/<name>')
def send(name):
    bz.send(name)
    return redirect(url_for('list'))
@app.route('/delete/<name>')
def delete(name):
    for file in glob.glob(f"./data/{name}.pdf"):
        os.remove(file)
    return redirect(url_for('list'))
@app.route('/list')
def list():
    pdfs =[]
    for file in glob.glob("./data/*.pdf"):
        pdfs.append(file.split(".")[1].split("\\")[1])
    return render_template('list.html', pdfs=pdfs)
if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000)
     #app.run(debug = True)