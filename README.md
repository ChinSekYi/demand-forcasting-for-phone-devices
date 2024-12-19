# Demand forcasting for phone devices in supply chain

## Installation
1. Clone the Repository
    ```
    git clone https://github.com/ChinSekYi/demand-forcasting-for-phone-devices
    cd demand-forcasting-for-phone-devices
    ```

2. Create and activate virtual environment  
    ```
    conda create -n dev python=3.11 
    conda activate dev
    ```
    Using venv:
    ```
    python -m venv dev
    source dev/bin/activate  #On macOS/Linux
    source dev/bin/activate  #On Windows
    ```

3. Install Project Dependencies   
    ```
    make install
    ```

## Makefile Commands
- `make install`: Upgrades `pip` and installs the dependencies listed in `requirements.txt`.

## Usage
Open the following 4 notebooks:
  - For Exploratory Data Analysis, Data Cleaning and Data Preprocessing:
    ```
    jupyter notebook notebook/EDA.ipynb   
    ```
  - For Feature Selection:
    ```
    jupyter notebook notebook/FEATURE_SELECTION.ipynb   
    ```
  - For Model Training and Evaluation:
    ```
    jupyter notebook notebook/MODEL_TRAINING.ipynb   
    ```
  - For data insights report
    ```
    jupyter notebook notebook/DATA_INSIGHTS.ipynb   
    ```