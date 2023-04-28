## Logistic Regression Intuition

**Logistic Regression** 🇸 is an improved version of **Linear Regression** but it's not really deals with a regression problem, it deals with classification problem (binary). Logistic Regression is a Supervised Machine Learning Classification Algorithm (binary) which works on probability 🇨🇶 that if target value is more than 0.5, we'll consider it 1 else 0. Let's look into it in detailed manner ⬇️

### How it is implemented 🤔 💭

Imagine you have a data, where **Distance from goal post** and **Goal** are two columns which depicts the relation of how much distance from goal post leads to goal or not.

⚽⚽⚽⚽
|Distance From Goal Post|Goal|
|-----------------------|----|
|10|1|
|15|1|
|22|1|
|27|0|
|30|1|
|30|0|
|35|1|
|40|0|
|50|0|
|54|0|
|..|..|
|..|..|

and so on ⚽⚽⚽

Here we can see, as the distance increases from goal post, probability of successfull goal decreases (0) and vice versa. If we plot the datapoints on a graph, it looks like as below :

<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/Screenshot%20from%202023-04-28%2019-09-49.png">

As I've told, it's kinda improved version of linear regression, so first fit a best fit line on the datapoints :

<img src = "https://github.com/Hg03/Story-Of-ML/blob/main/assets/fittingline.png">

This is the best possible fit line we can draw, but we can also see it can't able to coincide with all data points. Linear regression model for the classification problem is also sensitive to outliers, it value of **Distance from goal post** is higher, we can also get the negative target value but we need a value ranges from 0 to 1. Therefore sigmoid function here comes into action.

**Linear Regression outputs non probabilities whereas we are interested in probability(ranges from 0 to 1), that is why sigmoid function comes into action**

|Goal|No Goal|
|----|-------|
|<img src = "https://github.com/Hg03/Story-Of-ML/blob/main/assets/goal.png">|<img src = "https://github.com/Hg03/Story-Of-ML/blob/main/assets/nogoal.png">|

Sigmoid function helps the linear function to trim the continuous value to lies in range of 0 to 1, and classifies if value is more than 0.5, goal succeeds ✅ else goal failed ❎ .

1. First we'll fit a line just like linear regression did, but at every step, we'll trim the target value using formula of sigmoid function.

$$ h_ \theta (x) =  \frac{\mathrm{1} }{\mathrm{1} + e^-(mx+c) }  $$

here, first we'll calculate the value of y using equation of linear equation and then put the value in sigmoid function.




