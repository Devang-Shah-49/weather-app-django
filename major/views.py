from django.shortcuts import render
import json
import urllib.request
import datetime
# Create your views here.
def index(request):
	if request.method =='POST':
		city = request.POST['search']
		res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=1fc8804d7c82b05d0c1e4102e813824a')
		json_data = json.load(res)
		data = {
			"country_code" : str(json_data['sys']['country']),
			"coordinate": str(json_data['coord']['lon'])+' , '+str(json_data['coord']['lat']),
			"temp":str(json_data['main']['temp'])+'K',
			"pressure":str(json_data['main']['pressure'])+'psi',
			"humidity":str(json_data['main']["humidity"]),
			"wind":str(json_data['wind']['speed']) + 'm/s',
			"sunrise":datetime.datetime.fromtimestamp(int(json_data['sys']['sunrise'])).strftime('%c'),
			"sunset": datetime.datetime.fromtimestamp(int(json_data['sys']['sunset'])).strftime('%c'),
			
		}
	else:
		city=''
		data = {}
	return render(request,'index.html',{'city':city,'data':data})