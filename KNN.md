## K Nearest Neighbors Intuition

**K Nearest Neighbors** 🧑‍🦯 is a Supervised Machine Learning Algorithm which helps in both classification and regression tasks. **KNN** algorithm is different from other algorithms like **Linear Regression**, **Logistic Regression**, **Support Vector Machine** tries to create a decision boundary in form of line, plane or some hyperplane but KNN tries to predict the class (target) of new sample on the basis of its surrounding datapoints using **Euclidena**/**Manhattan** Distance. Let's look into it in more detail.

### How KNN is implemented ?? 🤔 💭

Imagine we have a data having features **IMDB ratings**, **Box office collection**, **PG ratings**

|IMDB Ratings|Box Office Collection|PG Ratings|
|------------|---------------------|----------|
|55|10|🟡|
|60|20|🟢|
|57|22|🟡|
|61|17|🟢|
|65|16|🔴|
|69|45|🔴|
|75|32|🟢|
|69|43|🟡|
|..|..|..|
|..|..|..|

and so on 🟢🟡🔴

Here 🟢 is for **PG** rated, 🟡 is for **PG13** rated and 🔴 is for **R** rated. Let's plot the datapoints.

<img src="https://github.com/Hg03/Story-Of-ML/blob/main/assets/ratingplotted.png">

As we can , it's very difficult to draw a decision boundary becuase data is so much random, there **KNN** is very best suited algorithm here. Let's say we encountered a new sample, we'll select some **K** value. Let's say K = 4, therefore we select 4 nearest datapoints from a new sample and check which majority target class those nearest datapoints favours :
1. If 2 datapoints favour 🔴, 1 favours 🟡 and 1 favours 🟢 depicts that new sample belongs to 🔴 class.
2. If 3 datapoints favour 🟡 and 1 favours 🟢 depicts that new sample belongs to 🟡 class.
3. If 2 datapoints favour 🔴, 2 favours 🟡 , then we'll calculate the average distance of 🔴 class as well as for 🟡 class. Then new sample belongs to those class whose class' average is lesser.



