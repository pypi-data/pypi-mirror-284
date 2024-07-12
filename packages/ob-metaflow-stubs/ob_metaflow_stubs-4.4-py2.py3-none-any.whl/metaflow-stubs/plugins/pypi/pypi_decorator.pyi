##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.7.1+ob(v1)                                                    #
# Generated on 2024-07-11T17:01:16.294767                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.decorators

class PyPIStepDecorator(metaflow.decorators.StepDecorator, metaclass=type):
    def step_init(self, flow, graph, step, decos, environment, flow_datastore, logger):
        ...
    ...

class PyPIFlowDecorator(metaflow.decorators.FlowDecorator, metaclass=type):
    def flow_init(self, flow, graph, environment, flow_datastore, metadata, logger, echo, options):
        ...
    ...

