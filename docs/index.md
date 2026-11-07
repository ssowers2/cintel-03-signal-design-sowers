
# Metadata Completeness & Governance Readiness Monitor

Continuous Intelligence | Project 03 | Signal Design

**Author:** Sabriya Sowers
**Date:** 2026 November

## Overview

This project explores how raw data can be transformed into meaningful monitoring signals using Python and Polars.

The instructor's example demonstrates signal design using system performance measurements such as request volumes, errors, and response times.

For my custom project, I plan to apply these same techniques to **Data Governance**, focusing on metadata completeness, data ownership, and documentation quality.

The goal is to develop a **Metadata Completeness & Governance Readiness Monitor** that helps identify gaps in metadata documentation and supports data stewardship activities.

## Data

### Instructor Example Dataset

The example contains 10 observations of system activity.

Each observation includes:

- `requests` - number of requests handled.
- `errors` - number of failed requests.
- `total_latency_ms` - cumulative response time.

[View Example Dataset](https://github.com/ssowers2/cintel-03-signal-design-sowers/blob/main/data/system_metrics.csv)

### Planned Custom Dataset

The custom project will use synthetic metadata records representing data assets across departments within a fictional healthcare organization.

Potential metadata fields include:

- Dataset name.
- Department or business area.
- Assigned data owner.
- Assigned data steward.
- Dataset description.
- Data classification.
- Business definition or documentation status.

This dataset will allow me to explore how calculated signals can identify documentation gaps and areas that may benefit from additional governance support.

## Methods

### Instructor Example Signals

The example pipeline calculates three monitoring signals.

#### Error Rate

Error rate measures the proportion of failed requests.

```python
error_rate = errors / requests
```

#### Average Latency

Average latency estimates response time per request.

```python
avg_latency_ms = total_latency_ms / requests
```

#### Throughput

The example uses the number of requests per observation as its throughput indicator.

```python
throughput = requests
```

The pipeline handles zero-request observations without dividing by zero.


### Part D2: Small Technical Modification — Success Rate

For my small technical experiment, I added a fourth signal,
`success_rate`, to the instructor's original system metrics pipeline.

The purpose was to measure the proportion of successful requests
and provide another perspective on system reliability.

#### Success Rate Calculation

`success_rate = (requests - errors) / requests`

I modified the `design_signals()` function in
`src/cintel/utils_system.py` using Polars and updated the logging
message in `src/cintel/signal_design.py`.

The calculation handles zero-request observations to avoid
division-by-zero errors.

I predicted that records with fewer errors relative to total
requests would have higher success rates.

### Planned Custom Governance Signals

The custom application will adapt these techniques to calculate governance-related metrics.

#### Metadata Completeness Rate

Measures the percentage of required metadata fields that are populated.

```text
metadata_completeness = completed_required_fields / total_required_fields
```

#### Ownership Coverage

Measures the percentage of datasets with an assigned data owner.

```text
ownership_coverage = datasets_with_owner / total_datasets
```

#### Documentation Gaps

Identifies datasets missing important metadata such as descriptions, definitions, or classifications.

#### Governance Readiness Indicator

A derived signal that identifies datasets requiring additional documentation or stewardship attention.

These signals will help transform individual metadata records into information that can support governance decisions.

## Results

### Instructor Example Results

The example demonstrates the following observed ranges:

| Signal | Observed Range |
|---|---|
| Error rate | 0% to 2.5% |
| Average latency | 25.0 to 33.71 ms |
| Requests per observation | 60 to 200 |

The output contains the original system measurements alongside the calculated signals.

[View Signal Results Including D2 Modification](https://github.com/ssowers2/cintel-03-signal-design-sowers/blob/main/artifacts/signals.csv)

### Part D2: Success Rate Experiment Results

The updated pipeline successfully processed all 10 system metric
records and generated a new `success_rate` column in
`artifacts/signals.csv`.

The table below shows selected observations from the experiment.

| Requests | Errors | Error Rate | Success Rate |
|---------:|-------:|-----------:|-------------:|
| 120 | 3 | 2.50% | 97.50% |
| 150 | 2 | 1.33% | 98.67% |
| 200 | 5 | 2.50% | 97.50% |
| 60 | 0 | 0.00% | 100.00% |

Across all 10 observations, success rates ranged from
97.5% to 100%.

The results matched my prediction. Records with lower error
rates had higher success rates.

[View Updated Signal Results](https://github.com/ssowers2/cintel-03-signal-design-sowers/blob/main/artifacts/signals.csv)

### Custom Project Results

The custom project will generate metadata governance signals and comparison results.

Planned outputs include:

- Metadata completeness rates.
- Ownership coverage measurements.
- Documentation gap indicators.
- Department-level comparisons.
- A visualization showing governance readiness.

Actual results and visualizations will be added after the custom pipeline has been implemented and verified.

## Interpretation

### Instructor Example

Error rate provides an indicator of system reliability, while average latency describes responsiveness.

Request counts provide additional context about system activity.

Together, these signals provide a more informative view of system behavior than the raw measurements alone.

### Part D2: Experiment Interpretation

This experiment demonstrated how a new signal can be calculated
from existing measurements without modifying the original data.

While error rate measures failed requests, success rate measures
the proportion of requests completed successfully.

I learned how to extend an existing Polars transformation,
update the pipeline output, and verify the calculated results.

The success-rate signal provides an additional perspective on
system reliability, although it is mathematically related to
the existing error-rate signal.

The experiment also reinforced the importance of validating
changes before committing them to GitHub.

### Planned Governance Application

Metadata completeness and ownership coverage can help identify where data assets may lack sufficient documentation or accountability.

Comparing these signals across departments could help data stewards prioritize improvements and support more consistent metadata management practices.

## Limitations

The instructor's example does not establish acceptable performance thresholds or evaluate changes over time.

Request counts are not normalized by elapsed time, so they represent throughput only when observation intervals are comparable.

For the custom project, the metadata inventory will be synthetic and will not represent actual organizational performance.

Metadata completeness alone does not guarantee that documentation is accurate, useful, or current. The results will need to be interpreted within the context of defined metadata requirements.

The D2 success-rate signal is derived from the same measurements
as error rate, so it provides an alternative perspective rather
than an independent measure of system performance.

## Conclusion

Effective monitoring begins with designing signals that answer meaningful questions.

This project will explore how the same techniques used to monitor system reliability can be applied to Data Governance.

By measuring metadata completeness, ownership coverage, and documentation gaps, the custom application aims to demonstrate how analytics can support data stewardship and organizational governance readiness.

## Documentation Index

- **Home** - this landing page
- [**Project Instructions**](project-instructions.md)
- [**Glossary**](glossary.md)
- [**API**](api.md)
- [**Reactive App**](./app/index.html)

## Project Links

- [GitHub Repository](https://github.com/ssowers2/cintel-03-signal-design-sowers)
- [Hosted Documentation](https://ssowers2.github.io/cintel-03-signal-design-sowers/)
- [Example Pipeline](https://github.com/ssowers2/cintel-03-signal-design-sowers/blob/main/src/cintel/signal_design.py)
- [Results and Artifacts](https://github.com/ssowers2/cintel-03-signal-design-sowers/tree/main/artifacts)
- [Project Instructions](project-instructions.md)

## Project Resources

- [Project Instructions](project-instructions.md)
- [Professional Python Guide](https://denisecase.github.io/pro-analytics-02/)
- [Professional Python Project Explainer](https://pup-pack.github.io/professional-python-project-explainer/)
- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)
