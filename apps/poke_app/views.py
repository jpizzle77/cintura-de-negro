from django.shortcuts import render, HttpResponse, redirect
from models import User
from django.contrib import messages
from .. poke_app.models import Poke
from django.db.models import Count
from django.db.models import Q
from collections import Counter



def index(request):
	print "------##############  inside POKE_APP INDEX route ##################----------"
	print request.session['user']['id']
	
	try:
 		request.session['person_being_poked']
 	except:
 		request.session['person_being_poked']=0
 	print request.session['person_being_poked'], "<-------------request.session['person_being_poked']"

 	
 	person_being_poked = Poke.objects.filter(person_being_poked=request.session['person_being_poked'])


	pokes= person_being_poked.values('user').annotate(Count('poke_count')).distinct().order_by('-poke_count__count')[:3]

	print pokes
	print list(pokes)
	#print dir(pokes)

	x=[]
	for poke in pokes:

		y = (User.objects.get(id=poke['user']))#.filter(user__name=)
		
		#y= y.values('name')
		print dir(y)
		
		print y, "why not"
		
		x.append(y)
		print x

	print x, "full list"
	x=list(x)


	
 	try:
 		request.session['poke_count']
 	except:
 		request.session['poke_count']=1

 	print request.session['poke_count'], "<-----------------------request.session['poke_count']-"

 	poke_count= request.session['poke_count']


	context = {
		
		'users': User.objects.all(),
		'pokes':pokes,
		'x':x
		

	}

	return render(request, 'poke_app/index.html', context)



def create_poke(request,number,methods="POST"):
	print "------##############  POKE METHOD ##################----------"

	
	
	the_poker = request.session['user']['id']
	print the_poker, "the person who is doing the poking"

	request.session['person_being_poked'] = request.POST['user_id']
	print request.session['person_being_poked'], "<--------------------here is the person that is being poked that is poked"



	if request.method == 'GET':
		return redirect('poke_app:index')
		
	else:
	
		poke = Poke.objects.create_poke(request,request.POST)
		print poke, "<----PIG IN A POKE OINK OINK"
		


	return redirect('poke_app:index')



def clear(request):
	print '----------------            CLEARING THE SESSION         ---------------------'

	request.session.clear()

	return redirect('login_app:index')
