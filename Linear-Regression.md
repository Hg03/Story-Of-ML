## Linear Regression Intuition 

**Linear Regression** 📈 is a type of **Supervised** Machine Learning model which tries to fit the line ⚟ (in terms of X-Y Plane) or a plane 🛬 (in terms of X-Y-Z Plane) or any higher dimensional linear entity to a data such that It can properly predict the future values. Linear Regression helps to predict the continuous value, hence it is a regression problem.

### How it is implemented 🤔 💭

Imagine you have a data as below

|Year|Price|
|----|-----|
|1985|0.50|
|1986|0.50|
|1987|0.52|
|1988|0.56|
|1989|0.53|
|1990|0.56|
|1991|0.65|
|1992|0.52|
|..|..|
|..|..|
|..|..|

and so on..

We can plot the data as below..

<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/plot_lr.png">

Therefore, On these data points we can plot different lines and react to that one line so that It coincides (intersect) most of the data and that line would be our best fit line.

|1.|2.|3.|
|--|--|--|
|<img src = "https://github.com/Hg03/Story-Of-ML/blob/main/assets/oneline.png">|<img src = "https://github.com/Hg03/Story-Of-ML/blob/main/assets/twolines.png">|<img src = "https://github.com/Hg03/Story-Of-ML/blob/main/assets/morelines.png">|

But But ??

We can't go and draw every possible lines possible because that would be tedious task therefore we'll try to tweak two parameters of line to reach to best fit i.e. **intercept (c)** and **slope (m)**.

As we know, equation of line is defined as 

```math 
y = mx + c
```
where m & c are,

|Intercept (c)|Slope (m)|
|-------------|---------|
|Intercept is defined as a distance of origin from y-axis at where line is intersecting the y-axis|Slope is defined as angle/inclination of line towards x-axis|
|<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/intercept.png">|<img src = "https://github.com/Hg03/Story-Of-ML/blob/main/assets/slope.png">|

So we have to tweak the value of intercept and slope to plot different lines on the datapoints. But how we'll identify that we've reached the best fit line. Now here comes Ordinary Least Square method. The OLS method aims to minimize the sum of square differences between the observed and predicted values. 

Inshort, we have to minimize the distance between actual datapoints and points which are predicted by lines. As in below diagram, see those **white dotted lines**, those are the distance I'm talking about, To be precise, those distances are called error and we have to minimize the error as much as possible to get the best fit line. 

<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/error.png">

First we start with our base line having **m = 0** and **c = 1**, Now we'll calculate the mean of square differences between observed and predicted values. We can call it a cost function.

$$ \sum_{i=1}^{D}(x_i-y_i)^2 / D $$

After getting the cost function, we'll differentiate cost function with respect to **m** as well as with **c** and obtain the next intercept and slope value so that we can plot next line. Doing this process iteratively results in reaching to our best fit line. You can see how the value of intercept and slope is updated as below.

<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/gradient.png"> 

View the plot that how plot of cost function and intercept-slope looks like

<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/gradient-descent.jpg">

Here, 𝛿 is a learning rate, it defines the variability of updation of intercept and slope. For e.g. If learning rate is higher, value of cost function will change with very high margin and if learning rate is lower, value of cost function will change with less margin with slow speed. So selection of learning rate is very essential.

<img src = "https://github.com/Hg03/Story-Of-ML/blob/main/assets/highlowrate.png">

If we've taken data having more independent variables (more than 1), we can fit plane as well as other high dimensional vectors like below :

|Multidimensional Data|Fitting plane into it|
|---------------------|---------------------|
|<img src = "https://github.com/Hg03/Story-Of-ML/blob/assets/plane1.png">
">|<img src = "https://github.com/Hg03/Story-Of-ML/blob/assets/plane2.png">|

