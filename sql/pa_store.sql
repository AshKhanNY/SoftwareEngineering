-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: pa_store
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'Ash','Ash'),(2,'Azwad','Azwad'),(3,'David','David'),(4,'Dewan','Dewan'),(5,'Jie','Jie');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appeal`
--

DROP TABLE IF EXISTS `appeal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appeal` (
  `for_who` int NOT NULL,
  `reason` varchar(1000) NOT NULL DEFAULT 'N/A',
  PRIMARY KEY (`for_who`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appeal`
--

LOCK TABLES `appeal` WRITE;
/*!40000 ALTER TABLE `appeal` DISABLE KEYS */;
INSERT INTO `appeal` VALUES (10,'I\'m very sorry, I will never say xbox gaming is better than PC!');
/*!40000 ALTER TABLE `appeal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bid`
--

DROP TABLE IF EXISTS `bid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bid` (
  `company` int NOT NULL,
  `delivery` int NOT NULL,
  `amount` int NOT NULL,
  PRIMARY KEY (`company`,`delivery`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bid`
--

LOCK TABLES `bid` WRITE;
/*!40000 ALTER TABLE `bid` DISABLE KEYS */;
INSERT INTO `bid` VALUES (1,2,40),(1,3,15),(2,2,20),(3,3,50),(4,2,25);
/*!40000 ALTER TABLE `bid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blacklistedcompany`
--

DROP TABLE IF EXISTS `blacklistedcompany`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blacklistedcompany` (
  `company_id` int NOT NULL,
  `reason` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blacklistedcompany`
--

LOCK TABLES `blacklistedcompany` WRITE;
/*!40000 ALTER TABLE `blacklistedcompany` DISABLE KEYS */;
INSERT INTO `blacklistedcompany` VALUES (7,'Highly suspicious company that always takes much longer to deliver than intended.');
/*!40000 ALTER TABLE `blacklistedcompany` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blacklistedcustomer`
--

DROP TABLE IF EXISTS `blacklistedcustomer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blacklistedcustomer` (
  `customer_id` int NOT NULL,
  `reason` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blacklistedcustomer`
--

LOCK TABLES `blacklistedcustomer` WRITE;
/*!40000 ALTER TABLE `blacklistedcustomer` DISABLE KEYS */;
INSERT INTO `blacklistedcustomer` VALUES (10,'Incredibly rude to customers who do not like AMD.');
/*!40000 ALTER TABLE `blacklistedcustomer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clerk`
--

DROP TABLE IF EXISTS `clerk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clerk` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clerk`
--

LOCK TABLES `clerk` WRITE;
/*!40000 ALTER TABLE `clerk` DISABLE KEYS */;
INSERT INTO `clerk` VALUES (1,'Ray','Ray'),(2,'John','John'),(3,'Rock','Rock'),(4,'Randy','Randy');
/*!40000 ALTER TABLE `clerk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clerkreport`
--

DROP TABLE IF EXISTS `clerkreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clerkreport` (
  `clerk_id` int NOT NULL,
  `num_reported` int DEFAULT NULL,
  `reason` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`clerk_id`),
  CONSTRAINT `clerk_id` FOREIGN KEY (`clerk_id`) REFERENCES `clerk` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clerkreport`
--

LOCK TABLES `clerkreport` WRITE;
/*!40000 ALTER TABLE `clerkreport` DISABLE KEYS */;
INSERT INTO `clerkreport` VALUES (4,2,'Tried to accept PCRUS for the second time, even after advised that they were banned.');
/*!40000 ALTER TABLE `clerkreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `type` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (1,'FedEx','FedEx','D'),(2,'UPS','UPS','D'),(3,'Amazon','Amazon','D'),(4,'Mother Truckers','MT','D'),(5,'Nvidia','NV','S'),(6,'Dell','Dell','S'),(7,'PCs R US','PCRUS','S');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companyreport`
--

DROP TABLE IF EXISTS `companyreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `companyreport` (
  `company_id` int NOT NULL,
  `num_reported` int DEFAULT NULL,
  `reason` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`company_id`),
  CONSTRAINT `company_id` FOREIGN KEY (`company_id`) REFERENCES `company` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companyreport`
--

LOCK TABLES `companyreport` WRITE;
/*!40000 ALTER TABLE `companyreport` DISABLE KEYS */;
INSERT INTO `companyreport` VALUES (6,1,'Multiple customers agree that Dell takes too long for G5 brand consoles.');
/*!40000 ALTER TABLE `companyreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `creditcard`
--

DROP TABLE IF EXISTS `creditcard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `creditcard` (
  `user` int NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `number` varchar(16) NOT NULL,
  `expiration` date DEFAULT NULL,
  PRIMARY KEY (`user`,`number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `creditcard`
--

LOCK TABLES `creditcard` WRITE;
/*!40000 ALTER TABLE `creditcard` DISABLE KEYS */;
INSERT INTO `creditcard` VALUES (1,'Alpha','1234432112344321','2023-08-30'),(3,'Charlie','9999888877776666','2021-07-07'),(4,'Delta','6666555544443333','2024-09-23'),(5,'Echo','1111221111222222','2023-01-01'),(6,'Foxtrot','1524152415241524','2023-02-20'),(9,'India','3476463480991234','2023-05-30');
/*!40000 ALTER TABLE `creditcard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `joined` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Alpha','a@gmail.com','A','2021-04-29 20:29:05'),(2,'Bravo','b@gmail.com','B','2021-04-29 20:29:05'),(3,'Charlie','c@gmail.com','C','2021-04-29 20:29:05'),(4,'Delta','d@gmail.com','D','2021-04-29 20:29:05'),(5,'Echo','e@gmail.com','E','2021-04-29 20:29:05'),(6,'Foxtrot','f@gmail.com','F','2021-04-29 20:29:05'),(7,'Golf','g@gmail.com','G','2021-04-29 20:29:05'),(8,'Hotel','h@gmail.com','H','2021-04-29 20:29:05'),(9,'India','i@gmail.com','I','2021-04-29 20:29:05'),(10,'Juliet','j@gmail.com','J','2021-04-29 20:29:05');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customerreport`
--

DROP TABLE IF EXISTS `customerreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customerreport` (
  `customer_id` int NOT NULL,
  `num_reported` int DEFAULT NULL,
  `reason` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`customer_id`),
  CONSTRAINT `customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customerreport`
--

LOCK TABLES `customerreport` WRITE;
/*!40000 ALTER TABLE `customerreport` DISABLE KEYS */;
INSERT INTO `customerreport` VALUES (1,1,'User report: Causing disturbance in forums chat.');
/*!40000 ALTER TABLE `customerreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery`
--

DROP TABLE IF EXISTS `delivery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery` (
  `tracking_num` int NOT NULL AUTO_INCREMENT,
  `item` int DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `company` int DEFAULT NULL,
  `customer` int DEFAULT NULL,
  `claimed` tinyint(1) DEFAULT '0',
  `status` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`tracking_num`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery`
--

LOCK TABLES `delivery` WRITE;
/*!40000 ALTER TABLE `delivery` DISABLE KEYS */;
INSERT INTO `delivery` VALUES (1,13,1,3,6,1,'Shipped'),(2,9,1,1,2,0,'Processing'),(3,8,1,3,3,0,'Processing'),(4,12,1,4,9,1,'Delivered');
/*!40000 ALTER TABLE `delivery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `price` decimal(6,2) DEFAULT NULL,
  `manufacturer` varchar(50) DEFAULT NULL,
  `details` varchar(1000) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `amount` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1,'i9-9900K',375.99,'Intel','8 core, 16 threads, 3.6 ghz','CPU',10),(2,'i9-10850KA',437.99,'Intel','10 core, 3.6 ghz, 125 W','CPU',10),(3,'Ryzen 7 5800X',449.99,'AMD','8 core, 3.8 ghz, 105W','CPU',10),(4,'GeForce RTX 9001',1999.98,'Nvidia','Achieve 16K gaming with this state of the art GPU. Very rare.','GPU',10),(5,'GeForce 1080',299.99,'Nvidia','For those who can\'t even find a card online.','GPU',10),(6,'Radeon RX 580',599.99,'AMD','It\'s a card.','GPU',10),(7,'MSI H310MPROVDHP',67.99,'MSI','Compatible for most builds.','MB',10),(8,'ASUS Prime Z490-A LGA 1200',245.99,'ASUS','N/A','MB',10),(9,'Y4CNC R920 V1',2450.00,'DELL','Extremely powerful motherboard, capable of powering a supercomputer.','MB',10),(10,'Phantom Black ATX Mid-Tower Case',89.99,'MUSETEX','Supports USB 3.0 with built in RGB fans.','CASE',10),(11,'CC-9011075-WW Carbide Series',99.99,'Corsair','For office builds, comes with matte black finish.','CASE',10),(12,'CC-8081077-WW Carbide Series',54.99,'Corsair','Provides clear view of internals, with adequate space for heat flow.','CASE',10),(13,'Vengeance RGB PRO 16GB',120.99,'Corsair','2x8GB','MEM',10),(14,'Vengeance LPX 16GB',92.99,'Corsair','2x8GB','MEM',10),(15,'Vengeance RGB PRO 32GB',289.99,'Corsair','2x16GB','MEM',10),(16,'Power Supply BR-0600',44.99,'EVGA','Bronze 600W, 3 Year Warranty','MISC',10),(17,'Monitor SB220Q',146.43,'Acer','21.5 Inches, Full HD','MISC',10),(18,'Webcam C922x Pro Stream',99.99,'Logitech','Full 1080p HD','MISC',10);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post` (
  `id` int NOT NULL AUTO_INCREMENT,
  `author` int DEFAULT NULL,
  `content` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (1,1,'Seriously, when the h*ll are these new graphics cards coming out!'),(2,1,'I\'ve been waiting FOREVER, my wallet is collecting dust. What type of business doesn\'t want money from ME.'),(3,2,'Calm down Alpha, you can get banned if you go out of hand.'),(4,4,'Alpha\'s got a point though. I\'ve been trying to get my hands on a RTX 3060 for ages and it\'s nowhere to be found. UGH'),(5,3,'I\'ll just stick to my Raspberry Pi, thank you very much. It runs Minecraft too! Well, sorta...');
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reply`
--

DROP TABLE IF EXISTS `reply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reply` (
  `id` int NOT NULL AUTO_INCREMENT,
  `author` int DEFAULT NULL,
  `thread` int DEFAULT NULL,
  `content` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reply`
--

LOCK TABLES `reply` WRITE;
/*!40000 ALTER TABLE `reply` DISABLE KEYS */;
INSERT INTO `reply` VALUES (1,5,3,'I hope you know there\'s a reply feature?');
/*!40000 ALTER TABLE `reply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoppingcart`
--

DROP TABLE IF EXISTS `shoppingcart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoppingcart` (
  `user` int NOT NULL,
  `item` int NOT NULL,
  `amount` int DEFAULT '1',
  PRIMARY KEY (`user`,`item`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoppingcart`
--

LOCK TABLES `shoppingcart` WRITE;
/*!40000 ALTER TABLE `shoppingcart` DISABLE KEYS */;
INSERT INTO `shoppingcart` VALUES (1,1,1),(1,4,7),(1,5,1),(1,6,3),(2,1,1),(3,3,1),(3,9,1),(4,16,1);
/*!40000 ALTER TABLE `shoppingcart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplyrequest`
--

DROP TABLE IF EXISTS `supplyrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplyrequest` (
  `supply_id` int NOT NULL AUTO_INCREMENT,
  `company` int DEFAULT NULL,
  `reason` varchar(1000) NOT NULL,
  PRIMARY KEY (`supply_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplyrequest`
--

LOCK TABLES `supplyrequest` WRITE;
/*!40000 ALTER TABLE `supplyrequest` DISABLE KEYS */;
INSERT INTO `supplyrequest` VALUES (1,6,'We\'d like to offer our new keyboards to your store.'),(2,5,'We have new 3000 series graphics cards that we\'d love to sell.');
/*!40000 ALTER TABLE `supplyrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taboo`
--

DROP TABLE IF EXISTS `taboo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taboo` (
  `word` varchar(50) NOT NULL,
  PRIMARY KEY (`word`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taboo`
--

LOCK TABLES `taboo` WRITE;
/*!40000 ALTER TABLE `taboo` DISABLE KEYS */;
INSERT INTO `taboo` VALUES ('bastard'),('crap'),('fuck'),('hell'),('penis'),('pussy'),('shit');
/*!40000 ALTER TABLE `taboo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL,
  `type` varchar(20) NOT NULL,
  `signed_in` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin',1),(1,'clerk',0),(1,'company',0),(1,'customer',0),(2,'admin',0),(2,'clerk',0),(2,'company',0),(2,'customer',0),(3,'admin',0),(3,'clerk',0),(3,'company',0),(3,'customer',0),(4,'admin',0),(4,'clerk',0),(4,'company',0),(4,'customer',0),(5,'admin',0),(5,'company',0),(5,'customer',0),(6,'company',0),(6,'customer',0),(7,'company',0),(7,'customer',0),(8,'customer',0),(9,'customer',0),(10,'customer',0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wallet`
--

DROP TABLE IF EXISTS `wallet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wallet` (
  `user` int NOT NULL,
  `amount` decimal(9,2) DEFAULT NULL,
  PRIMARY KEY (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wallet`
--

LOCK TABLES `wallet` WRITE;
/*!40000 ALTER TABLE `wallet` DISABLE KEYS */;
INSERT INTO `wallet` VALUES (1,1000000.00),(2,200.00),(3,155.00),(4,99.99),(5,300.00);
/*!40000 ALTER TABLE `wallet` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-13 11:30:13
