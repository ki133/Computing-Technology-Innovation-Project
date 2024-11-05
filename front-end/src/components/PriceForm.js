// src/components/PriceForm.js

import React, { useState } from 'react';
import { fetchPricePrediction } from '../services/api';

const PriceForm = ({ setResult }) => {
  // Initial state for the form inputs
  const [inputData, setInputData] = useState({
    year: 2023,
    month: 1,
    port1: '',
    port2: '',
    route: '',
  });

  // Handle input changes for controlled form inputs
  const handleChange = (e) => {
    const { name, value } = e.target;
    setInputData({ ...inputData, [name]: value });
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const result = await fetchPricePrediction(inputData);
      setResult(result);
    } catch (error) {
      console.error("Error fetching price prediction:", error);
      setResult({ error: "Failed to fetch prediction. Please try again." });
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Price Prediction</h2>

      <label>
        Year:
        <input
          type="number"
          name="year"
          value={inputData.year}
          onChange={handleChange}
          min="2000"
          max="2100"
          required
        />
      </label>

      <label>
        Month:
        <input
          type="number"
          name="month"
          value={inputData.month}
          onChange={handleChange}
          min="1"
          max="12"
          required
        />
      </label>

      <label>
        Port 1:
        <input
          type="text"
          name="port1"
          value={inputData.port1}
          onChange={handleChange}
          placeholder="Enter starting port"
          required
        />
      </label>

      <label>
        Port 2:
        <input
          type="text"
          name="port2"
          value={inputData.port2}
          onChange={handleChange}
          placeholder="Enter destination port"
          required
        />
      </label>

      <label>
        Route:
        <input
          type="text"
          name="route"
          value={inputData.route}
          onChange={handleChange}
          placeholder="Enter route"
          required
        />
      </label>

      <button type="submit">Predict Price</button>
    </form>
  );
};

export default PriceForm;
