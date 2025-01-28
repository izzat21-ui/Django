from django.db.models import Model, TextChoices, CharField, TextField


class Job(Model):
    class StatusType(TextChoices):
        FULLTIME = 'fulltime', 'Fulltime'
        WFH = 'wfh', 'Work from Home'
        CONTRACT = 'contract', 'Contract'
        REMOTE = 'remote', 'Remote'

    title = CharField(max_length=255)
    country = CharField(max_length=255)
    location = CharField(max_length=255)
    detail = TextField()
    status = CharField(
        max_length=20,
        choices=StatusType.choices,
        default=StatusType.FULLTIME,
    )
