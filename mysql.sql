DROP TABLE IF EXISTS `uniqvisitors`;
CREATE TABLE `uniqvisitors` (
  `id` int(11) NOT NULL auto_increment,
  `ip` varchar(15) NOT NULL,
  `date` date default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `UniqIpPerDay` (`ip`,`date`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TRIGGER `uniqvisitors_date_tr` BEFORE INSERT ON `uniqvisitors` FOR EACH ROW set new.date = CURDATE();


