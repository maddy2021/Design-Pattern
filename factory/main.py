# Factory Pattern : Creational Pattern
from apple import Apple
from samsung import Samsung
from nokia import Nokia

def get_mobile(m_name):
    if m_name.lower()=='samsung':
        return Samsung()
    elif m_name.lower()=='apple':
        return Apple()
    elif m_name.lower()=='nokia':
        return Nokia()

for mobile_name in ['samsung','nokia','apple']:
    mobile = get_mobile(mobile_name)
    mobile.battery_life()

