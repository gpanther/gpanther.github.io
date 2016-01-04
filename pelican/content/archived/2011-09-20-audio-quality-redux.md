Title: Audio quality redux
Date: 2011-09-20 15:20
Author: Attila-Mihaly Balazs
Tags: audio, audacity, audio processing, noise removal
Slug: audio-quality-redux
Status: published

Yet an other example for how [simple
steps](http://hype-free.blogspot.com/2011/03/audio-quality.html) can
improve the audio quality considerably. The clip below is taken from
[this
blogpost](http://garry.posterous.com/how-steve-jobs-handles-trolls-wwdc-1997)
(which I originally found trough [Hacker
News](http://news.ycombinator.com/item?id=2944579)). You can find the
processed version [here](http://www.youtube.com/watch?v=lQadOr9B7Qc), or
use the controls below to do a quick A/B comparison of the two. The
processing was very simple (1. noise removal and 2. running trough the
Levelator) and quick.

<link href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/themes/base/jquery-ui.css" rel="stylesheet" type="text/css"></link>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js"></script>
  

<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/jquery-ui.min.js"></script>
  

<script src="https://ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js"></script>
</p>
<style>
  #vplayerWrapper {<br></br>
    width: 424px;<br></br>
    height: 315px;<br></br>
  }</p>
<p>.vplayer {<br></br>
    overflow: hidden;<br></br>
    border: 1px solid black;<br></br>
  }</p>
<p>#firstVPlayer {<br></br>
    float: left;<br></br>
  }</p>
<p>#secondVPlayer {<br></br>
    float: right;<br></br>
  }</p>
<p>.vplayerContainer {<br></br>
    position: relative;<br></br>
    width: 420px;<br></br>
    height: 315px;<br></br>
  }<br></br>
  </style>
<div id="vplayerWrapper">

<div id="firstVPlayer" class="vplayer">

<div id="firstVPlayerContainer" class="vplayerContainer">

<div id="firstVPlayerTarget">

</div>

</div>

</div>

<div id="secondVPlayer" class="vplayer">

<div id="secondVPlayerContainer" class="vplayerContainer">

<div id="secondVPlayerTarget">

</div>

</div>

</div>

</div>

<input type="button" id="play"></input>  
Position:

<div id="video-position" style="margin: 10px; width: 420px;">

</div>

Volume:

<div id="video-volume" style="margin: 10px; width: 100px;">

</div>

Crossfade (Original - New):

<div id="video-crossfade" style="margin: 10px; width: 100px;">

</div>

<p>
<script><br />
var ytPlayers = [];<br />
var volume = 100, crossfade = 0;</p>
<p>function onPlayerError(errorCode) {<br />
  alert("An error occured of type:" + errorCode);<br />
}</p>
<p>function updatePlayerInfo() {<br />
  if (0 == ytPlayers.length) { return; }<br />
  if (!ytPlayers[0]) { return; }<br />
  if (!ytPlayers[0].getDuration) { return; }</p>
<p>var position = ytPlayers[0].getCurrentTime() * 100 / ytPlayers[0].getDuration();<br />
  $("#video-position").slider("option", "value", position);<br />
}</p>
<p>function setVolume() {<br />
  var p1 = (100 - crossfade) / 100;<br />
  var p2 = crossfade / 100;</p>
<p>ytPlayers[0].setVolume(volume * p1);<br />
  ytPlayers[1].setVolume(volume * p2);</p>
<p>var width = 420;<br />
  var w1 = width * p1;<br />
  var w2 = width * p2;</p>
<p>$('#firstVPlayer').width(w1);<br />
  $('#secondVPlayer').width(w2);<br />
  $('#secondVPlayerContainer').css('left', -w1);<br />
}</p>
<p>function onYouTubePlayerReady(playerId) {<br />
  var ytplayer = document.getElementById(playerId);<br />
  ytplayer.addEventListener("onError", "onPlayerError");<br />
  ytplayer.cueVideoById(playerId);<br />
  ytplayer.seekTo(0, true);<br />
  ytplayer.pauseVideo();<br />
  ytplayer.setVolume(0);<br />
  if (2 == ytPlayers.push(ytplayer)) {<br />
    var ppButton = $('#play');<br />
    ppButton.val('Play');<br />
    ppButton.click(function() {<br />
      if ('Play' == ppButton.val()) {<br />
        ppButton.val('Pause');<br />
        for (var i in ytPlayers) { ytPlayers[i].playVideo(); }<br />
      }<br />
      else {<br />
        ppButton.val('Play');<br />
        for (var i in ytPlayers) { ytPlayers[i].pauseVideo(); }<br />
      }<br />
    });</p>
<p>$("#video-position").slider({<br />
      change : function(e, u) {<br />
        if (!e.orginalEvent) { return; }<br />
        for (var i in ytPlayers) {<br />
          if (0 == ytPlayers[i].getDuration()) { return; }<br />
        }<br />
        for (var i in ytPlayers) {<br />
          var d = ytPlayers[i].getDuration();<br />
          ytplayer.seekTo(d * u.value / 100, true);<br />
        }<br />
      }<br />
    });</p>
<p>$("#video-volume").slider({<br />
      value: volume,<br />
      change: function(e, u) {<br />
        volume = u.value;<br />
        setVolume();<br />
      }<br />
    });</p>
<p>$("#video-crossfade").slider({<br />
      change: function(e, u) {<br />
        crossfade = u.value;<br />
        setVolume();<br />
      }<br />
    });</p>
<p>setVolume();<br />
  }<br />
}</p>
<p>function embedYTPlayer(videoId, targetDivId) {<br />
  var params = { allowScriptAccess: "always" };<br />
  var atts = { id: videoId };<br />
  swfobject.embedSWF("http://www.youtube.com/apiplayer?" +<br />
                     "version=3&enablejsapi=1&playerapiid=" + videoId,<br />
                     targetDivId, "420", "315", "9", null, null, params, atts)<br />
}</p>
<p>embedYTPlayer('FF-tKLISfPE', 'firstVPlayerTarget');<br />
embedYTPlayer('lQadOr9B7Qc', 'secondVPlayerTarget');<br />
setInterval(updatePlayerInfo, 250);<br />
</script>
</p>
PS: For people reading the post trough an RSS reader: you probably need
to click trough [to the
site](http://hype-free.blogspot.com/2011/09/audio-quality-redux.html) to
see the comparison in action, since most (all?) RSS readers filter out
javascript for security reasons.

PS: If you are interested in the simple script which was use to interact
with the two youtube players, you can find it in [my code
repository](http://code.google.com/p/hype-free/source/browse/trunk/youtube_mix/youtube_mix.html).
