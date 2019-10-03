#!/usr/bin/env python3
from bspump_albion.pipeline import SamplePipeline
from bspump_albion.app import BlankAppApplication


if __name__ == '__main__':
	app = BlankAppApplication()

	svc = app.get_service("bspump.PumpService")

	# Construct and register Pipeline
	pl = SamplePipeline(app, 'SamplePipeline')
	svc.add_pipeline(pl)

	app.run()
