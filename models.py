import mongoengine as me


class Users(me.Document):
    Name = me.StringField(max_length=50, required=True)
    PhoneNumber = me.IntField(max_value=9999999999, required=True)
    Email = me.StringField(max_length=50, required=True)
    Address = me.StringField(max_length=10, required=True)
