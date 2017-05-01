# [Start Bootstrap](http://startbootstrap.com/) - [Heroic Features](http://startbootstrap.com/template-overviews/heroic-features/)

[Heroic Features](http://startbootstrap.com/template-overviews/heroic-features/) is a multipurpose HTML template for [Bootstrap](http://getbootstrap.com/) created by [Start Bootstrap](http://startbootstrap.com/).

## Getting Started

To begin using this template, choose one of the following options to get started:
* [Download the latest release on Start Bootstrap](http://startbootstrap.com/template-overviews/heroic-features/)
* Clone the repo: `git clone https://github.com/BlackrockDigital/startbootstrap-heroic-features.git`
* Fork the repo

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

## Bugs and Issues

Have a bug or an issue with this template? [Open a new issue](https://github.com/BlackrockDigital/startbootstrap-heroic-features/issues) here on GitHub or leave a comment on the [template overview page at Start Bootstrap](http://startbootstrap.com/template-overviews/heroic-features/).

## Creator

Start Bootstrap was created by and is maintained by **[David Miller](http://davidmiller.io/)**, Owner of [Blackrock Digital](http://blackrockdigital.io/).

* https://twitter.com/davidmillerskt
* https://github.com/davidtmiller

Start Bootstrap is based on the [Bootstrap](http://getbootstrap.com/) framework created by [Mark Otto](https://twitter.com/mdo) and [Jacob Thorton](https://twitter.com/fat).

## Copyright and License

Copyright 2013-2016 Blackrock Digital LLC. Code released under the [MIT](https://github.com/BlackrockDigital/startbootstrap-heroic-features/blob/gh-pages/LICENSE) license.