-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 13, 2021 at 07:38 AM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `restaurant`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
CREATE TABLE IF NOT EXISTS `booking` (
  `bid` int(5) NOT NULL AUTO_INCREMENT,
  `rid` int(5) NOT NULL,
  `userid` int(5) NOT NULL,
  `bookingdate` date NOT NULL,
  `timeslot` varchar(25) NOT NULL,
  `numofpeople` decimal(5,0) NOT NULL,
  PRIMARY KEY (`bid`),
  KEY `rid` (`rid`),
  KEY `userid` (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`bid`, `rid`, `userid`, `bookingdate`, `timeslot`, `numofpeople`) VALUES
(5, 1, 27, '2021-03-09', 'A', '3'),
(32, 1, 30, '2021-03-19', 'E', '6'),
(33, 1, 12, '2021-03-17', 'B', '2'),
(34, 2, 31, '2021-03-20', 'C', '3'),
(35, 1, 31, '2021-03-14', 'A', '7'),
(37, 1, 31, '2021-03-15', 'H', '5'),
(38, 1, 31, '2021-03-12', 'F', '5'),
(39, 1, 31, '2021-03-12', 'B', '2'),
(40, 1, 31, '2021-03-12', 'C', '4'),
(41, 1, 31, '2021-03-12', 'D', '10'),
(46, 1, 43, '2021-03-27', 'G', '4'),
(47, 1, 36, '2021-03-27', 'H', '4'),
(49, 1, 36, '2021-04-05', 'F', '11'),
(51, 1, 48, '2021-03-27', 'H', '4'),
(52, 1, 48, '2021-03-29', 'H', '7'),
(53, 1, 48, '2021-03-29', 'H', '7');

-- --------------------------------------------------------

--
-- Table structure for table `cuisine`
--

DROP TABLE IF EXISTS `cuisine`;
CREATE TABLE IF NOT EXISTS `cuisine` (
  `cid` int(5) NOT NULL,
  `cname` varchar(25) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cuisine`
--

INSERT INTO `cuisine` (`cid`, `cname`) VALUES
(1, 'Chinese'),
(2, 'South Indian'),
(3, 'North Indian'),
(4, 'Kathiyawadi');

-- --------------------------------------------------------

--
-- Table structure for table `fooditems`
--

DROP TABLE IF EXISTS `fooditems`;
CREATE TABLE IF NOT EXISTS `fooditems` (
  `fooditemid` bigint(20) NOT NULL AUTO_INCREMENT,
  `rcid` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `price` decimal(4,0) NOT NULL,
  PRIMARY KEY (`fooditemid`),
  KEY `rcid` (`rcid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `restaurant`
--

DROP TABLE IF EXISTS `restaurant`;
CREATE TABLE IF NOT EXISTS `restaurant` (
  `rid` int(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  `street` varchar(25) NOT NULL,
  `area` varchar(25) NOT NULL,
  `rating` float(3,2) NOT NULL,
  `type` varchar(25) NOT NULL,
  `foodtype` varchar(25) NOT NULL,
  `capacity` int(5) NOT NULL,
  `openingtime` time NOT NULL,
  `closingtime` time NOT NULL,
  `imageurl` varchar(500) NOT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `restaurant`
--

INSERT INTO `restaurant` (`rid`, `name`, `street`, `area`, `rating`, `type`, `foodtype`, `capacity`, `openingtime`, `closingtime`, `imageurl`) VALUES
(1, 'Bayleaf', '19, Dr Rustom Cama Marg', 'Alkapuri', 5.00, 'Garden view', 'Veg', 100, '19:00:00', '23:30:00', 'https://b.zmtcdn.com/data/pictures/0/3200020/b74e3ce0b875215ee1a2ff47fcce36a2.jpg'),
(2, 'Sankalp', '101/102 Spenta Complex', 'Race Course Road', 5.00, 'AC', 'Veg', 75, '19:30:00', '23:30:00', '');

-- --------------------------------------------------------

--
-- Table structure for table `restaurantcuisine`
--

DROP TABLE IF EXISTS `restaurantcuisine`;
CREATE TABLE IF NOT EXISTS `restaurantcuisine` (
  `rcid` int(5) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  PRIMARY KEY (`rcid`),
  KEY `rid` (`rid`),
  KEY `cid` (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `restaurantcuisine`
--

INSERT INTO `restaurantcuisine` (`rcid`, `rid`, `cid`) VALUES
(1, 1, 1),
(2, 1, 3),
(3, 1, 2),
(4, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `slotcapacity`
--

DROP TABLE IF EXISTS `slotcapacity`;
CREATE TABLE IF NOT EXISTS `slotcapacity` (
  `scid` int(5) NOT NULL AUTO_INCREMENT,
  `rid` int(5) NOT NULL,
  `tsid` varchar(2) NOT NULL,
  `date` date NOT NULL,
  `availaiblecap` decimal(5,0) NOT NULL,
  PRIMARY KEY (`scid`),
  KEY `rid` (`rid`),
  KEY `tsid` (`tsid`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `slotcapacity`
--

INSERT INTO `slotcapacity` (`scid`, `rid`, `tsid`, `date`, `availaiblecap`) VALUES
(1, 1, 'A', '2021-02-21', '97'),
(17, 1, 'B', '2021-02-21', '96'),
(18, 1, 'C', '2021-02-21', '4'),
(19, 1, 'D', '2021-02-21', '94'),
(20, 1, 'E', '2021-02-21', '89'),
(21, 1, 'F', '2021-02-21', '87'),
(22, 1, 'G', '2021-02-21', '97'),
(23, 1, 'H', '2021-02-21', '100'),
(24, 2, 'A', '2021-03-01', '75'),
(25, 2, 'B', '2021-03-01', '75'),
(26, 2, 'C', '2021-03-01', '69'),
(27, 2, 'D', '2021-03-01', '75'),
(28, 2, 'E', '2021-03-01', '75'),
(29, 2, 'F', '2021-03-01', '75'),
(30, 2, 'G', '2021-03-01', '75'),
(31, 2, 'H', '2021-03-01', '75'),
(32, 1, 'A', '2021-03-07', '73'),
(33, 1, 'B', '2021-03-07', '75'),
(34, 2, 'C', '2021-03-05', '70'),
(35, 1, 'G', '2021-03-27', '61'),
(36, 1, 'H', '2021-03-27', '66'),
(37, 1, 'D', '2021-03-12', '60'),
(38, 1, 'B', '2021-03-12', '18'),
(39, 1, 'C', '2021-03-12', '4'),
(40, 2, 'G', '2021-03-19', '4'),
(41, 2, 'G', '2021-03-19', '61'),
(42, 1, 'C', '2021-04-15', '42'),
(43, 1, 'H', '2021-03-29', '86');

-- --------------------------------------------------------

--
-- Table structure for table `timeslots`
--

DROP TABLE IF EXISTS `timeslots`;
CREATE TABLE IF NOT EXISTS `timeslots` (
  `tsid` varchar(2) NOT NULL,
  `openingtime` time NOT NULL,
  `closingtime` time NOT NULL,
  PRIMARY KEY (`tsid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `timeslots`
--

INSERT INTO `timeslots` (`tsid`, `openingtime`, `closingtime`) VALUES
('A', '19:30:00', '20:00:00'),
('B', '20:00:00', '20:30:00'),
('C', '20:30:00', '21:00:00'),
('D', '21:00:00', '21:30:00'),
('E', '21:30:00', '22:00:00'),
('F', '22:00:00', '22:30:00'),
('G', '22:30:00', '23:00:00'),
('H', '23:00:00', '23:30:00');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `userid` int(5) NOT NULL AUTO_INCREMENT,
  `uname` varchar(50) NOT NULL,
  `phonenumber` decimal(10,0) NOT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`userid`, `uname`, `phonenumber`) VALUES
(2, 'Shiva', '9876543210'),
(3, 'Krishna', '9898989898'),
(12, 'Durga', '9999999999'),
(27, 'Shivani', '9123456788'),
(30, 'Krisha', '9223456799'),
(31, 'Krish', '9114567890'),
(34, 'Ramesh', '9912367890'),
(35, 'Shivam', '7112367890'),
(36, 'Shivaay', '9825329248'),
(37, 'Shiva', '9898989898'),
(40, 'Aashka', '7777777890'),
(43, 'Aashaka', '9123456799'),
(48, 'Ashaka', '9123456789'),
(49, 'Ashaka', '9123456789'),
(50, 'Ashaka', '9123456789');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`rid`) REFERENCES `restaurant` (`rid`),
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`);

--
-- Constraints for table `restaurantcuisine`
--
ALTER TABLE `restaurantcuisine`
  ADD CONSTRAINT `restaurantcuisine_ibfk_1` FOREIGN KEY (`rid`) REFERENCES `restaurant` (`rid`),
  ADD CONSTRAINT `restaurantcuisine_ibfk_2` FOREIGN KEY (`cid`) REFERENCES `cuisine` (`cid`);

--
-- Constraints for table `slotcapacity`
--
ALTER TABLE `slotcapacity`
  ADD CONSTRAINT `slotcapacity_ibfk_1` FOREIGN KEY (`rid`) REFERENCES `restaurant` (`rid`),
  ADD CONSTRAINT `slotcapacity_ibfk_2` FOREIGN KEY (`tsid`) REFERENCES `timeslots` (`tsid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
