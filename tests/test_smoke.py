from pathlib import Path
import sys


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    required = (
        "index.html",
        "open_app.ps1",
        "stop_local_server.ps1",
        "package_release.ps1",
        "generate_release_notes.ps1",
    )
    missing = [name for name in required if not (root / name).exists()]
    if missing:
        print("Missing required files:", ", ".join(missing))
        return 1

    target = root / "index.html"

    html = target.read_text(encoding="utf-8", errors="ignore")
    checks = {
        "Watchman": "watchman" in html.lower(),
        "Amulet": "amulet" in html.lower(),
        "title": "<title>" in html.lower(),
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        print("Smoke check failed:", ", ".join(failed))
        return 1

    print("test_smoke.py: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
