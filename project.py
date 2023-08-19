import numpy as np
#1 Represent the data in the appropriate numpy array..
data=np.array([[[[7,29],[15,31],[6,24],[15,21],[11,32],[14,24],[7,29]],[[10,29],[15,23],[15,24],[-13,27],[6,21],[13,26],[7,23]]
                ,[[9,22],[8,22],[9,25],[12,31],[13,25],[11,29],[9,23]],[[14,20],[8,21],[15,23],[12,29],[15,30],[11,22],[10,24]]]
                ,[[[7,20],[6,27],[13,23],[15,23],[7,23],[10,27],[9,29]],[[14,28],[14,20],[7,27],[6,30],[15,20],[7,25],[13,23]],
                  [[15,24],[13,29],[13,22],[6,25],[6,20],[10,20],[12,24]],[[13,27],[14,28],[15,22],[15,28],[6,23],[9,25],[14,30]]],
                  [[[2,18],[6,18],[5,22],[4,20],[2,19],[3,4],[3,21]],[[3,20],[6,21],[6,21],[7,18],[2,21],[6,8],[2,18]],
                [[3,19],[2,19],[4,18],[2,20],[6,18],[2,5],[4,18]],[[6,21],[6,20],[7,21],[2,19],[5,20],[5,5],[7,20]]]
                ,[[[12,21],[8,20],[-10,18],[8,20],[9,19],[8,71],[10,19]],[[12,18],[12,18],[8,22],[8,18],[12,18],[11,11],[7,18]],
                  [[8,20],[10,22],[8,19],[11,20],[11,18],[10,11],[8,21]],[[12,20],[12,20],[7,21],[10,22],[7,20],[7,12],[9,20]]]])
#2 write the dimensions and shape of numpy array created above.
print("Shape of Numpy array ",data.shape)
print("Dimensions of numpy array ",data.ndim)
#3 print the daily temprature for the first week of each month.
print(data[:,0,:,:])
#4 print the tempratures of tuesday of each month.
print(data[:,:,1,:])
#5 Print only the maximum temperature for all the weekdays of Dec and Feb.
print(data[1:,:,4,1])
#6 Print all the days along with the week number in November when the minimum temperature was less than 8 degrees.
print("the minimum temperature was less than 8 degrees\n")
print(data[0,:,:,0]<8)
#7 print all the weeks in Dec and Jan where the maximum temperature has crossed a threshold of 20 degrees
print("Dec and Jan where the maximum temperature has crossed a threshold of 20 degrees\n")
print(data[1:3,:,:,1]>20)

#10 Find and print the indexes of all the outlier(unusual) values present in the above dataset
print(np.where(data[:,:,:,0]<0)[0])
print(np.where(data[:,:,:,0]<0)[1])
print(np.where(data[:,:,:,0]<0)[2])

#11 Replace the outliers with an appropriate value
print(np.abs(data[0,1,3,0]))

#12 Find the average max temperature for the winter months in Jaipur.
print(data[:,:,:,1].mean())
#13 Find the weekly min avg temp for the month of Dec in Jaipur
print(data[1,:,:,0].mean())
#14 Find the overall avg temp for the months Dec and Jan
print(data[1:3,:,:,:].mean())
#15Find the least temp experienced by the city in the month of Dec and Jan. Also print the exact date( Day/Week/Month) for the same.
print

#16 Find the max temp in the month of Feb and return its date(Day/Week/Month)
print("Month ")
print(np.where(data[:,:,:,1]==np.max(data[3,:,:,1]))[0])
print("Week ")
print(np.where(data[:,:,:,1]==np.max(data[3,:,:,1]))[1])
print("Day ")
print(np.where(data[:,:,:,1]==np.max(data[3,:,:,1]))[2])

#17 Find the days in the month of Nov where the max temp of the day dropped below the avg temp of the month. As
x=np.count_nonzero(data[0,:,:,1]<data[0,:,:,1].mean())
print("Days in the november where the max temp of the day dropped below the avg ",x)

# 20. Sort the above data in descending order on the basis of weekly average for the month of Dec.
print(data[1,:,::-1,:])

#21 Sort the temp of the first three days of each month in descending order on the basis of overall average for the whole winter
print(data[:,:,3:0:-1,:])

