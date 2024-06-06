
rainy_days, cloudy_days = map(int, input().split())


clear_days = 7 - (rainy_days + cloudy_days)


print(clear_days)
