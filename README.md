<img src="https://studenthub.atu.ie/assets/ATU_Logo.fa93bf0a.svg" alt="ATU Logo" width="300" height="100">


# Applied-Statistics
Repository for the Applied Statistics module.


This repository contains the Jupyter Notebook (problems.ipynb) for the module assessment, which focuses on applying foundational statistical concepts using Python and NumPy.

The assessment requires the application of simulation techniques and statistical tests to solve four distinct problems. Please refer to the requirements.txt file to ensure your environment is set up correctly before running the notebook.


## Repository Structure

- problems.ipynb: The primary document where all problem solutions, simulations, code, visualizations, and required explanations/interpretations are developed progressively in line with the syllabus and serves as the basis for the module assessment. The final version will be published no later than December 21st.

- Roughwork/: A folder intended for drafts, exploratory work, and informal notes generated during the development process.

- requirements.txt: Lists all necessary Python packages and versions to ensure the reproducibility of the code.

- README.md

## Assessment Problems 
The official assessment can be found [here](https://github.com/ianmcloughlin/applied-statistics/tree/main/assessment)

The notebook addresses the following four problems. All code, visualizations, reported results, and interpretations must be included within the problems.ipynb file.

### Problem 1: Extending the Lady Tasting Tea

This problem requires a simulation-based approach to hypothesis testing.

    Task: Extend the classic Lady Tasting Tea experiment from 8 cups (4:4) to 12 cups (8 tea-first and 4 milk-first).

    Simulation Goal: Estimate the probability of the participant correctly identifying all cups by chance.

    Analysis: Compare this probability to the original 8-cup experiment's probability. Discuss the implications of this new probability on setting the p-value threshold.

### Problem 2: Normal Distribution and Standard Deviation

This problem explores the concept of bias in standard deviation estimation (Bessel's Correction).

    Task: Generate 100,000 samples (size n=10) from the standard normal distribution.

    Calculation: Compute the standard deviation for each sample using both ddof=1 (sample SD) and ddof=0 (population SD).

    Visualization: Plot the two resulting distributions as histograms on the same axes with transparency.

    Analysis: Describe the visual differences. Explain how the differences are expected to change if the sample size (n) were increased (i.e., how the bias changes).

### Problem 3: t-Tests and Type II Error

This problem involves simulating the power of the t-test and measuring the Type II error rate.

    Task: For mean differences d=0.0,0.1,0.2,…,1.0, simulate 1,000 independent samples t-tests (sample size n=100).

    Metric: Record the proportion of times the null hypothesis is not rejected (this is the Type II Error rate, β).

    Visualization: Plot the recorded proportion (β) against the mean difference (d).

    Analysis: Explain how the Type II error rate changes as the difference in means increases.

### Problem 4: ANOVA vs. Multiple t-Tests

This problem contrasts two methods for comparing multiple group means.

    Task: Generate three independent samples (n=30) from normal distributions with means 0, 0.5, and 1 (all SD=1).

    Tests:

        Perform a one-way ANOVA on the three samples.

        Perform three independent two-sample t-tests (1 vs 2, 1 vs 3, 2 vs 3).

    Analysis: Compare the conclusions reached by the ANOVA and the multiple t-tests. Write a short note explaining why ANOVA is the preferred method over running several independent t-tests in this scenario (addressing the family-wise error rate).

