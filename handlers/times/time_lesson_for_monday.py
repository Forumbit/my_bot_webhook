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
    x_b = datetime.timedelta(days=0, hours=12, minutes=39)
    x_c = (x_a - x_b).seconds
    new = time.struct_time(time.gmtime(x_c))
    hours = new.tm_hour
    minutes = new.tm_min


def one_more_time():

    y = datetime.timedelta(
        days=0, hours=datetime.datetime.now(pytz.timezone('Europe/Moscow')).hour, minutes=datetime.datetime.now(pytz.timezone('Europe/Moscow')).minute
        # days=0, hours=12, minutes=39
    )

    global a, c, lesson_number
    # До началы урока
    if y <= y_time(8, 20):
        x_time(8, 20)
        c = minutes
        a = hours
        if not a:
            a = '0'



    elif y_time(8, 20) <= y <= y_time(9, 5):
        x_time(9, 5)
        c = minutes
        lesson_number = 1



    elif y_time(9, 10) <= y <= y_time(9, 55):
        x_time(9, 55)
        c = minutes
        lesson_number = 2


    elif y_time(10, 10) <= y <= y_time(10, 55):
        x_time(10, 55)
        c = minutes
        lesson_number = 3


    elif y_time(11, 15) <= y <= y_time(12, 0):
        x_time(12, 0)
        c = minutes
        lesson_number = 4


    elif y_time(12, 20) <= y <= y_time(13, 5):
        x_time(13, 5)
        c = minutes
        lesson_number = 5


    elif y_time(13, 10) <= y <= y_time(13, 55):
        x_time(13, 55)
        c = minutes
        lesson_number = 6



    elif y_time(14, 5) <= y <= y_time(14, 25):
        x_time(14, 25)
        c = minutes
        lesson_number = 7

    elif y_time(14, 35) <= y <= y_time(15, 15):
        x_time(15, 15)
        c = minutes
        lesson_number = 8



    elif y > y_time(15, 15):
        c = 'lesson_no'



    else:
        c = 'new_lesson'
