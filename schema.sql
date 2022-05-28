CREATE TABLE IF NOT EXISTS `Sales` 
(
    ['Month', 'PromoInterval', 'Assortment', 'StoreType','WeekOfYear', 
    'DayOfWeek', 'DayOfMonth', 'Promo', 'Store', 'CompetitionDistance', 'Open']
   
    `open` INT NOT NULL,
    `competition_distance` INT NOT NULL,
    `store` INT NOT NULL,
    `promo` INT Not NULL,
    `day_of_month` INT NOT NULL,
    `day_of_week` INT NOT NULL,
    `week_of_year` INT NOT NULL,
    `store_type` TEXT DEFAULT NULL,
    `assortment` TEXT DEFAULT NULL,
    `month` INT NOT NULL
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
