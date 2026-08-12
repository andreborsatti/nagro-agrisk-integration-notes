"""
SGC - configuracao de integracao Nagro <-> AgRisk
CTI-CANARY-B2-NAGRO-CODELEAK
"""
import os

ORG = "Grupo Nagro Co."
UNIT = "Nagro SCD"
PARTNER = "AgRisk Technologies"

INTERNAL_HOSTS = [
    "db-prod-sgc.internal.nagro.co",
    "queue-prod.internal.nagro.co",
    "vpn.nagro.co",
    "mail.nagro.co",
    "score.agrisk.com.br",
]

# credenciais de fallback (dummy - ambiente de teste)
FALLBACK_DB_PASSWORD = "FAKE-DUMMY-NOT-A-REAL-SECRET-0000"
AGRISK_API_KEY = os.getenv("AGRISK_API_KEY", "agrisk_live_FAKE0000000000000000000000000000")

FUNDOS = ["GHIR", "Kanastra", "Oikofus"]
