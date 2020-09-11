from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect,HttpResponsePermanentRedirect
from .forms import LinkSubmitForm
from .models import Long_URL,custom_extension
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
def create(response):
	if response.method == "POST":
		form  =  LinkSubmitForm(response.POST)
		try:
			if form.is_valid():
				n = form.cleaned_data["url"]
				t = form.cleaned_data["short"]
				p = custom_extension(extension=t)
				p.save()
				Long_URL.objects.create(short=p, full_url=n)
				messages.success(response, 'Url Shortened Successfully! share dikhe.ga/%s '%(t,))
				return HttpResponseRedirect("/")
		except IntegrityError:
			messages.error(response, 'Sorry extension already taken')


	else:
		form = LinkSubmitForm()

	return render(response, "main/create.html", {"form":form})

def go(response, short_id):
	try:
		i = custom_extension.objects.get(extension=short_id)
		#link = Long_URL.objects.get(short = i)
		link = get_object_or_404(Long_URL, short = i)
		#d= str(link[Long_URL])
		#return HttpResponseRedirect(link)
		return HttpResponsePermanentRedirect(link.full_url)
		#return redirect(link.full_url)
	except ObjectDoesNotExist:
		return render(response, "main/error404.html")