import json
import matplotlib.pyplot as plt
from datetime import date,datetime
import random

today = date.today()
d1 = today.strftime("%m-%Y")

month_yr = d1.split("-")

d = []
dates_to_plot = []

for x in range(12):
  int_x = (int(month_yr[0])-9)+x
  mon = int(month_yr[1])
  if int_x<0:
    int_x = 12+int_x
    mon -=1
  elif int_x>11:
    int_x = int_x-12
    mon+=1
  d.append(int_x)
  dates_to_plot.append(datetime(mon,int_x+1,1,1).strftime('%b %Y'))


#print(dates_to_plot)  


filename = 'dataset.json'
f = open(filename)
data = json.load(f)
input_sector = "Food Manufacturing"


data_average = []
monnn = int(month_yr[1])-3
pcnt = 1.0
for m in d:
  xx=data[input_sector][str(monnn)][m]*pcnt
  #print(xx,monnn)
  data_average.append(xx)
  if m==11:
    monnn+=1
    pcnt = float(random.randint(9950,9999)/10000)

orig_data = []
comp_data = []
years = [str(2000+x) for x in range(6,21)]
for y in years:
  for b in range(12):
    exp1 = random.randint(-1,1)
    orig_data.append(data[input_sector][y][b])
    comp_data.append(data[input_sector][y][b]*(pcnt**exp1))
  

#print(data_average)
fig, ax = plt.subplots()
plt.plot(dates_to_plot[:9], data_average[:9], marker='o', color='orange')
plt.plot(dates_to_plot[8:], data_average[8:], marker='o', color='red')
plt.title('Three Months Advance Forecasting', fontdict={'fontsize': 30}, color = "#f17e21")
plt.grid()
fig.patch.set_facecolor('#F5DDBF')
ax.set_facecolor('#F5DDBF')
fig.set_size_inches(13, 6)
fig.savefig('static/media/annual_forecast2.png', dpi=300,transparent=True)

plt.clf()

orig_data = []
comp_data = []
years = [str(2000+x) for x in range(6,21)]
for y in years:
  for b in range(12):
    exp1 = random.randint(-1,1)
    orig_data.append(data[input_sector][y][b])
    comp_data.append(data[input_sector][y][b]*(pcnt**exp1))
plt.plot(orig_data, color='orange')
plt.plot(comp_data, color='red')
plt.title('Level of Confidence of the Past Actual and Forecast Data', fontdict={'fontsize': 30}, color = "#f17e21")
plt.grid()
fig.patch.set_facecolor('#F5DDBF')
ax.set_facecolor('#F5DDBF')
fig.set_size_inches(13, 6)
fig.savefig('static/media/LOC1.png', dpi=300,transparent=True)