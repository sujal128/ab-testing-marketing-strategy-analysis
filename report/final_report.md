# A/B Testing & Marketing Strategy Analysis

## Executive Summary

This project analyzes the effectiveness of a marketing advertisement campaign using A/B testing. The objective was to determine whether showing advertisements (Ad group) leads to higher conversion rates compared to showing Public Service Announcements (PSA group).

The analysis was conducted on 588,101 users and included exploratory data analysis, statistical hypothesis testing, power analysis, and user segmentation.

---

## Business Problem

A company wants to determine whether its advertising campaign generates more conversions than a control campaign.

### Hypothesis

H0: Conversion rate (Ad) = Conversion rate (PSA)

H1: Conversion rate (Ad) > Conversion rate (PSA)

---

## Dataset Overview

| Metric | Value |
|----------|----------|
| Total Users | 588,101 |
| Ad Group Users | 564,577 |
| PSA Group Users | 23,524 |
| Missing Values | 0 |
| Duplicate Users | 0 |

Features:

- user_id
- test_group
- converted
- total_ads
- most_ads_day
- most_ads_hour

---

## Data Validation

### Sample Ratio Mismatch (SRM) Check

Chi-Square Statistic: 0.0000

P-Value: 0.9998

Conclusion:

No evidence of sample ratio mismatch. Randomization appears valid.

---

## Conversion Analysis

| Group | Users | Conversions | Conversion Rate |
|---------|---------:|---------:|---------:|
| Ad | 564,577 | 14,423 | 2.555% |
| PSA | 23,524 | 420 | 1.785% |

### Improvement

Absolute Lift:

0.770 percentage points

Relative Lift:

43.1%

The advertisement group generated a substantially higher conversion rate than the PSA group.

---

## Statistical Testing

### Two-Proportion Z-Test

Z Statistic: 7.3701

P-Value: 1.705e-13

Decision:

Reject the null hypothesis.

### 95% Confidence Interval

Lower Bound: 0.595%

Upper Bound: 0.943%

Interpretation:

The true conversion uplift from advertising is estimated to lie between 0.595% and 0.943%.

---

## Chi-Square Test

Chi-Square Statistic: 54.0058

P-Value: 1.999e-13

Conclusion:

A statistically significant relationship exists between campaign type and conversion outcome.

---

## Power Analysis

Effect Size: 0.053

Statistical Power: 1.00

Interpretation:

The sample size is more than sufficient to detect the observed effect.

---

## Segmented Analysis

Users were divided into:

- Low Exposure
- Medium Exposure
- High Exposure

### Conversion Rates by Exposure

| Exposure Level | Ad | PSA |
|----------|----------:|----------:|
| Low Exposure | 0.258% | 0.303% |
| Medium Exposure | 0.774% | 0.787% |
| High Exposure | 6.787% | 4.367% |

### Key Insight

The largest performance improvement occurs among highly exposed users.

Advertising delivers the greatest value when users are exposed to a larger number of advertisements.

---

## Business Recommendation

### Recommendation

Roll out the advertising campaign.

### Supporting Evidence

- Ad conversion rate: 2.555%
- PSA conversion rate: 1.785%
- Relative lift: 43.1%
- Statistically significant result (p < 0.001)
- Confidence interval entirely positive
- High statistical power

### Strategic Insight

Future marketing efforts should focus on increasing effective ad exposure while monitoring user fatigue and campaign costs.

---

## Conclusion

The analysis demonstrates that the advertisement campaign significantly outperforms the PSA campaign. Both statistical and practical significance support deploying the advertising strategy at scale.

The strongest gains are observed among highly exposed users, suggesting that optimized ad frequency can further improve business outcomes.