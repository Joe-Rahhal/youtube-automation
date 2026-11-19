from config.settings import load_settings


def test_default_settings(monkeypatch):
    monkeypatch.delenv("APP_NAME", raising=False)
    monkeypatch.delenv("APP_ENV", raising=False)
    monkeypatch.delenv("LOG_LEVEL", raising=False)
    monkeypatch.delenv("DRY_RUN", raising=False)

    settings = load_settings()

    assert settings.app_name == "YouTube Automation"
    assert settings.environment == "development"
    assert settings.log_level == "INFO"
    assert settings.dry_run is True
