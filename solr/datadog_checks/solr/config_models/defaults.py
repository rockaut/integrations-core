# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>


def shared_collect_default_metrics():
    return False


def shared_new_gc_metrics():
    return False


def instance_collect_default_jvm_metrics():
    return True


def instance_empty_default_hostname():
    return False


def instance_is_jmx():
    return False


def instance_min_collection_interval():
    return 15


def instance_name():
    return 'solr_instance'


def instance_rmi_client_timeout():
    return 15000


def instance_rmi_connection_timeout():
    return 20000


def instance_rmi_registry_ssl():
    return False
