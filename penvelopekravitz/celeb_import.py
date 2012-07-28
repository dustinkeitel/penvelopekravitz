import os
import datetime

def main():
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from celebrity.models import Celebrity
    from django.contrib.auth.models import User

    celeb_file = os.path.join(os.path.abspath(os.curdir), 'celebs')
    f = open(celeb_file, 'rb')
    #adder = User.objects.get(username='dkeitel')
    current_names = [ celeb.name.lower() for celeb in Celebrity.objects.all() ]
    for name in f:
        if name.lower() in current_names:
            continue
        Celebrity.objects.get_or_create(name=name)

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "penvelopekravitz.settings")
    main()