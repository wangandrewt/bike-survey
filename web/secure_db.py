#!/usr/bin/env python
"""
Creates a secure, random password for the Django user 'admin'
"""
import hashlib, imp, os, sqlite3

# Load the OpenShift helper library
lib_path = os.environ['OPENSHIFT_REPO_DIR'] + 'web/'
modinfo = imp.find_module('openshiftlibs', [lib_path])
openshiftlibs = imp.load_module('openshiftlibs', modinfo[0], modinfo[1], modinfo[2])

# A default password so that OpenShift can secure it
default_password = { 'KEY': 'ZjSqGumxnGbLrFQd2eNrTgSGQYmbskThaqaba3etSJxwrA5Xnx'}

# Replace default keys with dynamic values
use_keys = openshiftlibs.openshift_secure(default_password)

# Set Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
import django
django.setup()
from django.contrib.auth.models import User
u = User.objects.get(username='admin')
u.set_password(use_keys['KEY'])
u.save()

# Print the new password info
print "Django application credentials:\n\tuser: admin\n\t" + use_keys['KEY']
