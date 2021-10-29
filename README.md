# action-assert-dh-tables-present

This action validates the presence of Deephaven tables within a workflow.

## Parameters

| Parameter | Description | Required |
|--|--|--|
| table-names | A string containing a comma separated list of table names to check. | Yes |
| host | The host name of the Deephaven instance. Defaults to `localhost`. | No |
| project-name | The docker-compose project name to bundle separate docker-compose files | Yes |

## Example

```
- name: Validate tables
  uses: deephaven/action-assert-dh-tables-present@main
  with:
    table-names: "source,result"
    host: "envoy"
    project-name: test-tables
```
