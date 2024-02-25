% Hello Future Joe this is the start of smt beautiful

Power_array = [];
Speed_array = [];


for speed = 3:12
    currW = (0.5)*(0.35)*(1.293)*(pi)*(50)^2*(speed^3);
    Power_array(end+1) = currW*24*365/4400;
    Speed_array(end+1) = speed;
end

for speed = 13:18
    currW = 6*10^6;
    Power_array(end+1) = currW;
    Speed_array(end+1) = speed;
end

for speed = 19:20
    currW = 0;
    Power_array(end+1) = currW;
    Speed_array(end+1) = speed;
end

plot(Speed_array,Power_array, 'r--');
% Labels and title
xlabel('Speed (in m/s)')
ylabel('Power (in kWh/year)')
title('Wind Turbine: Power vs speed')