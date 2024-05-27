from flask import Flask, render_template, request, send_file
import os
import yt_dlp as youtube_dl
import datetime
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/download", methods=["POST"])
def download_video():
    url = request.form["link"]
    ydl_opts = {
        'outtmpl': os.path.join('downloads', 'downloadedvideo.mp4'),  # Set filename to 'downloadedvideo.mp4'
        'format': 'best',
        'verbose': True
    }
    
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        file_path = os.path.join('downloads', 'downloadedvideo.mp4')
        return send_file(file_path, as_attachment=True)
    except youtube_dl.utils.DownloadError as e:
        return f"Download error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
