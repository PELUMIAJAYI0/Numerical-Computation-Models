import React from "react";
import { LineChart, Line, BarChart, Bar, PieChart, Pie, Cell, AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from "recharts";

const solarData = [
  { time: "00:00", energy: 20 },
  { time: "06:00", energy: 50 },
  { time: "12:00", energy: 100 },
  { time: "18:00", energy: 60 },
];

const windData = [
  { time: "00:00", energy: 35 },
  { time: "06:00", energy: 60 },
  { time: "12:00", energy: 85 },
  { time: "18:00", energy: 65 },
];

const hydroData = [
  { time: "00:00", energy: 50 },
  { time: "06:00", energy: 65 },
  { time: "12:00", energy: 85 },
  { time: "18:00", energy: 70 },
];

const geoData = [
  { time: "00:00", energy: 40 },
  { time: "06:00", energy: 55 },
  { time: "12:00", energy: 75 },
  { time: "18:00", energy: 65 },
];

const weatherData = [
  { time: "00:00", temperature: 22, humidity: 80 },
  { time: "06:00", temperature: 18, humidity: 90 },
  { time: "12:00", temperature: 30, humidity: 60 },
  { time: "18:00", temperature: 26, humidity: 75 },
];

const Dashboard = () => {
  return (
    <div className="min-h-screen bg-gray-200 flex flex-col items-center justify-center p-6 space-y-6">
      <h1 className="text-5xl font-extrabold text-gray-800 mb-6 text-center">Renewable Energy Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 w-full max-w-7xl">
        <div className="bg-white shadow-md rounded-lg p-6 border border-gray-300">
          <h2 className="text-2xl font-semibold text-gray-700 mb-2">Solar Energy</h2>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={solarData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="time" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="energy" fill="#facc15" />
            </BarChart>
          </ResponsiveContainer>
        </div>
        
        <div className="bg-white shadow-md rounded-lg p-6 border border-gray-300">
          <h2 className="text-2xl font-semibold text-gray-700 mb-2">Wind Energy</h2>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={windData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="time" />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey="energy" stroke="#3b82f6" strokeWidth={3} dot={{ r: 5 }} />
            </LineChart>
          </ResponsiveContainer>
        </div>
        
        <div className="bg-white shadow-md rounded-lg p-6 border border-gray-300">
          <h2 className="text-2xl font-semibold text-gray-700 mb-2">Hydropower</h2>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie data={hydroData} dataKey="energy" nameKey="time" cx="50%" cy="50%" outerRadius={80} fill="#60a5fa" label>
                {hydroData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={["#60a5fa", "#4f83cc", "#3b6ebf", "#2d5aad"][index % 4]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
        
        <div className="bg-white shadow-md rounded-lg p-6 border border-gray-300">
          <h2 className="text-2xl font-semibold text-gray-700 mb-2">Geothermal Energy</h2>
          <ResponsiveContainer width="100%" height={300}>
            <AreaChart data={geoData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="time" />
              <YAxis />
              <Tooltip />
              <Area type="monotone" dataKey="energy" stroke="#a855f7" fill="#d8b4fe" />
            </AreaChart>
          </ResponsiveContainer>
        </div>
        
        {/* Weather Forecast */}
        <div className="bg-white shadow-md rounded-lg p-6 border border-green-400">
          <h2 className="text-2xl font-semibold text-gray-700 mb-2">Weather Forecast</h2>
          <ResponsiveContainer width="100%" height={300}>
            <AreaChart data={weatherData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="time" />
              <YAxis />
              <Tooltip />
              <Area type="monotone" dataKey="temperature" stroke="#eab308" fill="#fde047" />
              <Area type="monotone" dataKey="humidity" stroke="#06b6d4" fill="#67e8f9" />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
