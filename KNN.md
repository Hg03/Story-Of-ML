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

