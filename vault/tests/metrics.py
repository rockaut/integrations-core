# (C) Datadog, Inc. 2019-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# Everything our environment may provides
METRICS = {
    'go.gc.duration.seconds',
    'go.goroutines',
    'go.info',
    'go.memstats.alloc.bytes',
    'go.memstats.alloc.bytes.total',
    'go.memstats.buck_hash.sys.bytes',
    'go.memstats.frees.total',
    'go.memstats.gc.cpu.fraction',
    'go.memstats.gc.sys.bytes',
    'go.memstats.heap.alloc.bytes',
    'go.memstats.heap.idle.bytes',
    'go.memstats.heap.inuse.bytes',
    'go.memstats.heap.objects',
    'go.memstats.heap.released.bytes',
    'go.memstats.heap.sys.bytes',
    'go.memstats.last.gc.time.seconds',
    'go.memstats.lookups.total',
    'go.memstats.mallocs.total',
    'go.memstats.mcache.inuse.bytes',
    'go.memstats.mcache.sys.bytes',
    'go.memstats.mspan.inuse.bytes',
    'go.memstats.mspan.sys.bytes',
    'go.memstats.next.gc.bytes',
    'go.memstats.other.sys.bytes',
    'go.memstats.stack.inuse.bytes',
    'go.memstats.stack.sys.bytes',
    'go.memstats.sys.bytes',
    'go.threads',
    'process.cpu.seconds.total',
    'process.max.fds',
    'process.open.fds',
    'process.resident_memory.bytes',
    'process.start_time.seconds',
    'process.virtual_memory.bytes',
    'process.virtual_memory.max.bytes',
    'vault.audit.log.request',
    'vault.audit.log.request.failure',
    'vault.audit.log.response',
    'vault.audit.log.response.failure',
    'vault.barrier.get',
    'vault.core.check.token',
    'vault.core.fetch.acl_and_token',
    'vault.core.handle.request',
    'vault.expire.fetch.lease.times',
    'vault.expire.fetch.lease.times.by_token',
    'vault.expire.num_leases',
    'vault.policy.get_policy',
    'vault.runtime.alloc.bytes',
    'vault.runtime.free.count',
    'vault.runtime.heap.objects',
    'vault.runtime.malloc.count',
    'vault.runtime.num_goroutines',
    'vault.runtime.sys.bytes',
    'vault.runtime.total.gc.runs',
    'vault.token.createAccessor',
    'vault.token.lookup',
}

METRICS_OPTIONAL = {
    'route.create.auth.jwt',
    'route.read',
    'route.read.auth.token',
    'route.rollback.auth.token',
    'route.rollback.auth.jwt',
    'secrets.pki.tidy.cert_store_current_entry',
    'secrets.pki.tidy.cert_store_deleted_count',
    'secrets.pki.tidy.cert_store_total_entries',
    'secrets.pki.tidy.cert_store_total_entries_remaining',
    'secrets.pki.tidy.duration',
    'secrets.pki.tidy.failure',
    'secrets.pki.tidy.revoked_cert_current_entry',
    'secrets.pki.tidy.revoked_cert_deleted_count',
    'secrets.pki.tidy.revoked_cert_total_entries',
    'secrets.pki.tidy.revoked_cert_total_entries_fixed_issuers',
    'secrets.pki.tidy.revoked_cert_total_entries_incorrect_issuers',
    'secrets.pki.tidy.revoked_cert_total_entries_remaining',
    'secrets.pki.tidy.start_time_epoch',
    'secrets.pki.tidy.success',
    'vault.barrier.list',
    'vault.barrier.put',
    'vault.cache.hit',
    'vault.cache.miss',
    'vault.cache.write',
    'vault.cache.delete',
    'vault.consul.get',
    'vault.consul.list',
    'vault.consul.put',
    'vault.core.handle.login_request',
    'vault.core.post_unseal',
    'vault.core.unseal',
    'vault.expire.fetch.lease',
    'vault.expire.register.auth',
    'vault.expire.renew_token',
    'vault.identity.entity',
    'vault.identity.entity.creation',
    'vault.policy.set_policy',
    'vault.rollback.attempt.auth.jwt',
    'vault.rollback.attempt.auth.token',
    'vault.rollback.attempt.cubbyhole',
    'vault.rollback.attempt.identity',
    'vault.rollback.attempt.sys',
    'vault.route.create',
    'vault.route.read',
    'vault.route.rollback',
    'vault.route.rollback.auth.jwt',
    'vault.route.rollback.auth.token',
    'vault.route.rollback.cubbyhole',
    'vault.route.rollback.identity',
    'vault.route.rollback.sys',
    'vault.runtime.gc.pause_ns',
    'vault.runtime.total.gc.pause_ns',
    'vault.token.count.by_policy',
    'vault.token.create',
    'vault.token.creation',
    'audit.sink.failure',
    'audit.sink.success',
    'autopilot.failure_tolerance',
    'autopilot.healthy',
    'autopilot.node.healthy',
    'autosnapshots.last.success.time',
    'autosnapshots.percent.maxspace.used',
    'autosnapshots.rotate.duration',
    'autosnapshots.save.duration',
    'autosnapshots.save.errors',
    'autosnapshots.snapshot.size',
    'autosnapshots.total.snapshot.size',
    'consul.transaction',
    'core.active',
    'core.activity.fragment_size',
    'core.activity.segment_write',
    'core.in_flight_requests',
    'core.license.expiration_time_epoch',
    'core.locked_users',
    'core.mount_table.num_entries',
    'core.mount_table.size',
    'core.performance_standby',
    'core.replication.build_progress',
    'core.replication.build_total',
    'core.replication.dr.primary',
    'core.replication.dr.secondary',
    'core.replication.performance.primary',
    'core.replication.performance.secondary',
    'core.replication.reindex_stage',
    'core.replication.write_undo_logs',
    'core.unsealed',
    'expire.num_irrevocable_leases',
    'ha.rpc.client.echo',
    'ha.rpc.client.echo.errors',
    'ha.rpc.client.forward',
    'ha.rpc.client.forward.errors',
    'identity.entity.active.monthly',
    'identity.entity.active.partial_month',
    'identity.entity.active.reporting_period',
    'identity.num_entities',
    'identity.upsert_entity_txn.quantile',
    'identity.upsert_entity_txn.count',
    'identity.upsert_entity_txn.sum',
    'identity.upsert_group_txn.quantile',
    'identity.upsert_group_txn.count',
    'identity.upsert_group_txn.sum',
    'logshipper.buffer.length',
    'logshipper.buffer.max_length',
    'logshipper.buffer.max_size',
    'logshipper.buffer.size',
    'logshipper.streamWALs.scanned_entries',
    'merkle.flushDirty.num_pages',
    'merkle.flushDirty.outstanding_pages',
    'merkle.saveCheckpoint.num_dirty',
    'metrics.collection',
    'metrics.collection.error',
    'quota.lease_count.counter',
    'quota.lease_count.max',
    'raft.apply',
    'raft.barrier',
    'raft.candidate.electSelf',
    'raft.commitNumLogs',
    'raft.commitTime',
    'raft.compactLogs',
    'raft.fsm.apply',
    'raft.fsm.applyBatch',
    'raft.fsm.applyBatchNum',
    'raft.fsm.enqueue',
    'raft.fsm.restore',
    'raft.fsm.snapshot',
    'raft.fsm.store_config',
    'raft.leader.dispatchLog',
    'raft.leader.dispatchNumLogs',
    'raft.peers',
    'raft.replication.appendEntries.log',
    'raft.replication.appendEntries.rpc',
    'raft.replication.heartbeat',
    'raft.replication.installSnapshot',
    'raft.restore',
    'raft.restoreUserSnapshot',
    'raft.rpc.appendEntries',
    'raft.rpc.appendEntries.processLogs',
    'raft.rpc.appendEntries.storeLogs',
    'raft.rpc.installSnapshot',
    'raft.rpc.processHeartbeat',
    'raft.rpc.requestVote',
    'raft.snapshot.create',
    'raft.snapshot.persist',
    'raft.snapshot.takeSnapshot',
    'raft.state.follower',
    'raft_storage.bolt.cursor.count',
    'raft_storage.bolt.freelist.allocated_bytes',
    'raft_storage.bolt.freelist.free_pages',
    'raft_storage.bolt.freelist.pending_pages',
    'raft_storage.bolt.freelist.used_bytes',
    'raft_storage.bolt.node.count',
    'raft_storage.bolt.node.dereferences',
    'raft_storage.bolt.page.bytes_allocated',
    'raft_storage.bolt.page.count',
    'raft_storage.bolt.rebalance.count',
    'raft_storage.bolt.rebalance.time',
    'raft_storage.bolt.spill.count',
    'raft_storage.bolt.spill.time',
    'raft_storage.bolt.split.count',
    'raft_storage.bolt.transaction.currently_open_read_transactions',
    'raft_storage.bolt.transaction.started_read_transactions',
    'raft_storage.bolt.write.count',
    'raft_storage.bolt.write.time',
    'raft_storage.follower.applied_index_delta',
    'raft_storage.follower.last_heartbeat_ms',
    'raft_storage.stats.applied_index',
    'raft_storage.stats.commit_index',
    'raft_storage.stats.fsm_pending',
    'raft.transition.heartbeat_timeout',
    'raft.transition.leader_lease_timeout',
    'raft.verify_leader',
    'replication.fsm.last_upstream_remote_wal',
    'replication.rpc.client.create_token_register_auth_lease',
    'replication.rpc.client.save_mfa_response_auth',
    'replication.rpc.server.save_mfa_response_auth',
    'replication.rpc.standby.server.create_token_register_auth_lease_request',
    'rollback.attempt',
    'rollback.inflight',
    'rollback.queued',
    'rollback.waiting',
    'route.rollback',
    'token.create_root',
    'wal.flushReady.queue_len',
    'raft_storage.entry_size',
    'raft_storage.transaction',
    'secrets_sync.associations.count',
    'secrets_sync.destinations.count',
    'raft.wal.head_truncations',
    'raft.wal.last_segment_age_seconds',
    'raft.wal.log_appends',
    'raft.wal.log_entries_read',
    'raft.wal.log_entries_written',
    'raft.wal.log_entry_bytes_read',
    'raft.wal.log_entry_bytes_written',
    'raft.wal.segment_rotations',
    'raft.wal.stable_gets',
    'raft.wal.stable_sets',
    'raft.wal.tail_truncations',
}

KNOWN_COUNTERS = {
    'vault.audit.log.request.failure',
    'vault.audit.log.response.failure',
    'vault.cache.delete',
    'vault.cache.hit',
    'vault.cache.miss',
    'vault.cache.write',
    'vault.identity.entity.creation',
    'vault.token.creation',
}

MERKLE_WAL_METRICS = [
    'vault.vault.merkle.flushdirty',
    'vault.vault.merkle.savecheckpoint',
    'vault.vault.wal.deletewals',
    'vault.vault.wal.persistwals',
    'vault.vault.wal.flushready',
]

MERKLE_WAL_QUANTILES = [
    'vault.vault.merkle.flushdirty',
    'vault.vault.merkle.savecheckpoint',
]
