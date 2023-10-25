-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-10-2023 a las 23:41:32
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `datashm`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datossensores`
--

CREATE TABLE `datossensores` (
  `ID` int(11) NOT NULL,
  `Tiempo` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Vibracion` float DEFAULT NULL,
  `Latitud` decimal(10,8) DEFAULT NULL,
  `Longitud` decimal(11,8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datossensores`
--

INSERT INTO `datossensores` (`ID`, `Tiempo`, `Vibracion`, `Latitud`, `Longitud`) VALUES
(1, '2023-10-19 00:17:21', 0.928665, 62.47867772, -135.83942896),
(2, '2023-10-19 00:17:22', 0.527604, 41.52123904, -126.22866053),
(3, '2023-10-19 00:17:23', 0.986405, -84.82546092, -114.79071625),
(4, '2023-10-19 00:17:24', 1.52305, -28.86320368, -127.67155201),
(5, '2023-10-19 00:17:25', 0.427251, -85.61421197, -72.58196900),
(6, '2023-10-19 00:17:26', 0.0859892, 71.02717410, 105.17518368),
(7, '2023-10-19 00:17:27', 0.576, 82.41878008, -34.98565566),
(8, '2023-10-19 00:17:28', 0.048187, -19.84274884, -61.24737383),
(9, '2023-10-19 00:17:29', 0.633886, 42.59296351, 18.96541273),
(10, '2023-10-19 00:17:30', 0.843165, 88.05517150, 29.57293448);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `datossensores`
--
ALTER TABLE `datossensores`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `datossensores`
--
ALTER TABLE `datossensores`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
