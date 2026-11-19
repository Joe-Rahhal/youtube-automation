import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str
    environment: str
    log_level: str
    dry_run: bool


def load_settings() -> Settings:
    """Load application settings from environment variables."""

    return Settings(
        app_name=os.getenv(
            "APP_NAME",
            "YouTube Automation",
        ),
        environment=os.getenv(
            "APP_ENV",
            "development",
        ),
        log_level=os.getenv(
            "LOG_LEVEL",
            "INFO",
        ).upper(),
        dry_run=os.getenv(
            "DRY_RUN",
            "true",
        ).lower() in ("true", "1", "yes"),
    )
