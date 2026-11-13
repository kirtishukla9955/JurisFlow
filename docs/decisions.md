# Decision Log

## 1. Single Database Setup (PostgreSQL-only)
**Decision**: Use PostgreSQL as the single source of truth, avoiding a multi-database setup (like DuckDB, ClickHouse, or SQLite).

**Rationale**: For a system demonstrating senior engineering practices, operational simplicity and transaction consistency are paramount. Modern PostgreSQL can handle complex analytics, real-time queues (via `FOR UPDATE SKIP LOCKED`), and JSONB document stores alongside standard transactional workloads. This avoids the cognitive overhead and failure domains of distributed data synchronization until scaling limits are actually proven and reached.
