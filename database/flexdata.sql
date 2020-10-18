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
-- Table structure for table `arena`
--

DROP TABLE IF EXISTS `arena`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `arena` (
  `arenaid` varchar(255) DEFAULT NULL,
  `arenaname` varchar(255) DEFAULT NULL,
  `latitude` decimal(10,6) DEFAULT NULL,
  `longitude` decimal(10,6) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arena`
--

LOCK TABLES `arena` WRITE;
/*!40000 ALTER TABLE `arena` DISABLE KEYS */;
INSERT INTO `arena` VALUES ('40001','Janki Devi Turf',19.139461,72.819264,NULL),('40002','Lokhandwala Sports Club Turf',19.146633,72.826316,NULL);
/*!40000 ALTER TABLE `arena` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_master`
--

DROP TABLE IF EXISTS `event_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_master` (
  `eventid` varchar(255) DEFAULT NULL,
  `arenaid` varchar(255) DEFAULT NULL,
  `playtime` varchar(255) DEFAULT NULL,
  `maxplayers` varchar(255) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `creator` varchar(255) DEFAULT NULL,
  `eventname` varchar(255) DEFAULT NULL,
  `groupid` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_master`
--

LOCK TABLES `event_master` WRITE;
/*!40000 ALTER TABLE `event_master` DISABLE KEYS */;
INSERT INTO `event_master` VALUES ('95786',NULL,'3465994','12','2020-10-15 14:14:32','3465994','Devesh\'s football plan','185573'),('17452',NULL,'3465994','12','2020-10-15 14:15:06','3465994','Devesh\'s football plan','185573'),('27296',NULL,'3465994','12','2020-10-15 14:16:36','3465994','Devesh\'s football plan','185573'),('16744',NULL,'3465994','12','2020-10-15 14:18:03','3465994','Devesh\'s football plan','185573'),('97351',NULL,'3465994','12','2020-10-15 14:27:27','3465994','Devesh\'s Cricket Footbal Plan','357307');
/*!40000 ALTER TABLE `event_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_players`
--

DROP TABLE IF EXISTS `event_players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_players` (
  `eventid` varchar(255) DEFAULT NULL,
  `playerid` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_players`
--

LOCK TABLES `event_players` WRITE;
/*!40000 ALTER TABLE `event_players` DISABLE KEYS */;
INSERT INTO `event_players` VALUES ('3465994','16744'),('3465994','97351');
/*!40000 ALTER TABLE `event_players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group_master`
--

DROP TABLE IF EXISTS `group_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `group_master` (
  `groupid` varchar(255) DEFAULT NULL,
  `groupname` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group_master`
--

LOCK TABLES `group_master` WRITE;
/*!40000 ALTER TABLE `group_master` DISABLE KEYS */;
INSERT INTO `group_master` VALUES ('185573','Rajhans Football'),('395994','National College Football Team'),('357307','AP Shah Institute of Technology FC');
/*!40000 ALTER TABLE `group_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player_groups`
--

DROP TABLE IF EXISTS `player_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player_groups` (
  `playerid` varchar(255) DEFAULT NULL,
  `groupid` varchar(255) DEFAULT NULL,
  `admin` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player_groups`
--

LOCK TABLES `player_groups` WRITE;
/*!40000 ALTER TABLE `player_groups` DISABLE KEYS */;
INSERT INTO `player_groups` VALUES ('9456394 ','423384','1'),('9456394 ','185573','1'),('9321670','185573','0'),('9456394','357307','1'),('3465994','357307','0');
/*!40000 ALTER TABLE `player_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player_master`
--

DROP TABLE IF EXISTS `player_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player_master` (
  `playerid` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phonenumber` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player_master`
--

LOCK TABLES `player_master` WRITE;
/*!40000 ALTER TABLE `player_master` DISABLE KEYS */;
INSERT INTO `player_master` VALUES ('1772743','jasmanarora','pbkdf2:sha256:150000$Jpvp2uhT$faba8dc3078f894e730c161436c729aa928a3e9d39091c2b2463c936ed2f757c','jasman','arora','jasmanarora@gmail.com','9664002799'),('9456394','deveshdatwani','pbkdf2:sha256:150000$sLSskyh3$e35d63f0cffe54d2391bee515c39e01c4e85c5d169b9c76789ce497088c131dc','devesh','datwani','datwanidevesh@gmail.com','9619183886'),('5327007','ayushkhurana','pbkdf2:sha256:150000$96MD1tSl$302f928e1276c0101e3574fc0556fd573f50f20d78723beefdcd90e9498fd212','ayush','khurana','ayushkhurana@gmail.com','9819453613'),('5035525','mohitgirdhar','pbkdf2:sha256:150000$DDYj3ApN$9d492ddf4fc59e6b962c103bf4334234147c65dbbe21383678dd8f04d91fad03','mohit','girdhar','mohitgirdhar@gmail.com','9773500095'),('2527867','anujanand','pbkdf2:sha256:150000$HDmYIonD$2868e7f7c077ee59c5b4918208eeac168910bed0e6fe94211b6c5ba79c95c367','anuja','nand','anujanand@gmail.com','9987306886'),('4986966','divyagaitonde','pbkdf2:sha256:150000$qEe7qpFc$dbfb86ff83e914551f94fa415a3347ca8f874eee20cb522b4dac76521fa35de1','divya','gaitonde','divyagaitonde@gmail.com','9892650119'),('8087708','urmikarambelkar','pbkdf2:sha256:150000$ctoIQIJJ$53bc3e375e959e16b971dae053373de8e082e57d51608c687ab08fd3248d6848','urmi','karambelkar','urmikarambelkar@gmail.com','9820072788'),('9321670','arjunpanchal','pbkdf2:sha256:150000$22wzd52N$e75aa7e9c1b28a0b035808679dc42cb85a9d5d6baa6a68f82602ce6e9d26dfb1','arjun','panchal','arjunpanchal@gmail.com','9773089191'),('2293503','rohannayyar','pbkdf2:sha256:150000$W74cgiU4$93b651fcc188e17c98b958d557f1cdfc7783948638d57de16f2a2a38d51e78ad','rohan','nayyar','rohannayyar@gmail.com','9820409475'),('6277378','vaibhavsrivastava','pbkdf2:sha256:150000$4oZ0SceQ$82c9b080f40832f62eb1313a5b76628dbac914c7401d4bdc8dd7a64fab9444b6','vaibhav','srivastava','vaibhavsrivastava@gmail.com','9943834762'),('6269810','saahillalwani','pbkdf2:sha256:150000$KUXAUZbd$5f665dbab46bac9725115c0db55ef88ea8b455e2899bb684b0428686dba18796','saahil','lalwani','saahillawalwani@gmail.com','9820284216'),('5143190','karanshah','pbkdf2:sha256:150000$ssZPU93z$04cad9e542c759ca3d58a02fd2f61a77ac67f636d9f400099ecb49c0100ce13d','karan','shah','karanshah@gmail.com','9619704288'),('3960650','deepalvarindani','pbkdf2:sha256:150000$fqQiB73V$f219f35cc8e5ce4b801984ddfc5d51526e0989214bd2c5fc0f6d5a38a5a7ff99','deepak','varindani','deepakvarindani@gmail.com','9920323838'),('7337788','stutidutta','pbkdf2:sha256:150000$RVCNshqC$8fc42358606e59bb779319eef3ef8358d1450041a9ec86dbce11bf4057d44098','stuti','dutta','stutidutta@gmail.com','8777807587'),('9586981','devarshshah','pbkdf2:sha256:150000$zUqRpmoV$5cc7761f004a7ec7a9530ca67df3f4ed2456beada3cba5ec530b61a2d826f38e','devarsh','shah','devarshshah@gmail.com','9833930989'),('9144841','jairohra','pbkdf2:sha256:150000$Vwgpge59$3e49918a21e22c871c9d0e3f252db184aaf8eb2c3ca58b32bf238e2bf37eafac','jai','rohra','jairohra@gmail.com','9769065334'),('8910725','sohrabrao','pbkdf2:sha256:150000$GFpK4OoY$e8b0c94804b9a61ce518fa5c3156ef80a283b3742264ae3a6736a5bbbfd96b24','sohrab','rao','sohrabrao@gmail.com','9819952824'),('4419383','varunpariani','pbkdf2:sha256:150000$qMHMHUj8$b0d8b2caa119dc2e33a2ca36d532dcba33f841065c73f5c3d12196247dee2d1b','varun','pariani','varunpariani@gmail.com','9821858749'),('1849038','nishilshah','pbkdf2:sha256:150000$UZCK5S15$a9d79f1b9bc3efb14a4b9ebf9c79cde522261a183e8d10bbc1953111e3ce2fa7','nishil','shah','nishilshah@gmail.com','7021846346'),('3465994','mihirshinde','pbkdf2:sha256:150000$k0IuacZo$d22d0da011066ef80102b256dd68eb2ed7dc882a4e4cadc334338660644df12f','mihir','shinde','mihirshinde@gmail.com','8828096886'),('3303519','jaymalaney','pbkdf2:sha256:150000$kVvYAGul$8cad64f7a4e9d7453ab56708b3cc600f27ae1d0fc4b6a029c2fb367a7f3b7202','jay','malaney','jaymalaney@gmail.com','9869736311'),('2445532','nikhilkapil','pbkdf2:sha256:150000$WFlDT6NM$d5c19a3393b1c5fd237f74c8037f16729bdb0647b0d5579d62e69159c444ff4c','nikhil','kapil','nikhilkapil@gmail.com','9930168197'),('4993277','manavrege','pbkdf2:sha256:150000$BEzklSgj$977e8aeaa271b372315fbb433f42b044b9cfe05bbbf5efa38df006d13c1ab941','manav','rege','manavrege@gmail.com','9833316627'),('9907120','moiztinwala','pbkdf2:sha256:150000$o1FS6bXV$d6e93bc1a3abbbe203707d5d8b341ea02d1ac07c60a7b422b69c1173a32792eb','moiz','tinwala','moiztinwala@gmail.com','959462212'),('9831148','hussaintinwala','pbkdf2:sha256:150000$ir7B5NT1$1d29598166a5c52d5034f192427a83538851c95fa36b50a210d9b5f60f739cb3','hussain','tinwala','hussaintinwala@gmail.com','9833632526'),('8944162','faizshaikh','pbkdf2:sha256:150000$929QIoik$872a32982c2f6c929980da454569bb6ac970c191f97c88782d8caa860d0cd7fd','faiz','shaikh','faizshaikh@gmail.com','828600070'),('5975359','christopherrodrigez','pbkdf2:sha256:150000$YZ5H0XC9$59ae8198e54ac0c89f9b81e734fbe7fe794abf9f79f46905b38dc91ca2640991','christopher','rodrigez','christopherrodrigez@gmail.com','9930758590'),('2867728','yashmachinder','pbkdf2:sha256:150000$WmQnCqGM$5e4506a716739da8385cf588f22a39cb105f53f14800750e6a916e6d57d40385','yash','machinder','yashmachinder@gmail.com','9920799501'),('8783947','namitlulla','pbkdf2:sha256:150000$Nvs4yE7b$7829bfde17b36aaec827960f489c5eb46d749c47806e19bb14c19b10c7e0d625','namit','lulla','namitlulla@gmail.com','9137840431'),('2421950','rohanjain','pbkdf2:sha256:150000$EJ4cVOfk$45e1ccee66d52d9441d643c994fc3f2b2b26a69734eabf86d3d50b408f9053cc','rohan','jain','rohanjain@gmail.com','9136867997');
/*!40000 ALTER TABLE `player_master` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-18 13:20:52
