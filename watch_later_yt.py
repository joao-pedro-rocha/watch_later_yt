import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from decouple import config

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = config('CLIENT_SECRETS_FILE')

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    subscribed_channels = []
    next_page_token = None

    # Gets the ids of the channels a logged in user is subscribed to and
    # put them in the subscribed_channels list
    while True:
        subscribed_channels_request = youtube.subscriptions().list(
            part='snippet',
            mine=True,
            maxResults=50,
            order="alphabetical",
            pageToken=next_page_token
        )
        subscribed_channels_response = subscribed_channels_request.execute()

        for item in subscribed_channels_response['items']:
            snippet = item['snippet']
            subscribed_channels.append(snippet['resourceId']['channelId'])

        next_page_token = subscribed_channels_response.get('nextPageToken')

        if not next_page_token:
            break

    BASE_URL = 'youtube.com/watch?v='

    # Create a file called watch_later.txt
    # If the file already exists, its contents will be deleted
    file = open('watch_later.txt', 'w')
    file.close()

    # Gets the id of the most recent video from each channel, assembles the
    # link and adds it in the watch_later.txt file
    try:
        for channel in subscribed_channels:
            video_request = youtube.search().list(
                part='snippet',
                channelId=channel,
                maxResults=1,
                order='date'
            )
            video_response = video_request.execute()
            if video_response['items'][0]['id']['kind'] == 'youtube#video':
                video_id = video_response['items'][0]['id']['videoId']
                video_title = video_response['items'][0]['snippet']['title']

                with open('watch_later.txt', 'a') as file:
                    file.write(f'{video_title} - {BASE_URL}{video_id}\n\n')
    except Exception:
        print('!!! An unexpected error has occurred !!!')


if __name__ == "__main__":
    main()
