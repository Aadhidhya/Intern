
function calculateWater(height) {
    let leftMax = [], rightMax = [];
    let water = 0;

    leftMax[0] = height[0];
    for (let i = 1; i < height.length; i++) {
        leftMax[i] = Math.max(leftMax[i - 1], height[i]);
    }

    rightMax[height.length - 1] = height[height.length - 1];
    for (let i = height.length - 2; i >= 0; i--) {
        rightMax[i] = Math.max(rightMax[i + 1], height[i]);
    }

    for (let i = 0; i < height.length; i++) {
        water += Math.max(0, Math.min(leftMax[i], rightMax[i]) - height[i]);
    }

    return water;
}

function solve() {
    const input = document.getElementById("input").value;
    const arr = input.split(",").map(Number);

    const water = calculateWater(arr);
    document.getElementById("result").innerText =
        "Stored Water: " + water + " Units";

    drawChart(arr);
}

function drawChart(arr) {
    const svg = document.getElementById("chart");
    svg.innerHTML = "";

    const barWidth = 40;
    const maxHeight = Math.max(...arr);
    const scale = 200 / maxHeight;

    // Draw blocks
    arr.forEach((h, i) => {
        const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        rect.setAttribute("x", i * barWidth);
        rect.setAttribute("y", 250 - h * scale);
        rect.setAttribute("width", barWidth - 4);
        rect.setAttribute("height", h * scale);
        rect.setAttribute("class", "block");
        svg.appendChild(rect);
    });

    // Draw water
    for (let i = 0; i < arr.length; i++) {
        let leftMax = Math.max(...arr.slice(0, i + 1));
        let rightMax = Math.max(...arr.slice(i));
        let waterHeight = Math.max(0, Math.min(leftMax, rightMax) - arr[i]);

        if (waterHeight > 0) {
            const waterRect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
            waterRect.setAttribute("x", i * barWidth);
            waterRect.setAttribute("y", 250 - (arr[i] + waterHeight) * scale);
            waterRect.setAttribute("width", barWidth - 4);
            waterRect.setAttribute("height", waterHeight * scale);
            waterRect.setAttribute("class", "water");
            svg.appendChild(waterRect);
        }
    }
}

solve();
