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


#get_lyrics("Walk-The-Moon","Shut-Up-and-Dance")
#get_lyrics("Justin-Bieber","No-Pressure")
#get_lyrics("Sia","Alive")
#get_lyrics("Brothers-Osborne","Stay-a-Little-Longer")
#get_lyrics("Selena-Gomez","Good-For-You")
#get_lyrics("Drake","Right-Hand")
#get_lyrics("Nathaniel-Rateliff","S.O.B.")
#get_lyrics("Jana-Kramer","I-Got-the-Boy")

#get_lyrics("Justin-Bieber","I'll-Show-You")
#get_lyrics("Coldplay","Adventure-of-a-Lifetime")
#get_lyrics("Justin-Bieber","The-Feeling")
#get_lyrics("Sam-Smith","Writing's-On-the-Wall")
#get_lyrics("Justin-Bieber","Purpose")
#get_lyrics("Drake","Jumpman")
#get_lyrics("Macklemore","Downtown")

#get_lyrics("The-Weeknd","Can't-Feel-My-Face")
#get_lyrics("X-Ambassadors","Renegades")
#get_lyrics("R-City","Locked-Away")
#get_lyrics("Rudimental","Lay-It-All-On-Me")
#get_lyrics("iLoveMemphis","Hit-the-Quan")

#get_lyrics("Rachel-Platten","Fight-Song")
#get_lyrics("The-Chainsmokers","Roses")

#get_lyrics("Calvin-Harris","How-Deep-Is-Your-Love")
#get_lyrics("Zac-Brown-Band","Beautiful-Drug")
#get_lyrics("twenty-one-pilots","Stressed-Out")
#get_lyrics("Meghan-Trainor","Better-When-I'm-Dancin'")
#get_lyrics("Old-Dominion","Break-Up-with-Him")
#get_lyrics("Carrie-Underwood","Smoke-Break")
#get_lyrics("Rachel-Platten","Stand-By-You")
#get_lyrics("Nelly","The-Fix")
#get_lyrics("James-Bay","Let-It-Go")
#get_lyrics("Justin-Bieber","Mark-My-Words")
#get_lyrics("Ed-Sheeran","Photograph")
#get_lyrics("Disclosure","Magnets")

#get_lyrics("Eric-Church","Mr-Misunderstood")
#get_lyrics("Fall-Out-Boy","Uma-Thurman")
#get_lyrics("One-Direction","If-I-Could-Fly")
#get_lyrics("Ed-Sheeran","Thinking-Out-Loud")
#get_lyrics("Gwen-Stefani","Used-To-Love-You")
#get_lyrics("Tory-Lanez","Say-It")
#get_lyrics("Omi","Cheerleader")
#get_lyrics("Mark-Ronson","Uptown-Funk")
#get_lyrics("Nick-Jonas","Levels")
#get_lyrics("Justin-Bieber","Company")
#get_lyrics("Charlie-Puth","Marvin-Gaye")
#get_lyrics("Dion","The-Wanderer")
#get_lyrics("Mariah-Carey","All-I-Want-for-Christmas-Is-You")

# get_lyrics("One Direction","A.M.")
# get_lyrics("Audien feat. Lady Antebellum","Something Better")
# get_lyrics("DNCE","Cake By the Ocean")
# get_lyrics("Justin Bieber","Life Is Worth Living")
# get_lyrics("Justin Bieber","Children")
# get_lyrics("Randy Houser","We Went")
# get_lyrics("One Direction","History")
# get_lyrics("G-Eazy","Random")
# get_lyrics("John Lennon","Imagine")
# get_lyrics("Chris Brown","Back To Sleep")
# get_lyrics("Drake","Back To Back")
# get_lyrics("Wes Walker & Dyl","Jordan Belfort")
# get_lyrics("Skrillex & Diplo","Where Are Now (with Justin Bieber)")
# get_lyrics("Jordan Smith","Halo (The Voice Performance)")
# get_lyrics("Alabama Shakes","Sound & Color")

# get_lyrics("IAmDLOW","Bet You Can't Do It Like Me")
# get_lyrics("Sheryl Crow feat. Kid Rock","Picture")
# get_lyrics("Keith Urban","Break On Me")
# get_lyrics("One Direction","Wolves")
# get_lyrics("Andy Grammer","Honey, I'm Good.")
# get_lyrics("Pentatonix","Can't Sleep Love")
# get_lyrics("Tim McGraw","Top of the World")
# get_lyrics("Cole Swindell","Let Me See Ya Girl")
# get_lyrics("Chris Stapleton","Nobody To Blame")
# get_lyrics("Charlie Puth","One Call Away")
# get_lyrics("Adele","Someone Like You")
# get_lyrics("Jason Derulo","Want to Want Me")
# get_lyrics("Florida Georgia Line","Confession")
# get_lyrics("Jordan Feliz","The River")
# get_lyrics("Hozier","Someone New")

# get_lyrics("Usher","Yeah! (feat. Lil' Jon & Ludacris)")
# get_lyrics("One Direction","I Want to Write You a Song")
# get_lyrics("Maroon 5","Sugar")
# get_lyrics("Justin Bieber feat. J Balvin","Sorry (Latino Remix)")
# get_lyrics("One Direction","Temporary Fix")
# get_lyrics("The Weeknd feat. Eminem","The Hills (Remix)")
# get_lyrics("Taylor Swift","Blank Space")
# get_lyrics("The Weeknd","Earned It (Fifty Shades of Grey)")
# get_lyrics("Ed Sheeran","Touch and Go")
# get_lyrics("Jason Aldean","Gonna Know We Were Here")
# get_lyrics("Kenny Chesney","Save It for a Rainy Day")
# get_lyrics("Fall Out Boy","Centuries")
# get_lyrics("Drake","Energy")
# get_lyrics("Rich Homie Quan","Flex (Ooh, Ooh, Ooh)")
# get_lyrics("Luke Bryan feat. Karen Fairchild","Home Alone Tonight")











