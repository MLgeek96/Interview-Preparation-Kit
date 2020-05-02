## Assume you need to generate a predictive model using multiple regression. Explain how you intend to validate this model.

There are two main ways that you can do this:

A) Adjusted R-squared

R Squared is a measurement that tells you to what extent the proportion of variance in the dependent variable is explained by the variance in the independent variables. In simpler terms, while the coefficients estimate trends, R-squared represents the scatter around the line of best fit.

However, every additional independent variable added to a model always increases the R-squared value — therefore, a model with several independent variables may seem to be a better fit even if it isn't. This is where adjusted R² comes in. The adjusted R² compensates for each additional independent variable and only increases if each given variable improves the model above what is possible by probability. This is important since we are creating a multiple regression model.

B) Cross-Validation

A method common to most people is cross-validation, splitting the data into two sets: training and testing data. 

## What are the drawbacks of a linear model?

There are a couple of drawbacks of a linear model:

* A linear model holds some strong assumptions that may not be true in application. It assumes a linear relationship, multivariate normality, no or little multicollinearity, no auto-correlation, and homoscedasticity
* A linear model can’t be used for discrete or binary outcomes.
* You can’t vary the model flexibility of a linear model.

## What are the assumptions required for linear regression? What if some of these assumptions are violated?

The assumptions are as follows:

* The sample data used to fit the model is representative of the population
* The relationship between X and the mean of Y is linear
* The variance of the residual is the same for any value of X (homoscedasticity)
* Observations are independent of each other
* For any value of X, Y is normally distributed.

Extreme violations of these assumptions will make the results redundant. Small violations of these assumptions will result in a greater bias or variance of the estimate.

## What is collinearity and what to do with it? How to remove multicollinearity?

Multicollinearity exists when an independent variable is highly correlated with another independent variable in a multiple regression equation. This can be problematic because it undermines the statistical significance of an independent variable.

You could use the Variance Inflation Factors (VIF) to determine if there is any multicollinearity between independent variables — a standard benchmark is that if the VIF is greater than 5 then multicollinearity exists.


## How to check if the regression model fits the data well?

There are a couple of metrics that you can use:

* R-squared/Adjusted R-squared: Relative measure of fit. This was explained in a previous answer
* F1 Score: Evaluates the null hypothesis that all regression coefficients are equal to zero vs the alternative hypothesis that at least one doesn’t equal zero
* RMSE: Absolute measure of fit.
