# Watch Later YT
## About the app

This app was created to get the most recent video from each YouTube channel the logged-in user is subscribed to. The link of each video is saved in a file called _watch_later.txt_. The main goal is that every week I go through each channel I am subscribed to and add the videos to a playlist to watch later during the week. This task becomes tedious when you are subscribed to many channels, so I wanted to automate this process.

The app was developed in Python 3 and uses the official YouTube API (YouTube Data API v3) to access the necessary information to achieve its goal.
Run the code locally on your machine.

## How to use

1. To use the app, you need to follow the steps in the YouTube Data API documentation to set up a project and its credentials. [Click here](https://developers.google.com/youtube/v3/quickstart/python?hl=pt-br) to access the YouTube Data API documentation. This step can be a bit tedious, but you only need to do it once;

2. With the project downloaded and in the correct folder, run pip install -r requirements.txt;

3. Create a .env file with your credential (a .json file that you downloaded after creating your credentials in the Google Cloud Console);

4. Run python watch_later_yt.py.

