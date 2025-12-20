
# Water Tank Problem – Frontend Solution

This project solves the classic **Water Tank (Trapping Rain Water)** problem
and visualizes it using **Vanilla JavaScript, HTML, CSS, and SVG**.

## How to Run
Just open `index.html` in any browser.

## Input
Enter block heights as comma-separated numbers.
Example:
```
0,4,0,0,0,6,0,6,4,0
```

## Output
- Total water units stored
- SVG visualization showing:
  - Yellow blocks (walls)
  - Blue water trapped

## Algorithm
Uses:
- Left max array
- Right max array
- Water at index = min(leftMax, rightMax) - height

## Technologies
- HTML
- CSS
- Vanilla JavaScript
- SVG rendering

## Notes
- No frameworks used
- Interview-friendly and easy to explain
