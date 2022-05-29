DROP TABLE IF EXISTS `rosmannfeatures`;
CREATE TABLE IF NOT EXISTS `rosmannfeatures` 
(
    `Store` INT NOT NULL,
    `DayOfWeek` INT NOT NULL,
    `Sales`  INT NOT NULL,
    `Customer` INT NOT NULL,
    `Open` INT NOT NULL,
    `Promo` INT NOT NULL,
    `StateHoliday` INT NOT NULL,
    `StoreType` TEXT NOT NULL,
    `Assortment` TEXT NOT NULL,
    `CompetitionDistance` TEXT NOT NULL
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
