hour, minute = map(int, input().split());

if(hour > 0 and minute < 45):
    hour -= 1;
    minute += 15;
elif(hour == 0 and minute < 45):
    hour = 23;
    minute += 15;
else:
    minute -= 45;
print(hour, minute);