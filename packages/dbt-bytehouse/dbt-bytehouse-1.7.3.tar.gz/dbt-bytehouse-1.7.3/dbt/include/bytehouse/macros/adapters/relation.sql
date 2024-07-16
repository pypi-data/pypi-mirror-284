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

{% macro bytehouse__get_or_create_relation(database, schema, identifier, type) %}
  {%- set target_relation = adapter.get_relation(database=database, schema=schema, identifier=identifier) %}
  {% if target_relation %}
    {% do return([true, target_relation]) %}
  {% endif %}

  {%- set can_exchange = adapter.can_exchange(schema, type) %}
  {%- set new_relation = api.Relation.create(
      database=None,
      schema=schema,
      identifier=identifier,
      type=type,
      can_exchange=can_exchange
  ) -%}
  {% do return([false, new_relation]) %}
{% endmacro %}

{% macro bytehouse__get_database(database) %}
  {%- set sql -%}
    show databases
  {%- endset -%}
  {%- set result = run_query(sql) -%}

  {% set data = [] %}
  {% for row in result %}
    {% set database_metadata = {
          'name': row[0],
          'engine': row[8],
          'comment': row[7]
        }
    %}
    {% do data.append(database_metadata) %}
  {% endfor %}

  {% set column_names = ['name', 'engine', 'comment'] %}
  {% set agate_table = adapter.create_agate_table(data, column_names) %}
  {% do return(agate_table) %}
{% endmacro %}