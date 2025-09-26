from opentelemetry.instrumentation.auto_instrumentation import initialize
# initialize() must be called before importing FastAPI because of how instrumentation is patched.
initialize()