from bspump import Sink
import bspump.mongodb
from mongoengine import *
import json
import sys

class ItemCity(Document):
    buy_price_max = IntField(min_value=0, required=True)
    buy_price_min = IntField(min_value=0, required=True)
    city = StringField(max_length=30, required=True)
    item_id = StringField(max_length=30, required=True)
    quality = IntField(min_value=0, required=True)
    sell_price_max = IntField(min_value=0, required=True)
    sell_price_max_date = DateTimeField(required=True)
    sell_price_min = IntField(min_value=0, required=True)
    sell_price_min_date = DateTimeField(required=True)


class MongoSink(Sink):

    def __init__(self, app, pipeline, id=None, config=None):
        super().__init__(app, pipeline, id, config)
        self.connection = connect(
            db="test",
            host="mongodb+srv://ples:test@alb-kalae.mongodb.net/test?retryWrites=true&w=majority",
        )

    @staticmethod
    def post_to_itemcity(to_post):
        post = ItemCity(**to_post)
        post.save()

    def process(self, context, event):
        print(event)
        self.post_to_itemcity(event)


bspump.mongodb.MongoDBConnection