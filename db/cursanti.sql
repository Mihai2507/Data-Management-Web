-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 19, 2024 at 10:44 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cursanti`
--

-- --------------------------------------------------------

--
-- Table structure for table `comisie`
--

CREATE TABLE `comisie` (
  `id` int(11) NOT NULL,
  `director` text NOT NULL,
  `secretar` text NOT NULL,
  `presedinte` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_romanian_ci;

--
-- Dumping data for table `comisie`
--

INSERT INTO `comisie` (`id`, `director`, `secretar`, `presedinte`) VALUES
(2, 'ss', 'sss', 'sssss'),
(5, 'q', 'w', 'e');

-- --------------------------------------------------------

--
-- Table structure for table `companie`
--

CREATE TABLE `companie` (
  `id` int(11) NOT NULL,
  `nume` text NOT NULL,
  `localitate` text NOT NULL,
  `judet` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_romanian_ci;

--
-- Dumping data for table `companie`
--

INSERT INTO `companie` (`id`, `nume`, `localitate`, `judet`) VALUES
(2, 'rrrrrrrr', 'fffs', 'fsfs'),
(4, 'telacad', 'buc', 'sector6');

-- --------------------------------------------------------

--
-- Table structure for table `curs`
--

CREATE TABLE `curs` (
  `id` int(11) NOT NULL,
  `nume_curs` text NOT NULL,
  `descriere` text NOT NULL,
  `cor` int(11) NOT NULL,
  `nr_registru` text NOT NULL,
  `data_incepere` date NOT NULL,
  `data_finalizare` date NOT NULL,
  `durata` int(11) NOT NULL,
  `anul_examinarii` int(11) NOT NULL,
  `luna_examinarii` int(11) NOT NULL,
  `ziua_examinarii` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_romanian_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cursant`
--

CREATE TABLE `cursant` (
  `id` int(10) UNSIGNED NOT NULL,
  `nume` text NOT NULL,
  `cnp` bigint(20) NOT NULL,
  `judet_sector` text NOT NULL,
  `localitate` text NOT NULL,
  `Prenume_mama` text NOT NULL,
  `Prenume_tata` text NOT NULL,
  `anul_nasterii` int(11) NOT NULL,
  `luna_nasterii` int(11) NOT NULL,
  `ziua_nasterii` int(11) NOT NULL,
  `locul_nasterii` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_romanian_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comisie`
--
ALTER TABLE `comisie`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `companie`
--
ALTER TABLE `companie`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `curs`
--
ALTER TABLE `curs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cursant`
--
ALTER TABLE `cursant`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comisie`
--
ALTER TABLE `comisie`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `companie`
--
ALTER TABLE `companie`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `curs`
--
ALTER TABLE `curs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `cursant`
--
ALTER TABLE `cursant`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
