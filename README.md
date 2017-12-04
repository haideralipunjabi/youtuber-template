# Youtuber-Template  ![Travis CI Build](https://travis-ci.org/HackeSta/youtuber-template.svg?branch=master)
A web template for Youtubers.  
<a href="https://bulma.io">
  <img src="https://bulma.io/images/made-with-bulma.png" alt="Made with Bulma" width="128" height="24">
</a>  
## Demo:

[DEMO SITE](https://hackesta.github.io/youtuber-template/index.html)
### Screenshots:
![SS index.html](https://i.imgur.com/Wtgrf5q.png)
![SS videos.html](https://i.imgur.com/LupfbUP.png)
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

## Credits:
* [Bulma](https://bulma.io) - Modern CSS framework based on Flexbox
* [BulmaJS](https://github.com/VizuaaLOG/BulmaJS) - Unofficial javascript extension to the awesome Bulma CSS framework  
* [Bulma Templates - Cover](https://github.com/dansup/bulma-templates) - Free flexbox templates built with the bulma css framework (Used for ` index.html `)

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Licence

Code released under [the MIT license](https://github.com/hackesta/youtuber-template/blob/master/LICENSE).
