# Validation

## Quick Checks

- Run `powershell -ExecutionPolicy Bypass -File .\open_app.ps1 -NoBrowser` to start or reuse the local app server without opening a browser window.
- Run `python tests/test_smoke.py` to confirm the repository structure and headline topic terms are present.
- Open `index.html` locally and verify the protocol, evidence, and WebR controls render.
- Run `powershell -ExecutionPolicy Bypass -File .\generate_release_notes.ps1 -Summary 'Describe the release scope.'` when you need standalone release notes without creating a zip.

## Manual Review Points

- Confirm the app still states the comparison as Amplatzer Amulet versus Watchman FLX.
- Check that the indirectness warning about legacy Watchman comparators is still visible.
- Run `powershell -ExecutionPolicy Bypass -File .\package_release.ps1` when you need a packaged release snapshot and matching release notes under `release/`.
