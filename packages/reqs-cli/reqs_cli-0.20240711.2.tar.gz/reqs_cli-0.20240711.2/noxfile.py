from pathlib import Path

import nox


package_path = Path.cwd()

# NOTE: uv is much faster at creating venvs and generally compatible with pip.
# Pip compat: https://github.com/astral-sh/uv/blob/main/PIP_COMPATIBILITY.md
nox.options.default_venv_backend = 'uv'


@nox.session
def pytest(session: nox.Session):
    session.install('-r', 'requirements/testing.txt')
    session.install('-e', '.')
    session.run(
        'pytest',
        '-ra',
        '--tb=native',
        '--strict-markers',
        '--cov=reqs',
        '--cov-config=.coveragerc',
        '--cov-report=xml',
        '--no-cov-on-fail',
        f'--junit-xml={package_path}/ci/test-reports/{session.name}.pytests.xml',
        'src',
        *session.posargs,
    )


@nox.session
def standards(session: nox.Session):
    session.install('-c', 'requirements/dev.txt', 'pre-commit')
    session.run(
        'pre-commit',
        'run',
        '--all-files',
    )
