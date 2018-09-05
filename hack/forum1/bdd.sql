CREATE TABLE `membres_hack` (
  `id` mediumint(8) NOT NULL auto_increment,
  `login` varchar(100) collate latin1_general_ci NOT NULL,
  `pass` varchar(50) collate latin1_general_ci NOT NULL,
  `mail` varchar(100) collate latin1_general_ci NOT NULL,
  `langue` varchar(100) collate latin1_general_ci NOT NULL,
  `admin` tinyint(1) NOT NULL default '0',
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM

INSERT INTO `membres_hack` VALUES (1, 'admin', 'admin', 'no@email.com', 'FR', 1);