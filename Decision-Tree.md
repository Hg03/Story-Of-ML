## Decision Tree Intuition

**Decision Tree** 🌳 is very popular Supervised Machine Learning Algorithm which creates tree and every node is known as **Decision node** or **Condition node** and leaf node results to predicting the target class (or any continuous value). This algorithm can be used both for regression and classification tasks. Let's look into it that how Decision Tree is built :

### How it is implemented ?? 🤔 ☁️

**Terminology -**
1. **Root Node** - It represents entire population or sample and it further gets divided into sub-nodes. It is the initial node of a tree.
2. **Splitting** - It is a process of dividing a node into further sub nodes.
3. **Decision Node** - When sub-nodes splits into a further sub nodes, it is decision nodes.
4. **Leaf/Terminal Node** - When node is pure or it can't be split further.
5. **Pruning** - When we remove sub-nodes , this process is known as pruning of decision tree.

<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/terminologies.png">

Imagine we have a data

|Size|Color|Class|
|----|-----|-----|
|1|yellow|⬤|
|2|red|▲|
|.|.|.|
|.|.|.|
|.|.|.|
|1.5|red|⬤|
|3|yellow|▲|
|3.5|yellow|⬤|

Now how we can choose condition or to be precise, decision tree to start building decision tree. Some conditions can be like :

<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/conditions.png">

and there are different conditions we can think about, how to choose optimal condition to start on ❗❗❗. Here **Information Gain** and **Gini Impurity**.

**Information Gain 🚩** defines the quality of split of nodes in further decision nodes. So when we have to choose the best split condition, we use this. We'll iterate through every splitting condtions and calculates their information gain, split which has **information gain** becomes the best split 🫶.

### How Information Gain is calculated : Information gain is the difference of **Gini Impurity** of parent node and weighted average of **Gini impurities** of both splitted nodes. 

Now what is **Gini Impurity** 🤔

Gini Impurity simply determines the purity of node. Purity of node means how random that decision node is filled with different target class. If decision node has only 1 class filled, means it is pure hence value of Gini Impurity is 1 , if decision node is filled half half with only 2 classes , value is 0.5 and it varies then.

**Formula of Gini Impurity** :

$$ \sum_{i=1}^{n} p(i) \times (1 - p(i)) $$

<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/gini.png">

