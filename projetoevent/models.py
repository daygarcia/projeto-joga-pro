from django.db import models


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    is_running = models.IntegerField()
    is_uploading = models.IntegerField(default=0)

    def __str__(self):
        return self.is_running


class Ticket(models.Model):
    code = models.IntegerField()
    rfid = models.IntegerField()
    status = models.IntegerField()
    user_id = models.IntegerField()
    type = models.IntegerField()
    gate = models.IntegerField()
    sector = models.IntegerField()
    block = models.CharField(max_length=100)
    row = models.CharField(max_length=100)
    seat = models.IntegerField()
    extra = models.IntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.row


class TicketLog(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.IntegerField()
    action = models.IntegerField()
    user_id = models.IntegerField()
    event_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.row
