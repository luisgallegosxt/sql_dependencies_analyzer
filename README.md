# sql_dependencies_analyzer
A little sql tables dependencies analyzer

Some times you have a relational datawarehouse analytics database. There you can create some tables that process the logic of your business analytics. You may have something like this.

```
create or replace table schema.dwt_business_table1 as 
select *
from schema.transactional_a
```

This is a basic example of how you can create a process table that i call datawarehouse table (dwt), in this case you have only one dependency, but in real live this can become very complex.

Asume this example:
```
create or replace table schema.dwt_business_table1 as 
select *
from schema.transactional_a ta
join schema.transactional_b tb on ...

create or replace table schema.dwt_business_table2 as 
select *
from schema.transactional_c tc
join schema.transactional_d td on ...

create or replace table schema.dwt_business_table3 as 
select *
from schema.dwt_business_table1 tc
join schema.dwt_business_table2 td on ...
```

Here we have a more interesting example, some table depends on trasactional tables, but it can depend on processed tables like a (dwt).
If you want to update this tables, you will need the correct order to update, for that we will user the Depth-First Search algoritm (DFS).

This will output the correct order to update, from the atomic tables to the parent one.
