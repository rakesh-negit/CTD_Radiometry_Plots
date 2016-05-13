% load('01May2016\\Mat Files\\001AB_L2s.mat');
% title_str = '01 May 2016';
% a1 = 10;
% a2 = 338;
% a3 = 670;
% a4 = 984;

% load('02May2016\\Mat Files\\001AC_L2s.mat');
% title_str = '02 May 2016';
% a1 = 9;
% a2 = 232;
% a3 = 468;
% a4 = 695;


load('03May2016\\Mat Files\\001AD_L2s.mat');
title_str = '03 May 2016';
a1 = 9;
a2 = 303;
a3 = 606;
a4 = 892;


wavelens = str2double(hdfdata.ED_hyperspectral_downcast_fields');

figure()
title(title_str);

a = subplot(4,2,1);
x = convert(hdfdata.ED_hyperspectral_downcast_data(a1,:),wavelens);
plot(wavelens,x);
legend([num2str(hdfdata.ED_hyperspectral_downcast_depth(a1)) 'm']);
title(a,'Downwelling irradiance');
b = subplot(4,2,2);
x = convert(hdfdata.LU_hyperspectral_downcast_data(a1,:),wavelens);
plot(wavelens,x);
title(b,'Upwelling radiance');
