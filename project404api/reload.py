from .models import Status


import sched, time

s = sched.scheduler(time.time, time.sleep)

def reset_status():
    Status.objects.update(status="True")
    return None

def reset_status_call(self):
    s.enter(15,1 , reset_status)
    s.run()
    return None
