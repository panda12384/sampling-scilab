clf;

t = 0:0.001:1; 
f = 5; 
x = sin(2 * %pi * f * t); 

subplot(3,1,1);
plot(t, x);
title('Continuous-time Signal');
xlabel('Time (s)');
ylabel('Amplitude');
legend(['Continuous-time Signal with freq ' string(f) ' Hz']);





fs1 = 25; 
ts1 = 0:1/fs1:1;
xs1 = sin(2 * %pi * f * ts1);

fs2 = 10;
ts2 = 0:1/fs2:1; 
xs2 = sin(2 * %pi * f * ts2); 


fs3 = 7; 
ts3 = 0:1/fs3:1; 
xs3 = sin(2 * %pi * f * ts3); 


subplot(3,1,2);
plot(t, x, 'b');
plot2d(ts1, xs1, style=-4,rect=[0,-1.5,1,1.5]); 
plot2d(ts2, xs2, style=-5,rect=[0,-1.5,1,1.5]); 
plot2d(ts3, xs3, style=-6,rect=[0,-1.5,1,1.5]); 
title('Sampled Signals');
xlabel('Time (s)');
ylabel('Amplitude');
legend(['Sampled-signal'], [string(fs1)], [ string(fs2)], [ string(fs3)]);



xr1 = interp1(ts1, xs1, t, 'linear'); 
xr2 = interp1(ts2, xs2, t, 'linear'); 
xr3 = interp1(ts3, xs3, t, 'linear');


subplot(3,1,3);
plot(t, x, 'b');
plot2d(t, xr1, style=1,rect=[0,-1.5,1,1.5]); 
plot2d(t, xr2, style=3,rect=[0,-1.5,1,1.5]); 
plot2d(t, xr3, style=5,rect=[0,-1.5,1,1.5]); 
title('Reconstructed Signals');
xlabel('Time (s)');
ylabel('Amplitude');
legend(['Reconstructed-signal'], [string(fs1)], [ string(fs2)], [ string(fs3)]);
