from flask import Flask,render_template,request,jsonify
import webbrowser
from threading import Timer
from test_v2 import *
app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def interface():
    if request.method == "POST":

        data = {}
              
        accounts = request.form["accounts"]
        subject = request.form["subject"]
        task = request.form["tasks"]
        threads = request.form["threads"]
        browsers = request.form["Radio"]   
        link = request.form["link"]
        if request.form.get("box", False):
            hide = request.form["box"]
        elif request.form.get("box", True):
            hide = 'dont_hide_browser'
        try :
            reply = request.form["reply_msg"]
        except :
            reply = "NAN"
        mark_as_read = request.form["Radio2"]
        
        data['subject'] = subject
        data['task'] = task
        data['threads'] = threads
        data['browsers'] = browsers
        data['link'] = link
        data['accounts'] = accounts
        data['hide'] = hide
        data['reply'] = reply
        data['mark_as_read'] = mark_as_read


        return launch(data)
    else:
        try:
            acc = request.args['acc']
        except:
            acc = ''
        try:
            subject = request.args['subject']
        except:
            subject = ''
        try:
            link = request.args['link']
        except:
            link = ''
        try:
            n = request.args['n']
        except:
            n = ''
        try:
            msg = request.args['msg']
        except:
            msg = ''
        try:
            class1 = request.args['class1']
        except:
            class1 = ''
        try:
            class2 = request.args['class2']
        except:
            class2 = ''
        try:
            class3 = request.args['class3']
        except:
            class3 = ''

        return render_template("interface.html",acc=acc,subject=subject,link=link,n=n,msg=msg,class1=class1,class2=class2,class3=class3)
    
@app.route('/resume', methods=["GET"])
def resume_script():
    return resume()

@app.route('/stop', methods=["GET"])
def stop_script():
    return stop()

@app.route('/pause', methods=["GET"])
def pause_script():
    return pause()

if __name__ == '__main__': 
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run('127.0.0.1',5000)
    