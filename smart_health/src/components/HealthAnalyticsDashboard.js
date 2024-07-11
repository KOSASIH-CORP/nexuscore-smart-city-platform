import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';

function HealthAnalyticsDashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('/api/health-analytics')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  return (
    <div>
      <h1>Health Analytics Dashboard</h1>
      <LineChart width={800} height={400} data={data}>
        <Line type="monotone" dataKey="heartRate" stroke="#8884d8" />
        <Line type="monotone" dataKey="bloodPressure" stroke="#82ca9d" />
        <XAxis dataKey="date" />
        <YAxis />
        <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
        <Tooltip />
      </LineChart>
    </div>
  );
}

export default HealthAnalyticsDashboard;
