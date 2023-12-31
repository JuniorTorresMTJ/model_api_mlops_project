# **<p align="center" style="color: #DA1B5D;"><strong>Welcome to Model API MLOps Project</strong></p>**

[![Documentation Status](https://readthedocs.org/projects/model-api-mlops-project/badge/?version=latest)](https://model-api-mlops-project.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/api-mlops-project.svg)](https://badge.fury.io/py/api-mlops-project)


## 💡 **Summary** 

-   [🚀 Run the project](https://github.com/JuniorTorresMTJ/model_api_mlops_project/tree/main#-run-the-project)
-   [📖 Documentation](https://github.com/JuniorTorresMTJ/model_api_mlops_project/tree/main#-documentation)
-   [📑 Overview of Project Technologies](https://github.com/JuniorTorresMTJ/model_api_mlops_project/tree/main#-overview-of-project-technologies)
-   [📝 Next Steps](https://github.com/JuniorTorresMTJ/model_api_mlops_project/tree/main#-next-steps)
-   [💻 CONTACT ME](https://github.com/JuniorTorresMTJ/model_api_mlops_project/tree/main#-contact-me-)

## 🌐 **Overview** 
***

This project aims to apply MLOps techniques to deploy a machine learning model through an API constructed with FastAPI. We utilize Poetry for dependency management and Docker for containerization, ensuring the code is modular, organized 📐, and maintainable 🛠️. Furthermore, this project boasts comprehensive documentation 📄, ensuring clarity and ease of replication for other developers.

### Key Tasks 🔑:

-   Code Modularization and Refactoring: The original script needed an overhaul to reach a modular, and potentially object-oriented, structure 🔄.

-   Documentation: Implementing clear and concise documentation 📚 to ensure smooth navigation and comprehension for fellow developers.

-   Preservation of Output: Despite alterations in the code's structure and logic, the model's predictions (output) ought to remain consistent ✔️.

-   Configuration File Modification: The structure of `artifacts/pipeline.jsonc` was amenable to changes to ensure it meshed seamlessly with the revamped code structure 🔧.

-   Incorporate TODOs: The code housed multiple TODOs that had to be addressed and realized as part of the challenge 📝.

-   Scalability Consideration: The reshaped code was anticipated to cater to hefty data scenarios, suggesting that the supplied sample data file might, in a real-world setting, symbolize a table spanning several gigabytes in a data lake 📊.

### Constraints and Considerations 🚫:

-   The generated code should be portable and capable of executing flawlessly in an alternate Python environment 🐍.

-   The provided "pickle" files were crafted using Python version 3.8.13 and Scikit-learn version 1.0.2. Though other libraries might be pivotal for diverse facets of the project, these particular versions were indispensable for the "pickle" files 📌.

-   Intricate or time-intensive modifications, if not instantly implementable, should be signposted within the code as TODOs. These markers should also sketch out the strategic approach intended for their eventual fulfillment 🕰️.


## 🚀 **Run the project**
***
The provided configuration appears to be from a `pyproject.toml` file, which is a configuration file for the [Poetry](https://python-poetry.org/) dependency management and packaging tool in Python. To install and execute this project, follow the steps below:

- Prerequisites:
- Docker
- Poetry
- Python

### 1️⃣ Install Poetry:
If you haven't installed Poetry yet, you can do so with the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Or you can use other installation methods detailed in the [official documentation](https://python-poetry.org/docs/#installation).

### 2️⃣ Clone the project (if you haven't already):
Assuming the project is hosted on a Git repository, clone it:

```bash
git clone https://github.com/JuniorTorresMTJ/model_api_mlops_project.git
cd api_mlops_project
```

### 3️⃣ Install project dependencies:
Navigate to the project directory and install the dependencies using Poetry:

```bash
poetry install
```

This command installs both the main dependencies and the dev dependencies of the project.

### 4️⃣ Activate the virtual environment:
Poetry creates a virtual environment for your project. Activate it with:

```bash
poetry shell
```

### 5️⃣ Build the Docker image:
The exact command to run the project depends on its structure. Typically, there's a main Python script or module you'd execute to start the project. If there's a clear entry point, you can run:


```bash
docker build -t api-mlops-project:latest .
```

### 6️⃣ Build the Docker image:

```bash
docker run -p 8000:8000 api-mlops-project:latest
```
API should now be running and accessible at http://localhost:8000.

###  Additional tasks:
The provided configuration also contains some tasks defined with `taskipy`. You can run these tasks using the `poetry run task` command. For example:

- To run the lint task: 

```bash
  poetry run task lint
```

- To serve the documentation:

```bash
  poetry run task doc
```

### 7️⃣ Endpoints:


#### ✅ GET /data

-   Purpose:

    -   This endpoint retrieves the original dataset from a predefined file location.
-   Usage:

    -   You simply send a GET request to this endpoint without any parameters.
-   Example with `curl`:

```bash
    curl -X 'GET' http://localhost:8000/data
```
-   Response:

![data](https://github.com/JuniorTorresMTJ/mlops_shape_project/blob/main/docs/assets/img/data.png)

If successful, you'll receive a JSON representation of the dataset. The structure will be a dictionary with columns as keys and their associated data as corresponding values.

* * * * *

#### ✅ POST /process_data

-   Purpose:

    -   Processes data from an uploaded file and returns the processed output.
-   Usage:

    -   Send a POST request to this endpoint with an attached file containing the data you want to process.
-   Example with `curl`:

```bash
    curl -X 'POST' -F 'file=@path_to_your_file.csv' http://localhost:8000/process_data
```
-   Response:

![predict_path](https://github.com/JuniorTorresMTJ/mlops_shape_project/blob/main/docs/assets/img/predict_path.png)

If successful, you'll receive processed data (like predictions) as a JSON response.



#### ✅ POST /predict

-   Purpose:

    -   This endpoint takes input data in the form of a JSON object and returns a prediction based on the provided data.
-   Usage:

    -   Send a POST request with a JSON payload representing the data for which you want a prediction.
-   Example with `curl`:

```bash
    `curl -X 'POST' -H "Content-Type: application/json" -d '{"vibration_x": 45.2947443182, "vibration_y": 91.0739650974, "vibration_z": 10.2298092532}' http://localhost:8000/predict`
```
-   Response:

![predict](https://github.com/JuniorTorresMTJ/mlops_shape_project/blob/main/docs/assets/img/predict.png)

If successful, you'll receive a JSON response with the prediction status and the predicted class.

* * * * *

#### ✅ POST /predict_batch

-   Purpose:

    -   Provides batch predictions based on the provided data.
-   Usage:

    -   Send a POST request with a JSON payload containing multiple rows of data for batch processing.
-   Example with `curl`:

```bash
    curl -X 'POST' -H "Content-Type: application/json" -d '[{"vibration_x": 44.9700689935, "vibration_y": 90.0999391234, "vibration_z": 10.2298092532},{"vibration_x": 45.2947443182, "vibration_y": 91.0739650974, "vibration_z": 10.2298092532},{"vibration_x": 45.9440949675, "vibration_y": 91.0739650974, "vibration_z": 10.2298092532}]' http://localhost:8000/predict_batch
```
-   Response:

![predict_batch](https://github.com/JuniorTorresMTJ/mlops_shape_project/blob/main/docs/assets/img/predict_batch.png)

 If successful, you'll receive a JSON response with the prediction status and the predicted classes for each input data row.


For each of the endpoints, if there's an error, the API will return a clear message indicating what went wrong, along with a status code indicating the nature of the error. Always make sure to check the returned message and status code to understand any issues.


## 📖 **Documentation**:

The documentation of this project is an essential component for understanding its structure, functionalities, and usage guides. We strongly believe that comprehensive documentation can speed up the adoption, contribution, and debugging processes of the project. The documentation was crafted using [MkDocs](https://www.mkdocs.org/), a swift and straightforward tool for creating documentation websites from markdown files. It allows us to concentrate on the content while automating the process of converting Markdown into a structured and styled website.

⚠️[Documentation Link](https://model-api-mlops-project.readthedocs.io/en/latest/)⚠️


## 📑 **Overview of Project Technologies**
***

This section offers a comprehensive understanding of the technologies incorporated into our project, shedding light on each tool in detail. Grasping these technologies is pivotal for any developer or stakeholder aiming to become acquainted with the infrastructure and the project code.

* * * * *

-   [Python](https://www.python.org/) 3.8.10 🐍
    -   Description: Language used for application development.

* * * * *

-   [Poetry](https://python-poetry.org/) 📦
    -   Description: A tool for dependency management and packaging in Python. Poetry provides a streamlined and consistent approach to handle Python projects and their dependencies, ensuring transparency and reproducibility throughout the process.

* * * * *

-   [Scikit-learn](https://scikit-learn.org/stable/) 1.0.2 📊
    -   Description: A machine learning library in Python. Scikit-learn, together with Pandas, stands as an essential tool for data processing, analysis, and the deployment of machine learning models. Both libraries bring forth a vast set of features and are widely recognized in the community.

* * * * *

-   [Pandas](https://pandas.pydata.org/docs/index.html) ^2.0.3 🐼
    -   Description: Used for data reading and transformations.

* * * * *

-   [Blue](https://pypi.org/project/blue/) ^0.9.1 🔵
    -   Description: Coding standard adopted for the project.

* * * * *

-   [isort](https://pycqa.github.io/isort/) ^5.12.0 📑
    -   Description: A coding utility to organize imports in a consistent format.

* * * * *

-   [taskipy](https://pypi.org/project/taskipy/1.0.0/) ^1.11.0 🛠️
    -   Description: Facilitates development by creating tasks.

* * * * *

-   [pyarrow](https://arrow.apache.org/docs/python/index.html) ^12.0.1 🏹
    -   Description: Enables reading of .parquet data files.

* * * * *

-   [Docker](https://hub.docker.com/) 🐳
    -   Description: Docker is a platform designed to develop, ship, and run applications within containers. It ensures our application and its dependencies are packaged into an isolated container, which enhances portability and ease of deployment across varied environments.

* * * * *

Grasping the intricate details of these technologies will significantly augment the efficiency and effectiveness of engagement with the project. 🚀🌟


##  📝 **Next Steps**
***

Here are some next steps that can be implemented in the future:

### 1️⃣ Model Registration in MLflow

Lastly, to track and manage our machine learning model iterations, we will use [MLflow](https://mlflow.org/) to register, version, and share models.


### 2️⃣ Validation with Stakeholders

We plan to conduct several feedback sessions with our stakeholders to ensure the project aligns with the expectations and needs of the end users.

### 3️⃣ Monitoring Setup

Monitoring the performance and functionality of the system is crucial to ensure its reliability and efficiency. It's important to implement tools and processes for keeping an eye on the system.

### 4️⃣ Alert Setup for Slack or Email

To ensure a swift response to any issues that may arise, we'll implement alerts that will send notifications to Slack or predetermined emails in case of system failures.

### 5️⃣ Refactoring of the `dataframe_checker.py` class

Currently, the `dataframe_checker.py` class is responsible for validating input data. Initially, it wasn't built with PySpark, but ideally, its internal logic should be replaced with [PySpark](https://spark.apache.org/docs/latest/api/python/index.html) to optimize validation and preparation of data on large datasets.

### 6️⃣ Scheduling with Airflow

To automate and orchestrate our workflows, we will use [Airflow](https://airflow.apache.org/). It will assist us in defining, scheduling, and monitoring workflows programmatically.


## 💻 **CONTACT ME** 💻
***


 <p align="center">
<a  href="https://www.linkedin.com/in/marivaldotorres/">
    <img align="center"alt="Junior Torres | Linkedin" target="_blank" width="24px" src="https://github.com/JuniorTorresMTJ/model_api_mlops_project/blob/main/docs/assets/linkedin.png" />
  </a>

  <a href="https://www.instagram.com/mlengineer.py/">
    <img align="center" alt="Junior Torres | Instagram" target="_blank" width="24px" src="https://github.com/JuniorTorresMTJ/model_api_mlops_project/blob/main/docs/assets/instagram.png" />
  </a>
  <a href="mailto:juniortorres.mtj@gmail.com">
    <img align="center" alt="Junior Torres | Gmail" target="_blank" width="26px" src="https://github.com/JuniorTorresMTJ/model_api_mlops_project/blob/main/docs/assets/gmail.png" />
  </a>
  <a href="https://github.com/JuniorTorresMTJ">
    <img align="center" alt="Junior Torres | Github" target="_blank" width="26px" src="https://github.com/JuniorTorresMTJ/model_api_mlops_project/blob/main/docs/assets/github.svg" />
  </a>
 </p>