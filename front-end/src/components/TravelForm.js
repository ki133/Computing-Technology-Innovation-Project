// src/components/TravelForm.js

import React, { useState } from 'react';
import { fetchTravelPrediction } from '../services/api';

const TravelForm = ({ setResult }) => {
  // Initial state for the form inputs
  const [inputData, setInputData] = useState({
    year: 2023,
    month: 1,
    hoursFlown: '',
    aircraftKmFlown: '',
    aircraftDepartures: '',
    totalRevPax: '',
    freightTonnes: '',
    mailTonnes: '',
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
      const result = await fetchTravelPrediction(inputData);
      setResult(result);
    } catch (error) {
      console.error("Error fetching travel prediction:", error);
      setResult({ error: "Failed to fetch prediction. Please try again." });
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Travel Metric Prediction</h2>

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
        Hours Flown:
        <input
          type="number"
          name="hoursFlown"
          value={inputData.hoursFlown}
          onChange={handleChange}
          placeholder="Enter hours flown"
          required
        />
      </label>

      <label>
        Aircraft Km Flown:
        <input
          type="number"
          name="aircraftKmFlown"
          value={inputData.aircraftKmFlown}
          onChange={handleChange}
          placeholder="Enter km flown by aircraft"
          required
        />
      </label>

      <label>
        Aircraft Departures:
        <input
          type="number"
          name="aircraftDepartures"
          value={inputData.aircraftDepartures}
          onChange={handleChange}
          placeholder="Enter number of departures"
          required
        />
      </label>

      <label>
        Total Revenue Passengers:
        <input
          type="number"
          name="totalRevPax"
          value={inputData.totalRevPax}
          onChange={handleChange}
          placeholder="Enter total revenue passengers"
          required
        />
      </label>

      <label>
        Freight Tonnes:
        <input
          type="number"
          name="freightTonnes"
          value={inputData.freightTonnes}
          onChange={handleChange}
          placeholder="Enter freight in tonnes"
          required
        />
      </label>

      <label>
        Mail Tonnes:
        <input
          type="number"
          name="mailTonnes"
          value={inputData.mailTonnes}
          onChange={handleChange}
          placeholder="Enter mail in tonnes"
          required
        />
      </label>

      <button type="submit">Predict Travel Metric</button>
    </form>
  );
};

export default TravelForm;
