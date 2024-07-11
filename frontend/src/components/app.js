import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
    const [devices, setDevices] = useState([]);
    const [data, setData] = useState({});

    useEffect(() => {
        axios.get("/devices")
           .then(response => {
                setDevices(response.data);
            })
           .catch(error => {
                console.error(error);
            });
    }, []);

    const handleDeviceSelect = (device) => {
        axios.get(`/devices/${device.device_id}`)
           .then(response => {
                setData(response.data);
            })
           .catch(error => {
                console.error(error);
            });
    };

    return (
        <div>
            <h1>Smart City Dashboard</h1>
            <ul>
                {devices.map(device => (
                    <li key={device.id}>
                        <span>{device.device_id}</span>
                        <button onClick={() => handleDeviceSelect(device)}>Select</button>
                    </li>
                ))}
            </ul>
            <div>
                <h2>Device Data</h2>
                <p>{data.data}</p>
            </div>
        </div>
    );
}

export default App;
