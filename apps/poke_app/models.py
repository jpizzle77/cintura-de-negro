from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
from ..login_app.models import User

class Poke_Manager(models.Manager):

	def create_poke(self,request,data):


	
		poke_count = Poke.objects.filter(person_being_poked=request.session['person_being_poked']).count()
		print poke_count, "<---poke_count for person being poked "
		request.session['poke_count']= poke_count
		print request.session['poke_count'], " <-----request.session['person_being_poked']   COUNT"

		
		poke = Poke(person_being_poked=User.objects.get(id=request.session['person_being_poked']), user=User.objects.get(id=request.session['user']['id']))
		poke.poke_count=poke_count
		print poke_count, "<------------what going on here"
		print poke.user.pokes.count(), "jigga what"
		poke.save()
		print poke.id, "the id"
		return poke



class Poke(models.Model):
	#username = models.CharField(max_length=255, unique= TRUE)
	person_being_poked = models.ForeignKey(User, related_name = "pokee")
	user = models.ForeignKey(User, related_name = "pokes")
	poke_count = models.IntegerField(default=0)
	objects = Poke_Manager()



	def __repr__(self):
		return "<Person being poked: {} Poker:{} Poke Count:{} >".format(self.person_being_poked, self.user, self.poke_count)
	


