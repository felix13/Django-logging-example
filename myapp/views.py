import logging
from django.http import HttpResponseServerError
from django.http import HttpResponse


logger = logging.getLogger(__name__)

def home(request):
   
    logger.error("Something went wrong !!")
    
    return HttpResponse("Just testing if logging works")
    
 
def log_server_error(request):
    
    return HttpResponseServerError("log internal server error ")
    
    
    

    
    

    
    

