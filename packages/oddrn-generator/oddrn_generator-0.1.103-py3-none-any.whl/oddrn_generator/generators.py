from typing import Type
from urllib.parse import urlparse

from oddrn_generator.path_models import (
    AirbytePathsModel,
    AirflowPathsModel,
    ApiPathsModel,
    AthenaPathsModel,
    AzureDataFactoryPathsModel,
    AzureSQLPathsModel,
    BasePathsModel,
    BigQueryStoragePathsModel,
    BigTablePathsModel,
    BlobPathsModel,
    CassandraPathsModel,
    CKANPathsModel,
    ClickHousePathsModel,
    CouchbasePathsModel,
    CubeJsPathModel,
    DatabricksFeatureStorePathModel,
    DatabricksLakehousePathModel,
    DatabricksUnityCatalogPathModel,
    DbtPathsModel,
    DmsPathsModel,
    DuckDBPathsModel,
    DynamodbPathsModel,
    ElasticSearchPathsModel,
    FeastPathsModel,
    FilesystemPathModel,
    FivetranPathsModel,
    GCSPathsModel,
    GluePathsModel,
    GreatExpectationsPathsModel,
    HivePathsModel,
    KafkaConnectorPathsModel,
    KafkaPathsModel,
    KinesisPathsModel,
    KubeflowPathsModel,
    LambdaPathsModel,
    MetabasePathModel,
    MongoPathsModel,
    MssqlPathsModel,
    MysqlPathsModel,
    Neo4jPathsModel,
    OdbcPathsModel,
    OraclePathsModel,
    PostgresqlPathsModel,
    PowerBiPathModel,
    PrefectPathsModel,
    PrestoPathsModel,
    QuicksightPathsModel,
    RedashPathsModel,
    RedshiftPathsModel,
    S3CustomPathsModel,
    S3PathsModel,
    SagemakerPathsModel,
    SingleStorePathsModel,
    SnowflakePathsModel,
    SQLitePathsModel,
    SupersetPathsModel,
    TableauPathsModel,
    TarantoolPathsModel,
    VerticaPathsModel,
)
from oddrn_generator.server_models import (
    AbstractServerModel,
    AWSCloudModel,
    AzureCloudSettings,
    AzureDomainCloudModel,
    BlobStorageCloudModel,
    CloudSettings,
    GCPCloudModel,
    GoogleCloudSettings,
    HostnameModel,
    HostSettings,
    S3CloudModel,
    S3CustomModel,
    S3CustomSettings,
    ServerModelConfig,
    SQLiteModel,
)
from oddrn_generator.utils import escape


def parse_url(url: str) -> dict:
    parsed = urlparse(url)
    return {k: v for k, v in parsed._asdict().items() if v}


class Generator:
    source: str = None
    server_model: Type[AbstractServerModel] = None
    paths_model: Type[BasePathsModel] = None

    def __new__(cls, *args, **kwargs):
        # TODO: didn't find any case when kwargs has data_source
        if not kwargs.get("data_source"):
            return super(Generator, cls).__new__(cls)

        # TODO: looks like useless statement
        subclass = {subclass.source: subclass for subclass in cls.__subclasses__()}.get(
            kwargs["data_source"]
        )

        if not subclass:
            raise ValueError("data_source is invalid")

        return super(Generator, subclass).__new__(subclass)

    def __init__(
        self,
        *,
        data_source=None,
        cloud_settings: dict = None,
        azure_cloud_settings: dict = None,
        host_settings: str = None,
        endpoint: str = None,
        google_cloud_settings: dict = None,
        **paths,
    ):
        config = ServerModelConfig(
            cloud_settings=CloudSettings(**cloud_settings) if cloud_settings else None,
            azure_cloud_settings=(
                AzureCloudSettings(**azure_cloud_settings)
                if azure_cloud_settings
                else None
            ),
            host_settings=HostSettings(host=host_settings) if host_settings else None,
            s3_custom_cloud_settings=(
                S3CustomSettings(endpoint=endpoint) if endpoint else None
            ),
            google_cloud_settings=(
                GoogleCloudSettings(**google_cloud_settings)
                if google_cloud_settings
                else None
            ),
        )

        self.server_obj: AbstractServerModel = self.server_model.create(config)
        self.paths_obj: BasePathsModel = self.__build_paths(**paths)

    def __build_paths(self, **paths) -> BasePathsModel:
        escaped = {k: escape(v) for k, v in paths.items()}

        path_obj: BasePathsModel = self.paths_model(**escaped)
        path_obj.validate_all_paths()
        return path_obj

    @property
    def base_oddrn(self) -> str:
        return f"//{self.source}/{self.server_obj}"

    @property
    def available_paths(self) -> tuple:
        return tuple(self.paths_obj.dependencies_map.keys())

    def get_oddrn_by_path(self, path: str, new_value: str = None) -> str:
        dependency = self.paths_obj.get_dependency(path)
        if new_value:
            self.paths_obj.set_path_value(path, new_value)
        else:
            self.paths_obj.check_if_path_is_set(path)
        paths_dict = self.paths_obj.model_dump(
            include=set(dependency), exclude_none=True, by_alias=True
        )
        return (
            f"{self.base_oddrn}/{'/'.join([f'{k}/{v}' for k, v in paths_dict.items()])}"
        )

    def set_oddrn_paths(self, **new_paths) -> None:
        old_paths = {
            k: v
            for k, v in self.paths_obj.model_dump(exclude_none=True).items()
            if k not in list(new_paths.keys())
        }

        self.paths_obj = self.__build_paths(**old_paths, **new_paths)

    def get_data_source_oddrn(self):
        return (
            self.get_oddrn_by_path(self.paths_obj.data_source_path)
            if self.paths_obj.data_source_path
            else self.base_oddrn
        )


class PostgresqlGenerator(Generator):
    source = "postgresql"
    paths_model = PostgresqlPathsModel
    server_model = HostnameModel


class GlueGenerator(Generator):
    source = "glue"
    paths_model = GluePathsModel
    server_model = AWSCloudModel


class MysqlGenerator(Generator):
    source = "mysql"
    paths_model = MysqlPathsModel
    server_model = HostnameModel


class KafkaGenerator(Generator):
    source = "kafka"
    paths_model = KafkaPathsModel
    server_model = HostnameModel


class KafkaConnectGenerator(Generator):
    source = "kafkaconnect"
    paths_model = KafkaConnectorPathsModel
    server_model = HostnameModel


class SnowflakeGenerator(Generator):
    source = "snowflake"
    paths_model = SnowflakePathsModel
    server_model = HostnameModel


class AirflowGenerator(Generator):
    source = "airflow"
    paths_model = AirflowPathsModel
    server_model = HostnameModel


class HiveGenerator(Generator):
    source = "hive"
    paths_model = HivePathsModel
    server_model = HostnameModel


class ElasticSearchGenerator(Generator):
    source = "elasticsearch"
    paths_model = ElasticSearchPathsModel
    server_model = HostnameModel


class FeastGenerator(Generator):
    source = "feast"
    paths_model = FeastPathsModel
    server_model = HostnameModel


class DynamodbGenerator(Generator):
    source = "dynamodb"
    paths_model = DynamodbPathsModel
    server_model = AWSCloudModel


class OdbcGenerator(Generator):
    source = "odbc"
    paths_model = OdbcPathsModel
    server_model = HostnameModel


class MssqlGenerator(Generator):
    source = "mssql"
    paths_model = MssqlPathsModel
    server_model = HostnameModel


class OracleGenerator(Generator):
    source = "oracle"
    paths_model = OraclePathsModel
    server_model = HostnameModel


class PrestoGenerator(Generator):
    source = "presto"
    paths_model = PrestoPathsModel
    server_model = HostnameModel


class TrinoGenerator(PrestoGenerator):
    source = "trino"


class RedshiftGenerator(Generator):
    source = "redshift"
    paths_model = RedshiftPathsModel
    server_model = HostnameModel


class ClickHouseGenerator(Generator):
    source = "clickhouse"
    paths_model = ClickHousePathsModel
    server_model = HostnameModel


class AthenaGenerator(Generator):
    source = "athena"
    paths_model = AthenaPathsModel
    server_model = AWSCloudModel


class QuicksightGenerator(Generator):
    source = "quicksight"
    paths_model = QuicksightPathsModel
    server_model = AWSCloudModel


class DbtGenerator(Generator):
    source = "dbt"
    paths_model = DbtPathsModel
    server_model = HostnameModel


class TableauGenerator(Generator):
    source = "tableau"
    paths_model = TableauPathsModel
    server_model = HostnameModel


class PrefectGenerator(Generator):
    source = "prefect"
    paths_model = PrefectPathsModel
    server_model = HostnameModel


class Neo4jGenerator(Generator):
    source = "neo4j"
    paths_model = Neo4jPathsModel
    server_model = HostnameModel


class S3Generator(Generator):
    source = "s3"
    paths_model = S3PathsModel
    server_model = S3CloudModel

    @classmethod
    def from_s3_url(cls, url: str):
        parsed = urlparse(url)
        bucket = parsed.netloc
        keys = parsed.path.lstrip("/")

        generator = cls(buckets=bucket)
        generator.set_oddrn_paths(keys=keys)

        return generator


class S3CustomGenerator(Generator):
    source = "s3-custom"
    paths_model = S3CustomPathsModel
    server_model = S3CustomModel


class CassandraGenerator(Generator):
    source = "cassandra"
    paths_model = CassandraPathsModel
    server_model = HostnameModel


class ScyllaDBGenerator(CassandraGenerator):
    source = "scylladb"


class SagemakerGenerator(Generator):
    source = "sagemaker"
    paths_model = SagemakerPathsModel
    server_model = AWSCloudModel


class KinesisGenerator(Generator):
    source = "kinesis"
    paths_model = KinesisPathsModel
    server_model = AWSCloudModel


class KubeflowGenerator(Generator):
    source = "kubeflow"
    paths_model = KubeflowPathsModel
    server_model = HostnameModel


class TarantoolGenerator(Generator):
    source = "tarantool"
    paths_model = TarantoolPathsModel
    server_model = HostnameModel


class MongoGenerator(Generator):
    source = "mongo"
    paths_model = MongoPathsModel
    server_model = HostnameModel


class VerticaGenerator(Generator):
    source = "vertica"
    paths_model = VerticaPathsModel
    server_model = HostnameModel


class CubeJsGenerator(Generator):
    source = "cubejs"
    paths_model = CubeJsPathModel
    server_model = HostnameModel


class SupersetGenerator(Generator):
    source = "superset"
    paths_model = SupersetPathsModel
    server_model = HostnameModel


class MetabaseGenerator(Generator):
    source = "metabase"
    paths_model = MetabasePathModel
    server_model = HostnameModel


class DmsGenerator(Generator):
    source = "dms"
    paths_model = DmsPathsModel
    server_model = AWSCloudModel


class PowerBiGenerator(Generator):
    source = "powerbi"
    paths_model = PowerBiPathModel
    server_model = AzureDomainCloudModel


class RedashGenerator(Generator):
    source = "redash"
    paths_model = RedashPathsModel
    server_model = HostnameModel


class AirbyteGenerator(Generator):
    source = "airbyte"
    paths_model = AirbytePathsModel
    server_model = HostnameModel


class FilesystemGenerator(Generator):
    source = "filesystem"
    paths_model = FilesystemPathModel
    server_model = HostnameModel


class GreatExpectationsGenerator(Generator):
    source = "great_expectations"
    paths_model = GreatExpectationsPathsModel
    server_model = HostnameModel


class DatabricksLakehouseGenerator(Generator):
    source = "databricks_lakehouse"
    paths_model = DatabricksLakehousePathModel
    server_model = HostnameModel


class DatabricksUnityCatalogGenerator(Generator):
    source = "databricks_unity_catalog"
    paths_model = DatabricksUnityCatalogPathModel
    server_model = HostnameModel


class DatabricksFeatureStoreGenerator(Generator):
    source = "databricks_feature_store"
    paths_model = DatabricksFeatureStorePathModel
    server_model = HostnameModel


class SingleStoreGenerator(Generator):
    source = "singlestore"
    paths_model = SingleStorePathsModel
    server_model = HostnameModel


class AzureSQLGenerator(Generator):
    source = "azure"
    paths_model = AzureSQLPathsModel
    server_model = HostnameModel


class FivetranGenerator(Generator):
    source = "fivetran"
    paths_model = FivetranPathsModel
    server_model = HostnameModel


class LambdaGenerator(Generator):
    source = "lambda"
    paths_model = LambdaPathsModel
    server_model = AWSCloudModel

    @classmethod
    def from_params(cls, region: str, account: str, function_name: str):
        generator = cls(
            cloud_settings={"region": region, "account": account},
            functions=function_name,
        )
        return generator


class CouchbaseGenerator(Generator):
    source = "couchbase"
    paths_model = CouchbasePathsModel
    server_model = HostnameModel


class SQLiteGenerator(Generator):
    source = "sqlite"
    paths_model = SQLitePathsModel
    server_model = SQLiteModel


class BigTableGenerator(Generator):
    source = "bigtable"
    paths_model = BigTablePathsModel
    server_model = GCPCloudModel


class DuckDBGenerator(Generator):
    source = "duckdb"
    paths_model = DuckDBPathsModel
    server_model = HostnameModel


class GCSGenerator(Generator):
    source = "gcs"
    paths_model = GCSPathsModel
    server_model = GCPCloudModel


class AzureBlobStorageGenerator(Generator):
    source = "blob_storage"
    paths_model = BlobPathsModel
    server_model = BlobStorageCloudModel


class BigQueryStorageGenerator(Generator):
    source = "bigquery_storage"
    paths_model = BigQueryStoragePathsModel
    server_model = GCPCloudModel


class CKANGenerator(Generator):
    source = "ckan"
    paths_model = CKANPathsModel
    server_model = HostnameModel


class AzureDataFactoryGenerator(Generator):
    source = "azure_data_factory"
    paths_model = AzureDataFactoryPathsModel
    server_model = AzureDomainCloudModel


class ApiGenerator(Generator):
    source = "api"
    paths_model = ApiPathsModel
    server_model = HostnameModel
