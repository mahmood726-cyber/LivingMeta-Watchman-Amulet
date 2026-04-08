# RapidMeta Cardiology - Watchman FLX vs Amulet

Browser-based living meta-analysis workspace for left atrial appendage occlusion evidence synthesis focused on Amplatzer Amulet versus Watchman FLX.

## Quick Start

1. Run `powershell -ExecutionPolicy Bypass -File .\open_app.ps1` to start the local launcher and open the app.
2. Review the built-in protocol, evidence tables, and validation controls.
3. Run `python tests/test_smoke.py` for a quick repository smoke check.

## Repository Contents

- `index.html`: primary browser application.
- `open_app.ps1`: local browser launcher with static-server support.
- `stop_local_server.ps1`: stops the local launcher server.
- `package_release.ps1`: creates a timestamped release zip under `release/`.
- `generate_release_notes.ps1`: writes timestamped release notes under `release/`.
- `tests/test_smoke.py`: lightweight structural validation.

## Release Hygiene

Use `generate_release_notes.ps1`, `package_release.ps1`, `CITATION.cff`, `.zenodo.json`, and `RELEASE_CHECKLIST.md` when preparing a public release. `package_release.ps1` calls the release-note generator automatically.
