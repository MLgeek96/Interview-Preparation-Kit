## You’re about to get on a plane to Seattle. You want to know if you should bring an umbrella. You call 3 random friends of yours who live there and ask each independently if it’s raining. Each of your friends has a 2/3 chance of telling you the truth and a 1/3 chance of messing with you by lying. All 3 friends tell you that “Yes” it is raining. What is the probability that it’s actually raining in Seattle?

You can tell that this question is related to Bayesian theory because of the last statement which essentially follows the structure, "What is the probability A is true given B is true?" Therefore we need to know the probability of it raining in London on a given day. Let’s assume it’s 25%.

P(A) = probability of it raining = 25%
P(B) = probability of all 3 friends say that it's raining
P(A|B) probability that it’s raining given they're telling that it is raining
P(B|A) probability that all 3 friends say that it's raining given it’s raining = (2/3)³ = 8/27

Step 1: Solve for P(B)
P(A|B) = P(B|A) * P(A) / P(B), can be rewritten as 
P(B) = P(B|A) * P(A) + P(B|not A) * P(not A)
P(B) = (2/3)³ * 0.25 + (1/3)³ * 0.75 = 0.25 * 8/27 + 0.75 * 1/27

Step 2: Solve for P(A|B)
P(A|B) = 0.25 * (8/27) / ( 0.25 * 8/27 + 0.75 * 1/27)
P(A|B) = 8 / (8 + 3) = 8/11

Therefore, if all three friends say that it’s raining, then there’s an 8/11 chance that it’s actually raining.

## There's one box — has 12 black and 12 red cards, 2nd box has 24 black and 24 red; if you want to draw 2 cards at random from one of the 2 boxes, which box has the higher probability of getting the same color? Can you tell intuitively why the 2nd box has a higher probability

The box with 24 red cards and 24 black cards has a higher probability of getting two cards of the same color. Let’s walk through each step.

Let’s say the first card you draw from each deck is a red Ace.

This means that in the deck with 12 reds and 12 blacks, there’s now 11 reds and 12 blacks. 
Therefore your odds of drawing another red are equal to 11/(11+12) or 11/23.

In the deck with 24 reds and 24 blacks, there would then be 23 reds and 24 blacks. Therefore your odds of drawing another red are equal to 23/(23+24) or 23/47.

Since 23/47 > 11/23, the second deck with more cards has a higher probability of getting the same two cards.

## Given two fair dices, what is the probability of getting scores that sum to 4? to 8?

There are 4 combinations of rolling a 4 (1+3, 3+1, 2+2): P(rolling a 4) = 3/36 = 1/12
There are combinations of rolling an 8 (2+6, 6+2, 3+5, 5+3, 4+4): P(rolling an 8) = 5/36

## Infection rates at a hospital above a 1 infection per 100 person-days at risk are considered high. A hospital had 10 infections over the last 1787 person-days at risk. Give the p-value of the correct one-sided test of whether the hospital is below the standard.

Since we looking at the number of events (# of infections) occurring within a given timeframe, this is a Poisson distribution question.

Null (H0): 1 infection per person-days
Alternative (H1): >1 infection per person-days

k (actual) = 10 infections
lambda (theoretical) = (1/100)*1787
p = 0.032372 or 3.2372% calculated using .poisson() in excel or ppois in R

Since p-value < alpha (assuming 5% level of significance), we reject the null and conclude that the hospital is below the standard.

## You roll a biased coin (p(head)=0.8) five times. What’s the probability of getting three or more heads?

Use the General Binomial Probability formula to answer this question:

p = 0.8
n = 5
k = 3,4,5
P(3 or more heads) = P(3 heads) + P(4 heads) + P(5 heads) = 0.94 or 94%

## A random variable X is normal with mean 1020 and a standard deviation 50. Calculate P(X>1200)

Using Excel…
p =1-norm.dist(1200, 1020, 50, true)
p= 0.000159

## Consider the number of people that show up at a bus station is Poisson with mean 2.5/h. What is the probability that at most three people show up in a four hour period?

x = 3
mean = 2.5*4 = 10

using Excel…
p = poisson.dist(3,10,true)
p = 0.010336

## An HIV test has a sensitivity of 99.7% and a specificity of 98.5%. A subject from a population of prevalence 0.1% receives a positive test result. What is the precision of the test (i.e the probability he is HIV positive)?

PV = Prevalence * Sensitivity / (Prevalence * Sensitivity + (1-Prevalence)*(1-Sensitivity)) 

Precision = Positive Predictive Value = PV
PV = (0.001* 0.997)/[(0.001* 0.997)+((1–0.001)*(1–0.985))]
PV = 0.0624 or 6.24%


## You are running for office and your pollster polled hundred people. Sixty of them claimed they will vote for you. Can you relax?

* Assume that there’s only you and one other opponent.
* Also, assume that we want a 95% confidence interval. This gives us a z-score of 1.96.

* p-hat +/- z* sqrt((p-hat * (1-p-hat))/n)

p-hat = 60/100 = 0.6
z* = 1.96
n = 100

This gives us a confidence interval of [50.4,69.6]. Therefore, given a confidence interval of 95%, if you are okay with the worst scenario of tying then you can relax. Otherwise, you cannot relax until you got 61 out of 100 to claim yes.

## Geiger counter records 100 radioactive decays in 5 minutes. Find an approximate 95% interval for the number of decays per hour.

* Since this is a Poisson distribution question, mean = lambda = variance, which also means that standard deviation = square root of the mean
* a 95% confidence interval implies a z score of 1.96
* one standard deviation = 10

Therefore the confidence interval = 12 * 100 +/- 19.6 = [964.8, 1435.2]

## The homicide rate in Scotland fell last year to 99 from 115 the year before. Is this reported change really noteworthy?

* Since this is a Poisson distribution question, mean = lambda = variance, which also means that standard deviation = square root of the mean
* a 95% confidence interval implies a z score of 1.96
* one standard deviation = sqrt(115) = 10.724

Therefore the confidence interval = 115+/- 21.45 = [93.55, 136.45]. Since 99 is within this confidence interval, we can assume that this change is not very noteworthy.

## Consider influenza epidemics for two-parent heterosexual families. Suppose that the probability is 17% that at least one of the parents has contracted the disease. The probability that the father has contracted influenza is 12% while the probability that both the mother and father have contracted the disease is 6%. What is the probability that the mother has contracted influenza?

Using the General Addition Rule in probability:
P(mother or father) = P(mother) + P(father) — P(mother and father)
P(mother) = P(mother or father) + P(mother and father) — P(father)
P(mother) = 0.17 + 0.06–0.12
P(mother) = 0.11

##  Suppose that diastolic blood pressures (DBPs) for men aged 35–44 are normally distributed with a mean of 80 (mm Hg) and a standard deviation of 10. About what is the probability that a random 35–44 year old has a DBP less than 70?

Since 70 is one standard deviation below the mean, take the area of the Gaussian distribution to the left of one standard deviation.
= 2.3 + 13.6 = 15.9%

## In a population of interest, a sample of 9 men yielded a sample average brain volume of 1,100cc and a standard deviation of 30cc. What is a 95% Student’s T confidence interval for the mean brain volume in this new population?

* X-bar +/- t * s / sqrt(n)

Given a confidence level of 95% and degrees of freedom equal to 8, the t-score = 2.306
Confidence interval = 1100 +/- 2.306*(30/3)
Confidence interval = [1076.94, 1123.06]

## A diet pill is given to 9 subjects over six weeks. The average difference in weight (follow up — baseline) is -2 pounds. What would the standard deviation of the difference in weight have to be for the upper endpoint of the 95% T confidence interval to touch 0?

* Upper bound = mean + t-score*(standard deviation/sqrt(sample size))
0 = -2 + 2.306*(s/3)
2 = 2.306 * s / 3
s = 2.601903
Therefore the standard deviation would have to be at least approximately 2.60 for the upper bound of the 95% T confidence interval to touch 0.

## In a study of emergency room waiting times, investigators consider a new and the standard triage systems. To test the systems, administrators selected 20 nights and randomly assigned the new triage system to be used on 10 nights and the standard system on the remaining 10 nights. They calculated the nightly median waiting time (MWT) to see a physician. The average MWT for the new system was 3 hours with a variance of 0.60 while the average MWT for the old system was 5 hours with a variance of 0.68. Consider the 95% confidence interval estimate for the differences of the mean MWT associated with the new system. Assume a constant variance. What is the interval? Subtract in this order (New System — Old System).

* (X1-bar - X2-bar) +/- t * Sp * sqrt(1/n1 + 1/n2)
* SE(X1-bar - X2-bar) = Sp * sqrt(1/n1 + 1/n2)
* Sp = sqrt(((n1-1) * s1² + (n2-1) * s2²)/(n1+n2-2))

Confidence Interval = mean +/- t-score * standard error 
mean = new mean — old mean = 3–5 = -2
t-score = 2.101 given df=18 (20–2) and confidence interval of 95%

standard error = sqrt((0.6² * 9 + 0.68² * 9)/(10+10–2)) * sqrt(1/10+1/10)
standard error = 0.352
confidence interval = [-2.75, -1.25]

## To further test the hospital triage system, administrators selected 200 nights and randomly assigned a new triage system to be used on 100 nights and a standard system on the remaining 100 nights. They calculated the nightly median waiting time (MWT) to see a physician. The average MWT for the new system was 4 hours with a standard deviation of 0.5 hours while the average MWT for the old system was 6 hours with a standard deviation of 2 hours. Consider the hypothesis of a decrease in the mean MWT associated with the new treatment. What does the 95% independent group confidence interval with unequal variances suggest vis a vis this hypothesis? (Because there’s so many observations per group, just use the Z quantile instead of the T.)

* (X1-bar - X2-bar) +/- z * Sp * sqrt(1/n1 + 1/n2)
* SE(X1-bar - X2-bar) = Sp * sqrt(1/n1 + 1/n2)
* Sp = sqrt(((n1-1) * s1² + (n2-1) * s2²)/(n1+n2-2))

Assuming we subtract in this order (New System — Old System):
mean = new mean — old mean = 4–6 = -2
z-score = 1.96 confidence interval of 95%

standard error = sqrt((0.5² * 99 + 2² * 99)/(100+100–2)) * sqrt(1/100+1/100)
standard error = 0.205061
lower bound = -2–1.96*0.205061 = -2.40192
upper bound = -2+1.96*0.205061 = -1.59808
confidence interval = [-2.40192, -1.59808]