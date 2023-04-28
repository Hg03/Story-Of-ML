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

<img src = "https://github.com/Hg03/Story-Of-ML/blob/main/assets/negativevalue.png">

**Linear Regression outputs non probabilities whereas we are interested in probability(ranges from 0 to 1), that is why sigmoid function comes into action**

|Goal|No Goal|
|----|-------|
|<img src = "https://github.com/Hg03/Story-Of-ML/blob/main/assets/goal.png">|<img src = "https://github.com/Hg03/Story-Of-ML/blob/main/assets/nogoal.png">|

Sigmoid function helps the linear function to trim the continuous value to lies in range of 0 to 1, and classifies if value is more than 0.5, goal succeeds ✅ else goal failed ❎ .

1. First we'll fit a line just like linear regression did, but at every step, we'll trim the target value using formula of sigmoid function.

$$ h_ \theta (x) =  \frac{\mathrm{1} }{\mathrm{1} + e^-(mx+c) }  $$

here, first we'll calculate the value of y using equation of linear equation and then put the value in sigmoid function. Let's see how it looks by trimming the continous value in a probability model :

<img src = "https://github.com/Hg03/Story-Of-ML/blob/main/assets/sigmoid.png">

Here we can see, applying sigmoid function results in coinciding with many datapoints and becomes very confident to predict the future datapoints. In below diagram, we can see as distance is lesser than 20 - 25, goal succeeds ✅ and if distance is greater than 30, goal failed ❎.

<img src = "https://github.com/Hg03/Story-Of-ML/blob/main/assets/goalnogoal.png">

but but , distance ranges from 25 to 30, we got a line means it can't accurately predicts it is goal or not. Therefore here comes the training part, more data we train our model on , less spread this line would be.

|If model is more confident, decision boundary is narrow|If model is less confident, decision boundary is wide|
|-------------------------------------------------------|-----------------------------------------------------|
|<img src = "https://github.com/Hg03/Story-Of-ML/blob/main/assets/narrow.png">|<img src = "https://github.com/Hg03/Story-Of-ML/blob/main/assets/wide.png">|






