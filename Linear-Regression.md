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
