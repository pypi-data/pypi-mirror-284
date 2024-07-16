/*
   Copyright 2016-2022 ClickHouse, Inc.

   Copyright 2022- 2023 Bytedance Ltd. and/or its affiliates

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/

{% macro bytehouse__get_catalog(information_schema, schemas) -%}
  {% set data = [] %}
  {%- for schema in schemas -%}
    {%- set sql -%}
      show tables from {{ schema }}
    {%- endset -%}
    {%- set tables = run_query(sql) -%}
    {%- for table in tables -%}
      {%- set describe_sql -%}
        describe table {{ schema }}.{{ table[0] }}
      {%- endset -%}
      {%- set result = run_query(describe_sql) -%}
      {% for row in result %}
        {% set table_type = 'view' if table[8] == 'VIEW' else 'table' %}
        {% set metadata = {
          'table_database': null,
          'table_schema': schema,
          'table_name': table[0],
          'table_type': table_type,
          'table_comment': table[7],
          'column_name': row[0],
          'column_index': loop.index,
          'column_type': row[1],
          'column_comment': row[4],
          'table_owner': null
        } %}
        {% do data.append(metadata) %}
      {% endfor %}
    {%- endfor %}
  {%- endfor %}
  {% set column_names = ['table_database', 'table_schema', 'table_name', 'table_type', 'table_comment', 'column_name', 'column_index', 'column_type', 'column_comment', 'table_owner'] %}
  {% set agate_table = adapter.create_agate_table(data, column_names) %}
  {% do return(agate_table) %}
{%- endmacro %}
