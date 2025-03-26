import React from "react";

const App = () => {
  return (
    <div>
    <div style={{ textAlign: "center" }}>
      <h2> Chart-1</h2>
      {/* Fetching chart from Flask */}
      <img
        src="http://localhost:5000/chart4"
        alt="Matplotlib Chart"
        style={{ width: "600px", border: "2px solid #333" }}
      />
    </div>

<div style={{ textAlign: "center" }}>
<h2>Chart-2</h2>
{/* Fetching chart from Flask */}
<img
  src="http://localhost:5000/chart3"
  alt="Matplotlib Chart"
  style={{ width: "600px", border: "2px solid #333" }}
/>
</div>

<div style={{ textAlign: "center" }}>
<h2> Chart-3</h2>
{/* Fetching chart from Flask */}
<img
  src="http://localhost:5000/pieChart"
  alt="Matplotlib Chart"
  style={{ width: "600px", border: "2px solid #333" }}
/>
</div>

<div style={{ textAlign: "center" }}>
<h2> Chart-4</h2>
{/* Fetching chart from Flask */}
<img
  src="http://localhost:5000/designCh"
  alt="Matplotlib Chart"
  style={{ width: "600px", border: "2px solid #333" }}
/>
</div>
<div style={{ textAlign: "center" }}>
      <h2>Crops Distribution by Average Rainfall</h2>
      {/* Display the Pie Chart from Flask */}
      <img
        src="http://localhost:5000/piechart2"
        alt="Crops Distribution Chart"
        style={{ width: "600px", border: "2px solid #333" }}
      />
    </div>

    {/* <div style={{ textAlign: "center" }}>
      <h2>Hover chart</h2>
      
      <img
        src="http://localhost:5000/HoverChart"
        alt="Crops Distribution Chart"
        style={{ width: "600px", border: "2px solid #333" }}
      />
    </div> */}
</div>
    
  );
};

export default App;
