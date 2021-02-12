This practice is based on the OpenClassroom class : “ Initiez-vous à l'algèbre relationnelle avec le langage SQL ”
We are using a modified database of the Panama papers (2016) : https://en.wikipedia.org/wiki/Panama_Papers
The goal of the exercice is to investigate on a society named “Big Data Crunchers Ltd”, that might be an offshore shell of some other company.


The entity table contains all the offshore societies

```SQL
select * from entity
```
![](tables/table_a01.png)

```SQL
select id, name, jurisdiction, status FROM entity Where name = 'Big Data Crunchers Ltd.' ;
```
![](tables/table_a02.png)

intermediary and officers are respectivly the tables containing all the intermediaries and all the beneficiaries

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
As we can see, Big Data Crunchers is only present in the entity table

```SQL
```

```SQL
```
