from django.shortcuts import render, render_to_response
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
#from django.contrib.auth.decorators import login_required

# Create your views here.
def get_index(request):
	pagetitle = "Tasty Times."
	subtitle = "Enjoy it."
	return render(request, 'index.html', {"pagetitle": pagetitle, "subtitle": subtitle})

def get_contact(request):
	pagetitle = "Contact Me"
	return render(request, 'contact.html', {"pagetitle": pagetitle})

def get_about(request):
	pagetitle = "About"
	return render(request, 'about.html', {"pagetitle": pagetitle})


##def get_thanksbkp(request):
##    name = request.POST.get('name', '')
#    message = request.POST.get('message', '')
#    from_email = request.POST.get('email', '')
#    if name and message and from_email:
#        try:
#            send_mail(name, message, from_email, ['alinechribeiro@gmail.com'])
#        except BadHeaderError:
#            return HttpResponse('Invalid header found.')
#        return HttpResponseRedirect('/thanks')
#    else:
#        # In reality we'd use a form class
#        # to get proper validation errors.
#        return HttpResponse('Make sure all fields are entered and valid.')

def get_thanks(request):
	pagetitle = "Thank you"
	return render(request, 'thanks.html', {"pagetitle": pagetitle})
    
#Testing the url
def test_check_content_is_correct(self):
    home_page = self.client.get('/')
    self.assertTemplateUsed(home_page, "index.html")
    home_page_template_output = render_to_response("index.html").content
    self.assertEqual(home_page.content, home_page_template_output)
