# Alloy Python SDK (AI generated)

This is a library to interact with Alloy's APIs. This library supports [Alloy Embedded](https://runalloy.com/embedded/).

## Documentation

Visit the [Alloy Docs site](https://docs.runalloy.com/docs) for more information on how to get started with Alloy APIs.

<!-- Start SDK Installation [installation] -->

## SDK Installation

You can install the SDK by cloning this repo or running

```bash
pip3 install git+https://github.com/onedebos/alloy-python-sdk-ai.git [--break-system-packages]
```

<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->

## SDK Example Usage

### Example

```python
import alloypythonsdk
from alloypythonsdk.models import operations

s = alloypythonsdk.AlloyPythonSDK(
    api_key="bearer <YOUR_API_KEY_HERE>",
)


res = s.update_a_user(user_id='<value>', request_body=operations.UpdateAUserRequestBody())

if res.object is not None:
    # handle response
    pass

```

<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->

## Available Resources and Operations

### [AlloyPythonSDK](docs/sdks/alloypythonsdk/README.md)

- [update_a_user](docs/sdks/alloypythonsdk/README.md#update_a_user) - Update a user
- [get_a_user](docs/sdks/alloypythonsdk/README.md#get_a_user) - Retrieve a single user
- [delete_a_user](docs/sdks/alloypythonsdk/README.md#delete_a_user) - Delete a user
- [create_a_user](docs/sdks/alloypythonsdk/README.md#create_a_user) - Create a user
- [list_all_users](docs/sdks/alloypythonsdk/README.md#list_all_users) - Retrieve a list of all users
- [create_a_credential](docs/sdks/alloypythonsdk/README.md#create_a_credential) - Create Credential
- [get_credential_metadata](docs/sdks/alloypythonsdk/README.md#get_credential_metadata) - Retrieve all credential structures
- [generate_jwt_token](docs/sdks/alloypythonsdk/README.md#generate_jwt_token) - Generate a new JWT for a user
- [list_user_credentials](docs/sdks/alloypythonsdk/README.md#list_user_credentials) - Retrieve all credentials for a user
- [list_workflows](docs/sdks/alloypythonsdk/README.md#list_workflows) - Retrieve a list of workflows
- [deactivate_a_workflow](docs/sdks/alloypythonsdk/README.md#deactivate_a_workflow) - Deactivate a workflow
- [activate_a_workflow](docs/sdks/alloypythonsdk/README.md#activate_a_workflow) - Activate a workflow
- [get_workflow_analytics](docs/sdks/alloypythonsdk/README.md#get_workflow_analytics) - Retrieve usage metrics for a workflow
- [disable_all_workflows_for_a_user](docs/sdks/alloypythonsdk/README.md#disable_all_workflows_for_a_user) - Deactivate workflows for a user
- [get_workflow_logs](docs/sdks/alloypythonsdk/README.md#get_workflow_logs) - Retrieve all execution logs for a workflow
- [get_workflow_errors](docs/sdks/alloypythonsdk/README.md#get_workflow_errors) - Retrieve all error logs for a workflow
- [delete_logs_for_a_user](docs/sdks/alloypythonsdk/README.md#delete_logs_for_a_user) - Delete all logs for a user
- [delete_a_credential](docs/sdks/alloypythonsdk/README.md#delete_a_credential) - Delete a Credential for a user
- [run_event](docs/sdks/alloypythonsdk/README.md#run_event) - Trigger an event for a user
- [rerun_workfow](docs/sdks/alloypythonsdk/README.md#rerun_workfow) - Rerun a single workflow execution
- [run_workflow](docs/sdks/alloypythonsdk/README.md#run_workflow) - Run Workflow
- [list_apps](docs/sdks/alloypythonsdk/README.md#list_apps) - Retrieve all supported apps
- [list_integrations](docs/sdks/alloypythonsdk/README.md#list_integrations) - Retrieve a list of all integrations
- [batch_create_users](docs/sdks/alloypythonsdk/README.md#batch_create_users) - Create a batch of users
- [list_events](docs/sdks/alloypythonsdk/README.md#list_events) - Retrieve a list of custom events
- [generate_alloy_link](docs/sdks/alloypythonsdk/README.md#generate_alloy_link) - Create an Embedded link for an integration
- [generate_oauth_link](docs/sdks/alloypythonsdk/README.md#generate_oauth_link) - Create OAuth Link
- [delete_workflow](docs/sdks/alloypythonsdk/README.md#delete_workflow) - Delete a workflow
- [find_a_workflow](docs/sdks/alloypythonsdk/README.md#find_a_workflow) - Retrieve a single workflow
- [get_an_integration](docs/sdks/alloypythonsdk/README.md#get_an_integration) - Retrieve a single integration
- [list_users_by_workflowid](docs/sdks/alloypythonsdk/README.md#list_users_by_workflowid) - List Users by workflowId
- [upgrade_workflow](docs/sdks/alloypythonsdk/README.md#upgrade_workflow) - Upgrade a workflow
- [list_versions](docs/sdks/alloypythonsdk/README.md#list_versions) - Retrieve a list of workflow versions
- [credential_medata_by_app](docs/sdks/alloypythonsdk/README.md#credential_medata_by_app) - Retrieve credential structure for an app
- [start_installation](docs/sdks/alloypythonsdk/README.md#start_installation) - Start Installation
- [complete_installation](docs/sdks/alloypythonsdk/README.md#complete_installation) - Complete Installation
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->

## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an error. If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                   | Status Code | Content Type     |
| ------------------------------ | ----------- | ---------------- |
| errors.UpdateAUserResponseBody | 401         | application/json |
| errors.SDKError                | 4xx-5xx     | _/_              |

### Example

```python
import alloypythonsdk
from alloypythonsdk.models import errors, operations

s = alloypythonsdk.AlloyPythonSDK(
    api_key="bearer <YOUR_API_KEY_HERE>",
)

res = None
try:
    res = s.update_a_user(user_id='<value>', request_body=operations.UpdateAUserRequestBody())

except errors.UpdateAUserResponseBody as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.object is not None:
    # handle response
    pass

```

<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->

## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                                   | Variables |
| --- | ---------------------------------------- | --------- |
| 0   | `https://embedded.runalloy.com/2024-03/` | None      |

#### Example

```python
import alloypythonsdk
from alloypythonsdk.models import operations

s = alloypythonsdk.AlloyPythonSDK(
    server_idx=0,
    api_key="bearer <YOUR_API_KEY_HERE>",
)


res = s.update_a_user(user_id='<value>', request_body=operations.UpdateAUserRequestBody())

if res.object is not None:
    # handle response
    pass

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:

```python
import alloypythonsdk
from alloypythonsdk.models import operations

s = alloypythonsdk.AlloyPythonSDK(
    server_url="https://embedded.runalloy.com/2024-03/",
    api_key="bearer <YOUR_API_KEY_HERE>",
)


res = s.update_a_user(user_id='<value>', request_body=operations.UpdateAUserRequestBody())

if res.object is not None:
    # handle response
    pass

```

<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->

## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library. In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:

```python
import alloypythonsdk
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = alloypythonsdk.AlloyPythonSDK(client=http_client)
```

<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->

## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type   | Scheme  |
| --------- | ------ | ------- |
| `api_key` | apiKey | API key |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:

```python
import alloypythonsdk
from alloypythonsdk.models import operations

s = alloypythonsdk.AlloyPythonSDK(
    api_key="bearer <YOUR_API_KEY_HERE>",
)


res = s.update_a_user(user_id='<value>', request_body=operations.UpdateAUserRequestBody())

if res.object is not None:
    # handle response
    pass

```

<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

This repository includes components generated by [Speakeasy](https://www.speakeasyapi.dev/) based on [this OpenAPI spec](https://github.com/onedebos/alloy-openapi-spec), as well as human authored code that simplifies usage.

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
