# создаем переменную для необратонной информации с сайта:
today=$(date +%Y%m%d)
weather_report=raw_data_$today
# скачиваем данные с сайта wttr.com:
city=Moscow
curl wttr.in/$city --output $weather_report
# сохраняем данные текущего часа, дня, месяца, года:
hour=$(TZ='Russia/Moscow' date -u +%H) 
day=$(TZ='Russia/Moscow' date -u +%d) 
month=$(TZ='Russia/Moscow' date +%m)
year=$(TZ='Russia/Moscow' date +%Y)
# Высортировываем все строки с температурой
grep °C $weather_report > temperatures.txt
# Получаем текущую температуру 
obs_tmp=$(head -1 temperatures.txt | tr -s " " | xargs | rev | cut -d " " -f2 | rev)
# Вытаскиваем прогноз за завтрашний полдень
fc_temp=$(head -3 temperatures.txt | tail -1 | tr -s " " | xargs | cut -d "C" -f2 | rev | cut -d " " -f2 |rev)
# создаем таблицу с данными
record=$(echo -e "$year\t$month\t$day\t$obs_tmp\t$fc_temp")
# Выгружаем record в rx_poc.log
echo $record>>rx_poc.log
cat rx_poc.log
