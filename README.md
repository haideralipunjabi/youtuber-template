# Youtuber-Template  ![Travis CI Build](https://travis-ci.org/HackeSta/youtuber-template.svg?branch=master)
A web template for Youtubers.  
[DEMO SITE](https://hackesta.github.io/youtuber-template/index.html)
## How to get videos?  
The ` video.html ` page gets Youtube Video data from ` data/youtube_videos.json `, which can be generated using the following ways:   
### Using [Travis CI](https://travis-ci.org/):  
All code required for getting video data from Youtube using [Travis](https://travis-ci.org/) is already present in the repo.  
1. Enable [Travis CI](https://travis-ci.org/) for your repo
2. Go to the Settings of your repo on [Travis](https://travis-ci.org/) and define the following Environment Variables  

| Name | Value |  
| ---- | ----- |
| **channelID** | *Youtube Channel ID* |
| **GH_TOKEN** | *Github Personal Account Token with Repo Scope* |
| **YOUTUBE_API_KEY** | *[Youtube Data API Server Key](https://developers.google.com/youtube/registering_an_application#Create_API_Keys)* |  

3. Enable daily cron job for your repo
4. Start the build

## Further Designing  
If you want to add more pages or redesign the website, you can use [Bulma](https://bulma.io/)
