Q1. What is a kernel? Explain the kernel trick.

```
A kernel is a way of computing the dot product of two vectors 𝐱x and 𝐲y in some (possibly very high dimensional) feature space, which is why kernel functions are sometimes called "generalized dot product".

The kernel trick is a method of using a linear classifier to solve a non-linear problem by transforming linearly inseparable data to linearly separable ones in a higher dimension.
```

Q2. Is it beneficial to perform dimensionality reduction before fitting an SVM? Why or why not?

```
When the number of features is greater than the number of observations, then performing dimensionality reduction will generally improve the SVM.
```