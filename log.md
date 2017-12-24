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


