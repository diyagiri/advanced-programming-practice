def birthdayCakeCandles(candles):
    tall=max(candles)
    count=candles.count(tall)
    return count

candles = input("Enter the list of Candle Height:").split(" ")
candlist= [int(x) for x in candles]
print("The number of tallest candles are : ",birthdayCakeCandles(candlist))