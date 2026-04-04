from django.db import models


class userdata(models.Model):
    user_id = models.CharField(max_length=10, unique=True, editable=False, blank=True)
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    username = models.CharField(max_length=225, unique=True)
    password = models.CharField(max_length=225)

    def save(self, *args, **kwargs):
        if not self.user_id:
            last_user = userdata.objects.all().order_by('user_id').last()
            if last_user and last_user.user_id and len(last_user.user_id) > 1:
                try:
                    last_id = int(last_user.user_id[1:])
                    new_id = last_id + 1
                except ValueError:
                    new_id = 1
            else:
                new_id = 1
            self.user_id = f'A{new_id:03d}'
        super().save(*args, **kwargs)
