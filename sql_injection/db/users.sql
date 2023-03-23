START TRANSACTION;
SET AUTOCOMMIT=0;


DROP TABLE IF EXISTS `users`;
CREATE TABLE `ctfdb`.`users` (
  `ID` INT(7) NOT NULL,
  `name` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`ID`)
);

INSERT INTO users VALUES ('1', 'yasuda');
INSERT INTO users VALUES ('2', 'dada');
INSERT INTO users VALUES ('3', 'kato');
INSERT INTO users VALUES ('4', 'sato');
INSERT INTO users VALUES ('5', 'matu');
INSERT INTO users VALUES ('6', 'ogawa');
INSERT INTO users VALUES ('7', 'kobayasi');
INSERT INTO users VALUES ('8', 'saito');
INSERT INTO users VALUES ('9', 'matuda');
INSERT INTO users VALUES ('10', 'kurita');

COMMIT;