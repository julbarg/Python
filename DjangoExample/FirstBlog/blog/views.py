#from django.shortcuts import render
from django.shortcuts import render_to_response
 
from blog.models import posts
 
def home(request):
	content = {
    	'title' : 'The secret to living high in the sky',
    	'author' : 'Jasmin Fox-Skelly',
    	'date' : '05th April 2015',
    	'body' : "Living on the peaks of the world's highest mountains is a tough challenge. At high altitudes the sunlight is intense, cold winds buffet you from every direction, and it's difficult to even breathe because there is so little oxygen in the air. But despite these extreme conditions, life endures. If you climb to the summit of Mount Everest, the world's tallest mountain, you will find life at every level. Jungles give way to alpine meadows and finally to snow-covered rock, but there will always be animals and plants if you know where to look. These organisms have made their homes in one of the most extreme environments on Earth. How do they do it? To find out, we must take a walk into the sky."
 	}
   	return render_to_response('index.html', content)

