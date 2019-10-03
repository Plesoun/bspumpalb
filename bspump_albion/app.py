import bspump
from bspump_albion.pipeline import SamplePipeline

class BlankAppApplication(bspump.BSPumpApplication):

	async def main(self):
		svc = self.get_service("bspump.PumpService")

		# Create and register all connections here

		# Create and register all lookups here

		# Create and register all pipelines here

		pl = SamplePipeline(self, 'TCPPipeline')
		svc.add_pipeline(pl)