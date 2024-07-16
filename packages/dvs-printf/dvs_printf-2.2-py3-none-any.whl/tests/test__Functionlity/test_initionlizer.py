from dvs_printf import *
import dvs_printf


def test_import_all(): 
    assert printf
    assert init
    assert list_of_str
    assert showLoading


def test_init():
    pf = dvs_printf.init()
    printf = pf.printf

    assert pf.set_style == "typing" 
    assert pf.set_speed == 3
    assert pf.set_delay == 0
    assert pf.set_stay == True
    assert pf.set_getmat == False

    pf = dvs_printf.init(
        style="left", 
        speed=2, 
        delay=2, 
        stay=False, 
        getmat=True
    )

    assert pf.set_style == "left" 
    assert pf.set_speed == 2
    assert pf.set_delay == 2
    assert pf.set_stay == False
    assert pf.set_getmat == True

    pf.set_style = "gunshort"
    pf.set_speed = 6
    pf.set_delay = 3
    pf.set_stay = True
    pf.set_getmat = "true"

    printf("hello world", 
        style="mid", 
        speed=4, 
        delay=.5, 
        stay=False, 
        getmat="show"
    )

    assert pf.set_style == "gunshort"
    assert pf.set_speed == 6
    assert pf.set_delay == 3
    assert pf.set_stay == True
    assert pf.set_getmat == "true"

