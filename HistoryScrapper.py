import datetime

from BybitClient import BybitClient
import csv

SYMBOL = "ETHUSD"

wallet_symbol = "USDT"

# Пример использования:
if __name__ == "__main__":
    client = BybitClient()

    # Получение баланса
    balance = client.get_balance(wallet_symbol)
    print(f"Баланс : {balance} {wallet_symbol}")

    # Размещение ордера
    # order = client.place_order(symbol="BTCUSD", side="Buy", order_type="Limit", qty=1, price=30000)
    # print("Ордер создан:", order)

    # Получение информации о ордере
    # order_info = client.get_order(order_id=order['result']['order_id'])
    # print("Информация о ордере:", order_info)

    # Отмена ордера
    # cancel_result = client.cancel_order(order_id=order['result']['order_id'])
    # print("Результат отмены ордера:", cancel_result)

    # Получение котировок за последние 15 минут для ETHUSD

    # hours_period = 16
    # current_dt = datetime.date.today()
    #
    # start_date = datetime.datetime(year=current_dt.year, month=current_dt.month,
    #                                day=current_dt.day - 1, hour=hours_period)
    # last_datetime = start_date - datetime.timedelta(days=25)
    #
    # with open('data_file', 'w', newline='') as csvfile:
    #     price_writer = csv.writer(csvfile, delimiter=' ')
    #     price_writer.writerow(['startTime', 'openPrice', 'highPrice', 'lowPrice', 'closePrice', 'volume', 'turnover'])
    #     while start_date.timestamp() > last_datetime.timestamp():
    #         candles = client.get_ticker(symbol=SYMBOL, end_time=int(start_date.timestamp()), interval="1",
    #                                     period_minutes=hours_period * 60)
    #         price_writer.writerows(candles['list'])
    #         start_date = start_date - datetime.timedelta(hours=hours_period)
    #
    # # Получение списка всех валютных пар
    # trading_pairs = client.get_trading_pairs()
    # print("Список валютных пар:", trading_pairs)
