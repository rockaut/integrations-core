# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
METRIC_MAP = {
    'apn_active_connections': 'appliance.active_connections',
    'apn_active_connections_max': 'appliance.active_connections.max',
    'apn_audit_events': 'appliance.audit_events',
    'apn_audit_logs': 'appliance.audit_logs',
    'apn_certificate_days_remaining': 'appliance.certificate_days.remaining',
    'apn_cpu_usage_percent': 'appliance.cpu.percent_usage',
    'apn_disk': 'appliance.disk',
    'apn_disk_partition_statistic': 'appliance.disk.partition_statistic',
    'apn_dns_cache_entries': 'appliance.dns.cache_entries',
    'apn_dns_requests_total': 'appliance.dns.requests',
    'apn_dns_responses_total': 'appliance.dns.responses',
    'apn_function_sessions': 'appliance.function.sessions',
    'apn_function_status': 'appliance.function.status',
    'apn_function_suspended': 'appliance.function.suspended',
    'apn_image_size': 'appliance.image.size',
    'apn_memory': 'appliance.memory',
    'apn_network_interface_speed': 'appliance.network_interface.speed',
    'apn_network_interface_statistic': 'appliance.network_interface.statistic',
    'apn_proxy_protocol_messages': 'appliance.proxy.protocol_messages',
    'apn_snat': 'appliance.snat',
    'apn_spa_dropped_packets': 'appliance.spa.dropped_packets',
    'apn_spa_packet_authorization_time': 'appliance.spa.packet_authorization_time',
    'apn_spa_packets': 'appliance.spa.packets',
    'apn_spa_replay_attack_cache_entries': 'appliance.spa.replay_attack_cache_entries',
    'apn_state_size': 'appliance.state_size',
    'apn_status': 'appliance.status',
    'apn_volume_number': 'appliance.volume_number',
    'ctr_admin_authentication': 'controller.admin.authentication',
    'ctr_admin_authorization': 'controller.admin.authorization',
    'ctr_admin_evaluate_all_policies': 'controller.admin.evaluate_all_policies',
    'ctr_admin_mfa': 'controller.admin.mfa',
    'ctr_client_authentication': 'controller.client.authentication',
    'ctr_client_authorization': 'controller.client.authorization',
    'ctr_client_csr': 'controller.client.csr',
    'ctr_client_enter_password': 'controller.client.enter.password',
    'ctr_client_evaluate_all_policies': 'controller.client.evaluate_all_policies',
    'ctr_client_mfa': 'controller.client.mfa',
    'ctr_client_new_ip_allocation': 'controller.client.new_ip_allocation',
    'ctr_client_risk_engine_response': 'controller.client.risk_engine_response',
    'ctr_client_sign_in_with_mfa': 'controller.client.sign_in_with_mfa',
    'ctr_database_conflicts': 'controller.database.conflicts',
    'ctr_database_node_state': 'controller.database.node_state',
    'ctr_database_raft_state': 'controller.database.raft_state',
    'ctr_database_replication': 'controller.database.replication',
    'ctr_database_replication_slot_replay_lag': 'controller.database.replication.slot_replay_lag',
    'ctr_database_size': 'controller.database.size',
    'ctr_evaluate_user_claim_script': 'controller.evaluate_user_claim_script',
    'ctr_ip_pool': 'controller.ip_pool',
    'ctr_license': 'controller.license',
    'ctr_license_days_remaining': 'controller.license.days_remaining',
    'ctr_memory_heap': 'controller.memory_heap',
    'ctr_policy_evaluator': 'controller.policy_evaluator',
    'ctr_threads': 'controller.threads',
    'gw_azure_resolver_cache': 'gateway.azure_resolver.cache',
    'gw_azure_resolver_cache_ttl': 'gateway.azure_resolver.cache_ttl',
    'gw_dns_forwarder_cache': 'gateway.dns_forwarder.cache',
    'gw_dns_forwarder_domain': 'gateway.dns_forwarder.domain',
    'gw_dns_forwarder_query': 'gateway.dns_forwarder.query',
    'gw_event_queue_period_peak': 'gateway.event_queue.period_peak',
    'gw_event_queue_size': 'gateway.event_queue.size',
    'gw_ha_interface': 'gateway.ha_interface',
    'gw_http_action': 'gateway.http.action',
    'gw_http_connection': 'gateway.http.connection',
    'gw_http_open_connection': 'gateway.http.open_connection',
    'gw_http_requests': 'gateway.http.requests',
    'gw_illumio_resolver_cache': 'gateway.illumio.resolver.cache',
    'gw_illumio_resolver_cache_ttl': 'gateway.illumio.resolver.cache_ttl',
    'gw_illumio_resolver_label': 'gateway.illumio.resolver.label',
    'gw_name_resolver_cache': 'gateway.name.resolver.cache',
    'gw_name_resolver_names_missing_resolver': 'gateway.name.resolver.names_missing_resolver',
    'gw_name_resolver_value': 'gateway.name.resolver.value',
    'gw_policy_evaluator': 'gateway.policy.evaluator',
    'gw_session_dropped_signin': 'gateway.session.dropped_signin',
    'gw_session_event': 'gateway.session.event',
    'gw_session_event_timing': 'gateway.session.event_timing',
    'gw_session_js_exectime': 'gateway.session.js_exectime',
    'gw_sessiond_heap': 'gateway.sessiond.heap',
    'gw_sessiond_thread_count': 'gateway.sessiond.thread_count',
    'gw_token_size': 'gateway.token_size',
    'gw_vpn_client_metric': 'gateway.vpn.client_metric',
    'gw_vpn_memory_usage': 'gateway.vpn.memory_usage',
    'gw_vpn_resolved_actions': 'gateway.vpn.resolved_actions',
    'gw_vpn_rules': 'gateway.vpn.rules',
    'gw_vpn_rules_size': 'gateway.vpn.rules_size',
    'gw_vpn_sessions': 'gateway.vpn.sessions',
    'ptl_client': 'portal.client',
}

RENAME_LABELS_MAP = {
    'version': 'protocol_version',
}
