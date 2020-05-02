## What is the statistical power?

"Statistical power" refers to the power of a binary hypothesis, which is the probability that the test rejects the null hypothesis given that the alternative hypothesis is true. [1]


## Explain selection bias (with regard to a dataset, not variable selection). Why is it important? How can data management procedures such as missing data handling make it worse?

Selection bias is the phenomenon of selecting individuals, groups or data for analysis in such a way that proper randomization is not achieved, ultimately resulting in a sample that is not representative of the population.

Understanding and identifying selection bias is important because it can significantly skew results and provide false insights about a particular population group.

Types of selection bias include:
* **sampling bias**: a biased sample caused by non-random sampling
* **time interval**: selecting a specific time frame that supports the desired conclusion. e.g. conducting a sales analysis near Christmas.
* **exposure**: includes clinical susceptibility bias, protopathic bias, indication bias. Read more here.
* **data**: includes cherry-picking, suppressing evidence, and the fallacy of incomplete evidence.
* **attrition**: attrition bias is similar to survivorship bias, where only those that 'survived' a long process are included in an analysis, or failure bias, where those that 'failed' are only included
* **observer selection**: related to the Anthropic principle, which is a philosophical consideration that any data we collect about the universe is filtered by the fact that, in order for it to be observable, it must be compatible with the conscious and sapient life that observes it. [2]

Handling missing data can make selection bias worse because different methods impact the data in different ways. For example, if you replace null values with the mean of the data, you adding bias in the sense that you’re assuming that the data is not as spread out as it might actually be.

## Provide a simple example of how an experimental design can help answer a question about behavior. How does experimental data contrast with observational data?

**Observational data** comes from observational studies which are when you observe certain variables and try to determine if there is any correlation.

**Experimental data** comes from experimental studies which are when you control certain variables and hold them constant to determine if there is any causality.

An example of experimental design is the following: split a group up into two. The control group lives their lives normally. The test group is told to drink a glass of wine every night for 30 days. Then research can be conducted to see how wine affects sleep.

## Is mean imputation of missing data acceptable practice? Why or why not?

Mean imputation is the practice of replacing null values in a data set with the mean of the data.

Mean imputation is generally bad practice because it doesn’t take into account feature correlation. For example, imagine we have a table showing age and fitness score and imagine that an eighty-year-old has a missing fitness score. If we took the average fitness score from an age range of 15 to 80, then the eighty-year-old will appear to have a much higher fitness score that he actually should.

Second, mean imputation reduces the variance of the data and increases bias in our data. This leads to a less accurate model and a narrower confidence interval due to a smaller variance.

## What is an outlier? Explain how you might screen for outliers and what would you do if you found them in your dataset. Also, explain what an inlier is and how you might screen for them and what would you do if you found them in your dataset.

An **outlier** is a data point that differs significantly from other observations.

Depending on the cause of the outlier, they can be bad from a machine learning perspective because they can worsen the accuracy of a model. If the outlier is caused by a measurement error, it's important to remove them from the dataset. There are a couple of ways to identify outliers:

* **Z-score/standard deviations**: if we know that 99.7% of data in a data set lie within three standard deviations, then we can calculate the size of one standard deviation, multiply it by 3, and identify the data points that are outside of this range. Likewise, we can calculate the z-score of a given point, and if it’s equal to +/- 3, then it’s an outlier.

Note: that there are a few contingencies that need to be considered when using this method; the data must be normally distributed, this is not applicable for small data sets, and the presence of too many outliers can throw off z-score.

* **Interquartile Range (IQR)**: IQR, the concept used to build boxplots, can also be used to identify outliers. The IQR is equal to the difference between the 3rd quartile and the 1st quartile. You can then identify if a point is an outlier if it is less than Q1–1.5*IRQ or greater than Q3 + 1.5*IQR. This comes to approximately 2.698 standard deviations.

Other methods include DBScan clustering, Isolation Forests, and Robust Random Cut Forests.

An **inlier** is a data observation that lies within the rest of the dataset and is unusual or an error. Since it lies in the dataset, it is typically harder to identify than an outlier and requires external data to identify them. Should you identify any inliers, you can simply remove them from the dataset to address them.

## How do you handle missing data? What imputation techniques do you recommend?

There are several ways to handle missing data:
* Delete rows with missing data
* Mean/Median/Mode imputation
* Assigning a unique value
* Predicting the missing values
* Using an algorithm which supports missing values, like random forests

The best method is to delete rows with missing data as it ensures that no bias or variance is added or removed, and ultimately results in a robust and accurate model. However, this is only recommended if there’s a lot of data to start with and the percentage of missing values is low.

## Explain likely differences between administrative datasets and datasets gathered from experimental studies. What are likely problems encountered with administrative data? How do experimental methods help alleviate these problems? What problem do they bring?

Administrative datasets are typically datasets used by governments or other organizations for non-statistical reasons.

Administrative datasets are usually larger and more cost-efficient than experimental studies. They are also regularly updated assuming that the organization associated with the administrative dataset is active and functioning. At the same time, administrative datasets may not capture all of the data that one may want and may not be in the desired format either. It is also prone to quality issues and missing entries.

## You are compiling a report for user content uploaded every month and notice a spike in uploads in October. In particular, a spike in picture uploads. What might you think is the cause of this, and how would you test it?

There are a number of potential reasons for a spike in photo uploads:

* A new feature may have been implemented in October which involves uploading photos and gained a lot of traction by users. For example, a feature that gives the ability to create photo albums.
* Similarly, it’s possible that the process of uploading photos before was not intuitive and was improved in the month of October.
* There may have been a viral social media movement that involved uploading photos that lasted for all of October. Eg. Movember but something more scalable.
* It’s possible that the spike is due to people posting pictures of themselves in costumes for Halloween.

The method of testing depends on the cause of the spike, but you would conduct hypothesis testing to determine if the inferred cause is the actual cause.


## What is: lift, KPI, robustness, model fitting, design of experiments, 80/20 rule?

**Lift**: lift is a measure of the performance of a targeting model measured against a random choice targeting model; in other words, lift tells you how much better your model is at predicting things than if you had no model.

**KPI**: stands for Key Performance Indicator, which is a measurable metric used to determine how well a company is achieving its business objectives. Eg. error rate.

**Robustness**: generally robustness refers to a system’s ability to handle variability and remain effective.

**Model fitting**: refers to how well a model fits a set of observations.

**Design of experiments**: also known as DOE, it is the design of any task that aims to describe and explain the variation of information under conditions that are hypothesized to reflect the variable. [4] In essence, an experiment aims to predict an outcome based on a change in one or more inputs (independent variables).

**80/20 rule**: also known as the Pareto principle; states that 80% of the effects come from 20% of the causes. Eg. 80% of sales come from 20% of customers.

## Define quality assurance, six sigma.

**Quality assurance**: an activity or set of activities focused on maintaining a desired level of quality by minimizing mistakes and defects.

**Six sigma**: a specific type of quality assurance methodology composed of a set of techniques and tools for process improvement. A six sigma process is one in which 99.99966% of all outcomes are free of defects.

## Give examples of data that does not have a Gaussian distribution, nor log-normal.

* Any type of categorical data won’t have a gaussian distribution or lognormal distribution.

* Exponential distributions — eg. the amount of time that a car battery lasts or the amount of time until an earthquake occurs.

## What is root cause analysis? How to identify a cause vs. a correlation? Give examples

**Root cause analysis**: a method of problem-solving used for identifying the root cause(s) of a problem [3]

**Correlation** measures the relationship between two variables, range from -1 to 1. **Causation** is when a first event appears to have caused a second event. Causation essentially looks at direct relationships while correlation can look at both direct and indirect relationships.

Example: a higher crime rate is associated with higher sales in ice cream in Canada, aka they are positively correlated. However, this doesn’t mean that one causes another. Instead, it’s because both occur more when it’s warmer outside.

You can test for causation using hypothesis testing or A/B testing.

## Give an example where the median is a better measure than the mean

When there are a number of outliers that positively or negatively skew the data.


## What is the Law of Large Numbers?

The **Law of Large Numbers** is a theory that states that as the number of trials increases, the average of the result will become closer to the expected value.

Eg. flipping heads from fair coin 100,000 times should be closer to 0.5 than 100 times.

## How do you calculate the needed sample size?

You can use the margin of error (ME) formula to determine the desired sample size.
ME = t * S/sqrt(n) or ME = z * \sigma/sqrt(n)
* t/z = t/z score used to calculate the confidence interval
* ME = the desired margin of error
* S = sample standard deviation

## When you sample, what bias are you inflicting?

Potential biases include the following:
* Sampling bias: a biased sample caused by non-random sampling
* Under coverage bias: sampling too few observations
* Survivorship bias: error of overlooking observations that did not make it past a form of selection process.

## How do you control for biases?

There are many things that you can do to control and minimize bias. Two common things include **randomization**, where participants are assigned by chance, and **random sampling**, sampling in which each member has an equal probability of being chosen.

## What are confounding variables?

A confounding variable, or a confounder, is a variable that influences both the dependent variable and the independent variable, causing a spurious association, a mathematical relationship in which two or more variables are associated but not causally related.

## What is A/B testing?

A/B testing is a form of hypothesis testing and two-sample hypothesis testing to compare two versions, the control and variant, of a single variable. It is commonly used to improve and optimize user experience and marketing.


## References
[1] Power, Statistics, Wikipedia
[2] Anthropic principle, Wikipedia
[3] Root cause analysis, Wikipedia