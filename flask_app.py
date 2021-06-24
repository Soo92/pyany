
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template
import pandas as pd
import sys,os
sys.path.append("templates/static")
sys.path.append("/home/SeongSuLee/mysite/templates/static")
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))+"/templates/static"

for p in sys.path:
    print( p )
import f_key as ff

app = Flask(__name__,static_url_path='/templates/static/')

@app.route('/t1')
def t1():
    return render_template('3tAcr.html',title='a')
@app.route('/t2')
def t2():
    return render_template('3tAcr.html',title='b')
@app.route('/t3')
def t3():
    return render_template('3tAcr.html',title='c')
@app.route('/t4')
def t4():
    return render_template('3tAcr.html',title='d')
@app.route('/t5')
def t5():
    return render_template('3tAcr.html',title='e')

@app.route('/admin')
def admin():
    FILE1 = os.path.join(THIS_FOLDER,"keyw.csv")
    FILE2 = os.path.join(THIS_FOLDER,"my.csv")
    FILE3 = os.path.join(THIS_FOLDER,"del.csv")
    FILE4 = os.path.join(THIS_FOLDER,"keyc.csv")
    html_all = pd.read_csv(FILE1, engine='python',encoding='euc-kr').to_html(table_id = "csv_table",classes="display compact")
    html_add = pd.read_csv(FILE2, engine='python',encoding='euc-kr').to_html(table_id = "add_table",classes="display compact")
    html_del = pd.read_csv(FILE3, engine='python',encoding='euc-kr').to_html(table_id = "del_table",classes="display compact")
    html_com = pd.read_csv(FILE4, engine='python',encoding='euc-kr').to_html(table_id = "key_com",classes="display compact")
    return render_template('ad_1.html',data_key=html_all,data_add=html_add,data_del=html_del,data_com=html_com)

@app.route('/reload')
def reload():
    ff.reload()
    return "hello"

if __name__ == '__main__':
    app.run()
