https://spark.apache.org/docs/latest/api/python/getting_started/install.html

### Step 0: INIT Working directory
```bash
# TERMINAL 0
ROOT_SPARK="/<path_to_project_streaming>/spark"
mkdir -p "${ROOT_SPARK}"
cd ${ROOT_SPARK}
```


### Step 1: Installation
```bash
# TERMINAL 0
ROOT_SPARK="/<path_to_project_streaming>/spark"
cd "${ROOT_SPARK}"


python -m venv .venv --prompt streaming
source .venv/bin/activate

# Spark SQL
pip install pyspark[sql]

# # pandas API on Spark
# pip install pyspark[pandas_on_spark] plotly  # to plot your data, you can install plotly together.
# # Spark Connect
# pip install pyspark[connect]
```


### Step 2: Execution
```bash
# TERMINAL 0
ROOT_SPARK="/<path_to_project_streaming>/spark"
cd "${ROOT_SPARK}"

bash submit.sh [kafka|console]
```
