atable={}

for i=1 ,10 do
       atable[i]=1
	
end

print(atable[1])
print("all number:",#atable,",")

table.insert(atable,1,10)

io.write("all",atable[10],"\n")


print(table.concat(atable,","))
