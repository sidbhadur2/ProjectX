import urllib2
import musixmatch
from urllib2 import Request, urlopen, URLError
import  xml.etree
import lxml
from lxml import objectify


def get_lyrics(artist, track):
	format = '&format=xml'
	request = 'http://api.musixmatch.com/ws/1.1/matcher.lyrics.get?q_track=' +track + '&q_artist=' +artist+ '&apikey=16fdae5bf1aed25e5a2fb06ce16045a8' +format
	response = urlopen(request)
	data = response.read()
	#song =  xml.etree.ElementTree.XML(data)
	song = objectify.fromstring(data)
	lyrics_val = song.body.lyrics.lyrics_body
	print lyrics_val

#ini = 'http://api.musixmatch.com/ws/1.1/'
#apikey = '16fdae5bf1aed25e5a2fb06ce16045a8'
#artist = 'queen'
#track = 'we%20are%20the%20champions'
#format = '&format=json&page_size=1&f_has_lyrics=1'
#request = Request(ini +'track.search?apikey=' + apikey + '&q_artist=' +artist+ '&q_track=' + track+format)
#track_id_val = '716432'

# try:
# 	response = urlopen(request)
# 	data = response.read()
# 	#print data
# except musixmatch.api.Error, e:
#     print 'No data. Got an error code:', 


# request2 = Request(ini + 'track.lyrics.get?apikey=' + apikey + 'track_id=' +track_id_val)
# try:
# 	response2 = urlopen(request2)
# 	data2 = response2.read()
# 	print data2
# except musixmatch.api.Error, e:
#     print 'No data. Got an error code:', 

   
#lyrics1  = get_lyrics("metallica","fuel");
#lyrics2  = get_lyrics("drake","hotline-bling");
#lyrics3  = get_lyrics("coldplay","yellow");
# lyrics4  = get_lyrics("james","wisemen");
#lyrics5  = get_lyrics("linkin","numb");
# lyrics6  = get_lyrics("eminem","mockingbird");
# lyrics7  = get_lyrics("fetty-wap","trap-queen");
#lyrics8  = get_lyrics("silento", "watch-me");
#lyrics9  = get_lyrics("bee-gees","stayin");
# lyrics10 = get_lyrics("bob-marley","buffalo-soldier");
# lyrics11 = get_lyrics("daft-punk","lose-yourself");
# lyrics12 = get_lyrics("owl-city","fireflies");
# lyrics13 = get_lyrics("imagine-dragons","demons");
# lyrics14 = get_lyrics("tove-lo","talking-body");
# lyrics15 = get_lyrics("capital-cities","safe-and");
# lyrics16 = get_lyrics("red-hot-chilli-peppers","dani-california");
# lyrics17 = get_lyrics("idina-menzel","let-it-go");
# lyrics18 = get_lyrics("mark-ronson","uptown-funk");
# lyrics19 = get_lyrics("Casting-Crowns","Who-Am-I");
# lyrics20 = get_lyrics("drake","furthest-thing");
# lyrics21 = get_lyrics("drake","headlines");
# lyrics22 = get_lyrics("ed-sheeran" ,"dont");
# lyrics23 = get_lyrics("calvin-harris","blame");
# lyrics24 = get_lyrics("david-guetta","titanium");
# lyrics25 = get_lyrics("simon-garfunkel","the-sounds-of-silence");
# lyrics26 = get_lyrics("scorpions","winds-of-change");
# lyrics27 = get_lyrics("cliff-richard","carrie");
# lyrics28 = get_lyrics("demi-lovato","cool-for-the-summer");
# lyrics29 = get_lyrics("beatles","yellow-submarine");
# lyrics30 = get_lyrics("aerosmith","rag-doll");
# lyrics31 = get_lyrics("phil-collins","against-all-odds");
# lyrics32 = get_lyrics("eric-clapton","layla");
# lyrics33 = get_lyrics("eric-clapton","cocaine");
# lyrics34 = get_lyrics("dire-straits","sultans-of-swing");
# lyrics35 = get_lyrics("wiz-khalifa","medicated");
# lyrics36 = get_lyrics("j-cole-2","workout");
# lyrics37 = get_lyrics("john-newman","love-me");
# lyrics38 = get_lyrics("tupac","changes");
# lyrics39 = get_lyrics("the-weeknd" , "often");
# lyrics40 = get_lyrics("nas","halftime");
# lyrics41 = get_lyrics("sol","2020");
# lyrics42 = get_lyrics("maroon-5","animals");
# lyrics43 = get_lyrics("pharell-williams","happy");
# lyrics44 = get_lyrics("drake","trophies");
# lyrics45 = get_lyrics("kendrick-lamar","money-trees");
# lyrics46 = get_lyrics("50-Cent", "Straight-to-the-Bank");
# lyrics47 = get_lyrics("kid-ink","hell");
# lyrics48 = get_lyrics("ac-dc","hells-bells");
# lyrics49 = get_lyrics("jay-sean","down");
# lyrics50 = get_lyrics("michael-jackson","dirty-diana");
