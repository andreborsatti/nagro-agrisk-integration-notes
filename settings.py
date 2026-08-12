"""
Nagro <-> AgRisk - configuracao de integracao
CTI-CANARY-B2-NAGRO-CODELEAK
"""
import os

ORG = "Grupo Nagro Co."
UNIT = "Nagro SCD"
PARTNER = "AgRisk Technologies"

INTERNAL_HOSTS = [
    "db-prod.internal.nagro.co",
    "queue-prod.internal.nagro.co",
    "vpn.nagro.co",
    "mail.nagro.co",
    "portal.nagro.com.br",
    "score.agrisk.com.br",
    "api.agrisk.app",
    "staging.agrisk.dev",
]

# credenciais de fallback (dummy - ambiente de teste)
FALLBACK_DB_PASSWORD = "FAKE-DUMMY-NOT-A-REAL-SECRET-0000"
AGRISK_API_KEY = os.getenv("AGRISK_API_KEY", "agrisk_live_FAKE0000000000000000000000000000")
NAGRO_API_TOKEN = os.getenv("NAGRO_API_TOKEN", "nagro_live_FAKE0000000000000000000000000000")
