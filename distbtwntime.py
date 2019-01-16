def dist(time1, time2):
    timeArr = list(time1)
    time1Arr = list(time2)
    colon_index = []
    colon_index.append(timeArr.index(":"))
    colon_index.append(time1Arr.index(":"))
    hours = ["", ""]
    minutes = ["", ""]

    # Error checking / format checking
    if(colon_index[0] > 2 or colon_index[1] > 2):
        return "Error; Type a correct time."
    # get hours
    for number in range(0, colon_index[0]):
        hours[0] += timeArr[number]
    for number in range(0, colon_index[1]):
        hours[1] += time1Arr[number]
    # get minutes
    for number in range(colon_index[0] + 1, len(timeArr)):
        minutes[0] += timeArr[number]
    for number in range(colon_index[1] + 1, len(time1Arr)):
        minutes[1] += time1Arr[number]
    # convert to int
    minutes[0] = int(minutes[0])
    minutes[1] = int(minutes[1])
    hours[0] = int(hours[0])
    hours[1] = int(hours[1])
    # checking if time is wrong
    if(minutes[0] > 59 or minutes[1] > 59 or hours[0] > 24 or hours[1] > 24):
        return "Please type a properly formatted time"
    # ha, actually do the subtraction now
    time1 = hours[0]*60 + minutes[0]
    time2 = hours[1]*60 + minutes[1]
    time3 = abs(time1 - time2);
    finalTime = [int(round(time3/60, 0)), time3%60]
    if finalTime[1] == 0 :
        if finalTime[0] == 1:
            print("The difference is exactly", finalTime[0], "hour.")
        else:
            print("The difference is exactly", finalTime[0], "hour.")
    else:
        print("The difference is", finalTime[0], "hours and", finalTime[1], "minutes.")

dist(input("Enter a time: "), input("Enter another time: "))
