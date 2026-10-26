1+1
#这里是注释，不会运行
gdp_2024<-134.9 # 2024年名义gdp，万亿元
gdp_2025<-140.2 # 2025年名义gdp，万亿元
nominal_gdp_growth <- (gdp_2025/gdp_2024-1)*100
nominal_gdp_growth
real_gdp_growth <- 5.0
deflator_change <- nominal_gdp_growth - real_gdp_growth
deflator_change
years <- c(2024, 2025)
gdp <- c(134.9, 140.2)
plot(years, gdp, type = "b")
GDP_2024
# GDP_2024 大小写在r中是不一样的