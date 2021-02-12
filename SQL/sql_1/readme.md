This practice is based on the OpenClassroom class : “ Initiez-vous à l'algèbre relationnelle avec le langage SQL ”
We are using a modified database of the Panama papers (2016) : https://en.wikipedia.org/wiki/Panama_Papers
The goal of the exercice is to investigate on a society named “Big Data Crunchers Ltd”, that might be an offshore shell of some other company.


The entity table contains all the offshore societies

```SQL
select * from entity
```
![](SQL/tables/table_a01.png)

```SQL
select id, name, jurisdiction, status FROM entity Where name = 'Big Data Crunchers Ltd.' ;
```
![](tables/table_a02.png)

Intermediary and officers are respectivly the tables containing all the intermediaries and all the beneficiaries.

```SQL
select * FROM
    (select name, id_address FROM entity
    Intersect
    select name, id_address FROM intermediary)
WHERE name = 'Big Data Crunchers Ltd.' ;
```
```SQL
select * FROM
    (select name, id_address FROM entity
    Intersect
    select name, id FROM officer)
WHERE name = 'Big Data Crunchers Ltd.' ;
```
Both return :
![](tables/table_a03.png)
As we can see, Big Data Crunchers is only present in the entity table.

The last table of the database : "adress" gives us the physical adresses of some of the compagnies or intermediaries.

```SQL
select 
    e.name,
    e.id_address,
    a.id_address,
    a.address,
    a.countries
FROM entity e, address a
WHERE e.id_address = a.id_address 
    AND e.name = 'Big Data Crunchers Ltd.' ; 
```
![](Code/SQL/tables/table_a04.png)
Strange address, isn't it ?

```SQL
select
    i.id as intermediary_id,
    i.name as intermediary_name,
    e.id as entity_id,
    e.name as entity_name,
    e.status as entity_status
FROM 
    intermediary i,
    assoc_inter_entity a,
    entity e
WHERE
    a.entity = e.id
    AND a.inter = i.id
    AND e.name = 'Big Data Crunchers Ltd.' ;
```

![](tables/table_a05.png)

```SQL

```

```SQL

```

```SQL

```

```SQL

```
