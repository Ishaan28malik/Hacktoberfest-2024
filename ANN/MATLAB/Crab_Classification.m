[x,t] = crab_dataset;
size(x)
size(t)

setdemorandstream(491218382)

net = patternnet(10);
view(net)

[net,tr] = train(net,x,t);
plotperform(tr)
testX = x(:,tr.testInd);
testT = t(:,tr.testInd);

testY = net(testX);
testIndices = vec2ind(testY)

plotconfusion(testT,testY)
[c,cm] = confusion(testT,testY)


fprintf('Percentage Incorrect Classification : %f%%\n', 100*c);

plotroc(testT,testY)
fprintf('Percentage Correct Classification   : %f%%\n', 100*(1-c));
