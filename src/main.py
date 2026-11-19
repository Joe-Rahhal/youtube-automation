from datetime import datetime, timezone

from config.settings import load_settings
from src.logger import configure_logging, get_logger


def main() -> None:
    """Run the YouTube automation application."""

    settings = load_settings()
    configure_logging(settings.log_level)

    logger = get_logger(__name__)

    now = datetime.now(timezone.utc)

    logger.info("=" * 50)
    logger.info("Application: %s", settings.app_name)
    logger.info("Environment: %s", settings.environment)
    logger.info("Execution time (UTC): %s", now.isoformat())
    logger.info("Dry run: %s", settings.dry_run)
    logger.info("Status: Application started successfully")
    logger.info("Pipeline: Not implemented yet")
    logger.info("=" * 50)


if __name__ == "__main__":
    main()
