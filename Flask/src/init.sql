USE app;
CREATE TABLE IF NOT EXISTS `data` (`key` VARCHAR(255) NOT NULL, `value` INT NOT NULL, PRIMARY KEY (`key`));
INSERT INTO `data` (`key`, `value`) VALUES ('view_count', 0);