<h1 align="center">
  DCS CLI v0.3.0
</h1>

> SDK for DataChecks


## Installation

> Python version `>=3.9,<3.12`

```bash

$ pip install dcs-cli[all-dbs]

```

## Available Commands



|    Option     | Short Option | Required |     Default     |                    Description                     |                                             Example                                              |
| :-----------: | :----------: | :------: | :-------------: | :------------------------------------------------: | :----------------------------------------------------------------------------------------------: |
| --config-path |      -C      | **Yes**  |      None       |    Specify the file path for the configuration     |                    dcs_cli run --config-path config.yaml --compare comp_name                     |
|   --compare   |              | **Yes**  |      None       | Run only specific comparison using comparison name |                    dcs_cli run --config-path config.yaml --compare comp_name                     |
|  --save-json  |      -j      |    No    |      False      |           Save the data into a JSON file           |              dcs_cli run --config-path config.yaml --compare comp_name --save-json               |
|  --json-path  |     -jp      |    No    | dcs_report.json |        Specify the file path for JSON file         |   dcs_cli run --config-path config.yaml --compare comp_name --save-json --json-path ouput.json   |
|    --stats    |              |    No    |      False      |            Print stats about data diff             |                dcs_cli run --config-path config.yaml --compare comp_name --stats                 |
|  --send-data  |              |    No    |      False      |                Send Data to server                 |              dcs_cli run --config-path config.yaml --compare comp_name --send-data               |
| --html-report |              |    No    |      False      |                 Save table as HTML                 |             dcs_cli run --config-path config.yaml --compare comp_name --html-report              |
| --report-path |              |    No    | dcs_report.html |       Specify the file path for HTML report        | dcs_cli run --config-path config.yaml --compare comp_name --html-report --report-path table.html |



### Example Command [CLI]

```sh
$ dcs_cli --version

$ dcs_cli --help

$ dcs_cli run -C example.yaml --compare comparison_one --stats -j -jp output.json --html-report --report-path result.html --send-data
```

<details>
<summary><h2>Example Configuration</h2></summary>

```yml
data_sources:
  - name: iris_snowflake
    type: snowflake
    connection:
      account: bp54281.central-india.azure
      username: username
      password: password
      database: TEST_DCS
      schema: PUBLIC
      warehouse: compute_wh
      role: accountadmin

  - name: pgsql_1
    type: postgres
    connection:
      host: localhost
      port: 5432
      username: postgres
      password: password
      database: dvdrental

  - name: pgsql_2
    type: postgres
    connection:
      host: localhost
      port: 5432
      username: postgres
      password: password
      database: dvdrental2

  - name: pgsql_3
    type: postgres
    connection:
      host: localhost
      schema: public
      port: 5432
      username: postgres
      password: password
      database: dc

  - name: pgsql_4
    type: postgres
    connection:
      host: localhost
      schema: test_schema #default schema is public
      port: 5432
      username: postgres
      password: password
      database: dc

  - name: qk_file1
    type: file
    file_path: "nk.kyc_data/SOURCE_EMPLOYEE_FILE.csv"

  - name: qk_file_raw
    type: file
    file_path: "nk.kyc_data/RAW_EMPLOYEE.csv"

  - name: qk_file1_tl
    type: file
    file_path: "nk.kyc_data/TL_EMPLOYEE.csv"

comparisons:
  # FLATFILE TO SNOWFLAKE
  comparison_one:
    source:
      data_source: qk_file1
      table: SOURCE_EMPLOYEE_FILE
    target:
      data_source: iris_snowflake
      table: RAW_EMPLOYEE
    key_columns:
      - custid
    columns:
      - FIRSTNAME
      - lastname
      - designation
      - salary
    columns_mappings:
      - source_column: custid
        target_column: CUSTID

      - source_column: lastname
        target_column: LASTNAME

      - source_column: designation
        target_column: DESIGNATION

      - source_column: salary
        target_column: SALARY

  # DB TO DB (SNOWFLAKE)
  comparison_two:
    source:
      data_source: iris_snowflake
      table: RAW_EMPLOYEE

    target:
      data_source: iris_snowflake
      table: TL_EMPLOYEE
    key_columns:
      - CUSTID
    columns:
      - FIRSTNAME
      - LASTNAME
      - DESIGNATION
      - SALARY

  # FILE TO FILE
  comparison_three:
    source:
      data_source: qk_file_raw
      table: RAW_EMPLOYEE

    target:
      data_source: qk_file1_tl
      table: TL_EMPLOYEE
    key_columns:
      - custid
    columns:
      - FIRSTNAME
      - lastname
      - designation
      - salary
    columns_mappings:
      - source_column: FIRSTNAME
        target_column: firstname

  # DB TO DB (Postgres)
  comparison_four:
    source:
      data_source: pgsql_1
      table: actor
    target:
      data_source: pgsql_2
      table: actor2
    key_columns:
      - actor_id
    columns:
      - first_name
      - last_name
      - last_update
    columns_mappings:
      - source_column: actor_id
        target_column: actor_id1

      - source_column: first_name
        target_column: first_name1

      - source_column: last_name
        target_column: last_name1

      - source_column: last_update
        target_column: last_update1

  # DB TO DB (Postgres)
  comparison_five:
    source:
      data_source: pgsql_1
      table: actor
    target:
      data_source: pgsql_2
      table: new_table
    key_columns:
      - actor_id
    columns:
      - first_name
      - last_name
      - last_update

  # DB TO DB (Postgres)
  comparison_six:
    source:
      data_source: pgsql_3
      table: actor
    target:
      data_source: pgsql_4
      table: actor2
    key_columns:
      - actor_id
    columns:
      - first_name
      - last_name
      - last_update
    columns_mappings:
      - source_column: actor_id
        target_column: actor_id1

      - source_column: first_name
        target_column: first_name1

      - source_column: last_name
        target_column: last_name1

      - source_column: last_update
        target_column: last_update1

```
</details>