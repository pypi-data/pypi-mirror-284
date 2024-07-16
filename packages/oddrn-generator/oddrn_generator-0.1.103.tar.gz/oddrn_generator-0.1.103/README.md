[![PyPI version](https://badge.fury.io/py/oddrn-generator.svg)](https://badge.fury.io/py/oddrn-generator)

# Open Data Discovery Resource Name Generator

Helps generate oddrn for data sources.

* [Requirements](#requirements)
* [Installation](#installation)
* [Available generators](#available-generators)
* [Generator properties](#generator-properties)
* [Generator methods](#generator-methods)
* [Generator properties](#generator-properties)
* [Example usage](#example-usage)
* [Exceptions](#example-usage)
* [Development](#development)

## Requirements

* __Python >= 3.7__

## Installation

```bash
poetry add oddrn-generator
# or
pip install oddrn-generator
```

## Usage and configuration

### Available generators
| DataSource   | Generator class name  |
|--------------|-----------------------|
| cassandra    | CassandraGenerator    |
| postgresql   | PostgresqlGenerator   |
| mysql        | MysqlGenerator        |
| glue         | GlueGenerator         |
| s3           | S3Generator           |
| kafka        | KafkaGenerator        |
| kafkaconnect | KafkaConnectGenerator |
| snowflake    | SnowflakeGenerator    |
| airflow      | AirflowGenerator      |
| hive         | HiveGenerator         |
| dynamodb     | DynamodbGenerator     |
| odbc         | OdbcGenerator         |
| mssql        | MssqlGenerator        |
| oracle       | OracleGenerator       |
| redshift     | RedshiftGenerator     |
| clickhouse   | ClickHouseGenerator   |
| athena       | AthenaGenerator       |
| quicksight   | QuicksightGenerator   |
| dbt          | DbtGenerator          |
| prefect      | PrefectGenerator      |
| tableau      | TableauGenerator      |
| neo4j        | Neo4jGenerator        |
| mongodb      | MongoGenerator        |
| vertica      | VerticaGenerator      |
| CubeJs       | CubeJsGenerator       |
| superset     | SupersetGenerator     |
| Presto       | PrestoGenerator       |
| Trino        | TrinoGenerator        |
| dms          | DmsGenerator          |
| powerbi      | PowerBiGenerator      |

### Generator properties

* base_oddrn - Get base oddrn (without path)
* available_paths - Get all available path of generator

### Generator methods

* get_oddrn_by_path(path_name, new_value=None) - Get oddrn string by path. You also can set value for this path using '
  new_value' param
* set_oddrn_paths(**kwargs) - Set or update values of oddrn path
* get_data_source_oddrn() - Get data source oddrn

### Generator parameters:

* host_settings: str - optional. Hostname configuration
* cloud_settings: dict - optional. Cloud configuration
* **kwargs - path's name and values

### Example usage

```python
# postgresql
from oddrn_generator import PostgresqlGenerator

oddrn_gen = PostgresqlGenerator(
    host_settings='my.host.com:5432',
    schemas='schema_name', databases='database_name', tables='table_name'
)

print(oddrn_gen.base_oddrn)
# //postgresql/host/my.host.com:5432
print(oddrn_gen.available_paths)
# ('databases', 'schemas', 'tables', 'views', 'tables_columns', 'views_columns', 'relationships')

print(oddrn_gen.get_data_source_oddrn())
# //postgresql/host/my.host.com:5432/databases/database_name

print(oddrn_gen.get_oddrn_by_path("schemas"))
# //postgresql/host/my.host.com:5432/databases/database_name/schemas/schema_name

print(oddrn_gen.get_oddrn_by_path("databases"))
# //postgresql/host/my.host.com:5432/databases/database_name

print(oddrn_gen.get_oddrn_by_path("tables"))
# //postgresql/host/my.host.com:5432/databases/database_name/schemas/schema_name/tables/table_name

# you can set or change path:
oddrn_gen.set_oddrn_paths(tables="another_table_name", tables_columns="new_column_name")
print(oddrn_gen.get_oddrn_by_path("tables_columns"))
# //postgresql/host/my.host.com:5432/databases/database_name/schemas/schema_name/tables/another_table_name/columns/new_column_name

oddrn_gen.set_oddrn_paths(relationships="references_table_2_with_constraint_fk")
print(oddrn_gen.get_oddrn_by_path("relationships"))
# //postgresql/host/my.host.com:5432/databases/database_name/schemas/schema_name/tables/another_table_name/relationships/references_table_2_with_constraint_fk

# you can get path wih new values:
print(oddrn_gen.get_oddrn_by_path("tables_columns", new_value="another_new_column_name"))
# //postgresql/host/my.host.com:5432/databases/database_name/schemas/schema_name/tables/another_table_name/columns/another_new_column_name


# glue
from oddrn_generator import GlueGenerator

oddrn_gen = GlueGenerator(
    cloud_settings={'account': 'acc_id', 'region': 'reg_id'},
    databases='database_name', tables='table_name', columns='column_name',
    jobs='job_name', runs='run_name', owners='owner_name'
)

print(oddrn_gen.available_paths)
# ('databases', 'tables', 'columns', 'owners', 'jobs', 'runs')

print(oddrn_gen.get_oddrn_by_path("databases"))
# //glue/cloud/aws/account/acc_id/region/reg_id/databases/database_name

print(oddrn_gen.get_oddrn_by_path("tables"))
# //glue/cloud/aws/account/acc_id/region/reg_id/databases/database_name/tables/table_name'

print(oddrn_gen.get_oddrn_by_path("columns"))
# //glue/cloud/aws/account/acc_id/region/reg_id/databases/database_name/tables/table_name/columns/column_name

print(oddrn_gen.get_oddrn_by_path("jobs"))
# //glue/cloud/aws/account/acc_id/region/reg_id/jobs/job_name

print(oddrn_gen.get_oddrn_by_path("runs"))
# //glue/cloud/aws/account/acc_id/region/reg_id/jobs/job_name/runs/run_name

print(oddrn_gen.get_oddrn_by_path("owners"))
# //glue/cloud/aws/account/acc_id/region/reg_id/owners/owner_name

```

### Exceptions

* WrongPathOrderException - raises when trying set path that depends on another path

```python
from oddrn_generator import PostgresqlGenerator

oddrn_gen = PostgresqlGenerator(
    host_settings='my.host.com:5432',
    schemas='schema_name', databases='database_name',
    tables_columns='column_without_table'
)
# WrongPathOrderException: 'tables_columns' can not be without 'tables' attribute
```

* EmptyPathValueException - raises when trying to get a path that is not set up

```python
from oddrn_generator import PostgresqlGenerator

oddrn_gen = PostgresqlGenerator(
    host_settings='my.host.com:5432', schemas='schema_name', databases='database_name',
)
oddrn_gen.get_oddrn_by_path("tables")

# EmptyPathValueException: Path 'tables' is not set up
```

* PathDoestExistException - raises when trying to get not existing oddrn path

```python
from oddrn_generator import PostgresqlGenerator

oddrn_gen = PostgresqlGenerator(
    host_settings='my.host.com:5432', schemas='schema_name', databases='database_name',
)
oddrn_gen.get_oddrn_by_path("jobs")

# PathDoestExistException: Path 'jobs' doesn't exist in generator
```

## Development

```bash
#Install dependencies
poetry install

#Activate shell
poetry shell

# Run tests
pytest tests/
```
