This practice is based on the OpenClassroom class : “ Initiez-vous à l'algèbre relationnelle avec le langage SQL ”
We are using a modified database of the Panama papers (2016) : https://en.wikipedia.org/wiki/Panama_Papers
The goal of the exercice is to investigate on a society named “Big Data Crunchers Ltd”, that might be an offshore shell of some other company.


The entity table contains all the offshore societies

```SQL
select * from entity
```
![](https://github.com/Condefruit/Code/blob/main/SQL/tables/table_a01.png)

```SQL
select id, name, jurisdiction, status FROM entity Where name = 'Big Data Crunchers Ltd.' ;
```
![](https://github.com/Condefruit/Code/blob/main/SQL/tables/table_a02.png)

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
Both return an empty table :
![](https://github.com/Condefruit/Code/blob/main/SQL/tables/table_a03.png)
As we can see, Big Data Crunchers is only present in the entity table.

The table "address" of the database, gives us the physical addresses of some of the compagnies or intermediaries.

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
![](https://github.com/Condefruit/Code/blob/main/SQL/tables/table_a04.png)  
Strange address, isn't it ?

The next step is looking for the intermediaries which are linked to the creation of our mysterious society.  
Thanks to the table "assoc_inter_entity", which is a assocation table with two foreign keys related to entity and intermediary, it's pretty easy.

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

![](https://github.com/Condefruit/Code/blob/main/SQL/tables/table_a042.png)

Let's find out how many societies are link to the two intermediaries Patcher and Plouf.  

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
    AND (i.id = 5000 OR i.id = 5001 OR lower(i.name) LIKE '%pacher%banking%'
        OR
        lower(i.name) LIKE '%plouf%financial%services%')
GROUP BY 
    i.id, i.name, e.jurisdiction;
```

![](https://github.com/Condefruit/Code/blob/main/SQL/tables/table_a05.png)

And where they have the most activity :


```SQL
select
    i.id as intermediary_id,
    i.name as intermediary_name,
    e.jurisdiction,
    e.jurisdiction_description,
    count(*) as cnt
FROM 
    intermediary i,
    assoc_inter_entity a,
    entity e
WHERE 
    a.entity = e.id 
    AND a.inter = i.id 
    AND (i.id = 5000 OR i.id = 5001) 
GROUP BY 
    i.id, i.name, e.jurisdiction, e.jurisdiction_description
HAVING
    count(*) > 100
ORDER BY cnt desc
    ;
```

![](https://github.com/Condefruit/Code/blob/main/SQL/tables/table_a07.png)

Finally, with the use of the last table : assoc_officer_entity, we can try to discover to whom belongs Big Data Crunchers

```SQL
select
    e.id as entity_id,
    e.name as entity_name,
    o.id as officer_id,
    o.name as officer_name
FROM 
    entity e,
    assoc_officer_entity a,
    officer o
WHERE
    e.id = a.entity 
    AND a.officer = o.id
    AND e.name = 'Big Data Crunchers Ltd.' ;
```

![](https://github.com/Condefruit/Code/blob/main/SQL/tables/table_a08.png)

Tada !
