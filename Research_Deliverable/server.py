# flask --app data_server run

from flask import Flask
from flask import render_template
from flask import request
from data.reformat_data import dictionary 
import json


app = Flask(__name__, static_url_path='', static_folder='static')

with open("data/data_bite.json") as f:
    bite_data = json.load(f)

@app.route('/')
def about():
    return render_template("about.html")

@app.route('/macro')
def index():
    f = open("data/data_bite.json", "r")
    data = json.load(f)
    f.close()
    bronx_endpoints = []
    brooklyn_endpoints = []
    manhattan_endpoints = []
    queens_endpoints = []
    staten_island_endpoints = []
    avg_endpoints = []

    years = sorted([int(y) for y in data["Bronx"].keys()])

    for i in range(len(years) - 1):
        year1 = str(years[i])
        year2 = str(years[i + 1])

        bx_y1 = float(data["Bronx"][year1])
        bx_y2 = float(data["Bronx"][year2])
        bronx_endpoints.append([bx_y1, bx_y2])

        bk_y1 = float(data["Brooklyn"][year1])
        bk_y2 = float(data["Brooklyn"][year2])
        brooklyn_endpoints.append([bk_y1, bk_y2])

        m_y1 = float(data["Manhattan"][year1])
        m_y2 = float(data["Manhattan"][year2])
        manhattan_endpoints.append([m_y1, m_y2])

        q_y1 = float(data["Queens"][year1])
        q_y2 = float(data["Queens"][year2])
        queens_endpoints.append([q_y1, q_y2])

        si_y1 = float(data["Staten Island"][year1])
        si_y2 = float(data["Staten Island"][year2])
        staten_island_endpoints.append([si_y1, si_y2])

        avg_y1 = float(bx_y1 + bk_y1 + m_y1 + q_y1 + si_y1)/5
        avg_y2 = float(bx_y2 + bk_y2 + m_y2 + q_y2 + si_y2)/5
        avg_endpoints.append([avg_y1, avg_y2])





    return render_template(
    "macro.html",
    bronx_endpoints = bronx_endpoints,
    brooklyn_endpoints = brooklyn_endpoints,  
    manhattan_endpoints = manhattan_endpoints,
    queens_endpoints = queens_endpoints,
    staten_island_endpoints = staten_island_endpoints,
    avg_endpoints = avg_endpoints,
    years=years
    )

    print (data)
@app.route('/micro')

def year(): 
    f = open("data/data_bite.json", "r")
    data = json.load(f)
    f.close()
    year = request.args.get("year")

    bx_val = float(data["Bronx"][str(year)])
    bk_val = float(data["Brooklyn"][str(year)])
    man_val = float(data["Manhattan"][str(year)]) 
    q_val = float(data["Queens"][str(year)]) 
    si_val = float(data["Staten Island"][str(year)]) 

    universal_val = (bx_val + bk_val + man_val + q_val + si_val)/5

    # dist from avg --> used for micro state

    delta_bx = round(bx_val - universal_val, 2)
    delta_bk = round(bk_val - universal_val, 2)
    delta_man = round(man_val - universal_val, 2)
    delta_q = round(q_val - universal_val, 2)
    delta_si = round(si_val - universal_val, 2)

    bronx_color = 100 * (400 - bx_val) / 400
    brooklyn_color = 100 * (400 - bk_val) / 400
    manhattan_color = 100 * (400 - man_val) / 400
    queens_color = 100 * (400 - q_val) / 400
    staten_island_color = 100 * (400 - si_val) / 400






    return render_template(
        "micro.html",
        year=year,
        bx_val = bx_val,
        bk_val = bk_val,
        man_val = man_val,
        q_val = q_val,
        si_val = si_val,

        universal_val=round(universal_val, 2), 
        delta_bx=delta_bx,
        delta_bk = delta_bk,
        delta_man=delta_man,
        delta_q=delta_q,
        delta_si=delta_si,

        bronx_color=bronx_color,
        brooklyn_color=brooklyn_color,
        manhattan_color=manhattan_color,
        queens_color=queens_color,
        staten_island_color=staten_island_color
    )

if __name__ == "__main__":
    app.run(debug=True)

