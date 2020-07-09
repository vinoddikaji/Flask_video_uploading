from flask import Flask, render_template, request, url_for, send_from_directory
import os


app = Flask(__name__)

path = '/Desktop'

#APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_ROOT = os.path.dirname(path)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=["POST","GET"])
def upload():
    if request.method=="POST":

        target = os.path.join(APP_ROOT, 'StoredVideos/')

        

        if not os.path.isdir(target):

            os.mkdir(target)
        for file in request.files.getlist('file'):

            print(file)
            filename = file.filename
            destination = "/".join([target,filename])
            print(destination)
            file.save(destination)
            return "File uploaded successfully"

    return render_template('upload.html')

@app.route('/upload<filename>')
def send_video(filename):
    return send_from_directory('StoredVideos', filename)



@app.route('/gallery')
def get_gallery():

    video_name = os.listdir('./StoredVideos')
    return render_template('gallery.html', video_name = video_name)




if __name__=="__main__":
    app.run(debug=True)