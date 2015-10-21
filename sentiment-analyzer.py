import numpy as np

def readSentimentList(file_name):
    ifile = open(file_name, 'r')
    happy_log_probs = {}
    sad_log_probs = {}
    ifile.readline() #Ignore title row
    
    for line in ifile:
        tokens = line[:-1].split(',')
        happy_log_probs[tokens[0]] = float(tokens[1])
        sad_log_probs[tokens[0]] = float(tokens[2])

    return happy_log_probs, sad_log_probs

def classifySentiment(words, happy_log_probs, sad_log_probs):
    # Get the log-probability of each word under each sentiment
    happy_probs = [happy_log_probs[word] for word in words if word in happy_log_probs]
    sad_probs = [sad_log_probs[word] for word in words if word in sad_log_probs]

    # Sum all the log-probabilities for each sentiment to get a log-probability for the whole tweet
    tweet_happy_log_prob = np.sum(happy_probs)
    tweet_sad_log_prob = np.sum(sad_probs)

    # Calculate the probability of the tweet belonging to each sentiment
    prob_happy = np.reciprocal(np.exp(tweet_sad_log_prob - tweet_happy_log_prob) + 1)
    prob_sad = 1 - prob_happy

    return prob_happy, prob_sad

def main():
    # We load in the list of words and their log probabilities
    happy_log_probs, sad_log_probs = readSentimentList('twitter_sentiment_list.csv')

    # Here we have tweets which we have already tokenized (turned into an array of words)

#song 52
    # tweet1 = ['Sometimes' ,'I', 'feel', 'like' ,'I', 'dont', 'have', 'a', 'partner']
    # tweet2 =['Sometimes' ,'I', 'feel', 'like' 'my' ,'only' ,'friend']
    # tweet3 = ['Is', 'the', 'city', 'I', 'live', 'in']
    # tweet4 = ['The', 'city', 'of', 'angels']
    # tweet5 = ['Lonely', 'as', 'I', 'am']
    # tweet6 = ['Together', 'we', 'cry']
    # tweet7 = ['I', 'drive', 'on', 'her', 'streets', 'cause']
    # tweet8 = ['Shes', 'my', 'companion']
    # tweet9 = ['I', 'walk', 'through', 'her', 'hills', 'cause']
    # tweet10 = ['She', 'knows', 'who', 'I', 'am']
    # tweet11 = ['She', 'sees', 'my', 'good', 'deeds', 'and']
    # tweet12 = ['She', 'kisses', 'me', 'windy']
    # tweet13 = ['Well', 'I', 'never', 'worry', 'now', 'that','is' , 'a', 'lie']
    # tweet14 = ['And', 'I', 'dont', 'ever', 'want', 'to', 'feel']
    # tweet15 = ['Like', 'I', 'did', 'that', 'day']
    # tweet16 = ['Take' ,'me' ,'to', 'the', 'place', 'I', 'love']
    # tweet17 = ['Take', 'me', 'all' ,'the','way']

# Song 1
    # tweet1 = ['Give' ,'me', 'fuel']
    # tweet2 =['Give', 'me', 'fire']
    # tweet3 = ['Give', 'me', 'that', 'which', 'I', 'desire']
    # tweet4 = ['Ooh']
    # tweet5 = ['Yeah']
    # tweet6 = ['Yeah']
    # tweet7 = ['Turn', 'on', 'I', 'see' ,'red']
    # tweet8 = ['Adrenaline', 'crash', 'crack', 'my', 'head']
    # tweet9 = ['Nitro', 'junkie', 'paint', 'me', 'dead']
    # tweet10 = ['And' ,'I' ,'see' ,'red']
    # tweet11 = ['A', 'hundred', 'plus', 'through', 'black' ,'and', 'white']
    # tweet12 = ['War', 'horse']
    # tweet13 = ['War' ,'head']
    # tweet14 = ['Fuck', 'em', 'man']
    # tweet15 = ['White', 'knuckle', 'tight']
    # tweet16 = ['Through', 'black', 'and' ,'white']
    # tweet17 = ['Ooh']

# Song 2
    # tweet1 = ['You', 'used' 'to', 'call',  'me',  'on',  'my',  'you',  'used',  'to',  'you',  'used',  'to']
    # tweet2 =['Yeah']
    # tweet3 = ['You', 'used' 'to', 'call',  'me',  'on',  'my','cell' , 'phone']
    # tweet4 = ['Late', 'night', 'when', 'you' ,'need' ,'my' ,'love']
    # tweet5 = ['call',  'me',  'on',  'my','cell' , 'phone']
    # tweet6 = ['Late', 'night', 'when', 'you' ,'need' ,'my' ,'love']
    # tweet7 = ['And' 'I' ,'know' , 'when' , 'that' ,'hotline' ,'bling']
    # tweet8 = ['That', 'can' ,'only' ,'mean', 'one', 'thing']
    # tweet9 = ['And' 'I' ,'know' , 'when' , 'that' ,'hotline' ,'bling']
    # tweet10 = ['That', 'can' ,'only' ,'mean', 'one', 'thing']
    # tweet11 = ['Ever', 'since' ,'I' ,'left', 'the', 'city' ,'you']
    # tweet12 = ['Got', 'a', 'reputation', 'for', 'yourself', 'now']
    # tweet13 = ['Everybody' ,'knows', 'and', 'I', 'feel', 'left', 'out' ,'head']
    # tweet14 = ['Girl', 'you' ,'got', 'me', 'down', 'you', 'got' ,'me' ,'stressed', 'out', 'man']
    # tweet15 = ['Cause', 'ever', 'since', 'I', 'left', 'the', 'city', 'you']
    # tweet16 = ['Started', 'wearing', 'less', 'and', 'goin', 'out', 'more','white']
    # tweet17 = ['Glasses', 'of', 'champagne', 'out', 'on', 'the', 'dance' ,'floor']

# Song 3
    # tweet1 = ['Look', 'at ','the' ,'stars']
    # tweet2 =['Look', ' how' , ' they' , 'shine', ' for', 'you']
    # tweet3 = ['And', '  everything', '  you', '  do']
    # tweet4 = ['Yeah', ' they', '  were', '  all', ' yellow']
    # tweet5 = ['I', ' came', ' along']
    # tweet6 = ['I', ' wrote', ' a ', 'song', ' for', ' you']
    # tweet7 = ['And ', 'all', ' the', ' things', ' you', ' do']
    # tweet8 = ['And ', 'it', ' was', ' called', ' Yellow']
    # tweet9 = ['So', ' then', ' I', ' took', ' my', ' turn']
    # tweet10 = ['Oh', ' what', ' a', ' thing', ' to ve', ' done']
    # tweet11 = ['And', ' it', ' was', ' all', ' yellow']
    # tweet12 = ['Your', ' skin']
    # tweet13 = ['Oh', ' yeah', ' your', ' skin', ' and', ' bones']

# Song 4
    # tweet1 = ['She', 'said',' to',' me',' Go',' steady',' on ','me']
    # tweet2 = ['Wont',' you',' tell',' me',' what',' the',' Wise',' Men',' said']
    # tweet3 = [ ' When',' they',' came',' down',' from',' Heaven']
    # tweet4 = ['Smoked ','nine',' til',' seven']
    # tweet5 = ['All',' the',' shit ','that ','they',' could',' find']
    # tweet6 = ['But',' they',' couldnt ','escape',' from',' you']
    # tweet7 = ['Couldnt',' be ','free ','of ','you']
    # tweet8 = ['And',' now',' they',' know ','theres',' no',' way',' out']
    # tweet9 = ['And',' theyre',' really ','sorry',' now',' for',' what',' theyve ','done']
    # tweet10 =['  They',' were ','three',' Wise',' Men',' just',' trying',' to',' have',' some',' fun']
    # tweet11 =[' Look ','whos',' alone ','now']
    # tweet12 =[' Its ','not',' me',' Its',' not',' me']
    # tweet13 =['Those',' three ','Wise',' Men']
    # tweet14 =['Theyve ','got',' a ','semi',' by ','the',' sea']
    # tweet15 =['Got',' to ','ask ','yourself ','the', 'question']
    # tweet16 =['Where','are',' you',' now']
    # tweet17 =['Got',' to',' ask',' yourself',' the',' question']

# Song 5
    # tweet1 = ['Im ','tired ','of ','being',' what',' you',' want',' me ','to ','be']
    # tweet2 = ['Feeling',' so ','faithless',' lost',' under ','the ','surface']
    # tweet3 = [ 'Dont',' know',' what',' youre',' expecting',' of',' me']
    # tweet4 = ['Put',' under',' the',' pressure ','of',' walking',' in ','your ','shoes']
    # tweet5 = ['Caught',' in',' the',' undertow',' just',' caught ','in ','the',' undertow']
    # tweet6 = ['Every',' step',' that ','I ','take ','is ','another mistake',' to',' you']
    # tweet7 = ['Caught',' in ','the ','undertow',' just ','caught',' in ','the ','undertow']
    # tweet8 = ['Ive',' become',' so',' numb']
    # tweet9 = ['I ','cant ','feel',' you',' there']
    # tweet10 =['Ive',' become',' so',' tired']
    # tweet11 =[' So',' much',' more ','aware']
    # tweet12 =[' Im',' becoming',' this']
    # tweet13 =['All',' I ','want ','to',' do']
    # tweet14 =['Is',' be',' more',' like',' me']
    # tweet15 =['And',' be ','less ','like',' you']
    # tweet16 =['Can',' you',' see',' that',' youre ','smothering ','me']
    # tweet17 =['Ooh']

# Song 6
    # tweet1 = ['Yeah']
    # tweet2 = ['I',' know ','sometimes',' things',' may',' not',' always',' make ','sense',' to ','you ','right',' now']
    # tweet3 = [ 'But',' hey',' what',' daddy',' always ','tell ','you']
    # tweet4 = ['Straighten ','up ','little ','soldier']
    # tweet5 = ['Stiffen',' up ','that upper',' lip']

    # tweet6 = ['What ','you ','crying',' about']
    # tweet7 = ['You',' got',' me']
    # tweet8 = ['Hailie',' I ','know you ','miss',' your',' mom']
    # tweet9 = ['And ','I',' know',' you',' miss',' your',' dad',' when',' Im',' gone']
    # tweet10 =['But',' Im ','trying ','to ','give ','you',' the',' life ','that',' I ','never',' had']

    # tweet11 =['I ','can ','see',' youre',' sad']
    # tweet12 =['Even',' when ','you ','smile']

    # tweet13 =['Even ','when',' you ','laugh']
    # tweet14 =['I ','can ','see ','it',' in ','your ','eyes']
    # tweet15 =['Deep ','inside',' you ','wanna',' cry']
    # tweet16 =['Cuz ','youre',' scared']
    # tweet17 =['I ','aint ','there']
  
# Song 7
    # tweet1 = ['Remy',' Boyz',' yeaahhhh']
    # tweet2 = ['1738']
    # tweet3 = ['Im ','like',' hey',' whats',' up',' hello']
    # tweet4 = ['Seen',' yo ','pretty ','ass',' soon',' as ','you',' came ','in',' that',' door']
    # tweet5 = ['I ','just ','wanna ','chill',' got',' a ','sack ','for ','us',' to ','roll']
    # tweet6 = ['Married',' to ','the',' money',' introduced ','her ','to',' my ','stove']
    # tweet7 = ['Showed',' her ','how',' to',' whip',' it',' now ','she ','remixin',' for',' low']
    # tweet8 = ['She ','my ','trap ','queen',' let ','her',' hit',' the',' bando']
    # tweet9 = ['We ','be',' countin',' up',' watch ','how ','far ','them',' bands',' go']
    # tweet10 = ['We ','just',' set ','a ','goal',' talkin',' matchin',' Lambos']
    # tweet11 = ['Got ','50',' 60 ','grand',' 500',' grams ','though']
    # tweet12 = ['Man',' I ','swear',' I ','love ','her',' how ','she ','work ','the ','damn',' pole']
    # tweet13 = ['Hit ','the ','strip ','club',' we',' be ','letting bands go']
    # tweet14 = ['Everybody ','hating',' we',' just',' call ','them ','fans ','though']
    # tweet15 = ['In',' love',' with',' the ','money',' I ','aint',' never ','letting',' go']
    # tweet16 = ['And ','I',' get',' high',' with',' my ','baby']
    # tweet17 = ['I ','just ','left ','the ','mall',' Im',' gettin',' fly ','with ','my ','baby']
    

   
    # tweet1 =['You ', 'already', ' know', ' who', ' it', 'is']
    # tweet2 =['Silento']
    # tweet3 =['Silento']
    # tweet4 =['Gonna', 'do',' it',' for',' you']
    # tweet5 =['Now ','watch ','me ','whip']
    # tweet6 =['Now ','watch',' me ','nae ','nae']
    # tweet7 =['Now ','watch',' me ','whip ','whip']
    # tweet8 =['Watch',' me ','nae ','nae']
    # tweet9 =['Now ','watch',' me ','whip',' Kill ','it']
    # tweet10 =['Watch ','me ','nae',' nae',' Okay']
    # tweet11 =['Now',' watch',' me ','whip ','whip']

    # tweet12 =['Watch',' me ','nae',' nae']
    # tweet13 =['Now',' watch ','me']
    # tweet13 = ['Ooh',' watch',' me',' watch',' me']
    # tweet14 = ['Ooh',' watch',' me',' watch',' me']
    # tweet15 = ['Ooh',' watch',' me',' watch',' me']
    # tweet16 =['Ooh',' ooh',' ooh',' ooh']
    # tweet17 =['Ooh',' ooh',' ooh',' ooh']

    # tweet1 = ['Well ','you ','can',' tell ','by',' the',' way ','I ','use ','my',' walk']
    # tweet2 = [' Im',' a ','womans ','man',' no',' time ','to',' talk']
    # tweet3 = ['Music ','loud',' and',' women',' warm.']
    # tweet4 = ['Ive ','been ','kicked ','around ','since',' I ','was',' born']
    # tweet5 = ['And ','now',' its ','all',' right',' its ','okay']
    # tweet6 = ['And',' you',' may',' look ','the ','other',' way']
    # tweet7 = ['We ','can ','try',' to',' understand']
    # tweet8 = ['The ','New ','York',' Times ','effect',' on ','man']
    # tweet9 = ['Whether',' youre ','a','',' brother']
    # tweet10 = ['Or ','whether ','youre',' a ','mother']
    # tweet11 = ['Youre ','stayin',' alive',' stayin ','alive']
    # tweet12 = ['Feel',' the',' city ','breakin']
    # tweet13 = ['And ','everybody',' shakin']
    # tweet14 = ['And ','were',' stayin ','alive ','stayin',' alive']
    # tweet15 = ['Ah',' ha',' ha',' ha']
    # tweet16 = ['Stayin ','alive']
    # tweet17 = ['Stayin ','alive']


    tweet1 = [' Buffalo',' soldier',' dreadlock',' rasta']
    tweet2 = ['There ','was ','a ','buffalo ','soldier',' in ','the ','heart ','of',' America']
    tweet3 = ['Stolen ','from ','Africa ','brought ','to',' America']
    tweet4 = ['Fighting',' on ','arrival ','fighting',' for ','survival']

    tweet5 = ['I ','mean',' it ','when',' I ','analyze',' the',' stench']
    tweet6 = ['To ','me ','it ','makes ','a',' lot ','of',' sense']
    tweet7 = ['How ','the ','dreadlock',' rasta ','was ','the',' buffalo ','soldier']
    tweet8 = ['And ','he',' was ','taken ','from ','Africa',' brought ','to ','America']
    tweet9 = ['Fighting ','on ','arrival ','fighting',' for',' survival']

    tweet10 = ['Said ','he',' was',' a ','buffalo',' soldier ','dreadlock ','rasta']
    tweet11 = ['Buffalo',' soldier',' in',' the',' heart',' of',' America']

    tweet12 = ['If ','you ','know',' your',' history']
    tweet13 = ['Then',' you ','would ','know',' where ','youre ','coming ','from']
    tweet14 = ['Then ','you ','wouldnt ','have ','to ','ask ','me']
    tweet15 = ['I ','mean',' it ','when',' I ','analyze',' the',' stench']
    tweet16 = ['To ','me ','it ','makes ','a',' lot ','of',' sense']
    tweet17 = ['How ','the ','dreadlock',' rasta ','was ','the',' buffalo ','soldier']

    # Calculate the probabilities that the tweets are happy or sad
    tweet1_happy_prob, tweet1_sad_prob = classifySentiment(tweet1, happy_log_probs, sad_log_probs)
    tweet2_happy_prob, tweet2_sad_prob = classifySentiment(tweet2, happy_log_probs, sad_log_probs)
    tweet3_happy_prob, tweet3_sad_prob = classifySentiment(tweet3, happy_log_probs, sad_log_probs)
    tweet4_happy_prob, tweet4_sad_prob = classifySentiment(tweet4, happy_log_probs, sad_log_probs)
    tweet5_happy_prob, tweet5_sad_prob = classifySentiment(tweet5, happy_log_probs, sad_log_probs)
    tweet6_happy_prob, tweet6_sad_prob = classifySentiment(tweet6, happy_log_probs, sad_log_probs)
    tweet7_happy_prob, tweet7_sad_prob = classifySentiment(tweet7, happy_log_probs, sad_log_probs)
    tweet8_happy_prob, tweet8_sad_prob = classifySentiment(tweet8, happy_log_probs, sad_log_probs)
    tweet9_happy_prob, tweet9_sad_prob = classifySentiment(tweet9, happy_log_probs, sad_log_probs)
    tweet10_happy_prob, tweet10_sad_prob = classifySentiment(tweet10, happy_log_probs, sad_log_probs)
    tweet11_happy_prob, tweet11_sad_prob = classifySentiment(tweet11, happy_log_probs, sad_log_probs)
    tweet12_happy_prob, tweet12_sad_prob = classifySentiment(tweet12, happy_log_probs, sad_log_probs)
    tweet13_happy_prob, tweet13_sad_prob = classifySentiment(tweet13, happy_log_probs, sad_log_probs)
    tweet14_happy_prob, tweet14_sad_prob = classifySentiment(tweet14, happy_log_probs, sad_log_probs)
    tweet15_happy_prob, tweet15_sad_prob = classifySentiment(tweet15, happy_log_probs, sad_log_probs)
    tweet16_happy_prob, tweet16_sad_prob = classifySentiment(tweet16, happy_log_probs, sad_log_probs)
    tweet17_happy_prob, tweet17_sad_prob = classifySentiment(tweet17, happy_log_probs, sad_log_probs)
    

    happy = (tweet1_happy_prob +tweet2_happy_prob + tweet3_happy_prob + tweet4_happy_prob + tweet5_happy_prob + tweet6_happy_prob + tweet7_happy_prob     + tweet8_happy_prob + tweet9_happy_prob + tweet10_happy_prob + tweet11_happy_prob + tweet12_happy_prob + tweet13_happy_prob
        + tweet14_happy_prob + tweet15_happy_prob + tweet16_happy_prob + tweet17_happy_prob) /17 
   
   # sad = (tweet1_sad_prob + tweet2_sad_prob + tweet3_sad_prob + tweet4_sad_prob + tweet5_sad_prob + tweet6_sad_prob + tweet7_sad_prob 
   # + tweet8_sad_prob + tweet9_sad_prob + tweet10_sad_prob + tweet11_sad_prob + tweet12_sad_prob + tweet13_sad_prob + tweet14_sad_prob + tweet15_sad_prob
   #+ tweet16_sad_prob + tweet17_sad_prob) /17 

    print (happy)
    print (1-happy)
    #print (sad)

if __name__ == '__main__':
    main()
