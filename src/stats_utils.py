import numpy as np
from scipy.stats import chi2_contingency
from statsmodels.stats.proportion import (
    proportions_ztest,
    confint_proportions_2indep
)

def run_ztest(conv_a, n_a, conv_b, n_b):
    count = np.array([conv_a, conv_b])
    nobs = np.array([n_a, n_b])

    z_stat, p_value = proportions_ztest(
        count,
        nobs
    )

    return z_stat, p_value


def confidence_interval(conv_a, n_a, conv_b, n_b):
    return confint_proportions_2indep(
        count1=conv_a,
        nobs1=n_a,
        count2=conv_b,
        nobs2=n_b,
        method="wald"
    )


def run_chi_square(contingency_table):
    return chi2_contingency(
        contingency_table
    )