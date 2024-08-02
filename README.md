# YouTube Video Downloader

This is a Flask web application that allows users to download YouTube videos. The user can input the URL of a YouTube video, and the application will download the video in MP4 format.

## Features

- Input a YouTube video URL to download the video.
- The downloaded video is saved in the `downloads` folder.
- Error handling for invalid URLs or download issues.

## Prerequisites

- Python 3.x
- Flask
- Pytube

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Ritwik740/youtube-video-downloader.git
    cd youtube-video-downloader
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install flask pytube
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Enter the YouTube video URL in the input field and click the "Download" button.

4. The video will be downloaded to the `downloads` folder.

## File Structure

- `app.py`: The main Flask application file.
- `templates/main.html`: The HTML template for the main page.
- `downloads/`: The folder where downloaded videos are saved.

## License

This project is licensed under the MIT License.
