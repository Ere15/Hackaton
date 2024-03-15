-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: hakatondb
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `запросы`
--

DROP TABLE IF EXISTS `запросы`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `запросы` (
  `id_запроса` int NOT NULL AUTO_INCREMENT,
  `Тема` varchar(45) NOT NULL,
  `Метки` varchar(45) NOT NULL,
  `Описание` varchar(45) NOT NULL,
  `Дата_запроса` datetime NOT NULL,
  `Дата_ответа` datetime DEFAULT NULL,
  `Статус` varchar(45) NOT NULL,
  `id_сотрудника` int NOT NULL,
  `Получатель` varchar(45) NOT NULL,
  PRIMARY KEY (`id_запроса`),
  UNIQUE KEY `id_UNIQUE` (`id_запроса`),
  CONSTRAINT `id_сотрудника` FOREIGN KEY (`id_запроса`) REFERENCES `сотрудники` (`id_сотрудника`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `запросы`
--

LOCK TABLES `запросы` WRITE;
/*!40000 ALTER TABLE `запросы` DISABLE KEYS */;
/*!40000 ALTER TABLE `запросы` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `сотрудники`
--

DROP TABLE IF EXISTS `сотрудники`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `сотрудники` (
  `id_сотрудника` int NOT NULL AUTO_INCREMENT,
  `Фамилия` varchar(45) NOT NULL,
  `Имя` varchar(45) NOT NULL,
  `Должность` varchar(45) NOT NULL,
  `Логин(почта)` varchar(45) NOT NULL,
  `Пароль` varchar(45) NOT NULL,
  `Роль_на_сайте` varchar(45) NOT NULL,
  PRIMARY KEY (`id_сотрудника`),
  UNIQUE KEY `ID_UNIQUE` (`id_сотрудника`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `сотрудники`
--

LOCK TABLES `сотрудники` WRITE;
/*!40000 ALTER TABLE `сотрудники` DISABLE KEYS */;
INSERT INTO `сотрудники` VALUES (1,'Иванов','Иван','Директор','ivan@example.com','password1','dir'),(2,'Петров','Петр','Директор','petr@example.com','password2','dir'),(3,'Сидоров','Алексей','Директор','alex@example.com','password3','dir'),(4,'Козлов','Александр','Менеджер','sasha@example.com','password4','admin'),(5,'Морозова','Елена','Менеджер','elena@example.com','password5','user'),(6,'Новиков','Дмитрий','Менеждер','dima@example.com','password6','user'),(7,'Федорова','Анна','Программист','anna@example.com','password7','user'),(8,'Кузнецов','Олег','Маркетолог','oleg@example.com','password8','user'),(9,'Белов','Сергей','Бизнес-аналитик','sergei@example.com','password9','user'),(10,'Васильев','Николай','Программист','nick@example.com','password10','user');
/*!40000 ALTER TABLE `сотрудники` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-15 12:21:35
