# Crumbkeeper

Operational bakery management platform for sourdough bakers, cottage bakeries, and microbakery businesses.

## Product Philosophy

Crumbkeeper is designed around:
- operational clarity
- production workflow management
- bakery organization
- production efficiency
- mobile-first usability

## Stack

### Frontend
- React
- TypeScript
- Vite
- Tailwind

### Backend
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic

### Infrastructure
- Docker
- Redis
- WebSockets

## Monorepo Structure

apps/
- api
- web
- worker

packages/
- ui
- types
- utils
- config

infrastructure/
- docker
- nginx
- deployment

docs/
- architecture
- database
- api
- workflows