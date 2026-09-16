# Standard Error of Measurement
Script to generate test-retest reliability (absolute repeatability) of a measurement using the standard error of measurement (SEM) and the minimal detectable change (MDC) (Portney, 2020). The UCLA repeated measures exercise dataset ([UCLA Office of Advanced Research Computing, n.d.](https://stats.oarc.ucla.edu/r/seminars/repeated-measures-analysis-with-r/)) is used for demonstration. The SEM and MDC with a 95% confidence interval are obtained through the following equations,

$$\text{SEM} = \sqrt{\text{MS}_E}$$
$$\text{MDC} = 1.96 \cdot \sqrt{2} \cdot \text{SEM}$$

where $\text{MS}_E$ is the residual mean square from repeated measures ANOVA.

Environment setup:

```bash
conda create -n myenv python=3.10
conda activate myenv
```

Dependencies installation:

```bash
pip install -r requirements.txt
```

Usage:

```bash
python sem_repeatability.py
```

Cite As

[Nzakimuena, C. B., Solano, M. M., Marcotte-Collard, R., Lesk, M. R., & Costantino, S. (2025). Spatial and temporal changes in choroid morphology associated with long-duration spaceflight. Investigative Ophthalmology & Visual Science, 66(5), 17-17.](https://doi.org/10.1167/iovs.66.5.17)

### References

1. Portney, L. G. (2020). Foundations of clinical research: applications to evidence-based practice. FA Davis.
1. UCLA Office of Advanced Research Computing. (n.d.). Repeated measures analysis with R. University of California, Los Angeles. Retrieved September 8, 2026, from https://stats.oarc.ucla.edu/r/seminars/repeated-measures-analysis-with-r/
