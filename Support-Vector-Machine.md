## Support Vector Machine Intuition

**Support Vector Machine** ⛷️ is a Supervised Machine Learning Classification algorithm which helps to classify different classes (labels) using **hyperplane** ✈️. Support Vector machine mainly chooses the optimal hyperplane with max **margin** distance from **support ⚇ vectors** ⚇. Let's make it more clear below :

### How it is implemented 🤔 💭

Imagine you have a data with 2 classes i.e. blue 🔵 and red 🔴, we will separate these classes using hyperplane. Hyperplane can be one-dimensional (separated by point), two-dimensional plane (separated by line), three-dimensional (separated by plane or circle) or more higher dimensional hyperplane.

|Linearly Separable|Plane Separable|
|------------------|---------------|
|<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/lineseparable.png">|<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/planeseparable.png">|

There are many ways we can create hyperplane to separate classes by varying angle (or we can say **slope**) :- 

1. Try to fit a hyperplane (for now, fit line) that separates two classes (or more).
2. Now create two hyperplanes attached to **support vectors** of each class.
3. Now try to maximize marginal (as you can see the **margin** gap) distance between two support vector attached hyperplanes so that it clearly separates.

**Support Vectors** are those extreme points of each class where the two hyperplanes other than middle hyperplane

<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/hyperplanes.png">

Equation of hyperplane (ho) is defined as :

$$ Wx + b = 0 $$

and equation of other two hyperplanes (h1 & h2) are :

1. h1 - for positive class

$$ Wx + b >= 1 $$

2. h2 - for negative class

$$ Wx + b <=1 $$

Now, the point is that, data in real world is not that much easy to be separated linearly like line, point or plane. Hyperplane can also be non-linear.

<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/nonlinear.png">





