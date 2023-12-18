from django.shortcuts import render
import datetime
from datetime import timedelta

# Create your views here.


myDict = {"value": 10, "string":"this is value 2", "list":[10,20,30], "tuple":(10,20,30),
           "quote": f'He said to me "do not run with sun" ', "date": datetime.datetime.now()
           , "dict":[
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31}, 
],  "multiline":
"""Programming
Is 
Fun
""",
'postDate': datetime.datetime.now() - timedelta(days=10), "nestedList":[10,20,40,[50,60]]
}
def home(request):
    return render(request, "index.html", myDict)

