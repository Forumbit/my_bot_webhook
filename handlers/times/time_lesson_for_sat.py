import time
import datetime
import pytz
hours = None
minutes = None
a = None
lesson_number = None

def y_time(y_hours, y_minutes):
    new_1 = datetime.timedelta(days=0, hours=y_hours, minutes=y_minutes)
    return new_1


def x_time(x_hours, x_minutes):
    global hours, minutes
    x_a = datetime.timedelta(days=0, hours=x_hours, minutes=x_minutes)
    x_b = datetime.timedelta(
        days=0, hours=datetime.datetime.now(pytz.timezone('Europe/Moscow')).hour, minutes=datetime.datetime.now(pytz.timezone('Europe/Moscow')).minute
    )
    # x_b = datetime.timedelta(days=0, hours=12, minutes=39)
    x_c = (x_a - x_b).seconds
    new = time.struct_time(time.gmtime(x_c))
    hours = new.tm_hour
    minutes = new.tm_min


def one_more_time():
    global a, c, lesson_number

    y = datetime.timedelta(
        days=0, hours=datetime.datetime.now(pytz.timezone('Europe/Moscow')).hour, minutes=datetime.datetime.now(pytz.timezone('Europe/Moscow')).minute
        # days=0, hours=12, minutes=39
    )


    if y <= y_time(8, 20):
        x_time(8, 20)
        c = minutes
        a = hours
        if not a:
            a = '0'


    elif y_time(8, 0) <= y <= y_time(8, 45):
        x_time(8, 45)
        c = minutes
        lesson_number = 1


    elif y_time(8, 50) <= y <= y_time(9, 35):
        x_time(9, 35)
        c = minutes
        lesson_number = 2


    elif y_time(9, 40) <= y <= y_time(10, 25):
        x_time(10, 25)
        c = minutes
        lesson_number = 3



    elif y_time(10, 40) <= y <= y_time(11, 25):
        x_time(11, 25)
        c = minutes
        lesson_number = 4



    elif y_time(11, 40) <= y <= y_time(12, 25):
        x_time(12, 50)
        c = minutes
        lesson_number = 5


    elif y > y_time(12, 25):
        c = 'lesson_no'


    else:
        c = 'new_lesson'
