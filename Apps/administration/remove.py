import os
from config import settings

def removeFIles(file):
    path = os.path.join(settings.BASE_DIR, 'media/', file)
    os.remove(path)
    return True
