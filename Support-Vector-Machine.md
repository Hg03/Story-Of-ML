## Support Vector Machine Intuition

**Support Vector Machine** ⛷️ is a Supervised Machine Learning Classification algorithm which helps to classify different classes (labels) using **hyperplane** ✈️. Support Vector machine mainly chooses the optimal hyperplane with max **margin** distance from **support ⚇ vectors** ⚇. Let's make it more clear below :

### How it is implemented 🤔 💭

Imagine you have a data with 2 classes i.e. yellow 🟡 and red 🔴, we will separate these classes using hyperplane. Hyperplane can be one-dimensional (separated by point), two-dimensional plane (separated by line), three-dimensional (separated by plane or circle) or more higher dimensional hyperplane.

|Point Separable|Linearly Separable|Plane Separable|
|---------------|------------------|---------------|
|<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/pointseparable.png">|<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/lineseparable.png">|<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/planeseparable.png">|

In above diagrams, data is only linearly separated, but it's not only the case. Real world data is so much messy so that It can be separated by a non linear hyperplane.

|1.|2.|
|--|--|
|<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/nonlinear.png">|<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/circleseparated.png">|

There are many ways we can create hyperplane to separate classes by varying angle (or we can say **slope**) :- 

1. Try to fit a hyperplane (for now, fit line) that separates two classes (or more).
2. Now create two hyperplanes attached to **support vectors** of each class.
3. Now try to maximize marginal (as you can see the **margin** gap) distance between two support vector attached hyperplanes so that it clearly separates.

<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/hyperplanes.png">


**Support Vectors** are those closest points touching or near to two hyperplanes other than middle one.

<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/sv.png">

Equation of hyperplane (ho) is defined as :

$$ Wx + b = 0 $$

and equation of other two hyperplanes (h1 & h2) are :

1. h1 - for positive class

$$ Wx + b >= 1 $$

2. h2 - for negative class

$$ Wx + b <=1 $$

### How we can calculate the max margin mathematically (Maths 🎃)

1. Create a vector (**w**) perpendicular to hyperplane (**ho**), as we can analyze that any new vector perpendicular to **ho** has a same projection on **w**.
2. Equation of **ho** is represented as 

$$ Wx + b = 0 $$

<img src = "https://github.com/Hg03/Story-Of-ML/blob/main/assets/hoequation.png">

If any new sample results to value more than 0, it lies in positive (or certain other) class, else if any new sample results to value less than 0, it lies in negative class.

<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/two_vectors.png">

3. Now create two vectors more perpendicular to h1 and h2 and get the equation for these vectors which are :

$$ Wx + b = k $$

$$ Wx + b = -k $$

Here k is a constant so we can replace it with 1 for more convenience, therefore

$$ Wx + b = 1 $$

$$ Wx + b = -1 $$

<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/h12equation.png">

4. We've calculated the equations of hyperplanes, let's evaluate the width of margin. For that , introduce two vectors, one on support vector of h1 and another on support vector of h2. Now take difference of both vectors and do the dot product of it with the vector perpendicular to **ho**, Hence width results to 

$$ Simplified Margin Width = 1/2 * |W.W| $$

<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/marginwidth.png">

But, This value of margin width is arbitrarily too large, instead we want near to 1. Therefore we'll optimize the value of margin width using **lagrange multiplier**. To look into more detail, view this amazing [video](https://youtu.be/ny1iZ5A8ilA).

**Overall, if new sample's value lies greater than or equal to 0, it resides in positive class else negative**. In case of multiple features, decision boundary will become more complicated.















