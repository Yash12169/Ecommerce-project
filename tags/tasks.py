from celery import shared_task
@shared_task
def process(number):
    for i in range(number+1):
        print(i)

        ##task tab me task nhi dikh rha hai