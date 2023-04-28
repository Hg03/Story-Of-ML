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



