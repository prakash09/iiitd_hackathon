from flask import render_template
import googlemaps
from . import hacks
import urllib2
#import yaml
import json
@hacks.route('/')
def index():
    return render_template('hacks/index.html')

@hacks.route('/workshop')
def workshop():
	final_url=('https://api.meetup.com/2/open_events?key=3947c3e2d3e196a1d4292396f334f&and_text=False&offset=0&format=json&limited_events=False&photo-host=public&page=20&radius=25.0&category=18%2C2%2C6%2C34&desc=False&status=upcoming&sig_id=161835092&sig=e5b75df3659d864d9ddbd92a5711545ff0f1ccdc')
	json_obj=urllib2.urlopen(final_url)
	data=json.load(json_obj)
        gmaps = googlemaps.Client(key='AIzaSyB3wNLhjT9wEyeFvSN1yjp3iEdTFp76pt8')
        import pdb; pdb.set_trace()
        new_list=[]
	for data1 in data['results']:
            if 'venue' in data1.keys():
                matrix=gmaps.distance_matrix("%s, %s " %(str(data1['venue']['lon']),str(data1['venue']['lat'])),"okhla,delhi")
                new_list.append(matrix)
            else:
                continue
        #return matrix
	return render_template('hacks/workshop.html',data=new_list)
	#for data1 in data['results']:
	#	return data1

@hacks.route('/social_events')
def social_events():
	final_url=('https://api.meetup.com/2/open_events?and_text=False&offset=0&format=json&limited_events=False&photo-host=public&page=20&radius=25.0&category=16%2C25%2C4%2C13%2C30%2C31%2C35&desc=False&status=upcoming&sig_id=161835092&sig=e5b75df3659d864d9ddbd92a5711545ff0f1ccdc')
	json_obj=urllib2.urlopen(final_url)
	data=json.load(json_obj)
	return render_template('hacks/social_events.html')

@hacks.route('/entertainment')
def entertainment():
	final_url=('https://api.meetup.com/2/open_events?and_text=False&offset=0&format=json&limited_events=False&photo-host=public&page=20&radius=25.0&category=10%2C11%2C29%2C3%2C23%2C20%2C27%2C9%2C32%2C1&desc=False&status=upcoming&sig_id=161835092&sig=e5b75df3659d864d9ddbd92a5711545ff0f1ccdc')
	json_obj=urllib2.urlopen(final_url)
	data=json.load(json_obj)
	for data1 in data['results']:
		if data1['venue']:
			data1['venue']['lon']
			data1['venue']['lat']

	return render_template('hacks/entertainment.html')

@hacks.route('/hobby')
def hobby():
	final_url=('https://api.meetup.com/2/open_events?and_text=False&offset=0&format=json&limited_events=False&photo-host=public&page=20&radius=25.0&category=22%2C24%2C28%2C8%2C15%2C5%2C21%2C26%2C14%2C33&desc=False&status=upcoming&sig_id=161835092&sig=e5b75df3659d864d9ddbd92a5711545ff0f1ccdc')
	json_obj=urllib2.urlopen(final_url)
	data=json.load(json_obj)
	return render_template('hacks/hobby.html')

@hacks.route('/user/<username>')
def user(username):
    return render_template('hacks/user.html', username=username)

