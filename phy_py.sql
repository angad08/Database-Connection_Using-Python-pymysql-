-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.1.13-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win32
-- HeidiSQL Version:             10.3.0.5771
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for phy_py
CREATE DATABASE IF NOT EXISTS `phy_py` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `phy_py`;

-- Dumping structure for table phy_py.phyrusspy_details
CREATE TABLE IF NOT EXISTS `phyrusspy_details` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `FIRST_NAME` char(100) DEFAULT NULL,
  `LAST_NAME` char(100) DEFAULT NULL,
  `AGE` int(90) DEFAULT NULL,
  `SEX` char(40) DEFAULT NULL,
  `INCOME` double DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

-- Dumping data for table phy_py.phyrusspy_details: ~6 rows (approximately)
/*!40000 ALTER TABLE `phyrusspy_details` DISABLE KEYS */;
INSERT INTO `phyrusspy_details` (`ID`, `FIRST_NAME`, `LAST_NAME`, `AGE`, `SEX`, `INCOME`) VALUES
	(2, 'Maria', 'std', 35, 'F', 0);
INSERT INTO `phyrusspy_details` (`ID`, `FIRST_NAME`, `LAST_NAME`, `AGE`, `SEX`, `INCOME`) VALUES
	(3, 'Angad', 'Kadam', 22, 'M', 0);
INSERT INTO `phyrusspy_details` (`ID`, `FIRST_NAME`, `LAST_NAME`, `AGE`, `SEX`, `INCOME`) VALUES
	(4, 'Ran', 'Man', 2, 'F', 1303753);
INSERT INTO `phyrusspy_details` (`ID`, `FIRST_NAME`, `LAST_NAME`, `AGE`, `SEX`, `INCOME`) VALUES
	(5, 'Ganga', 'Shiva', 45, 'M', 51928341);
INSERT INTO `phyrusspy_details` (`ID`, `FIRST_NAME`, `LAST_NAME`, `AGE`, `SEX`, `INCOME`) VALUES
	(6, 'Mariana', 'Db', 43, 'F', 40968192.6416);
INSERT INTO `phyrusspy_details` (`ID`, `FIRST_NAME`, `LAST_NAME`, `AGE`, `SEX`, `INCOME`) VALUES
	(7, 'A', 'B', 23, 'M', 202);
/*!40000 ALTER TABLE `phyrusspy_details` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
