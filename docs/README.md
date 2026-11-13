# JurisFlow

JurisFlow is a portfolio-grade backend system simulating the growth engineering infrastructure of a B2B SaaS company:
- Lead enrichment
- Rate-limited outbound automation (Playwright)
- A/B and multi-armed bandit experimentation (scipy, numpy)
- Multi-touch attribution
- CRM synchronization

## Stack
- **Backend**: FastAPI (Python 3.11+, fully async)
- **Task Queue**: Celery + Redis
- **Database**: PostgreSQL (single source of truth)
- **ORM / Migrations**: SQLAlchemy 2.0 (async) + Alembic
- **Automation**: Playwright
- **Analytics & Experimentation**: scipy, numpy
- **Dashboard**: Streamlit
- **Observability**: Prometheus + Grafana
- **Testing**: pytest + pytest-asyncio

## Documentation
- Architecture Diagram: [docs/architecture.md](docs/architecture.md)
- Decision Log: [docs/decisions.md](docs/decisions.md)
