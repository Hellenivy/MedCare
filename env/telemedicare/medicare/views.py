# Create your views here.
from django.shortcuts import render
from .models import Appointment

def appointment_list(request):
    if request.user.is_authenticated:
        appointments = Appointment.objects.filter(patient=request.user.patient)
        return render(request, 'appointments.html', {'appointments': appointments})
    else:
        return redirect('login')
