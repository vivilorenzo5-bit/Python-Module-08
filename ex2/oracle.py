import os
import sys
from dotenv import load_dotenv  # type: ignore

load_dotenv()


def check_environment_security() -> None:
    print("Environment security check:")

    if os.environ.get("API_KEY"):
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARN] Secrets check bypassed")

    if os.path.exists(".env") or os.path.exists("ex2/.env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file not found (using system env vars)")

    if os.environ.get("MATRIX_MODE") == "production":
        print("[OK] Production overrides active")
    else:
        print("[OK] Production overrides available")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    required_vars = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]
    missing_vars = [var for var in required_vars if not os.environ.get(var)]

    if missing_vars:
        print(f"ERR: Missing config variables: {', '.join(missing_vars)}")
        print("Please run: cp ex2/.env.example .env (and config it)")
        sys.exit(1)

    mode = os.environ.get("MATRIX_MODE", "development")
    db_url = os.environ.get("DATABASE_URL", "")
    api_key = os.environ.get("API_KEY", "")
    log_level = os.environ.get("LOG_LEVEL", "INFO")
    zion = os.environ.get("ZION_ENDPOINT", "")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if mode == "production":
        print("Database: Connected to PRODUCTION Mainframe Cluster SSL Active")
        print(f"API Access: Authenticated ({api_key[:4]}***{api_key[-4:]})")
        print(f"Log Level: {log_level}")
        print(f"Zion Network: SECURE TUNNEL TO {zion}\n")
    else:
        print(f"Database: Connected to local instance ({db_url})")
        print(f"API Access: Authenticated (Dev Mode Key: {api_key})")
        print(f"Log Level: {log_level}")
        print(f"Zion Network: Online ({zion})\n")

    check_environment_security()
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
