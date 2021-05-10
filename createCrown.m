clear all
close all
clc

min = [0.277, -0.11864]; %[raggio, spessore]
max = [0.313, -0.0996871];  %[raggio, spessore]

layers_r = 2;
layers_s = 3;

points_r = linspace(min(1),max(1), layers_r);
points_spessore = linspace(min(2),max(2), layers_s);

points = zeros(2*length(points_r),3);

k = 1;

for i = 1:length(points_r)
    for j = 1:length(points_spessore)
    points(k,:) = [points_r(i), points_spessore(j), points_r(i)];
    k = k+1;
    end
end


        
alpha = linspace(0,360,50);
alpha = alpha(1:end-1);


k=1;

for i = 1:length(alpha)
	for j = 1:length(points)
            punti(k,:) = points(j,:) * [cosd(alpha(i)), 0, sind(alpha(i));
                                             0        , 1,      0        ;
                                       -sind(alpha(i)), 0, cosd(alpha(i))];
            k = k+1;

        end
end

plot3(punti(:,1), punti(:,2), punti(:,3),'*')
xlabel('x')
ylabel('y')
zlabel('z')
axis equal
grid on

csvwrite('punti.csv', punti)
   
   
   
   
