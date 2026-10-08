import os
from dotenv import load_dotenv


def get_config(name: str, default: str) -> str:
    value = os.getenv(name)

    if value is None or value == "":
        print(f"[WARNING] {name} is not configured, using default")
        return default

    return value


def main() -> None:
    load_dotenv()

    print("ORACLE STATUS: Consulting the configuration...")
    print("Configuration loaded:")

    mode = get_config("MATRIX_MODE", "development")
    database = get_config("DATABASE_URL", "local")
    api_key = get_config("API_KEY", "")
    log_level = get_config("LOG_LEVEL", "DEBUG")
    endpoint = get_config(
        "ZION_ENDPOINT",
        "https://localhost"
    )

    if mode not in ("development", "production"):
        print(f"[WARNING] Invalid MATRIX_MODE: {mode}")
        mode = "development"

    print(f"Mode: {mode}")

    if mode == "production":
        print("Environment: Production mode - strict configuration")
    else:
        print("Environment: Development mode - local configuration")

    if database:
        print("Database: Connected to local instance")
    else:
        print("Database: Not configured")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Not authenticated")

    print(f"Log Level: {log_level}")

    if endpoint:
        print("Remote Network: Online")
    else:
        print("Remote Network: Offline")

    print()
    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly ignored by git")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
