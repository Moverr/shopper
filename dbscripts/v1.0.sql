-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.16-log - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for shopper
CREATE DATABASE IF NOT EXISTS `shopper` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `shopper`;

-- Dumping structure for table shopper.categories
CREATE TABLE IF NOT EXISTS `categories` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL DEFAULT '0',
  `status` enum('ACTIVE','ARCHIVED') NOT NULL DEFAULT 'ACTIVE',
  `author_id` bigint(20) NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_by` bigint(20) NOT NULL,
  `date_updated` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
-- Dumping structure for table shopper.contacts
CREATE TABLE IF NOT EXISTS `contacts` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `type` varchar(50) NOT NULL DEFAULT '0',
  `details` varbinary(150) NOT NULL DEFAULT '0',
  `status` enum('ACTIVE','ARCHIVED') NOT NULL DEFAULT 'ACTIVE',
  `author_id` bigint(20) NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
-- Dumping structure for table shopper.featureditems
CREATE TABLE IF NOT EXISTS `featureditems` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `featuretype` bigint(20) NOT NULL DEFAULT '0',
  `item_id` bigint(20) NOT NULL DEFAULT '0',
  `start_date` bigint(20) NOT NULL DEFAULT '0',
  `end_date` bigint(20) NOT NULL DEFAULT '0',
  `status` enum('ACTIVE','ARCHIVED') NOT NULL DEFAULT 'ACTIVE',
  `author_id` bigint(20) NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Featured';

-- Data exporting was unselected.
-- Dumping structure for table shopper.featuretypes
CREATE TABLE IF NOT EXISTS `featuretypes` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '0',
  `code` varchar(10) NOT NULL DEFAULT '0',
  `issystem` enum('Y','N') NOT NULL DEFAULT 'N',
  `status` enum('ACTIVE','ARCHIVED') NOT NULL DEFAULT 'ACTIVE',
  `author_id` bigint(20) NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
-- Dumping structure for table shopper.items
CREATE TABLE IF NOT EXISTS `items` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `category_id` bigint(20) NOT NULL DEFAULT '0',
  `name` varchar(100) NOT NULL DEFAULT '0',
  `code` varchar(10) NOT NULL DEFAULT '0',
  `status` enum('ACTIVE','ARCHIVED') NOT NULL DEFAULT 'ACTIVE',
  `author_id` bigint(20) NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `last_updated` datetime NOT NULL,
  `updated_by` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_items_categories` (`category_id`),
  CONSTRAINT `FK_items_categories` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Items';

-- Data exporting was unselected.
-- Dumping structure for table shopper.itemtags
CREATE TABLE IF NOT EXISTS `itemtags` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `item_id` bigint(20) NOT NULL DEFAULT '0',
  `tag_id` bigint(20) NOT NULL DEFAULT '0',
  `status` enum('ACTIVE','ARCHIVED') NOT NULL DEFAULT 'ACTIVE',
  `author_id` bigint(20) NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
-- Dumping structure for table shopper.permissions
CREATE TABLE IF NOT EXISTS `permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `grouping` varchar(50) NOT NULL DEFAULT '0',
  `name` varchar(50) NOT NULL DEFAULT '0',
  `code` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='PERMISSIONS';

-- Data exporting was unselected.
-- Dumping structure for table shopper.profiles
CREATE TABLE IF NOT EXISTS `profiles` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(50) NOT NULL DEFAULT '0',
  `lastname` varchar(50) NOT NULL DEFAULT '0',
  `gender` enum('MALE','FEMALE') NOT NULL,
  `age` bigint(20) NOT NULL DEFAULT '0',
  `status` enum('ACTIVE','ARCHIVED') NOT NULL DEFAULT 'ACTIVE',
  `author_id` bigint(20) NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
-- Dumping structure for table shopper.roles
CREATE TABLE IF NOT EXISTS `roles` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '0',
  `code` varchar(50) NOT NULL DEFAULT '0',
  `status` enum('ACTIVE','ARCHIVED') NOT NULL DEFAULT 'ACTIVE',
  `issystem` enum('Y','N') NOT NULL DEFAULT 'N',
  `author_id` bigint(20) NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='ROLES';

-- Data exporting was unselected.
-- Dumping structure for table shopper.tags
CREATE TABLE IF NOT EXISTS `tags` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL DEFAULT '0',
  `code` varchar(10) NOT NULL DEFAULT '0',
  `author_id` bigint(20) NOT NULL DEFAULT '0',
  `date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='TAGS';

-- Data exporting was unselected.
-- Dumping structure for table shopper.userroles
CREATE TABLE IF NOT EXISTS `userroles` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL DEFAULT '0',
  `role_id` bigint(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
-- Dumping structure for table shopper.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL DEFAULT '0',
  `password` varchar(255) NOT NULL DEFAULT '0',
  `previouspassword` varchar(255) NOT NULL DEFAULT '0',
  `email` varchar(255) NOT NULL DEFAULT '0',
  `status` enum('PENDING','ACTIVE','DEACTIVATED','ONHOLD') NOT NULL DEFAULT 'PENDING',
  `author_id` bigint(20) NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='USER';

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
