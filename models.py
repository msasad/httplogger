import peewee as pv

db = pv.SqliteDatabase('logs.db')

class BaseModel(pv.Model):
    class Meta:
        database = db


class Log(BaseModel):
    id = pv.AutoField(column_name='rowid')
    request_body = pv.TextField()
    response_body = pv.TextField()
    response_headers = pv.TextField()
    request_headers = pv.TextField()
    uid = pv.CharField(max_length=27)
    rtt = pv.DecimalField(decimal_places=2, auto_round=True)
    time = pv.DateTimeField()
    url = pv.TextField()
    method = pv.CharField(max_length=8)
    code = pv.IntegerField()
