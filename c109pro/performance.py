import random
import plotly.figure_factory as ff
import statistics as st
import plotly.graph_objects as go
import pandas as pd
import csv

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = st.mean(data)
median  = st.median(data)
mode = st.mode(data)
sd = st.stdev(data)

print("mean, median, mode and standard deviation of the Students Performance are {}, {}, {} and {} respectively ".format(mean, median, mode, sd))

first_sd_start, first_sd_end = mean-sd, mean+sd
second_sd_start, second_sd_end = mean-(2*sd), mean+(2*sd)
third_sd_start, third_sd_end = mean-(3*sd), mean+(3*sd)

figure = ff.create_distplot([data],["Reading Score"],show_hist = False)
figure.add_trace(go.Scatter(x=[mean,mean],y=[0,1], mode = "lines", name = "Mean"))
figure.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,1], mode = "lines", name ="First sd Start "))
figure.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,1], mode = "lines", name = "First sd End"))

figure.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,1], mode = "lines", name ="Second sd Start "))
figure.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,1], mode = "lines", name = "Second sd End"))

figure.add_trace(go.Scatter(x=[third_sd_start,third_sd_start],y=[0,1], mode = "lines", name ="Third sd Start "))
figure.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,1], mode = "lines", name = "Third sd End"))

figure.show()

list_of_data_within_sd1 = [result for result in data if result > first_sd_start and result < first_sd_end]
list_of_data_within_sd2 = [result for result in data if result > second_sd_start and result< second_sd_end]
list_of_data_within_sd3 = [result for result in data if result > third_sd_start and result < third_sd_end]

sd1_percentage = (len(list_of_data_within_sd1)/len(data))*100
sd2_percentage = (len(list_of_data_within_sd2)/len(data))*100
sd3_percentage = (len(list_of_data_within_sd3)/len(data))*100

print("sd1, sd2 and sd3 are {}, {} and {} respectively ".format(sd1_percentage, sd2_percentage, sd3_percentage))