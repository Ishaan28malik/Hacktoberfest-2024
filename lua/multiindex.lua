amultiindex={}

for i=0,9 do
	amultiindex[i]={}
	for j=0,9 do
	amultiindex[i][j]=tostring(i) .. tostring(j)
	end
end

io.write("table[0][0]:",amultiindex[0][0])

for i=0,9 do
	
	for j=0,9 do
		io.write(amultiindex[i][j],":")
	end
	print()
end
