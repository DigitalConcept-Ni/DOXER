import os
from config import settings


def removefiles(file):
    data = {}
    try:
        path = os.path.join(settings.BASE_DIR, 'media/', file)
        os.remove(path)
        data['process'] = True
    except Exception as e:
        data['error'] = str(e)
    return data
