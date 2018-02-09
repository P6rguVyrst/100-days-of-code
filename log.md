# 100 Days Of Code - Log

### Day 0: December 5, 2017 (fs_poller.py)
**Today's Progress**: Discover pre-defined format video files recursively from specified folder.

### Day 1: December 6, 2017 (Flask)
**Today's Progress**: Had higher expectations for today but got nothing special done...

**Thoughts**: Thought I'd get further and present fs_poller results in some decent manner, but did'nt really get that far off into coding and spent more time debugging, exploring Flask and unit testing a Flask application. Failed today.

### Day 2: December 7, 2017 - ??? 
**Today's Progress**: No real progress. Went to yoga, and favourite bar after work. After getting home, checked out Celery and started tower of hanoi - a codeclub exericise that gives max ammunt of points for one exericise.

**Thougts**: Technical debt is increasing. Need to work extra on weekend to get shit done.

### Day 3: December 8, 2017 - ??? 
**Today's Progress**: An utility that runs command on remote host and spits out its' results as the command is being run. Reads configuration from local ssh conf and therefore can be used over hoppers. Plays audio when done executing. 

**Thougts**: I know I can do it with Ansible, but I needed it for a purpose that ansible is not suited for.

### Day 4: December 9, 2017 - Working Flask API
**Today's Progress**: Working on Flask API and added some off the shelf code for testing my own applications.

**Thougts**: Noting interesting going on here...

### Day 5: December 10, 2017 - Coding music
**Today's Progress**: Wrote code to explore sounds in sonic-pi powered by python-sonic.

**Thougts**: Yesterday I talked about an idea I had once with a friend and he reccommended me an awesome tool called sonic-pi. Although it seems to be written in Ruby, there's a Python interface in pypi called python-sonic. Check it out, it's awesome!

### Day 6: December 11, 2017 - Flask
**Today's Progress**: Fixed stuff.

**Thougts**: Nothing to see here, move along. Not 100% sure where I'm going with this, but I seem to be moving along just nicely. Speed is another factor...

### Day 7: December 12, 2017 - ???
**Today's Progress**: Working on filtering out unique titles.

**Thougts**: Need to filter out unique media files. Get their imdb code (or any other unique id), and look for more interesting stuff about the unique title - to eventually, present the titles, enriched with metadata, through Flask API. 

### Day 8: December 13, 2017 - Regex magic
**Today's Progress**: REGEX magic - Working on filtering out unique titles - pretty solid work so far (good enough, but not perfect)

**Thougts**: Packaged some code into easily deployable application at work today, unfortunatelly that doesn't count for this challenge. Worked on filtering results to filter unique titles. Unique titles must be searched for additional data: trailer, imdb etc... The data is then passed to Flask API that will display the enriched information.

### Day 9: December 14, 2017 - Thursdays's the hardest
**Today's Progress**: I would if I could, but I don't think I should.

**Thougts**: Seriouslly... Not today.

### Day 10: December 15, 2017 - Working my way up to frontend stuff... 
**Today's Progress**: Worked through Flask+React frontend development tutorial [Realpython](https://realpython.com/blog/python/the-ultimate-flask-front-end/)

**Thougts**: Now I have a basic template to display results from fs_discovery.py

### Day 11: December 16, 2017 - Know your tools 
**Today's Progress**:  Worked my way through dozens of cookiecutter [templates](https://github.com/audreyr/cookiecutter#python), testing flask, pyramid and django. Later on worked on project repository a little.

**Thougts**: There's a plethora of awesome python and to save your nerve and time it pays to get to know what is out there... It's amazing how easily you can get up and running with cookiecutter templates - it takes the hassle away from packaging your code.

### Day 12: December 17, 2017 - python-sonic
**Today's Progress**:  Started work on my fork of [python-sonic](https://github.com/P6rguVyrst/python-sonic/tree/restructuring). Structuring code and making smaller logical pieces. Learning unit testing.

**Thougts**: First challenge I had with the library was that it was difficult to explore sounds (listening to them while actually seeing what's playing). The get_sounds() function at samples package returns a dictionary which allows to play the values while actually print out the keys.

### Day 13: December 18, 2017 - IMDB
**Today's Progress**: Trying to enforce myself to do TDD. Started working on a script to fetch IMDB data. 

**Thougts**: Still need to get access to AWS IMDB bucket.

### Day 14: December 19, 2017 - data cleanup...
**Today's Progress**: Cleaning data is pain. I feel for all the data science people out there. Got the regexes to the point they work. But the code is a mess and needs cleanup.

**Thougts**: S3 "imdb-datasets" access denied - really? 

### Day 15: December 20, 2017 - Little boxes...
**Today's Progress**: Hacked some of the backend pieces more or less together.

**Thougts**: Next year at [POFF Movie festival](https://poff.ee/eng/index) I'm definetly going to do my *TO WATCH* research using this tool I'm building right now. It's terribly annoying going through frontend trying to figure out what to whatch..

**Result**:
> {'media': [{'movies': [{'imdb': [],
>                        'title': 'CAPTAIN AMERICA CIVIL WAR',
>                        'year': 2016},
>                       {'imdb': [{'creators': [],
>                                  'genres': ['Comedy', 'Drama'],
>                                  'imdb_id': 'tt5962210',
>                                  'rating': 6.7,
>                                  'runtime': 98.0,
>                                  'tagline': "She'll Follow You",
>                                  'title': 'Ingrid Goes West',
>                                  'type': 'feature',
>                                  'uri': 'http://www.imdb.com/title/tt5962210/',
>                                  'votes': 10172,
>                                  'year': '2017'}],
>                        'title': 'INGRID GOES WEST',
>                        'year': 2017},
>                       {'imdb': [{'creators': [],
>                                  'genres': ['Crime', 'Drama'],
>                                  'imdb_id': 'tt0087843',
>                                  'rating': 8.4,
>                                  'runtime': 139.0,
>                                  'tagline': 'Crime, passion and lust for '
>                                             "power - Sergio Leone's explosive "
>                                             'saga of gangland America. '
>                                             '[Australia Theatrical]',
>                                  'title': 'Once Upon a Time in America',
>                                  'type': 'feature',
>                                  'uri': 'http://www.imdb.com/title/tt0087843/',
>                                  'votes': 247454,
>                                  'year': '1984'}],
>                        'title': 'ONCE UPON A TIME IN AMERICA',
>                        'year': 1984}]},
>           {'series': [{'imdb': [], 'title': 'House of Cards', 'year': None},
>                       {'imdb': [], 'title': 'South Park', 'year': None},
>                       {'imdb': [], 'title': 'Archer', 'year': None},
>                       {'imdb': [], 'title': 'Rick and morty', 'year': None}]}]}

### Day 16: December 21, 2017 - Skipped a beat
**Today's Progress**: Christmas party after work. Skipped a day.

### Day 17: December 22, 2017 - filesystem directory monitoring
**Today's Progress**: Made use of watchdog and wrote a script to monitor a directory and log events to /dev/jsonlog or redis queue.

**Thoughts**: Had hard time picking up application-I and worked on something else to ease my mind.

### Day 18: December 23, 2017 - IP packet inspection
**Today's Progress**: Started building IP packet inspection tool for myself to monitor my network traffic.

**Thoughts**: Since I started building tools yestarday, I thought it would be a good idea to build something I've wanted to explore before in the past. Didn't build anything myself yet but found incredibly useful code that I am extremely grateful for. Next step will be to structure the packet data, direct it to Elastic and build tool to query to query/monitor Elasticsearch indices and set up notifications for interesting traffic. It's awesome to explore networking fundamentals again. 

### Day 19: December 24, 2017 - IP packet inspection - structuring
**Today's Progress**: Worked on the packet inspection code and found out I could have done it easier with scapy. On to exploring scapy!

### Day 20: December 25, 2017 - scrapy
**Today's Progress**: Explored scrapy. [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3) had a nice tutorial for getting started with scrapy. Built a script to get all the legos from a given year, just followed the tutorial and completed the extra challenges at the end. Using scrapy also fetched all movie titles from POFF website. Now would be a good time to enrich them with extra data, but have to use tools that do not rely on imdb
unoficial API.

**Thoughts**: So it wasn't my code.. imdb-pie "search_for_title" seems to be non-functional. Should not rely on fragile external dependencies that are not built on official APIs. If I am to continue first idea, I should make it with different tools such as beautifulsoup/selenium/scrapy. 

### Day 21: December 26, 2017 - scrapy v2
**Today's Progress**: So I made a script to gather all minecraft servers just to add them to hosts file and redirect all minecraft server requests to /dev/null - or 0.0.0.0 to be exact.. There still seems to be some kind of endless loop problem but I thnk it won't be dfficult to work that out. Otherwse all the awesome info is being gathered. 

**Thoughts**: It started in the morning when my nephew asked for my computer to play Minecraft. Yeah, I'm partly responsible for that craze, but it was painful to see them playing mind-numbing games.. That gave me an idea to make a Minecraft firewall. I'm sure that's going to protect my mothers computer from those meddling kids :P If they're smart enough they'll get to play, until I get to firewall config. :)

**Data Sample**:
{'id': '88.150.171.23', 'href': 'http://minecraft-server-list.com/server/390744/', 'tags': ['Survival', 'Factions', 'McMMO', 'PVP', 'RP', 'Economy'], 'version': '1.8.8', 'ip': '88.150.171.23', 'players': '/ 50'}
{'id': 'avatarcentral2.mcserver.ws', 'href': 'http://minecraft-server-list.com/server/403444/', 'tags': ['Survival', 'PVP', 'Economy'], 'version': '1.8.8', 'ip': 'avatarcentral2.mcserver.ws', 'players': '/ 50'}
{'id': '172.106.203.31:28601', 'href': 'http://minecraft-server-list.com/server/405119/', 'tags': ['Survival', 'Factions', 'Economy'], 'version': '1.12.2', 'ip': '172.106.203.31:28601', 'players': '/ 50'}

### Day 22: December 27, 2017 - 
**Today's Progress**: Skipped a day.

**Thoughts**: I feel like I'm lacking in JavaScript skills to get awesome stuff done.

### Day 23: December 28, 2017 - Celery
**Today's Progress**: Got started with celery examples. Wanted to get more done but had to troubleshoot celery. It wasn't working out of the box in virtualenv because I had one instance of it installed system wide. Wasted too much time debugging the issue... 

**Thoughts**: Pay attention to error messages!!! Would have been clear instantly that I wasn't using the celery defined in virtualenv...
Traceback (most recent call last):
  File "/usr/local/bin/celery", line 7, in <module>
      from celery.__main__ import main
      ImportError: No module named celery.__main__

### Day 24: December 29, 2017 - Celery vol II
**Today's Progress**: I was wondering why tasks were not going to my queues, but after following [Digitalocean](https://www.digitalocean.com/community/tutorials/how-to-use-celery-with-rabbitmq-to-queue-tasks-on-an-ubuntu-vps) tutorial I noticed that I wasn't pushing jobs to Rabbit queue. I finaly got the jobs going to queues but they stayed there. Need to see how I can consume them properly using celery. Tried out flower API - looks promising for monitoring purposes.

**Thoughts**: While reaing [StackOverflow](https://stackoverflow.com/questions/9077687/why-use-celery-instead-of-rabbitmq) I came to think that celery is not something for me. What I like about the whole thing is that it has a nice API to interact with and when using flower you could potentially monitor whole message flow pretty neatly.  


### Day 25: December 30, 2017 - lost a day again.
**Today's Progress**: days += 1

**Thoughts**: End of the year and christmas time is terrible time to find time for coding. I seem to be skipping days too regularly...

### Day 26: December 31, 2017 - Sonic pi
**Today's Progress**: Actually had to start a stopwatch to get my hour of code today. Thought I'd spend it creatively - continued with sonic-pi and understood how terrible it is to create something in it. No wonder programs such as Ableton exist. While it's a cool concept the creative process flow would probavlly be better in a program such as Ableton. She potential show element with sonic-pi is still awesome though.

**Thoughts**: When living gets in the way. Testing out sonic-pi is easier in python interactive shell.

### Day 27: January 1, 2018 - lost aday and
**Today's Progress**: days += 1

**Thoughts**: Not that I want to skip days, but lost my backpack on the new year's eve. Since I hoped I'd get it back I avoided setting up a new development environment from scratch. Luckily I got my computer back! Great start for a new year. Karma sure seems to work. Even if I had had permanently lost my backpack, it still would've been the best new year's eve I've had! :)

### Day 28: January 2, 2018 - back in black

**Today's Progress**: Tried scraping skyscanner.net with requests, but the site seems to be blocking robots. That sucks! 

**Thoughts**: So, since I made a new friend who lives in England I thought I'd make something to monitor plane tickets with. Scyscanner only seems to provide their API to legal entities, so I'm on my own to scrape the web. Considering that the site blocks robots, it's something I should not do as part of #100DaysOfCode. Another project idea eliminated -.-


### Day 29: January 3, 2018 - Estonia

**Today's Progress**: Started building a spider to monitor open data that our government [publishes](http://www.rik.ee/et/avaandmed) publishes.

**Thoughts**: Wish I had a bigger project to work on. Maybe I should continue with my branch of python-sonic. Last time I ran into some architectural problems. I need to think it through and find a solid design pattern to work with.


### Day 30: January 4, 2018 - codeclub

**Today's Progress**: Started doing codeclub again. Maybe it would be a good idea to keep those exericises for backup. For times when I'm in dire need of coding hours but lack ideas to work on with. Since I'm ashamed how little I got done today, I can't count it as an hour of code. 

**Thoughts**: Looked at python-sonic and decied it takes more time than I have today to get started with that. At daytime I stashed 7 articles I need to read about packaging Python software. I thought I had everything figured out, until I wanted to run tests for a coe that's meant to run in virtualenv and CI server lacks all the dependencies.


### Day 31: January 5, 2018 - codeclub II 

**Today's Progress**: Codeclub stuff.

**Thoughts**: This week I kinda ended up in Python Packaging Hell... Luckily I found a nice example from [github](https://github.com/pypa/sample-namespace-packages) of how to package different things in one namespace. Regarding the challenge, just worked on some codeclub stuff.


### Day 32: January 6, 2018 - codeclub III

**Today's Progress**: Tower of Hanoi.

**Thoughts**: Although lists are considered to be the most dangerous data types in Python, because they can be so easily be misused, in my case, today, they were performing faster than appending instructions to a string. The goal was to have a STRING of instructions. Generating it from a list is MUCH faster than dynamically appending to a string. There probably are better solutions for solving this, but today this was good emough.


### Day 33: January 7, 2018 - writing tests

**Today's Progress**: testing code

**Thoughts**: Trying to get myself in the habbit of writing the test before functionality.


### Day 34: January 8, 2018 - atm

**Today's Progress**: worked on atm

**Thoughts**: Thought it would be easier to build the return bill logic, but at the end of a workday it's not that easy :(


### Day 35: January 9, 2018

**Today's Progress**: directory_monitor

**Thoughts**: Packaged watchdog feature into a console script.


### Day 36: January 10, 2018

**Today's Progress**: RLE

**Thoughts**: Well, managed to get run-length encoding and decoding functions pretty compact. My tests are passing, but the codeclub tests fail, and I have no idea why.


### Day 37: January 11, 2018

**Today's Progress**: None 

**Thoughts**: missed a day. days += 1


### Day 38: January 12, 2018

**Today's Progress**: Moved my Design pattern learning foler to this repository. I really do need to put more effort on design...

**Thoughts**: I tried and I tried, but at the end of the day I was too worn out to o anything productive.


### Day 39: January 13, 2018

**Today's Progress**: Design patterns.

**Thoughts**: ... 


### Day 40: January 14, 2018

**Today's Progress**: Moved to structural design patterns

**Thoughts**: Working your way through examples is the easy way out, and prabably violates the 100daysofcode thing, but ideas are scarce.


### Day 41: January 15, 2018

**Today's Progress**: Design patterns.

**Thoughts**: More structural patterns. I really need an idea for an interesting pet project.


### Day 42: January 16, 2018

**Today's Progress**: Played around with Trello API.

**Thoughts**: I hate working with API authentication, credential management and all that shit. Should finally look into JWT as well...


### Day 43: January 17, 2018

**Today's Progress**: Started building tolerance against my cryptonite - tests.


### Day 44: January 18, 2018

**Today's Progress**: Building tests that fail. And pass. Sometimes.


### Day 45: January 19, 2018

**Today's Progress**: Skipped. days += 1


### Day 46: January 20, 2018

**Today's Progress**: Finished chapter 2 of Python Testing with pytest


### Day 47: January 21, 2018

**Today's Progress**: Finished chapter 3 of Python Testing with pytest

**Thoughts**: Since I didn't have all the project functions set up, it was easier to just fetch the project code from The Web. At least this way more tests pass, though, db teardown functions still throw errors.


### Day 48: January 22, 2018

**Today's Progress**: Half way through the book.

**Thoughts**: Luckily when I'm done with this one, I should have Python Tricks waiting for me in the post office, I think.


### Day 49: January 23, 2018

**Today's Progress**: days += 1

**Thoughts**: It's a matter of choices. I did read some at Philly Joes, but didn't have enough time to log a day.


### Day 50: January 24, 2018

**Today's Progress**: One last chapter to go.

**Thoughts**: There was some nice intro to packaging Python, but nothing I didn't already know. The book itself really enforces good coding practice, and I think, would be awesome for someone starting out with Python - better than codecademy for sure, in my humble opinion. If I hadn't skipped any days, I'd be half way through my challenge, alas, tomorrow I will not be able to log a day either.


### Day 51: January 25, 2018

**Today's Progress**: days += 1

**Thoughts**: Estonian Music Awards


### Day 52: January 26, 2018

**Today's Progress**: Finished "Python Testing with pytest". 

**Thoughts**: ~3 hours of sleep, productive day at work, coding challenge and the night's still young. After just reading about tox, It sounds like something I might want to use for CD.


### Day 53: January 27, 2018

**Today's Progress**: days += 1 

**Thoughts**: Went to gym and ran out of time to code :( On my way to company "christmas party" grabbed my copy of Dan Bader's "Python Tricks" from the post office.


### Day 54: January 28, 2018

**Today's Progress**: Started reading Dan bader's "Python Tricks". Finished first 2 chapters so far.

**Thoughts**: Went to gym and ran out of time to code :( Went to post office to get my copy of Dan Bader's "Python Tricks".


### Day 55: January 29, 2018

**Today's Progress**: Well, started a project that should keep me busy for a long, long time.

**Thoughts**: from earth.animalia.chordata.mammalia.primates.haplorhini.simiiformes.hominidae.homo import sapiens as homo_sapiens - see the potential here?


### Day 56: January 30, 2018

**Today's Progress**: 1/3 of Python tricks read

**Thoughts**: Although today is a busy day, since last week I skipped to many days, I can't afford to skip days. Even when it's the re-opening of my fav jazz club.


### Day 57: January 31, 2018

**Today's Progress**: Almost half through the book. Python Tricks.

**Thoughts**: Picking up tricks..


### Day 58: February 1, 2018

**Today's Progress**: Didn't feel like reading today. Worked on my endless project.

**Thoughts**: On a project this scale you really start to think about design patterns and effective use of data structures. Neither of which reflects on my current code base.


### Day 58: February 2, 2018

**Today's Progress**: 2/3 of Python Tricks. 

**Thoughts**: Thought about doing more coding on world_project but it seemed overwhelming at the moment.


### Day 58: February 3, 2018

**Today's Progress**: Packaging monitoring tools into single Python namespace.

**Thoughts**: Found some Twitter keyword monitoring code, that works in my Zabbix server curreny to monitor specified keywords. Thought it would be nice to package some monitoring tools into single Python monitoring namespace.


### Day 59: February 4, 2018

**Today's Progress**: Worked out some bugs on Twitter keyword monitor and got a MVP out. Might add more functionality to it later. Read some more Python Tricks.

**Thoughts**: Almost forgot to log the hours today. I should really move some other monitoring tools that are in #100daysofcode repo to my pymon-tools repository.

###########################################


### Day 60: February 5, 2018

**Today's Progress**: Reading Python Tricks.

**Thoughts**: Did the commit, but forgot to fill in the log.


### Day 61: February 6, 2018

**Today's Progress**: days += 1

**Thoughts**: Did some work on pymon-tools repo while sitting in a bar, but not enough to log an hour.


### Day 62: February 7, 2018

**Today's Progress**: Worked on pymon-tools. Structuring and moved dirmon to monitoring namespace. Finished chapter6 of Python Tricks.


### Day 63: February 8, 2018

**Today's Progress**: days += 1


### Day 64: February 9, 2018

**Today's Progress**: Finished Python Tricks. Really awesome book.

**Thoughts**: When I look at the code I wrote when the challenge started, I see how un-Pythonic it is. Without mentors, the way of natural evolution, learning is slow and painful. Organic growth.










