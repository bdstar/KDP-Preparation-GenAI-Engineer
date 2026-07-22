import logging, time
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger("llm-service")
 
@app.middleware("http")
async def observe(request, call_next):
    start = time.time()
    response = await call_next(request)
    log.info(f"path={request.url.path} status={response.status_code} "
             f"latency_ms={(time.time()-start)*1000:.0f}")   # to ELK / Loki
    return response
# Also expose /metrics (request counts, latencies, token usage) for the metrics system.
