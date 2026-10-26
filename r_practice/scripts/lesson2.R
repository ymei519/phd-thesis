library(readxl)
raw <- read_excel ("data_raw/china_gdp_annual_wind_20261021.xlsx",
                   skip = 5, n_max = 74, col_names = FALSE)
View(raw)
names(raw) <- c("date", "gdp_nominal", "gdp_index")
raw$year <- as.numeric (format(raw$date, "%Y"))
head (raw)
tail (raw)
plot (raw$year, raw$gdp_nominal, type = "1")
plot(raw$year, raw$gdp_nominal, type = "l")
plot(raw$year, log(raw$gdp_nominal), type = "l")
plot(raw$year, raw$gdp_index, type = "l")
raw$gdp_index[raw$year == 2020]