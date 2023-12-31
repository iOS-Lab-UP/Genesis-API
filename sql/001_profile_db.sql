SET NAMES utf8mb4;

-- Drop the table if it exists
DROP TABLE IF EXISTS `PROFILE`;

-- Create the PROFILE table
CREATE TABLE `PROFILE` (
  `ID` int NOT NULL AUTO_INCREMENT COMMENT 'Unique identifier for each profile',
  `PROFILE` varchar(255) NOT NULL COMMENT 'Name of the profile',
  `STATUS` tinyint NOT NULL DEFAULT '0' COMMENT 'Status of the profile',
  `CREATION_DATE` date NOT NULL COMMENT 'Date when the profile was created',
  `LAST_UPDATE` datetime NOT NULL COMMENT 'Date and time when the profile was last updated',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='Table containing profile information';

INSERT INTO `PROFILE` (`ID`, `PROFILE`, `STATUS`, `CREATION_DATE`, `LAST_UPDATE`) VALUES
(1,	'Patient',	1,	'2023-07-10',	'2023-07-10 18:12:58'),
(2,	'Doctor',	1,	'2023-07-10',	'2023-07-10 18:13:08'),
(3,	'Admin',	1,	'2023-07-10',	'2023-07-10 18:13:19');