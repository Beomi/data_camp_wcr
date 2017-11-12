from dateutil import parser

p_time = parser.parse('2017/05/23')
p_time_2 = parser.parse('2017-12-22')

print(p_time, p_time_2)
