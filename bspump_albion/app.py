import bspump
from bspump_albion.pipeline import SamplePipeline
import bspump.kafka


class BlankAppApplication(bspump.BSPumpApplication):

	def __init__(self):
		super().__init__()
		svc = self.get_service("bspump.PumpService")

		svc.add_connection(
			bspump.kafka.KafkaConnection(self, "KafkaConnection")
		)

		svc.add_pipeline(
			SamplePipeline(self, "SamplePipeline")
		)
