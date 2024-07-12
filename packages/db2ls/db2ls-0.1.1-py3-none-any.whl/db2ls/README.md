### How to install 

```sh
pip install db2ls
```



```sh
git clone https://github.com/Jianfengliu0413/db2ls.git
```



### usage:

```python
from db2ls import db2ls
```

db path


```python
# Example usage
db_path = 'test.db'
```

connect


```python
# option 1:  dirrect connect
db2ls.connect(db_path)
```




    <db2ls.db2ls.db2ls at 0x1110ff5c0>




```python
db2ls.connect(db_path).vacuum()
```

    Error executing query: no such table: change_log
    Database vacuumed


create a table


```python
table="germany"
```


```python
# option 2: use "with" method
with db2ls(db_path) as db:
    db.create(table,["id integer primary key", "city text", "postcode text"])
```

    Error executing query: no such table: change_log
    Table created with definition: CREATE TABLE IF NOT EXISTS germany (id integer primary key, city text, postcode text)
    Connection closed


insert info


```python
with db2ls(db_path) as db:
    db.insert(table, ['id', 'city',"postcode"], [1,"Heidelberg","69115"])

```

    Error executing query: no such table: change_log
    Data inserted into germany: [1, 'Heidelberg', '69115']
    Connection closed


take a look


```python
with db2ls(db_path) as db:
    db.print(table, ['id', 'city',"postcode"])
```

    (1, 'Heidelberg', '69115')
    Connection closed


only check specific columns


```python
with db2ls(db_path) as db:
    db.print(table, ['id', 'city'])
```

    (1, 'Heidelberg')
    Connection closed


or check all (*)


```python
with db2ls(db_path) as db:
    db.print(table, ["*"])
    db.print(table, "*") # not work
```

    (1, 'Heidelberg', '69115')
    (1, 'Heidelberg', '69115')
    Connection closed


insert more data


```python
with db2ls(db_path) as db:
    db.insert(table, ['id', 'city',"postcode"], [2,"Neckargemuend","69151"])
    db.insert(table, ['id', 'city',"postcode"], [3,"Wiesloch","69168"])
    db.insert(table, ['id', 'city',"postcode"], [4,"Leimen","69181"])
    db.insert(table, ['id', 'city',"postcode"], [5,"Walldorf","69190"])
    db.insert(table, ['id', 'city',"postcode"], [6,"Schriesheim","69198"])
    db.insert(table, ['id', 'city',"postcode"], [7,"Sandhausen","69207"])

```

    Error executing query: no such table: change_log
    Data inserted into germany: [2, 'Neckargemuend', '69151']
    Error executing query: no such table: change_log
    Data inserted into germany: [3, 'Wiesloch', '69168']
    Error executing query: no such table: change_log
    Data inserted into germany: [4, 'Leimen', '69181']
    Error executing query: no such table: change_log
    Data inserted into germany: [5, 'Walldorf', '69190']
    Error executing query: no such table: change_log
    Data inserted into germany: [6, 'Schriesheim', '69198']
    Error executing query: no such table: change_log
    Data inserted into germany: [7, 'Sandhausen', '69207']
    Connection closed



```python
with db2ls(db_path) as db:
    db.print(table, ["*"])
```

    (1, 'Heidelberg', '69115')
    (2, 'Neckargemuend', '69151')
    (3, 'Wiesloch', '69168')
    (4, 'Leimen', '69181')
    (5, 'Walldorf', '69190')
    Connection closed


you see: only first 5 get printed


```python
with db2ls(db_path) as db:
    db.print(table, "*",n=10)
```

    (1, 'Heidelberg', '69115')
    (2, 'Neckargemuend', '69151')
    (3, 'Wiesloch', '69168')
    (4, 'Leimen', '69181')
    (5, 'Walldorf', '69190')
    (6, 'Schriesheim', '69198')
    (7, 'Sandhausen', '69207')
    Connection closed


update table

if i want to change the postcode in city 'Leimen'


```python
db.connect(db_path).execute("update germany set city='Tübingen' where city = 'Leimen'")
db.connect(db_path).print("germany")
```

    Error executing query: no such table: change_log
    (1, 'Heidelberg', '69115')
    (2, 'Neckargemuend', '69151')
    (3, 'Wiesloch', '69168')
    (4, 'Tübingen', '69181')
    (5, 'Walldorf', '69190')



```python
with db2ls(db_path) as db:
    db.update(table, "postcode = '72076'", "postcode = '69181'")
    db.print(table,"*")
```

    UPDATE germany SET postcode = '72076' WHERE postcode = '69181'
    Error executing query: no such table: change_log
    (1, 'Heidelberg', '69115')
    (2, 'Neckargemuend', '69151')
    (3, 'Wiesloch', '69168')
    (4, 'Tübingen', '72076')
    (5, 'Walldorf', '69190')
    Connection closed


get columns names


```python
db.connect(db_path).columns(table)
```




    ['id', 'city', 'postcode']



conver to DataFrame()


```python
db.connect(db_path).to_df(table)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>city</th>
      <th>postcode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Heidelberg</td>
      <td>69115</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Neckargemuend</td>
      <td>69151</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Wiesloch</td>
      <td>69168</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Tübingen</td>
      <td>72076</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Walldorf</td>
      <td>69190</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Schriesheim</td>
      <td>69198</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Sandhausen</td>
      <td>69207</td>
    </tr>
  </tbody>
</table>
</div>




```python
db.connect(db_path).to_df(table)["city"].tolist()
```




    ['Heidelberg',
     'Neckargemuend',
     'Wiesloch',
     'Tübingen',
     'Walldorf',
     'Schriesheim',
     'Sandhausen']




```python

```
