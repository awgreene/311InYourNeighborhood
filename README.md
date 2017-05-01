# 311InYourNeighborhood
In an effort to improve transparency between the local government and its citizens, our team proposes a web solution that uses freely available open-source APIs coupled with Analyze Boston’s datasets to engage citizens and streamline 311 requests.

Our solution will engage citizens by providing them the ability to collaborate in the submission and resolution process for 311 requests in their neighborhood. Our interactive dashboard will show all 311 requests on a map. Users will be able to drill down into each submission and view details about the request, including the problem location, the submission date, any updates, and the eventual resolution. Users will also have the ability to vote on which 311 requests should be prioritized, giving users a voice in how their tax dollars are put to work.

311 requests made through our solution will use available data to recommend which department the request should be filed against. Our solution’s approach will reduce both the time required to submit a 311 request as well as the amount of user input error. As a result of the improved information provided to the 311 database, the city will be better equipped to quickly address requests.

In the future, this solution could be expanded to recognize the user intent using natural language processing. The solution could use these intents to reduce duplicate complaints and better improve the solutions ability streamline the 311 submission processes.

# Special Thank You
Our team would like to thank [Start Bootstrap](http://startbootstrap.com/) for providing the [Heroic Features](http://startbootstrap.com/template-overviews/heroic-features/) template we used to build the frontend portion of our project.

Start Bootstrap was created by and is maintained by **[David Miller](http://davidmiller.io/)**, Owner of [Blackrock Digital](http://blackrockdigital.io/).

* https://twitter.com/davidmillerskt
* https://github.com/davidtmiller

Start Bootstrap is based on the [Bootstrap](http://getbootstrap.com/) framework created by [Mark Otto](https://twitter.com/mdo) and [Jacob Thorton](https://twitter.com/fat).

## Source Code Setup

### 1. Requirements
The backend services are built in python. Once you download the code, you can install the python requirements by

`pip install -r requirements.txt`

### 2. Directory Setup

The python code will need access to some folders for storing prediction results and classifiers. Please make sure that after you have cloned the repo, you create the following directories in the project's home folder

    resources
        -- classifiers 
        -- predictions

that is, a folder named `resources` that contains two folders named `classifiers` and `predictions`

### 3. Running the project

Please run

`python 311.py`

from the project's home directory. This will start the service at `localhost:7080`

### 4. Training the models

Navigate to `http://localhost:7080/static/predictions.html` and hit the `Train` button. The backend code will then create and train Machine Learning classifiers and store them. For now, we will be using 80% of our data for training and 20% for prediction. Once this is done, a message saying `Training Complete` can be seen on the webpage.

### 5. Reviewing the results

Navigate to `http://localhost:7080/static/predictions.html` and hit the `Pull` button. This will pull the results of the predictions and display them in a table. The accuracy score will be displayed beside the Train and Pull buttons. The table will have orange rows where the prediction was inaccurate.
