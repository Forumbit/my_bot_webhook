import time
import datetime

hours = None
minutes = None
a = None


def y_time(y_hours, y_minutes):
    new_1 = datetime.timedelta(days=0, hours=y_hours, minutes=y_minutes)
    return new_1


def x_time(x_hours, x_minutes):
    global hours, minutes
    x_a = datetime.timedelta(days=0, hours=x_hours, minutes=x_minutes)
    x_b = datetime.timedelta(
        days=0, hours=datetime.datetime.now().hour, minutes=datetime.datetime.now().minute
    )
    # x_b = datetime.timedelta(days=0, hours=12, minutes=39)
    x_c = (x_a - x_b).seconds
    new = time.struct_time(time.gmtime(x_c))
    hours = new.tm_hour
    minutes = new.tm_min


def one_more_time():
    global a, c

    y = datetime.timedelta(
        days=0, hours=datetime.datetime.now().hour, minutes=datetime.datetime.now().minute
        # days=0, hours=12, minutes=39
    )

    # До началы урока
    if y <= y_time(8, 20):
        x_time(8, 20)
        c = minutes
        a = hours
        if not a:
            a = '0'

    # 1-ый урок
    elif y_time(8, 20) <= y <= y_time(9, 5):
        x_time(9, 5)
        c = minutes

    # 2-ой урок
    elif y_time(9, 10) <= y <= y_time(9, 55):
        x_time(9, 55)
        c = minutes

    # 3-ий урок
    elif y_time(10, 10) <= y <= y_time(10, 55):
        x_time(10, 55)
        c = minutes


    # 4-ый урок
    elif y_time(11, 5) <= y <= y_time(11, 50):
        x_time(11, 50)
        c = minutes


    # 5-ый урок
    elif y_time(12, 5) <= y <= y_time(12, 50):
        x_time(12, 50)
        c = minutes

    # Уроки закончились
    elif y > y_time(12, 50):
        c = 'lesson_no'

    # Идет перемена
    else:
        c = 'new_lesson'
