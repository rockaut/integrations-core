# (C) Datadog, Inc. 2025-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from .instance import InstanceConfig
from .shared import SharedConfig


class ConfigMixin:
    _config_model_instance: InstanceConfig
    _config_model_shared: SharedConfig

    @property
    def config(self) -> InstanceConfig:
        return self._config_model_instance

    @property
    def shared_config(self) -> SharedConfig:
        return self._config_model_shared
