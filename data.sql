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
	-- Customer, Clerk, Manager, Delivery, Supplier
	type VARCHAR(50) NOT NULL DEFAULT "Customer",
	name VARCHAR(50) NOT NULL,
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

-- Store Item
DROP TABLE IF EXISTS Item;
CREATE TABLE Item(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) PRIMARY KEY,
    price DECIMAL(6,1),
    manufacturer VARCHAR(50),
    details VARCHAR(1000),
    -- CPU, GPU, Motherboard, Case, Memory, Miscellaneous
    type VARCHAR(50)
);

-- Shopping Cart
DROP TABLE IF EXISTS ShoppingCart;
CREATE TABLE ShoppingCart(
    user INT REFERENCES Customer(id),
    item INT REFERENCES Item(id),
    PRIMARY KEY (user, item)
);

-- Credit Cards
DROP TABLE IF EXISTS CreditCard;
CREATE TABLE CreditCard(
    user INT REFERENCES Customer(id),
    name VARCHAR(100),
    number INT, -- TODO: Check what kind of input you want for #
    expiration DATETIME,
    PRIMARY KEY (id, number)
);

-- Wallet
DROP TABLE IF EXISTS Wallet;
CREATE TABLE Wallet(
    user INT REFERENCES Customer(id),
    amount DECIMAL(9,1),
    PRIMARY KEY (id)
);

-- Partner Companies
DROP TABLE IF EXISTS Company;
CREATE TABLE Company(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    type VARCHAR(1) -- (D)elivery or (S)upplier
);

-- Delivery
DROP TABLE IF EXISTS Delivery;
CREATE TABLE Delivery(
    tracking_num INT PRIMARY KEY AUTO_INCREMENT,
    from INT REFERENCES Company(id),
    item INT REFERENCES Item(id),
    to INT REFERENCES User(id),
    status VARCHAR(150)
);

-- Bids
DROP TABLE IF EXISTS Bid;
CREATE TABLE Bid(
    company INT REFERENCES Company(id),
    amount INT NOT NULL
);

-- Stock
DROP TABLE IF EXISTS Stock;
CREATE TABLE Stock(
    item INT REFERENCES Item(id),
    amount INT NOT NULL DEFAULT 0
);

-- Blacklisted Users
DROP TABLE IF EXISTS Blacklist;
CREATE TABLE Blacklist(
    user INT PRIMARY KEY
);

-- Taboo Words
DROP TABLE IF EXISTS Taboo;
CREATE TABLE Taboo(
    word VARCHAR(50) NOT NULL
);

-- Appeal Form
DROP TABLE IF EXISTS Appeal;
CREATE TABLE Appeal(
    for INT REFERENCES Customer(id),
    reason VARCHAR(1000) NOT NULL DEFAULT "N/A"
);

-- Supply Request
DROP TABLE IF EXISTS SupplyRequest;
CREATE TABLE SupplyRequest(
    orderNumber INT PRIMARY KEY AUTO_INCREMENT,
    company INT REFERENCES Company(id),
    reason VARCHAR(1000) NOT NULL
);

-- Approved Supply Requests
DROP TABLE IF EXISTS ApprovedSupplyRequest;
CREATE TABLE ApprovedSupplyRequest(
    orderNumber INT REFERENCES SupplyRequest(orderNumber)
);

