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
3. Now try to maximize marginal distance between two support vector attached hyperplanes so that it clearly separates.






