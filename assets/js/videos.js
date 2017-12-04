$(document).ready(function(){
  $.getJSON("data/youtube_videos.json", function(data){
    $.each(data.videos, function(index,video){
      $("#video-container").append('<div class="column is-one-third-desktop is-half-tablet "><iframe id="ytplayer" type="text/html" style="float:none; margin-bottom: 10px;" width="100%" height="360" src="https://www.youtube.com/embed/'+video.video_id+'?autoplay=0 frameborder="0"></iframe></div>');

  });
});
});
