import random
import string

from django.db.utils import IntegrityError
from django.db import models, transaction

# Uses code from https://github.com/jbrendel/django-randomprimary/
class RandomPrimaryIdModel(models.Model):
    class Meta:
        abstract = True
        
    CRYPT_KEY_LEN_MIN = 5
    CRYPT_KEY_LEN_MAX = 9
    _IDCHARS = string.digits
    
    id = models.SmallIntegerField(db_index = True,
            primary_key = True,
            max_length = CRYPT_KEY_LEN_MAX+1,
            unique = True)
    
    def __init__(self, *args, **kwargs):
        """
        Nothing to do but to call the super class' __init__ method and initialize a few vars.
        """
        super(RandomPrimaryIdModel, self).__init__(*args, **kwargs)
        self._retry_count = 0 # used for testing and debugging, nothing else
    
    
    def _make_random_key(self, key_len):
        """
        Produce a new unique primary key.
        """
        return ''.join([ random.choice(self._IDCHARS) for dummy in xrange(0, key_len-1) ])
    
    def save(self, *args, **kwargs):
        """
        Modified save() function, which selects a special unique ID if necessary.
        Calls the save() method of the first model.Models base class it can find
        in the base-class list.
        """
        
        if self.id:
            # Apparently, we know our ID already, so we don't have to
            # do anything special here.
            super(RandomPrimaryIdModel, self).save(*args, **kwargs)
            return

        try_key_len                     = self.CRYPT_KEY_LEN_MIN
        try_since_last_key_len_increase = 0
        while try_key_len <= self.CRYPT_KEY_LEN_MAX:
            # Randomly choose a new unique key
            _id = self._make_random_key(try_key_len)
            sid = transaction.savepoint()       # Needed for Postgres, doesn't harm the others
            try:
                if kwargs is None:
                    kwargs = dict()
                kwargs['force_insert'] = True           # If force_insert is already present in
                                                        # kwargs, we want to make sure it's
                                                        # overwritten. Also, by putting it here
                                                        # we can be sure we don't accidentally
                                                        # specify it twice.
                self.id = _id
                super(RandomPrimaryIdModel, self).save(*args, **kwargs)
                break                                   # This was a success, so we are done here

            except IntegrityError, e:                   # Apparently, this key is already in use
                # Only way to differentiate between different IntegrityErrors is to look
                # into the message string. Too bad. But I need to make sure I only catch
                # the ones for the 'id' column.
                #
                # Sadly, error messages from different databases look different and Django does
                # not normalize them. So I need to run more than one test. One of these days, I
                # could probably just examine the database settings, figure out which DB we use
                # and then do just a single correct test.
                #
                # Just to complicates things a bit, the actual error message is not always in
                # e.message, but may be in the args of the exception. The args list can vary
                # in length, but so far it seems that the message is always the last one in
                # the args list. So, that's where I get the message string from. Then I do my
                # DB specific tests on the message string.
                #
                msg = e.args[-1]
                if msg.endswith("for key 'PRIMARY'") or msg == "column id is not unique" or \
                        "Key (id)=" in msg:
                    transaction.savepoint_rollback(sid) # Needs to be done for Postgres, since
                                                        # otherwise the whole transaction is
                                                        # cancelled, if this is part of a larger
                                                        # transaction.

                    self._retry_count += 1              # Maintained for debugging/testing purposes
                    try_since_last_key_len_increase += 1
                    if try_since_last_key_len_increase == try_key_len:
                        # Every key-len tries, we increase the key length by 1.
                        # This means we only try a few times at the start, but then try more
                        # and more for larger key sizes.
                        try_key_len += 1
                        try_since_last_key_len_increase = 0
                else:
                    # Some other IntegrityError? Need to re-raise it...
                    raise e

        else:
            # while ... else (just as a reminder): Execute 'else' if while loop is exited normally.
            # In our case, this only happens if we finally run out of attempts to find a key.
            self.id = None
            raise IntegrityError("Could not produce unique ID for model of type %s" % type(self))


class SurveyInstance(RandomPrimaryIdModel):
    LOCATION_CHOICES = (
        ('Regents Drive @ Rt. 1', 'Regents Drive @ Rt. 1'),
        ('Mowatt Lane Garage Exit @ Knox Rd.', 'Mowatt Lane Garage Exit @ Knox Rd.'),
        ('Mall @ Woods Hall', 'Mall @ Woods Hall'),
        ('Regents Dr. @ Main Administration', 'Regents Dr. @ Main Administration'),
        ('Campus Dr. @ Paint Branch Dr.', 'Campus Dr. @ Paint Branch Dr.'),
        ('Campus Dr. @ The Stamp', 'Campus Dr. @ The Stamp'),
        ('Regents Drive @ Stadium Drive', 'Regents Drive @ Stadium Drive'),
        ('Paint Branch Drive @ Lot 11b', 'Paint Branch Drive @ Lot 11b'),
        ('Campus Drive @ Adelphi Road', 'Campus Drive @ Adelphi Road'),
    )
    
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, choices=LOCATION_CHOICES)
    comments = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name + " at " + self.location


class Biker(RandomPrimaryIdModel):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    HELMET_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    LOCATION_CHOICES = (
        ('Sidewalk', 'Sidewalk'),
        ('Street', 'Street'),
    )
    
    surveyInstance = models.ForeignKey(SurveyInstance)
    bikerGender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None)
    bikerHelmet = models.CharField(max_length=1, choices=HELMET_CHOICES, default=None)
    bikerLocation = models.CharField(max_length=30, choices=LOCATION_CHOICES, default=None)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    
    def __unicode__(self):
        return "Gender: "+self.bikerGender+", Helmet: "+self.bikerHelmet+", Location: "+self.bikerLocation+" at "+self.date.strftime('%Y-%m-%d')+" at "+self.time.strftime('%H:%M')
