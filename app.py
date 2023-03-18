import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory
from video import get_srt_file, trans_to_chinese
from caption import write_caption

UPLOAD_FOLDER = './mp4'
Directory_PATH = os.path.abspath(UPLOAD_FOLDER) + '/'
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        lang = request.form['lang']
        filename = secure_filename(file.filename)
        file.save(os.path.join(Directory_PATH, filename))
        abs_path = Directory_PATH+filename
        get_srt_file(abs_path, lang, './srt_file')
        srt_file = filename.split('.')[0]+'.srt'
        res_srt_file = trans_to_chinese(srt_file)
        output = './result/'+filename
        write_caption(res_srt_file, abs_path, output)
        return redirect(url_for('show_filepath', filename=filename))
    return render_template('home.html')


@app.route('/show_filepath/<filename>')
def show_filepath(filename):
    output = os.path.abspath('./result/')+filename
    return render_template('file_path.html', file_path=output, filename=filename)


@app.route('/uploaded_file/<filename>')
def uploaded_file(filename):
    output_dir = os.path.abspath('./result/')
    return send_from_directory(output_dir, filename)


@app.route('/')
def home():
    return render_template('home.html')
