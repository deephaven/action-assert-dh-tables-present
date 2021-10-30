# action-assert-dh-tables-present

This action asserts the presence of Deephaven tables with specific names within a running Deephaven instance.

## Parameters

| Parameter | Description | Required |
|--|--|--|
| table-names | A string containing a comma separated list of table names to check. | Yes |
| host | The host name of the Deephaven instance. Defaults to `envoy`. | No |
| project-name | The docker-compose project name to bundle separate docker-compose files | Yes |

## Example

```
- name: Assert Deephaven tables are present
  uses: deephaven/action-assert-dh-tables-present@main
  with:
    table-names: "source,result"
    host: "envoy"
    project-name: test-tables
```
