from django.http import test
from historyModel.models import history 

def add(requset):
    ea1 = requset.GET.get(eid)
    ea2 = requset.GET.get(ename)
    ea3 = requset.GET.get(eAddress)
    historys = history(ea1=eid,ea2=ename,ea3=eAddress)
    historys.seve
    return test("ok") 