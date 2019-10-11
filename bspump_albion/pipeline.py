#!/usr/bin/env python3
import logging

import bspump
import bspump.common
import bspump.http
import bspump.trigger
from bspump_albion.sink.mongo_sink import MongoSink
from bspump_albion.transformator import ProcessorExample

###

L = logging.getLogger(__name__)

###


class SamplePipeline(bspump.Pipeline):

	def __init__(self, app, pipeline_id):
		super().__init__(app, pipeline_id)

		self.build(
			bspump.http.HTTPClientSource(app, self, config={
				'url': "https://www.albion-online-data.com/api/v2/stats/prices/T6_HIDE"
			}).on(bspump.trigger.PeriodicTrigger(app, 10)),
			bspump.common.JsonBytesToDictParser(app, self),
			ProcessorExample(app, self),
#			bspump.common.PrintSink(app, self)
			MongoSink(app, self),
		)

