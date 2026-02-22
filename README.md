# Radar Tracking Simulation

## Overview
For this project, I wanted to simulate an aircraft moving in 2D and explore how radar measurements aren’t always perfect.  
I added random noise to the measurements to make it more realistic and then tried to improve them using a simple moving average filter.  

---

## What I’ve Done
- Simulated an aircraft flying in a straight line (constant speed)  
- Added radar noise to mimic real-world measurements  
- Made a simple moving average filter to try and clean up the data  
- Measured how well the filter worked using Mean Squared Error (MSE)  
- Made a plot showing:  
  - True path of the aircraft  
  - Noisy radar measurements  
  - Filtered path  
- Exported all the simulation data to a CSV using pandas for analysis

---

## What I Learned / Results
- MSE (Measured): 8.10  
- MSE (Filtered): 6.66  
- Improvement: 17.7%  

The filter made the noisy measurements closer to the real aircraft path, which was really interesting to see.

---

## Files in This Project
- `main.py` → the Python code for the simulation and filter  
- `radar_tracking_plot.png` → the plot of everything  
- `radar_tracking_data.csv` → CSV of all the simulation data (time step, true, measured, and filtered positions)

---

## Next Steps / Ideas
- Try different sizes for the moving average window  
- Experiment with more advanced filters, like a Kalman filter  
- Simulate multiple aircraft at the same time  
- Test with different levels of noise  

I want to see how far I can take this idea and learn more about filtering, tracking, and how engineers handle real-world measurements.

---

## Why I’m Interested in Software Engineering
This project also made me realise how much I enjoy building small software systems:  
- Handling and storing data efficiently (lists, arrays, CSVs)  
- Writing algorithms to process and clean data  
- Making clear visualisations of results  
- Thinking about how to measure if the software actually works (MSE!)

It made me really curious about how software and hardware interact in real systems, and why engineers have to think about both.  
I’m really interested to explore more in both aerospace and software engineering.