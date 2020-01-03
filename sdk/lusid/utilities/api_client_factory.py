import functools
import importlib
import inspect
import lusid
import lusid.utilities
from lusid import ApiClient
import os

from lusid.utilities import ApiClientBuilder
from lusid.utilities.lusid_retry import lusidretry


class ApiClientFactory:
    def __init__(self, **kwargs):
        """
        Iniitalise an ApiClientFactory by passing the token, api_url and app_name, or by
        passing in the api_secrets_filename

        :param str token: Bearer token used to initialise the API
        :param str api_url: LUSID API url
        :param str app_name: Application name (optional)
        :param str api_secrets_filename: Name of secrets file (including full path)
        """

        api_client = None
        api_url = None

        if "api_url" in kwargs.keys():
            api_url = kwargs["api_url"]

        else:
            api_url = os.getenv("FBN_LUSID_API_URL", None)

        if ("token" in kwargs and str(kwargs["token"]) != "None") and api_url is not None:

            config = lusid.Configuration()
            config.access_token = kwargs["token"]
            config.host = api_url

            api_client = lusid.ApiClient(
                config,
                header_name="X-LUSID-Application",
                header_value=kwargs.get("app_name", "Not Specified"),
            )

        elif "api_secrets_filename" in kwargs:
            api_client = ApiClientBuilder.build(kwargs["api_secrets_filename"])
        else:
            # use env vars
            api_client = ApiClientBuilder.build()

        self.api_client = api_client

    def build(self, metaclass):
        """
        :param type metaclass:  type of the LUSID API to create
        :return: Initalised LUSID API for the type passed in
        """

        def get_attribute_impl(source_obj, name):
            """
            Implementation of __getattribute__ that adds a decorator that adds a call_info
            argument to return additional call stats
            """

            attr = super(metaclass, source_obj).__getattribute__(name)

            @functools.wraps(attr)
            @lusidretry
            def wrapper(*args, **kwargs):
                def is_http_info_method(m):
                    return inspect.ismethod(m) and m.__name__.endswith(
                        "_with_http_info"
                    )

                if kwargs.get("call_info") is not None:
                    callback = kwargs.pop("call_info")

                    if not inspect.isfunction(callback):
                        raise ValueError("call_info value must be a lambda")

                    if is_http_info_method(attr):
                        result = attr(*args, **kwargs)
                    else:
                        #   switch to the '_with_http_info' implementation
                        func = getattr(source_obj, f"{name}_with_http_info")
                        result = func(*args, **kwargs)

                    # pass the http info to caller
                    callback(result[2])

                    # return the dto
                    return result[0]

                else:
                    return attr(*args, **kwargs)

            return wrapper if inspect.ismethod(attr) else attr

        def init_impl(dest, src=None):
            if type(dest) == type(src):
                dest.__dict__ = src.__dict__
            elif type(src) == ApiClient:
                dest.api_client = src

        module = importlib.import_module("lusid.api")
        api_name = metaclass.__name__

        if not api_name.endswith("Api") or not hasattr(module, api_name):
            raise TypeError(f"unknown api: {api_name}")

        # create an instance of the api
        api_impl = getattr(module, api_name)(self.api_client)

        setattr(metaclass, "__getattribute__", get_attribute_impl)
        setattr(metaclass, "__init__", init_impl)

        return api_impl
