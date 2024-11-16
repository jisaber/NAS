from flask import Flask, send_from_directory
from flask import render_template, flash
from flask_bootstrap import Bootstrap
import os
import tool
import time
import datetime

from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields import StringField
class MyForm(FlaskForm):
    shuaxin = StringField(label = "shuaxin")
    submit = SubmitField(label="提交")
 
app = Flask(__name__)
app.secret_key = "zxxxxxxxxx"

bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/media")
def hello_world(name = None):
    current_directory = os.getcwd() + "\\source\\"  # 获取当前目录
    print(current_directory)
    filenames = []
    for root, directories, files in os.walk(current_directory):
        for file in files:
            path = os.path.join(root, file)
            size = tool.human_size(os.path.getsize(path))
            time = datetime.datetime.fromtimestamp(os.path.getctime(path)).strftime("%Y-%m-%d")

            file = path.split(os.getcwd())[-1]
            file = file[1:].replace("\\", "/")
            filetype = tool.get_file_type(path)
            if filetype != tool.FILR_TYPE_ERROR:
                filenames.append([file, size, time, tool.get_file_type(path)])
    return render_template('index.html', filenames=filenames, name=name)

@app.route("/play/<path:path>/")
def play(path):
    base_name = path.rsplit('.', 1)[0]
    imgfile = base_name + ".jpg"
    return render_template('play.html', mediafile=path, imgfile=imgfile, filetype=tool.get_file_type(path))

@app.route("/about")
def about():
    import psutil, platform
    envInfo={}
    # 获取CPU的使用率，以百分比表示
    cpu_usage_percent = psutil.cpu_percent(interval=1)
    envInfo["cpuusage"] = f"当前CPU使用率: {cpu_usage_percent}%"

    envInfo["cpuCnt"] = "逻辑CPU个数:" + str(psutil.cpu_count()) + " 物理CPU个数:" + str(psutil.cpu_count(logical=False))
    envInfo["platform"] = platform.architecture(),platform.uname()

    mem = psutil.virtual_memory()
    envInfo["memusage"] = "空余内存/使用内存/总内存/内存使用率:" + \
                        str(tool.human_size(mem.free)) + "/" + \
                        str(tool.human_size(mem.used)) + "/" + \
                        str(tool.human_size(mem.total)) + "/" + \
                        str(format(mem.used / mem.total * 100, '.2f') + "%")
    return render_template('about.html', envInfo=envInfo)

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = MyForm()
    if form.validate_on_submit():
            text = form.submit.data
            print(text)
            flash("1111")
    return render_template('edit.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/source/<path:filename>')
def sendfile(filename):
    return send_from_directory('source', filename)