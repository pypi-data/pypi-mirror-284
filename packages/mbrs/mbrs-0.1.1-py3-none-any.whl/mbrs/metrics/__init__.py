from mbrs import registry

from .base import Metric, MetricCacheable, MetricReferenceless

register, get_metric = registry.setup("metric")

from .bleu import MetricBLEU
from .chrf import MetricChrF
from .comet import MetricCOMET
from .cometqe import MetricCOMETQE
from .ter import MetricTER
from .xcomet import MetricXCOMET
from .bleurt import MetricBLEURT

__all__ = [
    "Metric",
    "MetricCacheable",
    "MetricReferenceless",
    "MetricBLEU",
    "MetricChrF",
    "MetricCOMET",
    "MetricCOMETQE",
    "MetricTER",
    "MetricXCOMET",
    "MetricBLEURT",
]
