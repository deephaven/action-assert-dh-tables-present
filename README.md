# action-assert-dh-tables-present

This action asserts the presence of Deephaven tables with specific names within a running Deephaven instance.

## Parameters

| Parameter | Description | Required |
|--|--|--|
| table-names | A string containing a comma separated list of table names to check. | Yes |
| host | The host name or IP address of the Deephaven instance. | Yes |
| docker-compose-project-name | The docker-compose project name for the assertion. | Yes |
| max-retries | The number of times to retry connecting to Deephaven before performing the table assertion. | Yes |

## Example

```
- name: Assert Deephaven tables are present
  uses: deephaven/action-assert-dh-tables-present@main
  with:
    table-names: source,result
    host: envoy
    docker-compose-project-name: test-tables
    max-retries: 4
```
