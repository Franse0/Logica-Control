# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Logica Control** is a local Python application for gym access control using biometric validation (fingerprint). It runs on Windows at the gym location, interfaces with Digital Persona 4500 fingerprint reader, validates member status/membership, and controls magnetic lock/relay for door access.

## Database

- **SQLite** - Local database for offline-first operation
- Schema: `src/database/schema.sql` (4 tables: socios, planes_gimnasio, socio_plan_inscripcion, asistencia_socio)
- Setup: `python src/database/setup_db.py`
- Location: `data/gimnasio.db` (gitignored)

## Access Control Logic

Access is **ALLOWED** when ALL of:
- Socio status = 'activo'
- Membership vigente (fecha_vencimiento >= today)
- Payment status = 'pagado'

Otherwise: **DENIED** with warning message.

## Agent Development Workflow (ADW)

This repo uses an automated SDLC workflow powered by Claude Code agents:

### Workflow Commands

- `/classify_issue` - Classifies GitHub issue as `/feature`, `/bug`, or `/chore`
- `/feature` - Creates implementation plan in `specs/feature-*.md`
- `/bug` - Creates bug fix plan in `specs/bug-*.md`
- `/implement <plan-file>` - Executes the plan step-by-step (DO NOT invent scope)
- `/generate_branch_name` - Generates branch: `<type>-<number>-<slug>`
- `/commit` - Generates formatted commit: `<agent>: <type>: <message>`
- `/pull_request` - Creates PR with full context
- `/find_plan_file` - Locates plan file in `specs/`
- `/prime` - Quick codebase analysis before starting work

### Full Automated Flow

```bash
# Run complete workflow for GitHub issue #N
uv run adws/adw_plan_build.py <issue-number> [adw-id]
```

**Orchestration:** `adws/adw_plan_build.py`
1. Classify issue type
2. Generate branch name
3. Create plan (`/feature` or `/bug`) → `specs/*.md`
4. Find plan file path
5. Commit plan
6. Implement plan (`/implement`)
7. Commit implementation
8. Create pull request

**Agent execution:** `adws/agent.py`
- `execute_template()` - Runs slash commands via Claude Code CLI
- `prompt_claude_code()` - Low-level Claude Code CLI wrapper
- Output: `agents/{adw_id}/{agent_name}/raw_output.jsonl`

**Utilities:** `adws/utils.py`
- `make_adw_id()` - Generates 7-char workflow ID
- `setup_logger()` - Creates logger at `agents/{adw_id}/{agent_name}/execution.log`

### When Planning Features

- Plan goes in `specs/feature-*.md`
- Use template from `.claude/commands/feature.md`
- Focus areas: `src/models/`, `src/database/`, `src/ui/`, `src/utils/`
- Consider offline-first behavior, hardware integration (fingerprint reader, relay)
- Last step must be validation commands

### When Implementing

- Read plan from `specs/*.md` completely
- Execute steps in exact order
- Do NOT invent scope beyond the plan
- If blocked, document and propose minimal adjustment

## Development Commands

```bash
# Initialize project structure
/init

# Setup database
python src/database/setup_db.py

# Run application
python src/main.py

# Run ADW workflow for issue
uv run adws/adw_plan_build.py <issue-number>

# Run webhook server (for GitHub webhooks)
uv run adws/trigger_webhook.py
```

## Environment Variables

Required in `.env`:
- `ANTHROPIC_API_KEY` - Claude API key
- `CLAUDE_CODE_PATH` - Path to Claude CLI (default: `claude`)
- `DATABASE_PATH` - SQLite database path (default: `data/gimnasio.db`)
- `GITHUB_PAT` - GitHub token (optional, for API auth)
- `FINGERPRINT_READER` - Device model (e.g., DigitalPersona4500)
- `RELAY_PORT` - Serial port for lock control (e.g., COM3)

## Architecture Principles

- **Minimal scope** - Keep app small for learning
- **Offline-first** - Must work without internet
- **SQLite** - Fast local database
- **Biometric security** - Fingerprint templates stored encrypted
- **Reglas de negocio** - Access rules centralized in validation logic
- **Agent-driven development** - Use ADW workflow for features and bugs
