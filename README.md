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


## Tools & Libraries

- Mathematical functions from the standard library: [math](https://docs.python.org/3/library/math.html)

- Permutations and combinations: [itertools](https://docs.python.org/3/library/itertools.html)

- Random selections: [random](https://docs.python.org/3/library/random.html)

- Statistical functions: [stats](https://docs.scipy.org/doc/scipy/reference/stats.html)

- For numerical arrays: [Numpy](https://numpy.org/). The fundamental package for scientific computing with Python.

- For plotting: [Metplotlib](https://matplotlib.org/stable/) is a comprehensive library for creating static, animated, and interactive visualizations.

## References & Referencing Style

Code-specific references are included inside the respective code blocks. All other references (such as those for concepts or background information) are listed under each problem in this notebook. The referencing style chosen for this project is MLA: *Author(s). "Title of Web Page." Website Title, Publisher (if different from website title), Date of Publication, URL.* 


## Assessment Problems 
The official assessment can be found [here](https://github.com/ianmcloughlin/applied-statistics/tree/main/assessment).

The notebook addresses the following four problems. All code, visualizations, reported results, and interpretations are included within the problems.ipynb file.


### Problem 1: Extending the Lady Tasting Tea

This problem requires a simulation-based approach to hypothesis testing.

    Task: Extend the classic Lady Tasting Tea experiment from 8 cups (4:4) to 12 cups (8 tea-first and 4 milk-first).

    Simulation Goal: Estimate the probability of the participant correctly identifying all cups by chance.

    Analysis: Compare this probability to the original 8-cup experiment's probability. Discuss the implications of this new probability on setting the p-value threshold.

**References:** \
"The Lady Tasting Tea Experiment – A Classic of Modern Statistics." Statistics Easily, Accessed 14 Dec. 2025, statisticseasily.com/lady-tasting-tea/. \
lryan30. "problems.ipynb." applied_statistics, GitHub, Accessed 14 Dec. 2025, https://github.com/lryan30/applied_statistics/blob/main/problems.ipynb. \
Salsburg, David. "The Lady Tasting Tea." [The Lady Tasting Tea: How Statistics Revolutionized Science in the Twentieth Century], dlsun.github.io/ds-seminar/readings/LadyTastingTea-HypothesisTesting.pdf. Accessed 14 Dec. 2025.

### Problem 2: Normal Distribution and Standard Deviation

This problem explores the concept of bias in standard deviation estimation (Bessel's Correction).

    Task: Generate 100,000 samples (size n=10) from the standard normal distribution.

    Calculation: Compute the standard deviation for each sample using both ddof=1 (sample SD) and ddof=0 (population SD).

    Visualization: Plot the two resulting distributions as histograms on the same axes with transparency.

    Analysis: Describe the visual differences. Explain how the differences are expected to change if the sample size (n) were increased (i.e., how the bias changes).

**References:** \
lryan30. "problems.ipynb." applied_statistics, GitHub, Accessed 14 Dec. 2025, https://github.com/lryan30/applied_statistics/blob/main/problems.ipynb.


### Problem 3: t-Tests and Type II Error

This problem involves simulating the power of the t-test and measuring the Type II error rate.

    Task: For mean differences d=0.0,0.1,0.2,…,1.0, simulate 1,000 independent samples t-tests (sample size n=100).

    Metric: Record the proportion of times the null hypothesis is not rejected (this is the Type II Error rate, β).

    Visualization: Plot the recorded proportion (β) against the mean difference (d).

    Analysis: Explain how the Type II error rate changes as the difference in means increases.

**References:** \
Berberyan, Toros, et al. "9.2: t-Test for the Difference Between Two Means." Statistics C1000: Introduction to Statistics, LibreTexts, 21 Aug. 2025, stats.libretexts.org/Courses/Citrus_College/Statistics_C1000%3A_Introduction_to_Statistics/09%3A_Hypothesis_Testing_for_Two_Samples/9.02%3A__t-Test_for_the_Difference_Between_Two_Means. \
Bhandari, Pritha. "Type I and Type II Errors | Differences, Examples, Visualizations." Scribbr, 22 June 2023, www.scribbr.com/statistics/type-i-and-type-ii-errors/. \
Grimm, Taylor. "Hypothesis Testing: Error Types and Power." 16 July 2024, trgrimm.github.io/posts/2024/07/error-types/. \
Chugani, Vinod. "Understanding Type I and Type II Errors in Statistics." Statology, 9 Jan. 2025, www.statology.org/understanding-type-errors/.

### Problem 4: ANOVA vs. Multiple t-Tests

This problem contrasts two methods for comparing multiple group means.

    Task: Generate three independent samples (n=30) from normal distributions with means 0, 0.5, and 1 (all SD=1).

    Tests:

        Perform a one-way ANOVA on the three samples.

        Perform three independent two-sample t-tests (1 vs 2, 1 vs 3, 2 vs 3).

    Analysis: Compare the conclusions reached by the ANOVA and the multiple t-tests. Write a short note explaining why ANOVA is the preferred method over running several independent t-tests in this scenario (addressing the family-wise error rate).

**References:** \
Benjamini, Yoav, and Yosef Hochberg. "Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing." Journal of the Royal Statistical Society: Series B (Methodological), vol. 57, no. 1, 1995, pp. 289-300, https://www.math.tau.ac.il/~ybenja/MyPapers/benjamini_hochberg1995.pdf. \
Frost, Jim. "Family-Wise Error Rate." Statistics By Jim, statisticsbyjim.com, Accessed 13 Dec. 2025, https://statisticsbyjim.com/glossary/family-wise-error-rate/. \
Frost, Jim. "What is the Bonferroni Correction and How to Use It." Statistics By Jim, statisticsbyjim.com, Accessed 13 Dec. 2025, https://statisticsbyjim.com/hypothesis-testing/bonferroni-correction/. \
Frost, Jim. "Using Post Hoc Tests with ANOVA." Statistics By Jim, statisticsbyjim.com, Accessed 13 Dec. 2025, https://statisticsbyjim.com/anova/post-hoc-tests-anova/. \
Frost, Jim. "Tukey-Kramer Test." Statistics By Jim, statisticsbyjim.com, Accessed 13 Dec. 2025, https://statisticsbyjim.com/glossary/tukey-kramer-test/.

