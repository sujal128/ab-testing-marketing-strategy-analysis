# A/B Testing & Marketing Strategy Analysis — Final Report

**Prepared by:** Sujal Singh
**Dataset:** Marketing A/B Testing (588,101 users)

---

## 1. The Question We're Actually Answering

A marketing team wants to know if their ad campaign is worth the spend, or if they're just paying to show ads to people who would've converted anyway. That's the real question behind every A/B test like this — not "did conversions go up," but "did *the ads* cause it, and is the effect big enough to act on."

Here, the company ran two groups: one saw the actual ad campaign (564,577 users), the other saw a public service announcement instead (23,524 users) — a neutral placeholder ad that doesn't promote the product. That PSA group is the control. It's a smart setup, because it isolates the effect of *this specific ad*, not just "seeing any ad at all."

**Hypotheses:**
- H0: Ad exposure has no effect on conversion rate (Ad conversion rate = PSA conversion rate)
- H1: Ad exposure changes conversion rate

**Significance threshold:** α = 0.05

**Test used:** Two-proportion z-test. This isn't a t-test problem — we're not comparing two averages of a continuous number, we're comparing two proportions (converted vs. not, in each group). Using a t-test here is the single most common mistake I see in A/B testing writeups, so it's worth stating explicitly that this was a deliberate choice, not a default.

---

## 2. Before Trusting Any Result, I Checked If the Test Was Even Valid

This is the step most people skip, and it's the one I'd defend hardest if asked about it in an interview.

If the 564,577 / 23,524 split happened by accident — say, a bug in the randomization that pushed more users into one bucket than intended — then nothing downstream matters, because the comparison itself is broken. So before looking at conversion rates at all, I ran a Sample Ratio Mismatch check: a chi-square goodness-of-fit test comparing the actual group sizes against what they should be.

**Result:** χ² = 0.0000, p = 0.9998

That p-value sitting almost exactly at 1.0 isn't a coincidence — it's exactly what you want to see. It means the split lines up with what was intended, no hidden bias in how users got bucketed. I also checked for missing values and duplicate users — zero of each. Clean dataset, valid randomization. Green light to move forward.

If this check had failed, the honest move would've been to stop here and flag the randomization process for investigation, not push ahead and report a misleading result. That's the difference between running a test and actually trusting one.

---

## 3. What Actually Happened

| Group | Users | Conversions | Conversion Rate |
|---|---|---|---|
| Ad | 564,577 | 14,423 | 2.555% |
| PSA | 23,524 | 420 | 1.785% |

On the surface, that's a 0.77 percentage point gap — small in absolute terms, but a **43.1% relative lift**. That distinction matters: a jump from 1.785% to 2.555% sounds unremarkable until you frame it as "almost half again as many people converted." Both framings are true. I'm including both because whichever one a stakeholder hears first tends to anchor how big they think the effect is, and I'd rather hand over both numbers than let someone pick the flattering one.

---

## 4. Is This Real, or Just Noise?

Two-proportion z-test:

| Metric | Value |
|---|---|
| Z statistic | 7.3701 |
| p-value | 1.705 × 10⁻¹³ |

That p-value is not a typo — it's genuinely that small. With 588K users, even a modest difference in conversion rate becomes statistically obvious very fast. **Reject the null.** The ads are doing something.

I also ran a chi-square test of independence as a second check (campaign type vs. conversion outcome), partly to confirm the z-test result, partly because it's good practice not to lean on a single test when the sample is this large:

| Metric | Value |
|---|---|
| χ² statistic | 54.0058 |
| p-value | 1.999 × 10⁻¹³ |

Same conclusion, different angle. Good — that's the kind of agreement that makes a result easy to defend rather than something I'd hedge on.

**95% Confidence Interval for the lift:** 0.595% – 0.943%

This is the number I'd actually put in front of a decision-maker, more than the p-value. The p-value tells you the effect is real; the confidence interval tells you how big it probably is. Even at the low end of that range, you're still looking at a meaningful lift — the interval doesn't come anywhere close to crossing zero.

**Statistical power:** 1.00 (effect size ≈ 0.053)

With this sample size, if there were *any* meaningful difference between groups, this test was essentially guaranteed to catch it. Worth saying directly: a result this clean is partly a function of having 588K users, not just a function of the ad being amazing. A smaller company running the same test on 5,000 users might not see a result this crisp even with the same true effect — sample size buys you certainty, it doesn't manufacture the effect itself.

---

## 5. The Part of the Data That Actually Changes the Recommendation

This is where I think the analysis gets more interesting than "ads work, ship it." I broke conversion rate down by how many ads each user was actually exposed to:

| Exposure Level | Ad Conversion | PSA Conversion |
|---|---|---|
| Low | 0.258% | 0.303% |
| Medium | 0.774% | 0.787% |
| High | 6.787% | 4.367% |

Look at the low and medium rows first — Ad and PSA are basically tied, and PSA is actually *slightly* ahead in both. The entire 43.1% lift we calculated earlier isn't spread evenly across the user base. It's almost entirely coming from the high-exposure segment, where Ad pulls meaningfully ahead of PSA (6.79% vs 4.37%).

That changes what "deploy the ad campaign" should actually mean. If I'd stopped at the headline z-test result, the natural recommendation is "run more ads, broadly." But the segmented view says something more specific: the campaign isn't really moving people who see it once or twice — it's working on people who see it repeatedly. That's a frequency/retargeting story, not a reach story.

---

## 6. Recommendation

**Don't read this as "the campaign works, scale it everywhere."** Read it as: the campaign works specifically for users who get enough exposure to it, and that's the lever worth pulling.

**What I'd actually tell the marketing team:**

1. **Keep the campaign running** — the lift is real, statistically solid, and the confidence interval doesn't get close to zero even in the worst case.
2. **Don't optimize for reach, optimize for frequency.** Spreading the same budget thinner across more low-exposure users is likely to underperform compared to concentrating spend on getting existing high-intent users to a higher exposure threshold.
3. **Treat the low/medium exposure result as a flag, not a footnote.** Those segments show no real advantage over the PSA — meaning a chunk of current ad spend may be going to users who were never going to be moved by it. Worth investigating whether that spend could be reallocated rather than assumed to be working just because the topline number is positive.
4. **Next test:** rather than re-running the same Ad vs. PSA comparison, I'd test exposure thresholds directly — e.g., capped-frequency ad delivery vs. uncapped — to find the point where additional exposure stops paying off. Right now we know "more exposure = more lift" trends upward, but we don't know where it plateaus, and that's the number that actually informs a budget decision.

**Caveat worth stating plainly:** this dataset doesn't include cost-per-impression or campaign spend, so everything above is about whether the ad changes behavior — not whether it's profitable. A 43% relative lift that costs more to achieve than the converted users are worth wouldn't be worth shipping, and that's a separate calculation this dataset can't answer on its own.

---

## Tech Notes

Two-proportion z-test and chi-square test via `statsmodels` / `scipy.stats`. Power analysis via `statsmodels.stats.power`. Full code in `notebooks/` and `src/stats_utils.py`.
