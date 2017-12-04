import urllib3.request, urllib.request
import requests as req
import os
import json
import simplejson



def youtube_videos():
    YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search?order=date&maxResults=50&part=snippet&channelId=%s&key=' + os.environ.get('YOUTUBE_API_KEY')
    response = req.get(YOUTUBE_API_URL % (os.environ.get('channelID')))
    jsdata = simplejson.loads(response.text)
    data = {}
    videos = []
    for video in jsdata['items']:
        if video['id']['kind'] == 'youtube#video':
            videoData = {}
            videoData['video_id'] = video['id']['videoId']
            videoData['title'] = video['snippet']['title']
            videoData['thumbnail'] = video['snippet']['thumbnails']['high']['url']
            videos.append(videoData)
    data['videos'] = videos

    print(json.dumps(data), file=open('data/youtube_videos.json','w'))

youtube_videos()
