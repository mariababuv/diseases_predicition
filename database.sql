/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - plantdisease
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`plantdisease` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `plantdisease`;

/*Table structure for table `enquiry` */

DROP TABLE IF EXISTS `enquiry`;

CREATE TABLE `enquiry` (
  `enquiry_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmer_id` int(11) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `enquiry_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`enquiry_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `enquiry` */

insert  into `enquiry`(`enquiry_id`,`farmer_id`,`description`,`reply`,`enquiry_date`) values (1,1,'well','srdfgygg','23-02-2020'),(2,2,'gddkshxu','NA','25-02-2020'),(3,3,'dghueuh','NA','14-01-2020'),(4,3,'dggdff','NA','2020-03-18');

/*Table structure for table `farmers` */

DROP TABLE IF EXISTS `farmers`;

CREATE TABLE `farmers` (
  `farmer_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(40) DEFAULT NULL,
  `last_name` varchar(40) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `gender` varchar(40) DEFAULT NULL,
  `latitude` varchar(40) DEFAULT NULL,
  `longitude` varchar(40) DEFAULT NULL,
  `place` varchar(40) DEFAULT NULL,
  `pincode` varchar(40) DEFAULT NULL,
  `phone` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`farmer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `farmers` */

insert  into `farmers`(`farmer_id`,`login_id`,`first_name`,`last_name`,`dob`,`gender`,`latitude`,`longitude`,`place`,`pincode`,`phone`) values (1,1,'Ram','Dev','1970-10-05','Male','10.1004\"N','76.3570\"E','Aluva','683101','8813247599'),(2,2,'Krishna','M.P','1964-07-23','Male','11.6854\"N','76.1320\"E','Wayanad','673121','9947155072'),(3,4,'ndnddn','xhz','11091994','Male','9.9786543','76.7804','dhz','6787666','464346642');

/*Table structure for table `govtpolicies` */

DROP TABLE IF EXISTS `govtpolicies`;

CREATE TABLE `govtpolicies` (
  `policy_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(40) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`policy_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `govtpolicies` */

insert  into `govtpolicies`(`policy_id`,`title`,`description`) values (6,'policy','crop insurance for farmers');

/*Table structure for table `greenhouses` */

DROP TABLE IF EXISTS `greenhouses`;

CREATE TABLE `greenhouses` (
  `green_house_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmer_id` int(11) DEFAULT NULL,
  `total_area` varchar(50) DEFAULT NULL,
  `crops_details` varchar(70) DEFAULT NULL,
  `build_date` varchar(50) DEFAULT NULL,
  `facilities` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`green_house_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `greenhouses` */

insert  into `greenhouses`(`green_house_id`,`farmer_id`,`total_area`,`crops_details`,`build_date`,`facilities`) values (1,1,'3000sq.m','none','20-02-2020','good'),(2,2,'2500sq.km','ghtyui','30-01-2020','ikgdett'),(3,3,'dbhd','hygcnn','11/07/1882','bfnggg');

/*Table structure for table `krishibhavan` */

DROP TABLE IF EXISTS `krishibhavan`;

CREATE TABLE `krishibhavan` (
  `krishibhavan_id` int(11) NOT NULL AUTO_INCREMENT,
  `latitude` varchar(40) DEFAULT NULL,
  `longitude` varchar(40) DEFAULT NULL,
  `place` varchar(40) DEFAULT NULL,
  `pincode` varchar(40) DEFAULT NULL,
  `phone` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`krishibhavan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `krishibhavan` */

insert  into `krishibhavan`(`krishibhavan_id`,`latitude`,`longitude`,`place`,`pincode`,`phone`) values (2,'10.1324\"N','76.1004\"E','Wayanad','613151','8281154998'),(8,'10.0261\"N','76.3125\"E','Edappally','682024','9061145584'),(9,'9.4949\"N','76.3304\"E','Alappuzha','688001','7745856512');

/*Table structure for table `label` */

DROP TABLE IF EXISTS `label`;

CREATE TABLE `label` (
  `label_id` int(11) NOT NULL AUTO_INCREMENT,
  `model_id` int(11) DEFAULT NULL,
  `label` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`label_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `label` */

insert  into `label`(`label_id`,`model_id`,`label`) values (1,1,'Tomato_Bacterial_spot'),(2,1,'Tomato_Early_blight'),(3,1,'Tomato_healthy'),(4,1,'Tomato_Late_blight'),(5,1,'Tomato_Leaf_Mold'),(6,1,'Tomato_Septoria_leaf_spot'),(7,1,'Tomato_Spider_mites_Two_spotted_spider_mite'),(8,1,'Tomato__Target_Spot'),(9,1,'Tomato__Tomato_mosaic_virus'),(10,1,'Tomato__Tomato_YellowLeaf__Curl_Virus');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(40) DEFAULT NULL,
  `password` varchar(40) DEFAULT NULL,
  `usertype` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'agdept','agdept','agdept'),(2,'njk','njk','farmer'),(3,'njks','njks','farmer'),(4,'mk','mk','farmer');

/*Table structure for table `model` */

DROP TABLE IF EXISTS `model`;

CREATE TABLE `model` (
  `model_id` int(11) NOT NULL AUTO_INCREMENT,
  `model_class` varchar(500) NOT NULL,
  `model_path` varchar(500) DEFAULT NULL,
  `image` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`model_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `model` */

insert  into `model`(`model_id`,`model_class`,`model_path`,`image`) values (1,'Tomato','models/tomato.hdf5',NULL);

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  `notification_date` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`description`,`notification_date`) values (7,'farmers meeting','2020-02-20'),(8,'yogana','2020-03-08');

/*Table structure for table `photos` */

DROP TABLE IF EXISTS `photos`;

CREATE TABLE `photos` (
  `photo_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmer_id` int(11) DEFAULT NULL,
  `leaf_image` varchar(80) DEFAULT NULL,
  `uploaded_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`photo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `photos` */

insert  into `photos`(`photo_id`,`farmer_id`,`leaf_image`,`uploaded_date`) values (1,1,'pictures','27-02-2020'),(2,2,'leafimage','23-02-2020');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
