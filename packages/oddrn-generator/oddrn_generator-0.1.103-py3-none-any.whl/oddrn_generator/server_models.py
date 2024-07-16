from abc import ABC, abstractmethod
from typing import Optional
from urllib.parse import urlparse

from pydantic import BaseModel, field_validator


class HostSettings(BaseModel):
    host: str


class CloudSettings(BaseModel):
    account: str
    region: str


class AzureCloudSettings(BaseModel):
    domain: Optional[str] = None
    account: Optional[str] = None
    container: Optional[str] = None


class GoogleCloudSettings(BaseModel):
    project: str


class S3CustomSettings(BaseModel):
    endpoint: str

    @field_validator("endpoint")
    @classmethod
    def name_must_contain_space(cls, endpoint):
        try:
            parsed = urlparse(endpoint)
            return parsed.hostname
        except Exception as e:
            print(f"Could not parse {endpoint=}")
            return endpoint


class ServerModelConfig(BaseModel):
    host_settings: Optional[HostSettings] = None
    cloud_settings: Optional[CloudSettings] = None
    azure_cloud_settings: Optional[AzureCloudSettings] = None
    s3_custom_cloud_settings: Optional[S3CustomSettings] = None
    google_cloud_settings: Optional[GoogleCloudSettings] = None


class AbstractServerModel(ABC):
    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError

    @classmethod
    def create(cls, config: ServerModelConfig):
        raise NotImplementedError


class HostnameModel(AbstractServerModel, BaseModel):
    host: str

    def __str__(self) -> str:
        return f"host/{self.host}"

    @classmethod
    def create(cls, config: ServerModelConfig):
        host_settings = config.host_settings

        if host_settings:
            return cls(host=host_settings.host)
        else:
            raise ValueError("You must specify host settings")


class AWSCloudModel(AbstractServerModel, BaseModel):
    account: str
    region: str

    def __str__(self) -> str:
        return f"cloud/aws/{'/'.join('{}/{}'.format(*p) for p in self.model_dump().items())}"

    @classmethod
    def create(cls, config: ServerModelConfig):
        cloud_settings = config.cloud_settings

        if cloud_settings:
            return cls(account=cloud_settings.account, region=cloud_settings.region)
        else:
            raise ValueError("You must specify cloud settings")


class AzureDomainCloudModel(AbstractServerModel, BaseModel):
    domain: str

    def __str__(self) -> str:
        return f"cloud/azure/{'/'.join('{}/{}'.format(*p) for p in self.model_dump().items())}"

    @classmethod
    def create(cls, config: ServerModelConfig):
        azure_cloud_settings = config.azure_cloud_settings

        if azure_cloud_settings:
            return cls(domain=azure_cloud_settings.domain)
        else:
            raise ValueError("You must specify cloud settings")


class BlobStorageCloudModel(AbstractServerModel, BaseModel):
    account: str
    container: str

    def __str__(self) -> str:
        return f"cloud/azure/{'/'.join('{}/{}'.format(*p) for p in self.model_dump().items())}"

    @classmethod
    def create(cls, config: ServerModelConfig):
        azure_cloud_settings = config.azure_cloud_settings

        if azure_cloud_settings:
            return cls(
                account=azure_cloud_settings.account,
                container=azure_cloud_settings.container,
            )
        else:
            raise ValueError("You must specify cloud settings")


class S3CustomModel(AbstractServerModel, BaseModel):
    endpoint: str

    def __str__(self) -> str:
        return f"{'/'.join('{}/{}'.format(*p) for p in self.model_dump().items())}"

    @classmethod
    def create(cls, config: ServerModelConfig):
        return cls(endpoint=config.s3_custom_cloud_settings.endpoint)


class S3CloudModel(AbstractServerModel, BaseModel):
    """Bucket name is unique across AWS"""

    def __str__(self) -> str:
        return "cloud/aws"

    @classmethod
    def create(cls, config):
        return cls()


class SQLiteModel(BaseModel):
    @classmethod
    def create(cls, config):
        return cls()


class GCPCloudModel(BaseModel):
    project: str

    def __str__(self) -> str:
        return f"cloud/gcp/project/{self.project}"

    @classmethod
    def create(cls, config: ServerModelConfig):
        gcp_cloud_settings = config.google_cloud_settings

        if gcp_cloud_settings:
            return cls(project=gcp_cloud_settings.project)
        else:
            raise ValueError("You must specify cloud settings")
