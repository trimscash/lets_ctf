START TRANSACTION;

DROP TABLE IF EXISTS `flag_table`;
CREATE TABLE `ctfdb`.`flag_table` (
  `ID` INT(7) NOT NULL,
  `name` VARCHAR(20) NOT NULL,
  `flag` VARCHAR(20) NULL,
  PRIMARY KEY (`ID`)
);

INSERT INTO flag_table VALUES ('1', 'yosida','flag{SQL_1NJECT10N_4ND_LEAK_T4BLES!!}');
INSERT INTO flag_table VALUES ('2', 'dada', '');