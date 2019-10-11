#!/usr/bin/env python3
from bspump_albion.pipeline import SamplePipeline
from bspump_albion.app import BlankAppApplication
import bspump.kafka


if __name__ == '__main__':
	app = BlankAppApplication()

	app.run()
