# Optimization the rejection method of generating the random variables  
I would like to decrease the time of generating N random variables from distribution, which has density: f(x) = 3/2 * sin(x) * (cos(x))^2 on the interval [0, π]. Firstly, let’s take a look for results using while function in python. First graph is frequency histogram with probability density function f(x). Second graph is histogram of the time, which program needs to generate 100 000 random variables. As we can see in the second graph, to generate 100 000 variables, we need about 1.5 seconds.     
Screenshots:  
![alt text](https://github.com/dpalatynski/optimization_rejection_method/blob/master/histogram_1.png)  
![alt text](https://github.com/dpalatynski/optimization_rejection_method/blob/master/time_before_optimization.png)    
  
Is it possible to reduce that time? Of course, one of the best method of speed up this calculations is replace standard loop functions, which are implemented in python by arrays, which are available in Numpy library. I use:  
•	numpy.random.uniform(a, b, N) – to generate N-size array filled with decimal numbers from interval [a,b]  
•	numpy.empty(N) – to generate empty N-size array  
•	numpy.where(“condition”, “true”, “false”) – to check if defined condition is reached  
•	numpy.extract(“condition”, array) – to generate array with elements, which fulfilled condition  
  
Pseudocode:  
1)	Generate N (integer) random variables from uniform distribution on the interval [a,b]  
2)	Generate N (integer) random variables from uniform distribution on the interval [n,m], where n = min(f(x)) and m = max(f(x))  
3)	Create array with defined condition  
a)	If true -> accept   
b)	Else -> reject (change number for -1)  
4)	Delete every negative number  

Where is problem in that method? It’s impossible to generate exact number of random variables, because number of generating variables is defined as N. Some numbers can be negative and it’s important to delete them. It means that we should generate a bit more random variables. It is know, that number of iteration of rejection method has geometric distribution with parameter (m*(b-a))^(-1). Expected value of that distribution is m*(b-a) to generate one random variable.  

Based on defined function f(x) = 3/2 * sin(x) * (cos(x))^2 on the interval [0, π]. The minimum value is 0, so in pseudocode n = 0. What about maximum value? It’s about m  = 0.5773. To solve problem from previous paragraph we use maximum value to defined how many random variables is needed. Size of array define as M = N * m * (b – a). To be sure that it returns at least N numbers it’s worth to increase maximum number to 0.6. It should work for every N higher than 1000.   
  
Changing calculation for numpy arrays instead of calculating using python loops and increasing maximum value of function can help to generate N random variables faster. Compare to first two screenshots. Let’s generate 100 000 random variables after than optimization. Let’s take a look for new graphs.   

![alt text](https://github.com/dpalatynski/optimization_rejection_method/blob/master/compare_histograms.png)  

Firstly, frequency histogram are similar, so random variables were generated in a proper way. Secondly, we can see histogram of the time, which program needs to generate 100 000 random variables.      


![alt text](https://github.com/dpalatynski/optimization_rejection_method/blob/master/time_after_optimization.png) 

As we can see in the second graph, to generate 100 000 variables, we need about 0.03 seconds. It is almost 50 times faster. 

![alt text](https://github.com/dpalatynski/optimization_rejection_method/blob/master/compare_times.png) 

Moreover, that calculations were for 100 000 variables. Third graph show average time to generate N random variables. For small numbers, the difference between generating using python loops and numpy arrays are not significant, but for more than 10 000 variables it is more visible.  

Conclusion: If it's needed to generate 100 000 random variables using rejection method, final code works more than 1 second faster. This result is really satisfying in optimization. It's worth to point out, that changing python loops to numpy arrays can be significant not only in this optimization. Module numpy is great for big calculations and this example shows that arrays are more effective than loops. 
