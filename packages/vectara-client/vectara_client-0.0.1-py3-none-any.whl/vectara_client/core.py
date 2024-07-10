import logging
import vectara_client
from vectara_client.config import JsonConfigLoader, PathConfigLoader, HomeConfigLoader
from vectara_client.auth import OAuthUtil, ApiKeyUtil
from vectara_client.api import QueriesApi
#from vectara_client.corpus import CorpusManager
from vectara_client.models.app_client import AppClient
from vectara_client.models.create_app_client_request import CreateAppClientRequest
from vectara_client.rest import ApiException
from pprint import pprint
import os


class Client:

    def __init__(self, customer_id: str, queries_api: QueriesApi):
        self.logging = logging.getLogger(self.__class__.__name__)
        logging.info("initializing Client")
        self.customer_id = customer_id
        self.queries_api = queries_api


class Factory():

    def __init__(self, config_path: str = None, config_json: str = None, profile: str = None):
        """
        Initialize our factory using configuration which may either be in a file or serialized in a JSON string

        :param config_path: the file containing our configuration
        :param config_json: the JSON containing our configuration
        """

        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info("initializing builder")
        self.config_path = config_path
        self.config_json = config_json
        self.profile = profile

    def build(self) -> Client:
        """
        Builds our client using the configuration which .
        :return:
        """

        # 1. Load the config whether we're doing file or we've had it passed in as a String.
        if self.config_path:
            self.logger.info("Factory will load configuration from path")
            config_loader = PathConfigLoader(config_path=self.config_path, profile=self.profile)
        elif self.config_json:
            self.logger.info("Factory will load configuration from JSON")
            config_loader = JsonConfigLoader(config_json=self.config_json, profile=self.profile)
        else:
            self.logger.info("Factory will load configuration from home directory")
            config_loader = HomeConfigLoader(profile=self.profile)

        # 2. Parse and validate the client configuration
        try:
            client_config = config_loader.load()
        except Exception as e:
            # Raise a new exception without extra stack trace. We know the JSON failed to parse.
            raise TypeError(f"Unable to build factory due to configuration error: {e}")

        errors = client_config.validate()
        if errors:
            raise TypeError(f"Client configuration is not valid {errors}")

        # 3. Load the validated configuration into our client.
        auth_config = client_config.auth
        auth_type = auth_config.getAuthType()
        logging.info(f"We are processing authentication type [{auth_type}]")

        # Defining the host is optional and defaults to https://api.vectara.io
        # See configuration.py for a list of all supported configuration parameters.
        configuration = vectara_client.Configuration(
            host="https://api.vectara.io"
        )

        if auth_type == "ApiKey":
            auth_util = ApiKeyUtil(client_config.customer_id, client_config.auth.api_key)
            # Configure API key authorization: ApiKeyAuth
            configuration.api_key['ApiKeyAuth'] = client_config.auth.api_key
        elif auth_type == "OAuth2":
            auth_util = OAuthUtil(auth_config.auth_url, auth_config.app_client_id, auth_config.app_client_secret,
                                  client_config.customer_id)
            # TODO: Refactor client to refresh token.
            token = auth_util.getToken()
            configuration.access_token = token
            # configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'
        else:
            raise TypeError(f"Unknown authentication type: {auth_type}")

        # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed

        # Enter a context with an instance of the API client
        api_client = vectara_client.ApiClient(configuration)

        # Create an instance of the API class
        #api_instance = vectara_client.ApplicationClientsApi(api_client)
        #create_app_client_request = vectara_client.CreateAppClientRequest()  # CreateAppClientRequest |  (optional)

        queries_api = QueriesApi(api_client)

        #try:
        #    # Create an App Client
        #    api_response = api_instance.create_app_client(create_app_client_request=create_app_client_request)
        #    print("The response of ApplicationClientsApi->create_app_client:\n")
        #    pprint(api_response)
        #except Exception as e:
        #    print("Exception when calling ApplicationClientsApi->create_app_client: %s\n" % e)

        # TODO Use the type of authentication to validate whether we can enabled the admin service.
        #corpus_manager = CorpusManager(admin_service, indexer_service)

        return Client(client_config.customer_id, queries_api)
