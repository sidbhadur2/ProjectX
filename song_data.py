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

def get_lyrics_list():
	format = '&format=xml'
	request = 'http://api.musixmatch.com/ws/1.1/chart.tracks.get?page=3' +'&page_size=15' +'&ountry='+  '&f_has_lyrics=1' +'&apikey=16fdae5bf1aed25e5a2fb06ce16045a8' +format
	response = urlopen(request)
	data = response.read()
	song = objectify.fromstring(data)
	for i in range(15):
		artist = song.body.track_list.track[i].artist_name
		track = song.body.track_list.track[i].track_name 
		print "get_lyrics" + "(" "\"" + artist + "\"" "," + "\"" + track + "\"" +  ")"
		

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
#lyrics51 = get_lyrics("Green-Day", "Boulevard-of-Broken-Dreams") 
#lyrics52 = get_lyrics("Red-Hot-Chili-Peppers" ,"Under-the-Bridge")
#lyrics53 = get_lyrics("Adele", "Hello");
#lyrics54 = get_lyrics("One-Direction" , "Home")
#lyrics55 = get_lyrics("Justin-Bieber", "Sorry")
#lyrics56 = get_lyrics("The-Weeknd" , "The-Hills")
#lyrics57 = get_lyrics("Alessia-Cara" ,"Here")
#lyrics58 = get_lyrics("Ariana-Grande", "Focus")
#lyrics59 = get_lyrics("One-Direction" , "Drag-Me-Down")
#lyrics60 = get_lyrics("Ellie-Goulding", "On-My-Mind")
#lyrics61 = get_lyrics("Fetty-Wap-feat-Remy-Boyz" , "679")
#lyrics62 = get_lyrics("Post-Malone" , "White-Iverson")
#lyrics63 = get_lyrics("One-Direction", "What-a-Feeling")
#lyrics64 = get_lyrics("Drake",  "Under-Ground-Kings")
#lyrics65 = get_lyrics("Logic-feat-Big-Lenbo", "Young-Jesus")
#lyrics66 = get_lyrics("Drake","Back-To-Back")
#lyrics67 = get_lyrics("Ed-Sheeran", "Don-t")
#lyrics68 = get_lyrics("Bee-Gees", "Staying-Alive")
#lyrics69 = get_lyrics("Drake","Energy")
#lyrics70 = get_lyrics("Kwabs", "Walk")
#lyrics71 = get_lyrics("Kendrick-Lamar","Alright")
#lyrics72 = get_lyrics("Lionel-Richie", "Hello")
#lyrics73 = get_lyrics("Kirko-Bangz","Drank-In-My-Cup")
#lyrics74 = get_lyrics("Bruno-Mars","Just-the-Way-You-Are")
#lyrics75 = get_lyrics("Imagine-Dragons","Underdog")
#lyrics76 = get_lyrics("Eminem","Space-Bound")
#lyrics77 = get_lyrics("Young-the-Giant","Cough-Syrup")
#lyrics78 = get_lyrics("Kanye-West","Stronger")
#lyrics79 = get_lyrics("Andy-Grammer","The-Pocket")
#lyrics80 = get_lyrics("John-Mayer","Half-of-My-Heart")
#lyrics81 = get_lyrics("Aerosmith","Dream-On")
#lyrics82 = get_lyrics("Oasis-3","Wonderwall")
#lyrics83 = get_lyrics("Elton-John","Rocket-Man")
#lyrics84 = get_lyrics("Alex-Clare","Too-Close")
#lyrics85 = get_lyrics("Sol-6","2020")
#lyrics86 = get_lyrics("Whitesnake","Here-I-Go-Again")
#lyrics87 = get_lyrics("Adele-3","Someone-Like-You")
#lyrics88 = get_lyrics("Ellie-Goulding","On-My-Mind")
#lyrics89 = get_lyrics("One-Direction","Wolves")
#lyrics90 = get_lyrics("Demi-Lovato","Confident")
get_lyrics_list()
# lyrics91 = get_lyrics()
# lyrics92 = get_lyrics()
# lyrics93 = get_lyrics()
# lyrics94 = get_lyrics()
# lyrics95 = get_lyrics()
# lyrics96 = get_lyrics()
# lyrics97 = get_lyrics()
# lyrics98 = get_lyrics()
# lyrics99 = get_lyrics()
# lyrics100 = get_lyrics()
# lyrics101 =
# lyrics102 =
# lyrics103 =
# lyrics104 =
# lyrics105 =
# lyrics106 =
# lyrics107 =
# lyrics108 =
# lyrics109 =
# lyrics110 =
# lyrics111 =
# lyrics112 =
# lyrics113 =
# lyrics114 =
# lyrics115 =
# lyrics116 =
# lyrics117 =
# lyrics118 =
# lyrics119 =
# lyrics120 =
# lyrics121 =
# lyrics122 =
# lyrics123 =
# lyrics124 =
# lyrics125 =
# lyrics126 =
# lyrics127 =
# lyrics128 =
# lyrics129 =
# lyrics130 =
# lyrics131 =
# lyrics132 =
# lyrics133 =
# lyrics134 =
# lyrics135 =
# lyrics136 =
# lyrics137 =
# lyrics138 =
# lyrics139 =
# lyrics140 =
# lyrics141 =
# lyrics142 =
# lyrics143 =
# lyrics144 =
# lyrics145 =
# lyrics146 =
# lyrics147 =
# lyrics148 =
# lyrics149 =
# lyrics150 =
