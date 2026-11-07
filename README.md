
# cintel-03-signal-design-sowers

[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](pyproject.toml)
[![CI](https://github.com/ssowers2/cintel-03-signal-design-sowers/actions/workflows/ci-python-zensical.yml/badge.svg)](https://github.com/ssowers2/cintel-03-signal-design-sowers/actions/workflows/ci-python-zensical.yml)
[![Documentation](https://img.shields.io/badge/docs-site-blue?logo=github)](https://ssowers2.github.io/cintel-03-signal-design-sowers/)

[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

> Transform raw data into meaningful monitoring signals to support data governance and informed decision-making.

## Project Overview

**Author:** Sabriya Sowers
**Date:** 2026 November

This project explores signal design for continuous intelligence using Python and Polars.

The goal is to transform raw measurements into meaningful indicators that help identify patterns, monitor performance, and support decision-making.

The instructor's example focuses on system reliability using request volumes, errors, and response times.

For my custom application, I plan to develop a **Metadata Completeness & Governance Readiness Monitor** using a fictional healthcare organization's metadata inventory. The project will focus on measuring metadata completeness, data ownership coverage, and documentation gaps to help identify opportunities for improving data governance practices.

The project is configured in [pyproject.toml](pyproject.toml).

## Data

### Instructor Example

The example uses system metrics from the `data/` directory.

Each observation includes:

- `requests` - number of requests handled.
- `errors` - number of failed requests.
- `total_latency_ms` - total response time in milliseconds.

### Planned Custom Dataset

The custom application will use synthetic metadata records representing data assets across departments in a fictional healthcare organization.

Potential fields include:

- Dataset name and department.
- Assigned data owner and data steward.
- Dataset description.
- Data classification.
- Business definition or documentation status.

Using synthetic data allows the project to demonstrate realistic governance challenges without exposing organizational or sensitive information.

## Approach

The instructor's example uses Polars to calculate derived signals:

- **Error rate** - errors relative to requests.
- **Average latency** - average response time per request.
- **Throughput** - request volume represented in the example.

The planned custom application will adapt these signal design techniques to calculate:

- **Metadata completeness rate** - percentage of required metadata fields completed.
- **Ownership coverage** - percentage of datasets with an assigned owner.
- **Documentation gaps** - missing descriptions, definitions, or other required information.
- **Governance readiness indicators** - calculated measures that help identify assets requiring attention.

Explore these project components:

- [pyproject.toml](pyproject.toml) - project configuration and dependencies.
- [src/cintel/signal_design.py](src/cintel/signal_design.py) - main signal design pipeline.
- [data/](data/) - input measurements and datasets.
- [artifacts/](artifacts/) - generated signals and results.
- [tests/](tests/) - automated tests.
- [.github/workflows/](.github/workflows/) - automated checks and documentation deployment.
- [docs/](docs/) - project documentation.

## Run the Project

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/) to set up your machine and project environment.

From a VS Code terminal in the project root:

```shell
uv run python -m cintel.signal_design
```

## Run the Reactive App

From a VS Code terminal in the project root (press CTRL + C to quit):

```shell
uv run marimo run src/cintel/app.py
```

## Results

The instructor's example pipeline adds calculated signals to the original system measurements and writes the results to:

`artifacts/signals.csv`

The resulting dataset includes the original measurements alongside the derived monitoring signals.

The planned custom application will produce metadata governance metrics that help identify documentation gaps and areas requiring stewardship attention.

Successful execution of the example pipeline produces:

```text
========================
Pipeline executed successfully!
========================
```

A `project.log` file is created in the project root to support debugging and transparency.

Custom project results and visualizations will be documented as the application is developed and verified.

## Verification

Run the automated tests:

```shell
uv run pytest
```

Additional validation will be documented as the custom signals and calculations are implemented.

## Project Documentation

The [hosted documentation site](https://ssowers2.github.io/cintel-03-signal-design-sowers/) is published using Zensical and GitHub Pages.

The documentation site presents the project report, including:

- Data and operational questions.
- Signal calculations and methods.
- Technical modifications.
- Results and visualizations.
- Interpretation and limitations.
- Conclusions.

## CI/CD and GitHub Actions

This project includes continuous integration and continuous deployment (CI/CD) workflows to check project files and publish documentation.

GitHub Actions include:

- [CI: Python and Documentation Checks](https://github.com/ssowers2/cintel-03-signal-design-sowers/actions/workflows/ci-python-zensical.yml)
- [CD: Documentation Deployment](https://github.com/ssowers2/cintel-03-signal-design-sowers/actions/workflows/deploy-zensical.yml)

## Developer Reference

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/) for detailed instructions and troubleshooting.

### Initialize and Update the Python Environment

With the project open in VS Code, open a terminal and run:

```shell
uvx pup-clean --delete
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync
uv audit
```

### Set Up and Run Git Hooks

Set up and run the Git hooks to perform basic checks automatically before changes are pushed to GitHub.

```shell
uvx prek install --force
uvx prek update --freeze --cooldown-days 7

git add -A
uvx prek run --all-files
# Repeat if changes were made
uvx prek run --all-files
```

### Run Common Chores

Run linters, formatters, type checks, tests, and build the documentation.

```shell
uv run ruff check . --fix
uv run ruff format .

uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

### Git Add-Commit-Push to GitHub

After making useful changes, save your work to GitHub.

```shell
git add -A
git commit -m "describe your changes in quotes"
git push -u origin main
```

## Developer Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through previous commands.
- Use `CTRL+F` to find and replace text within a file.

## Developer Tools

This project uses professional Python tools to support development, testing, documentation, and code quality.

- [uv](https://docs.astral.sh/uv/) - Python environments and dependencies.
- [Ruff](https://docs.astral.sh/ruff/) - Python linting and formatting, configured in [.ruff.toml](.ruff.toml).
- [ty](https://docs.astral.sh/ty/) - Python type checking.
- [pytest](https://docs.pytest.org/) - automated Python testing, configured in [.pytest.toml](.pytest.toml).
- [prek](https://prek.j178.dev/) - Git hooks and automated checks, configured in [prek.toml](prek.toml).
- [Zensical](https://zensical.org/) - project documentation, configured in [zensical.toml](zensical.toml).

## Links

- [GitHub Repository](https://github.com/ssowers2/cintel-03-signal-design-sowers)
- [Hosted Documentation](https://ssowers2.github.io/cintel-03-signal-design-sowers/)
- [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
- [Citation](CITATION.cff)
- [License](LICENSE)

### Small Technical Modification — Success Rate Signal

For this experiment, I added a new `success_rate` signal to the
original system metrics pipeline using Python and Polars.

**Purpose:** Measure the proportion of requests completed
successfully, providing another way to evaluate system reliability.

**Calculation:**

success_rate = (requests - errors) / requests

The calculation handles zero requests to avoid division-by-zero errors.

**Prediction:** I expected the new signal to show higher success
rates when fewer requests failed.

**Results:** The updated pipeline successfully generated the
`success_rate` column in `artifacts/signals.csv`. Across the 10
records, success rates ranged from 97.5% to 100%.

**What I learned:** Adding a derived signal can provide another
perspective on existing data without changing the original
measurements.
