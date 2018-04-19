
# coding= UTF-8

import json



project_older = ['id', 'name', 'owner_id', 'public' 'date_added', 'status', 'slug', 'team_id', 'platform', ]

PROJECT_ALL_FIELDS = ['id','name', 'public', 'date_added','status','slug', 'team_id', 'organization_id','first_event', 'forced_color', 'flags', 'platform']

sameFields = ['id','name', 'public', 'date_added','status','slug', 'team_id',  'platform',]
supFields = ['organization_id']

newfields = ['organization_id', 'forced_color','flags','first_event']
deletefields = [ 'owner_id']

FieldsINdexes = { 'id':0, 'name':1, 'public':3, 'date_added':4, 'status':5, 'slug':6, 'team_id':7, 'platform':8, }

def makeNewWithOld():

	file = open("dict.txt","w")	 
	for oldProject in Projects:
		
		NewProject = {}

		for field in FieldsINdexes:
			NewProject[field] = oldProject[FieldsINdexes[field]]
		
		NewProject['organization_id'] = '1'
		dictToWrite = {'dictToWrite': NewProject }
		file.write(json.dumps(dictToWrite))


















Projects = [
["1","Sentry (Internal)","1","0","2013-01-04 16:00:38","0","sentry",'','']
,["4","gites-de-france.mobi","1","0","2013-01-04 16:27:00","0","gites-de-francemobi","1",'']
,["5","rovaltain","1","0","2013-01-04 16:40:09","0","rovaltainfr","1","django"]
,["9","fnapback","1","0","2013-08-02 17:17:50","0","fnapback","1","django"]
,["10","fnapback.staging","1","0","2013-08-09 10:22:27","0","fnapbackstaging","1",'']
,["16","fnapfront","1","0","2013-09-26 13:14:57","0","fnapfront","1","django"]
,["18","Clairette-de-die.mobi","1","0","2013-10-02 08:04:21","0","clairette-de-diemobi","1",'']
,["25","ot-tournonais","1","0","2014-01-17 14:17:51","0","ot-tournonais-back","1",'']
,["26","ot-2alpes-showcase","1","0","2014-01-20 06:50:01","0","ot-2alpes-showcase","1",'']
,["32","otsi-ardecheverte","1","0","2014-03-14 14:10:35","0","otsi-ardecheverte","1",'']
,["34","tenthingstosee","1","0","2014-04-24 15:05:26","0","tenthingstosee","1","django"]
,["35","Clairette-de-die.com","1","0","2014-05-12 15:24:02","0","clairette-de-diecom","1",'']
,["36","kapt-demo","1","0","2014-05-19 17:19:04","0","kapt-demo","2",'']
,["40","ot-nyons","1","0","2014-06-18 13:30:11","0","ot-nyons","1",'']
,["41","kapt-land","1","0","2014-07-11 06:53:14","0","kapt-land","1",'']
,["42","ot-montelimar","1","0","2014-08-01 07:25:35","0","ot-montelimar","1",'']
,["43","ot-grenoble","1","0","2014-09-04 08:16:10","0","ot-grenoble","1",'']
,["45","fnapfront_staging","1","0","2014-09-29 13:31:27","0","fnapfront_staging","1","django"]
,["46","mercurart","1","0","2014-10-16 09:02:22","0","mercurart","1","django"]
,["48","ot-vercors-drome","1","0","2014-11-13 14:40:06","0","ot-vercors-drome","1","django"]
,["49","gdf-ardeche","1","0","2014-12-02 09:24:10","0","gdf-ardeche","1","django"]
,["50","bdc-grenoble","1","0","2015-02-06 15:54:09","0","bdc-grenoble","1","django"]
,["51","frapna","1","0","2015-03-18 08:19:33","0","frapna","1","django"]
,["52","kapt-demo","1","0","2015-05-12 17:13:24","0","kapt-demo","1","django"]
,["53","kapt-geo","1","0","2015-05-22 14:10:56","0","kapt-geo","1","django"]
,["54","ot-ht-route-vins","1","0","2015-06-10 12:26:20","0","ot-ht-route-vins","1","django"]
,["56","Kookooning","1","0","2015-07-23 07:36:31","0","kookoon","1","django"]
,["57","choranche-snat","1","0","2015-08-13 14:50:00","0","choranche-snat","1","django"]
,["58","kapt.travel","1","0","2015-08-19 07:53:52","0","kapttravel","1","django"]
,["59","bioconvergence","1","0","2015-10-21 07:27:01","0","bioconvergence","1","django"]
,["60","10thingstosee-cdn","1","0","2015-11-09 10:05:59","0","10thingstosee-cdn","2","django"]
,["61","bcbg","1","0","2016-01-20 15:18:15","0","bcbg","1","django"]
,["62","ot-valence-romans","1","0","2016-06-03 08:19:00","0","ot-valence-romans","1","django"]
,["63","kapt.mobi","1","0","2016-08-19 08:09:54","0","kaptmobi","1","django"]
,["64","Kookooning-js","1","0","2017-01-20 09:03:09","0","kookooning-js","1","javascript"]
,["65","10thingstosee-js","1","0","2017-01-25 13:21:25","0","10thingstosee-js","1","javascript"]
,["66","ot-matheysine","1","0","2017-04-25 09:41:16","0","ot-matheysine","1","django"]
,["67","isere-cheval-vert","1","0","2017-04-25 09:47:35","0","isere-cheval-vert","1","django"]
,["68","ot-matheysine-js","1","0","2017-05-02 08:52:38","0","ot-matheysine-js","1","javascript"]
,["69","kapt-intranet-js","1","0","2017-07-17 13:11:07","0","ot-vercors-drome-js","1","javascript"]
,["70","gdf-ardeche-js","1","0","2017-08-29 15:29:21","0","gdf-ardeche-js","1","javascript"]
,["72","ot-lamastre","1","0","2017-09-29 12:56:47","0","ot-lamastre","1","django"]
,["73","dolce-via","1","0","2017-09-29 12:59:02","0","dolce-via","1","django"]
,["74","arche-agglo","1","0","2017-09-29 12:59:16","0","arche-agglo","1","django"]
,["75","cosmebio-js","1","0","2017-11-08 12:57:34","0","cosmebio-js","1","javascript"]
,["76","cosmebio","1","0","2017-11-08 14:25:24","0","cosmebio","1","django"]
,["77","valence-en-gastronomie","1","0","2018-01-25 12:09:44","0","valence-en-gastronomie","1","django"]
,["78","valence-en-gastronomie-js","1","0","2018-01-25 12:10:26","0","valence-en-gastronomie-js","1","javascript"]
,["79","lpbvdf","1","0","2018-02-01 16:04:24","0","lpbvdf","1","django"]
,["80","lpbvdf-js","1","0","2018-02-03 16:04:43","0","lpbvdf-js","1","javascript"]
,["81","savoir-faire-trieves","1","0","2018-02-02 08:31:46","0","savoir-faire-trieves","1","django"]
,["82","balcon-est-vercors","1","0","2018-02-16 08:47:01","0","balcon-est-vercors","1","django"]
,["83","Drôme Aventure","1","0","2018-02-27 14:45:26","0","drome-aventure","1","django"]
,["84","maisons-logelis","1","0","2018-02-27 14:50:37","0","maisons-logelis","1","django"]

]
