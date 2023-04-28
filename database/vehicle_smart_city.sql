-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 28 Apr 2023 pada 08.26
-- Versi server: 10.4.21-MariaDB
-- Versi PHP: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vehicle_smart_city`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `vehicles`
--

CREATE TABLE `vehicles` (
  `id` int(25) NOT NULL,
  `vehicleType` varchar(225) DEFAULT NULL,
  `plateNumber` varchar(255) DEFAULT NULL,
  `plateCity` varchar(255) DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `vehicles`
--

INSERT INTO `vehicles` (`id`, `vehicleType`, `plateNumber`, `plateCity`, `timestamp`) VALUES
(1, 'Truck', 'AG 1889 FGA', 'Tulungagung, Blitar', '2023-04-17 05:07:57'),
(2, 'Car', 'AG 6774 AES', 'Tulungagung, Blitar', '2023-04-17 20:38:45'),
(3, 'Car', 'AG 9554 ADS', 'Tulungagung, Blitar', '2023-04-17 20:38:45'),
(4, 'Motorcycle', 'AG 4444 ADV', 'Tulungagung, Blitar', '2023-04-17 20:38:45'),
(24, 'Motorcycle', 'AG 3111 BDN', 'Tulungagung, Blitar', '2023-04-17 20:38:45'),
(25, 'Truck', 'AG 1866 FGA', 'Tulungagung, Blitar', '2023-04-18 06:28:14'),
(26, 'Motorcycle', 'AG 9677 TDB', 'Tulungagung, Blitar', '2023-04-17 20:38:45');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `vehicles`
--
ALTER TABLE `vehicles`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `vehicles`
--
ALTER TABLE `vehicles`
  MODIFY `id` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
