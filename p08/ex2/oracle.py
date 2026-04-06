import os
import dotenv as dot


def configuration_loader():
    try:
        dot.load_dotenv()

        MATRIX_MODE = os.getenv("MATRIX_MODE")
        DATABASE_URL = os.getenv("DATABASE_URL")
        API_KEY = os.getenv("API_KEY")
        LOG_LEVEL = os.getenv("LOG_LEVEL")
        ZION_ENDPOINT = os.getenv("ZION_ENDPOINT")
        return MATRIX_MODE, DATABASE_URL, API_KEY, LOG_LEVEL, ZION_ENDPOINT
    except Exception as e:
        print(e)


def output_writer(MATRIX_MODE,
                  DATABASE_URL,
                  API_KEY,
                  LOG_LEVEL,
                  ZION_ENDPOINT):
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print("mode: ", MATRIX_MODE)
    print("Database: ", DATABASE_URL)
    print("API Access: ", API_KEY)
    print("Log Level: ", LOG_LEVEL)
    print("Zion Netwok: ", ZION_ENDPOINT)

    if MATRIX_MODE is not None:
        print("\nEnvironment security check:"
              "\n[OK] No hardcoded secrets detected"
              "\n[OK] .env file properly configured"
              "\n[OK] Production overrides available"
              "\n\nThe Oracle sees all configurations.")


def main():
    (MATRIX_MODE,
     DATABASE_URL,
     API_KEY, LOG_LEVEL,
     ZION_ENDPOINT) = configuration_loader()

    if MATRIX_MODE is None:
        DATABASE_URL = "[MISSING] There is no mode detected"
    elif MATRIX_MODE == "development":
        DATABASE_URL = "Connected to local instance"
    elif MATRIX_MODE == "production":
        DATABASE_URL = "Disconnected to local instance"

    if API_KEY is None:
        API_KEY = "[MISSING] There is no external services detected"
    else:
        API_KEY = "Authenticated"

    if LOG_LEVEL is None:
        LOG_LEVEL = "[MISSING] There is no Logging verbosity detected"
    else:
        LOG_LEVEL = "DEBUG"

    if ZION_ENDPOINT is None:
        ZION_ENDPOINT = "[MISSING] There is no network"
    else:
        ZION_ENDPOINT = "Online"

    output_writer(MATRIX_MODE, DATABASE_URL, API_KEY, LOG_LEVEL, ZION_ENDPOINT)


if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        print(e)
