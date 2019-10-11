import bspump.common
import bspump
from bspump.elasticsearch import ElasticSearchSink


class Transformator(bspump.common.MappingTransformator):

	def build(self, app):
		return {
			'title': self.category,
		}


	def category(self, key, value):
		return key, value.upper()


class ProcessorExample(bspump.Processor):

	def __init__(self, app, pipeline, id=None, config=None):
		super().__init__(app, pipeline, id, config)

	def process(self, context, event):
		del event[0]["buy_price_min_date"]
		del event[0]["buy_price_max_date"]
		print(event[0])
		return event[0]  # Pass event to the following processor
