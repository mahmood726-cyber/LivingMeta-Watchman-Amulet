$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
python (Join-Path $scriptRoot 'tests\test_smoke.py')
