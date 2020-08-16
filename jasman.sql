-- MySQL dump 10.13  Distrib 8.0.21, for Linux (x86_64)
--
-- Host: localhost    Database: flexplay
-- ------------------------------------------------------
-- Server version	8.0.21-0ubuntu0.20.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `events_master`
--

DROP TABLE IF EXISTS `events_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events_master` (
  `creater` varchar(255) NOT NULL,
  `player` varchar(255) NOT NULL,
  `daytime` timestamp NOT NULL,
  `eventarena` varchar(255) NOT NULL,
  `team` varchar(255) NOT NULL,
  `privacy` int NOT NULL,
  `gameplaytime` int DEFAULT NULL,
  `lat` double DEFAULT NULL,
  `lng` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events_master`
--

LOCK TABLES `events_master` WRITE;
/*!40000 ALTER TABLE `events_master` DISABLE KEYS */;
INSERT INTO `events_master` VALUES ('deveshdatwani','deveshdatwani','2020-08-20 16:30:00','jankidevi turf','rajhans football',0,1,NULL,NULL),('jasmanarora','jasmanarora','2020-08-05 10:30:00','St. Theresa\'s','khar blazers',1,4,NULL,NULL),('arjunpanchal','arjunpanchal','2020-08-05 07:30:00','Inorbit','rajhans football',1,4,124.2,220.3),('arjunpanchal','kaushalk','2020-08-05 07:30:00','Inorbit','rajhans football',1,4,124.2,220.3),('deveshdatwani','deveshdatwani','2020-08-20 16:30:00','PVR Juhu','devesh@gmail.com',1,1,123.4,120.4),('deveshdatwani','deveshdatwani','2020-08-08 14:30:00','Andheri Sports Complex','devesh@gmail.com',0,1,200,200),('ayushkhurana','ayushkhurana','2020-08-15 16:30:00','St. Andrew\'s','ayush@gmail.com',0,2,200,30.3),('zohebshaikh','zohebshaikh','2020-08-07 16:30:00','Lokhandwala Turf','zoheb@gmail.com',1,2,230,1223);
/*!40000 ALTER TABLE `events_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifications_master`
--

DROP TABLE IF EXISTS `notifications_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notifications_master` (
  `invitor` varchar(255) DEFAULT NULL,
  `team` varchar(255) DEFAULT NULL,
  `invited` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications_master`
--

LOCK TABLES `notifications_master` WRITE;
/*!40000 ALTER TABLE `notifications_master` DISABLE KEYS */;
INSERT INTO `notifications_master` VALUES ('deveshdatwani','devesh@gmail.com','jasmanarora'),('jasmanarora','khar blazers','deveshdatwani'),('ayushkhurana','khar blazers','deveshdatwani'),('arjunpanchal','rajhans football','deveshdatwani');
/*!40000 ALTER TABLE `notifications_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `players_master`
--

DROP TABLE IF EXISTS `players_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `players_master` (
  `playerid` int DEFAULT NULL,
  `username` varchar(255) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phonenumber` int DEFAULT NULL,
  `groupid` int DEFAULT NULL,
  `teamname` varchar(255) DEFAULT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players_master`
--

LOCK TABLES `players_master` WRITE;
/*!40000 ALTER TABLE `players_master` DISABLE KEYS */;
INSERT INTO `players_master` VALUES (86360552,'yashmachindar','yash','machindar','yash@gmail.com',98235,NULL,'rajhans football','pbkdf2:sha256:150000$bxld9W1K$6526dd127173aca6bb83d0a2b4ffaa72974e85188e8799327616379c807a9bed'),(58694356,'deveshdatwani','devesh','datwani','devesh@gmail.com',96191,NULL,'rajhans football','pbkdf2:sha256:150000$fSH43f59$7af268d14c94ac407970c19d393bb98a43f677485c6c811556d9589913532409'),(90662913,'jasmanarora','jasman','arora','jasman@gmail.com',96640,NULL,'khar blazers','pbkdf2:sha256:150000$mQyd9u8o$f638d46472d2ecbe43f826f2981b0a4f67728acde9d58f5f6c9288345a316f93'),(59813600,'ashishdatwani','ashish','datwani','ashish@gmail.com',98194,NULL,'worli giants','pbkdf2:sha256:150000$DGdLY6UE$97f488232694116c7899eb1ad58493382f52d6d3e697dad0bfd46e3f0f46dec8'),(25260339,'arjunpanchal','arjun','panchal','arjun@gmail.com',9773089,NULL,'rajhans football','pbkdf2:sha256:150000$T87EJGZF$1a8d2aed9e6c582213a4fe2d5f12c868346de5596dca8f633e08307a2e8c9a00'),(36008444,'vaibhavsrivastava','vaibhav','srivastava','vaibhav@gmail.com',88998,NULL,'rajhans football','pbkdf2:sha256:150000$oCP1Uihi$c92a51a5ee8ad49f907e6d651076d2d6907e46247650cd63fae4bbef3acbafd9'),(33778054,'rohannayyar','rohan','nayyar','rohan@gmail.com',98204,NULL,'rajhans football','pbkdf2:sha256:150000$maCstS0c$3795be2f2d11aaef1f72791a66361c68816df926118d4b62628620270c975e5d'),(24863116,'zohebshaikh','zoheb','shaikh','zoheb@gmail.com',98974,NULL,'rajhans football','pbkdf2:sha256:150000$Z0g8CbLs$6d08b68935d2f945532c0789c60e91e6a45f72f6ed0059478b740b01aac1df9e'),(55225219,'ayushkhurana','ayush','khurana','ayush@gmail.com',997823,NULL,'khar blazers','pbkdf2:sha256:150000$TkD2G3E5$bc03487ffd22a8b3bce349866392cd74b7a136696c9ddffbb74e355b05d7fe93'),(81625010,'vanshadnani','vansh','adnani','vansh@gmail.com',986234,NULL,'worli giants','pbkdf2:sha256:150000$3Ckti7If$51514b228d4a53344f607cdbf90e77073c192db5d89b4d6def047e13f17d3788'),(71431074,'devarshshah','devarsh','shah','devarsh@gmail.com',99830,NULL,'shivam maniancs','pbkdf2:sha256:150000$WMUOSmJj$2939b0859fe804b599145bb5a1ce0299a34e77a67466d516a04589e013436129'),(28516742,'hussaintinwala','hussain','tinwala','hussain@gmail.com',998336,NULL,'shivam maniancs','pbkdf2:sha256:150000$SEh4pC8Y$1345f1dd0dd1f018ccbca9117be254b4be5a54b5d971549048912109937c4369'),(99106021,'moiztinwala','moiz','tinwala','moiz@gmail.com',95946,NULL,'shivam maniancs','pbkdf2:sha256:150000$gxov2XnF$7f7d251e3497d8f4fa0a09fce7c168707b9629b19cfc99e9da2567c64578bafb'),(69671462,'karanshah','karan','shah','karan@gmail.com',972324,NULL,'GG boys','pbkdf2:sha256:150000$VpCwv7ic$91d9cba8f748b812d414088ef92497070f08de55e2da8dc934e7dfec53e6f448'),(47383001,'saahillalwani','saahil','lalwani','saahil@gmail.com',972324,NULL,'GG boys','pbkdf2:sha256:150000$TwmwcjDe$938a385e361e3c45b2464d1650db85455bb9e2a3215b4d6cd2d48b74b3ec12df'),(99171583,'deepakvarindani','deepak','varindani','deepak@gmail.com',394759,NULL,'GG boys','pbkdf2:sha256:150000$Cgshpct2$21c71724b613492c7578264ff0bcba222bd9eb9c4a39a56c467393c0b9a4965c'),(40466665,'sushanthsunil','sushanth','sunil','sushanth@gmail.com',9872364,NULL,'rajhans football','pbkdf2:sha256:150000$oaNopqry$ec3c6f6360d0f70ccfba41fb862633f01c5a626728d7d3ba7b5dd8f454bb3097'),(56930984,'anirudhbakshi','anirudh','bakshi','anirudh@gmail.com',9824364,NULL,'rajhans football','pbkdf2:sha256:150000$4CHgHUFf$07b5d4df1de474ed40d9fa9f17de6af503b1e4738bdab6c3f85df791a1cd789a'),(84653770,'pratikshetty','pratik','shetty','pratik@gmail.com',9823241,NULL,'rajhans football','pbkdf2:sha256:150000$B2NWs4Xd$e5ccdc41e520880a13969ea6cf37eddb78162881b400b3de34365daa97811ff2'),(96894772,'kaushalk','kaushal','k','kaushal@gmail.com',983421,NULL,'rajhans football','pbkdf2:sha256:150000$vZizI2GN$a81d1c172d9557f1aa64db925d187ff479ccb28141a4686e4db4c2da9a565fa8');
/*!40000 ALTER TABLE `players_master` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-16 21:41:07
