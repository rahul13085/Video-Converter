import os
BOT_TOKEN = os.environ.get("6803340220:AAHDEwHIDtsu6eflm8a9o6-mKRJ7_1DPbqw")
API_ID = int(os.environ.get("26418113"))
API_HASH = os.environ.get("c0d33dba1c7d9f9d644d4aa13a2e6926")
API_ID = os.environ.get("26418113")
if API_ID:
    try:
        API_ID = int(26418113)
    except (TypeError, ValueError):
        print("Error converting API_ID to integer. Please set a valid integer value for the API_ID environment variable.")
        API_ID = 26418113
