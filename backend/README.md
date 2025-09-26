# Setup

## Installing Dependencies
```bash
uv sync
```

### Open Telemetry Support

1. Add the required packages.
```bash
uv run opentelemetry-bootstrap -a requirements | uv pip install --requirement -
```
