import pandas as pd
bmi=[]
column=["Maria","Betmen","Sundjer"]
titled_columns={
    "Ime Liste":column,
    "height":[1.67,1.9,0.25],
    "weight":[55,100,2],
    
    
}
data=pd.DataFrame(titled_columns)
select_column=data["weight"][1] #kilaza betmena
select_row=data.iloc[2]


for i in range(len(data)):
    rez=data["weight"][i]/(data["height"][i]**2)
    bmi.append(rez)
drugi_recnik={
    "bmi":bmi
}
#moglo je i kroz isti recnik sa data["bmi"]=bmi
data_score=pd.DataFrame(drugi_recnik)
print(data)
print(select_column)
print(select_row)
print(data_score)

data.to_csv("glupak.csv ")