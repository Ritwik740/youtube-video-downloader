
from flask import Flask, render_template, request, send_file
import os
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/download", methods=["POST"])
def download_video():
    url = request.form["link"]
    
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension='mp4', progressive=True).first()
        if not os.path.exists('downloads'):
            os.makedirs('downloads')
        file_path = os.path.join('downloads', 'downloadedvideo.mp4')
        stream.download(output_path='downloads', filename='downloadedvideo')
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return f"Download error: {e}"

if __name__ == '__main__':
    app.run(debug=True)

