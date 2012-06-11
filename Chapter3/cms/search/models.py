from django.db import models

from django.contrib.flatpages.models import FlatPage





# This is a simple Django model with two fields.

# keyword: This is a CharField with max_length = 50 which means upto 50 characters can go into this field.
# In the database, Django will turn this into a column declared as VARCHAR(50)

# page: This is a foreign key pointing at the FlatPage model, meaning that each SearchKeyword is tied to a specific
# page. Django will turn this into a foreign-key column referencing the table that the flat pages are stored in.



class SearchKeyword(models.Model):
    keyword = models.CharField(max_length=50)
    page = models.ForeignKey(FlatPage)


    def __unicode__(self):
        return self.keyword


