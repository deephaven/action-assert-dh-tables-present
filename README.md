# action-assert-dh-tables-present

This action asserts the presence of Deephaven tables with specific names within a running Deephaven instance.

## Parameters

| Parameter | Description | Required |
|--|--|--|
| table-names | A string containing a comma separated list of table names to check. | Yes |
| host | The host name or IP address of the Deephaven instance. | Yes |
| max-retries | The number of times to retry connecting to Deephaven before performing the table assertion. Defaults to 5. | No |
| session-type | The Deephaven session type. Defaults to `python`. | No |

## Example

```
- name: Assert Deephaven tables are present
  uses: deephaven/action-assert-dh-tables-present@main
  with:
    table-names: source,result
    host: envoy
    max-retries: 4
    session-type: python
```

## License

Licensed under the Apache License, Version 2.0
