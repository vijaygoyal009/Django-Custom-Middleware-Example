from django.utils.deprecation import MiddlewareMixin


class CustomeMiddleware(MiddlewareMixin):
    # process_request ----> Called before the view is executed
    def process_request(self, request):
        print("Welcome this is before view  print statement")
    

    # process_view ----> Called Just before the view is excuted
    def process_view(self , request,view_func , view_args , view_kwargs):
        print("----------------------------------------------------")
        print("Called Just Before the view is excuted")
    


    # process_exception ----> Called if an exception is raised in the view
    def process_exception(self,request,exception):
        print(" -------------------------------------------------------")
        print("An exception is occures")
        print("-------------------------------------------------------")

    
  




class CustomeMiddleware1(MiddlewareMixin):

    # process_response ----> Called after the view is execution and before the response is send
    def process_response(self,request,response):
        print("-------------------------------------------------------")
        print("Called after the view is execution and before the response is send")
        return response