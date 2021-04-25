-- PARTS AUTHORITY DATABASE BLUEPRINT FOR COMPUTER STORE
-- APRIL 2021
-- AUTHORS: Ashraq Khan, Azwad Shameem, Dewan Tahmid, David Diop
DROP DATABASE IF EXISTS pa_store;
CREATE DATABASE pa_store;
USE pa_store;

-- Registered User
-- Ex: visitors/browsers, registered customers, store clerks, store managers/supervisors,
-- computer parts companies, delivery companies
DROP TABLE IF EXISTS User;
CREATE TABLE User(
	id INT PRIMARY KEY AUTO_INCREMENT,
	type VARCHAR(50) NOT NULL,
	name VARCHAR(50) NOT NULL DEFAULT "Customer",
	email VARCHAR(100) UNIQUE NOT NULL,
	password VARCHAR(255) NOT NULL,
    joined DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    isSignedIn BOOLEAN NOT NULL
);

-- Post
DROP TABLE IF EXISTS Post;
CREATE TABLE Post(
	id INT PRIMARY KEY AUTO_INCREMENT,
	author INT REFERENCES Customer(id),
	content VARCHAR(1000)
);

-- Reply
DROP TABLE IF EXISTS Reply;
CREATE TABLE Reply(
    id INT PRIMARY KEY AUTO_INCREMENT,
	author INT REFERENCES Customer(id),
	thread INT REFERENCES Post(id),
	content VARCHAR(1000)
);

-- CPU
DROP TABLE IF EXISTS CPU;
CREATE TABLE CPU(
    name VARCHAR(100) PRIMARY KEY,
    cores INT,
    threads INT,
    generation INT,
    frequency DECIMAL(3,1),
    price DECIMAL(6,1),
    manufacturer VARCHAR(50)
);

-- GPU
DROP TABLE IF EXISTS GPU;
CREATE TABLE GPU(
    name VARCHAR(100) PRIMARY KEY,
    price DECIMAL(6,1),
    manufacturer VARCHAR(50)
);

-- Motherboard
DROP TABLE IF EXISTS Motherboard;
CREATE TABLE Motherboard(
    name VARCHAR(100) PRIMARY KEY,
    price DECIMAL(6,1),
    manufacturer VARCHAR(50)
);

-- Case
DROP TABLE IF EXISTS Case;
CREATE TABLE Case(
    name VARCHAR(100) PRIMARY KEY,
    price DECIMAL(6,1),
    manufacturer VARCHAR(50)
);

-- Memory
DROP TABLE IF EXISTS Memory;
CREATE TABLE Memory(
    name VARCHAR(100) PRIMARY KEY,
    price DECIMAL(6,1),
    manufacturer VARCHAR(50)
);

-- Miscellaneous
DROP TABLE IF EXISTS MiscItems;
CREATE TABLE MiscItems(
    name VARCHAR(100) PRIMARY KEY,
    price DECIMAL(6,1),
    manufacturer VARCHAR(50)
);




