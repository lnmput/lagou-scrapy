/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2017-05-16 23:36:53
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for lagou
-- ----------------------------
DROP TABLE IF EXISTS `lagou`;
CREATE TABLE `lagou` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `url` varchar(255) CHARACTER SET utf8 NOT NULL,
  `url_id` varchar(255) CHARACTER SET utf8 NOT NULL,
  `title` varchar(255) CHARACTER SET utf8 NOT NULL,
  `salary` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `city` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `work_years` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `degree_need` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `types` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `publish_time` varchar(0) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `tags` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `descs` varchar(1000) CHARACTER SET utf8 DEFAULT NULL,
  `address` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `company_url` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `company_name` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=648 DEFAULT CHARSET=latin1;

