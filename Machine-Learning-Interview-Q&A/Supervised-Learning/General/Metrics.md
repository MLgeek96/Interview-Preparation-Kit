## How to define/select metrics for any trained model?

There isn't a one-size-fits-all metric. The metric(s) chosen to evaluate a machine learning model depends on various factors:

* Is it a regression or classification task?
* What is the business objective? Eg. precision vs recall
* What is the distribution of the target variable?

There are a number of metrics that can be used, including Adjusted R-Squared, Mean Absolute Error (MAE), Mean Squared Error (MSE), accuracy, recall, precision, f1 score, and the list goes on.

## Explain what precision and recall are

Recall attempts to answer "What proportion of actual positives was identified correctly?"

Precision attempts to answer "What proportion of positive identifications was actually correct?"

## Explain what a false positive and a false negative are. Why is it important these from each other? Provide examples when false positives are more important than false negatives, false negatives are more important than false positives and when these two types of errors are equally important

A false positive is an incorrect identification of the presence of a condition when it's absent.

A false negative is an incorrect identification of the absence of a condition when it's actually present.

An example of when false negatives are more important than false positives is when screening for cancer. It's much worse to say that someone doesn't have cancer when they do, instead of saying that someone does and later realizing that they don't.

This is a subjective argument, but false positives can be worse than false negatives from a psychological point of view. For example, a false positive for winning the lottery could be a worse outcome than a false negative because people normally don’t expect to win the lottery anyways.

## Why is mean square error a bad measure of model performance? What would you suggest instead?

Mean Squared Error (MSE) gives a relatively high weight to large errors — therefore, MSE tends to put too much emphasis on large deviations. A more robust alternative is MAE (mean absolute deviation).


