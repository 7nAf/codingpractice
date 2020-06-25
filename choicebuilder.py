state_choices =  "(\"Andhra Pradesh\", \"Andhra Pradesh\"), (\"Arunachal Pradesh\", \"Arunachal Pradesh\"), (\"Assam\", \"Assam\"),\r\n                     (\"Bihar\", \"Bihar\"),\r\n                     (\"Chhattisgarh\", \"Chhattisgarh\"), (\"Goa\", \"Goa\"), (\"Gujarat\", \"Gujarat\"), (\"Haryana\", \"Haryana\"),\r\n                     (\"Himachal Pradesh\", \"Himachal Pradesh\"), (\"Jammu and Kashmir\", \"Jammu and Kashmir\"),\r\n                     (\"Jharkhand\", \"Jharkhand\"),\r\n                     (\"Karnataka\", \"Karnataka\"), (\"Kerala\", \"Kerala\"), (\"Madhya Pradesh\", \"Madhya Pradesh\"), (\"Maharashtra\", \"Maharashtra\"),\r\n                     (\"Manipur\", \"Manipur\"), (\"Meghalaya\", \"Meghalaya\"), (\"Mizoram\", \"Mizoram\"), (\"Nagaland\", \"Nagaland\"),\r\n                     (\"Odisha\", \"Odisha\"), (\"Punjab\", \"Punjab\"), (\"Rajasthan\", \"Rajasthan\"), (\"Sikkim\", \"Sikkim\"),\r\n                     (\"Tamil Nadu\", \"Tamil Nadu\"), (\"Telangana\", \"Telangana\"), (\"Tripura\", \"Tripura\"), (\"Uttar Pradesh\", \"Uttar Pradesh\"),\r\n                     (\"Uttarakhand\", \"Uttarakhand\"), (\"West Bengal\", \"West Bengal\"),\r\n                     (\"Andaman and Nicobar Islands\", \"Andaman and Nicobar Islands\"),\r\n                     (\"Chandigarh\", \"Chandigarh\"), (\"Dadra and Nagar Haveli\", \"Dadra and Nagar Haveli\"), (\"Daman and Diu\", \"Daman and Diu\"),\r\n                     (\"Lakshadweep\", \"Lakshadweep\"),\r\n                     (\"National Capital Territory of Delhi\", \"National Capital Territory of Delhi\"), (\"Puducherry\", \"Puducherry\")"

print(state_choices)

str1=""
l=[]
c=0
index3rdquote=0
co=0
for i in state_choices[::-1]:
  if(i=='"'):
    c+=1
  if(c%3==0 and c!=0):
    if i=='"':
      index3rdquote=co
      continue
    if(i==' '):
      str1+='_'
      co+=1
    else:
      str1+=i.upper()
      co+=1
  else:
    if c%4==0 and i=='"':
      str1+=''
      c=0
      temp=str1[index3rdquote:co:]
      l.append(temp[::-1])
      index3rdquote=0
    else:
      str1+=i
      co+=1 
print(str1[::-1])




